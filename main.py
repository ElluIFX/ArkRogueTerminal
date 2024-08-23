import datetime
import os
import shelve
import sys
import tempfile
import uuid
from copy import copy
from dataclasses import dataclass

from loguru import logger
from PySide6.QtCore import QFile, QPoint, Qt, QTimer, Slot
from PySide6.QtGui import QCloseEvent, QIcon, QPixmap
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QInputDialog,
    QMainWindow,
    QMenu,
    QMessageBox,
)

import richuru
from ui import MainUITemplate
from utils import ReqClientExQThread

"""
qdarktheme import after QT
"""
import qdarktheme

UUID_NAMESPACE = uuid.UUID("1b671a64-40d5-491e-99b0-da01ff1f3342")
VERSION = "1.0.0"
AVATAR_SIZE = 140  # 软件内头像大小
OBS_AVATAR_SIZE = 180  # OBS头像大小
MAX_SLOT = 16  # 最大记录槽位
DEFAULT_NOTE = "无备注信息"  # 默认备注信息
DATA_DIR_NAME = "ark_data"  # 数据文件夹
RESOURCE_DIR_NAME = "resource"  # 资源文件夹

AVATAR_DIR_NAME = "avatar"  # 头像文件夹
OBS_TEMP_DIR_NAME = "obstemp"  # OBS素材临时文件夹
START_OPERATOR_DIR_NAME = "operator"  # 开局干员文件夹
START_TEAM_DIR_NAME = "team"  # 开局队伍文件夹
OBS_TOAST_PLUS_IMG_NAME = "plus.png"  # OBS弹幕加分图片
OBS_TOAST_MINUS_IMG_NAME = "minus.png"  # OBS弹幕减分图片
LOGFILE_NAME = "log.txt"  # 日志文件名
DATABASE_NAME = "players.db"  # 数据库前缀
DATABASE_BACKUP_NAME = "players_backup.db"  # 数据库备份前缀
OBS_TOAST_DURATION = 2  # OBS弹幕显示时间

PATH = os.path.dirname(os.path.abspath(__file__))  # 打包后的临时路径
ARGV_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))  # 实际上的运行路径

DATA_PATH = os.path.join(ARGV_PATH, DATA_DIR_NAME)
RESOURCE_PATH = os.path.join(ARGV_PATH, RESOURCE_DIR_NAME)

AVATAR_PATH = os.path.join(DATA_PATH, AVATAR_DIR_NAME)
OBS_TEMP_PATH = os.path.join(DATA_PATH, OBS_TEMP_DIR_NAME)
DATABASE_PATH = os.path.join(DATA_PATH, DATABASE_NAME)
DATABASE_BACKUP_PATH = os.path.join(DATA_PATH, DATABASE_BACKUP_NAME)
LOGFILE_PATH = os.path.join(DATA_PATH, LOGFILE_NAME)
START_OPERATOR_PATH = os.path.join(RESOURCE_PATH, START_OPERATOR_DIR_NAME)
START_TEAM_PATH = os.path.join(RESOURCE_PATH, START_TEAM_DIR_NAME)

if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)
if not os.path.exists(AVATAR_PATH):
    os.makedirs(AVATAR_PATH)
if not os.path.exists(OBS_TEMP_PATH):
    os.makedirs(OBS_TEMP_PATH)
if not os.path.exists(START_OPERATOR_PATH):
    os.makedirs(START_OPERATOR_PATH)
if not os.path.exists(START_TEAM_PATH):
    os.makedirs(START_TEAM_PATH)

logger.remove()
logger.add(LOGFILE_PATH, level="DEBUG", backtrace=True)
if os.path.samefile(PATH, ARGV_PATH):  # 直接运行
    richuru.install()

generate_uuid = lambda name: str(
    uuid.uuid5(UUID_NAMESPACE, name + str(datetime.datetime.now()))
).upper()


@dataclass
class Record:
    data: list[str]  # 记录数据
    base_score: int = 0  # 基础分
    score: int = 0  # 总分
    start_operator: str = "未知"  # 开局干员
    start_team: str = "未知"  # 开局队伍
    time: int = 0  # 时间戳
    valid: bool = False  # 是否是有效记录


@dataclass
class Player:
    name: str  # 昵称
    note: str  # 备注
    uuid: str  # UUID
    records: list[Record]  # 作战记录


TEMP_PLAYER = Player(
    "临时招募·迷迭香",
    "超大杯",
    generate_uuid("临时招募·迷迭香"),
    [Record(list()) for _ in range(MAX_SLOT)],
)


class MainWindow(QMainWindow, MainUITemplate):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(
            f"罗德岛裁判终端 Beta - 荆楚歌/萨卡兹的无终奇语 - {VERSION} by Ellu"
        )
        self.setWindowIcon(QIcon(os.path.join(PATH, "icon.png")))

        self.players: dict[str, Player] = {}
        self.connected = False
        self.obs: ReqClientExQThread = None

        for i in range(MAX_SLOT):
            self.comboBoxSelRecord.addItem(f"{i+1}")
        self.frameAvatar.setMinimumSize(AVATAR_SIZE + 8, AVATAR_SIZE + 8)

        # 添加开局干员
        for file in os.listdir(START_OPERATOR_PATH):
            if file.endswith(".png"):
                self.comboBoxStartOperator.addItem(os.path.splitext(file)[0])
        # 添加开局队伍
        for file in os.listdir(START_TEAM_PATH):
            if file.endswith(".png"):
                self.comboBoxStartTeam.addItem(os.path.splitext(file)[0])

        # 移除鼠标滚轮事件防止误操作
        self.comboBoxSelRecord.wheelEvent = lambda _: None
        self.comboBoxSelPlayer.wheelEvent = lambda _: None

        # 载入数据库
        self.load_database()

        # 创建一个定时器, 自动保存数据库
        self.db_timer = QTimer(self)
        self.db_timer.timeout.connect(self.save_database)
        self.db_timer.start(10000)  # 10s

        self.listRecord.setContextMenuPolicy(Qt.CustomContextMenu)

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        重写关闭事件, 保存数据库并关闭OBS连接
        """
        self.save_database()
        if self.connected:
            self.obs.stop()
        logger.info("Application closed")
        event.accept()

    def load_database(self):
        """
        从数据库载入数据, 如果数据库不存在则创建一个新的数据库
        """
        self.players = {}
        with shelve.open(DATABASE_PATH) as db:
            if "__version__" not in db:
                db["__version__"] = "0.0.0"
            if db["__version__"] != VERSION:
                logger.warning(
                    f"Database version mismatch, expect {VERSION}, got {db['__version__']}"
                )
            for name in db:
                if name == "__version__":
                    continue
                self.players[name] = db[name]
        if len(self.players) == 0:
            self.players[TEMP_PLAYER.name] = TEMP_PLAYER
        self.comboBoxSelPlayer.clear()
        for name in self.players:
            self.comboBoxSelPlayer.addItem(name)
        self.comboBoxSelPlayer.setCurrentIndex(0)
        logger.info(f"Database loaded from {DATABASE_PATH}")
        # logger.debug(f"Players={self.players}")

    def save_database(self):
        """
        保存数据到数据库, 如果保存失败则备份到另一个数据库
        """
        # t0 = time.perf_counter()
        try:
            with shelve.open(DATABASE_PATH, "n") as db:
                for name in self.players:
                    db[name] = self.players[name]
                db["__version__"] = VERSION
        except Exception as e:
            logger.error(f"Database save failed: {e}, try save to backup")
            try:
                with shelve.open(DATABASE_BACKUP_PATH, "n") as db:
                    for name in self.players:
                        db[name] = self.players[name]
                    db["__version__"] = VERSION
                logger.info("Database backup success")
            except Exception as e:
                logger.exception("Database backup save failed")
            return
        # t1 = time.perf_counter()
        # logger.debug(f"Database saved, cost {t1-t0:.5f}s")
        # logger.debug(f"Players={self.players}")

    def update_player_info(self):
        """
        更新干员信息面板, 包括头像, 记录数, 最后保存时间, 最高分数等
        """
        self.lineEditPlayerName.setText(self.player_now.name)
        self.lineEditPlayerNote.setText(self.player_now.note)
        self.labelPlayerUUID.setText(self.player_now.uuid)
        valid_num = 0
        max_score = -1
        max_index = -1
        latest_time = -1
        latest_index = -1
        for i, record in enumerate(self.player_now.records):
            if record.valid:
                valid_num += 1
                if record.time > latest_time:
                    latest_time = record.time
                    latest_index = i
                if record.score > max_score:
                    max_score = record.score
                    max_index = i
        self.labelPlayerRecordNum.setText(
            "Slot "
            + ", ".join(
                str(i + 1) for i in range(MAX_SLOT) if self.player_now.records[i].valid
            )
            if valid_num
            else "无记录"
        )
        self.labelPlayerLastSaveTime.setText(
            datetime.datetime.fromtimestamp(latest_time).strftime("%Y-%m-%d %H:%M:%S")
            + f" ( Slot {latest_index+1} )"
            if latest_time > 0
            else "N/A"
        )
        score = f"{max_score:.4f}".rstrip("0").rstrip(".")
        self.labelPlayerMaxRecord.setText(
            f"{score} ( Slot {max_index+1} )" if max_score >= 0 else "N/A"
        )

    def sync_obs_player_info(self, skip_sync_name=False):
        """
        同步OBS直播间的玩家信息

        skip_sync_name: 是否跳过同步干员名字(耗时, 因为要计算文本对齐)
        """
        if not self.connected:
            return
        if not skip_sync_name:
            self.obs.fake.set_player(self.player_now.name, self.avatar_obs_path)
        self.obs.fake.set_start(
            os.path.join(START_TEAM_PATH, f"{self.record.start_team}.png")
            if self.record.start_team != "未知"
            else "",
            os.path.join(START_OPERATOR_PATH, f"{self.record.start_operator}.png")
            if self.record.start_operator != "未知"
            else "",
        )
        self.obs.fake.set_score(f"{self.record.score:.4f}".rstrip("0").rstrip("."))

    def load_player(self, name: str):
        """
        载入干员信息, 包括头像, 记录等
        """
        if name not in self.players:
            logger.warning(f"Player {name} not found")
            return
        logger.info(f"Loading player {name}")
        self.player_now = self.players[name]
        self.load_avatar()
        self.update_player_info()
        self.comboBoxSelRecord.setCurrentIndex(-1)
        self.comboBoxSelRecord.setCurrentIndex(0)
        self.sync_obs_player_info()
        # will call on_comboBoxSelRecord_currentIndexChanged

    def load_avatar(self):
        """
        载入头像
        """
        name = self.player_now.name
        for ext in ["jpg", "jpeg", "png"]:
            path = os.path.join(AVATAR_PATH, f"{name}.{ext}")
            if QFile.exists(path):
                break
        else:
            self.labelAvatar.setPixmap(QPixmap())
            self.labelAvatar.setText("无头像")
            logger.warning(f"Missing avatar for {name}")
            self.avatar_obs_path = ""
            return
        pixmap = QPixmap(path)
        self.labelAvatar.setText("")
        self.labelAvatar.setPixmap(
            pixmap.scaled(
                AVATAR_SIZE,
                AVATAR_SIZE,
                mode=Qt.TransformationMode.SmoothTransformation,
            )
        )
        logger.info(
            f"Avatar for {name} loaded from {path} "
            f"({pixmap.width()}x{pixmap.height()})"
        )
        obs_path = os.path.join(
            OBS_TEMP_PATH,
            f"avatar_{OBS_AVATAR_SIZE}_{self.player_now.uuid}.png",
        )
        if not QFile.exists(obs_path):
            pixmap.scaled(
                OBS_AVATAR_SIZE,
                OBS_AVATAR_SIZE,
                mode=Qt.TransformationMode.SmoothTransformation,
            ).save(obs_path, "PNG", 100)
            logger.info(
                f"Avatar for {name} resized to OBS size "
                f"{OBS_AVATAR_SIZE}x{OBS_AVATAR_SIZE} and saved to {obs_path}"
            )
        self.avatar_obs_path = obs_path

    @Slot(int)
    def on_comboBoxSelPlayer_currentIndexChanged(self, index: int):
        if len(self.players) == 0 or index < 0:
            return
        self.load_player(self.comboBoxSelPlayer.currentText())

    def load_record(self, index: int):
        """
        载入记录
        """
        logger.info(f"Loading record {index+1} for {self.player_now.name}")
        self.record = self.player_now.records[index]
        self.listRecord.clear()
        for item in self.record.data:
            self.listRecord.addItem(item)
        if self.record.start_operator in [
            self.comboBoxStartOperator.itemText(i)
            for i in range(self.comboBoxStartOperator.count())
        ]:
            self.comboBoxStartOperator.setCurrentText(self.record.start_operator)
        else:
            self.comboBoxStartOperator.setCurrentIndex(0)
        if self.record.start_team in [
            self.comboBoxStartTeam.itemText(i)
            for i in range(self.comboBoxStartTeam.count())
        ]:
            self.comboBoxStartTeam.setCurrentText(self.record.start_team)
            self.comboBoxStartOperator.setCurrentText(self.record.start_operator)
        self.spinBoxBaseScore.setValue(self.record.base_score)
        self.recalc_score()

    @Slot()
    def on_pushButtonClrRecord_clicked(self):
        reply = QMessageBox.question(
            self,
            "你再想想",
            f"确定要清零干员 {self.player_now.name} 的记录 {self.comboBoxSelRecord.currentText()} 吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return
        self.record.valid = False
        self.record.data.clear()
        self.record.base_score = 0
        self.record.score = 0
        self.record.time = 0
        self.record.start_operator = "未知"
        self.record.start_team = "未知"
        self.spinBoxBaseScore.setValue(0)
        self.listRecord.clear()
        self.recalc_score()
        self.update_player_info()
        logger.info(f"Record {self.comboBoxSelRecord.currentText()} cleared")

    @Slot(int)
    def on_comboBoxSelRecord_currentIndexChanged(self, index: int):
        if len(self.players) == 0 or index < 0:
            return
        self.load_record(index)

    @Slot()
    def on_pushButtonDelPlayer_clicked(self):
        reply = QMessageBox.question(
            self,
            "确认",
            f"确定要删除干员 {self.player_now.name} 吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply != QMessageBox.Yes:
            return
        if len(self.players) == 1:
            QMessageBox.warning(
                self,
                "兄弟, 迷迭香真的超大杯, 信我!",
                "删除最后一个干员将获得一只可爱的迷迭香,\n想要删除她请招募新干员",
            )
            if self.player_now.name == TEMP_PLAYER.name:
                return
        name = self.player_now.name
        del self.players[name]
        self.comboBoxSelPlayer.removeItem(self.comboBoxSelPlayer.currentIndex())
        logger.info(f"Player {name} deleted")
        self.comboBoxSelPlayer.setCurrentIndex(-1)
        if len(self.players) == 0:
            self.players[TEMP_PLAYER.name] = copy(TEMP_PLAYER)
            self.comboBoxSelPlayer.addItem(TEMP_PLAYER.name)
        self.comboBoxSelPlayer.setCurrentIndex(0)

    @Slot()
    def on_pushButtonAddPlayer_clicked(self):
        name, ok = QInputDialog.getText(self, "添加干员", "请输入干员昵称")
        if not ok:
            return
        if name in self.players:
            QMessageBox.warning(self, "错误", "干员已存在")
            return
        if not name:
            QMessageBox.warning(self, "错误", "干员昵称不能为Sora")
            return
        self.players[name] = Player(
            name,
            DEFAULT_NOTE,
            generate_uuid(name),
            [Record(list()) for _ in range(MAX_SLOT)],
        )
        self.comboBoxSelPlayer.addItem(name)
        self.comboBoxSelPlayer.setCurrentText(name)
        logger.info(f"Player {name} added")

    @Slot()
    def on_lineEditPlayerName_editingFinished(self):
        name = self.lineEditPlayerName.text()
        if name == self.player_now.name:
            return
        if name in self.players:
            QMessageBox.warning(self, "错误", "新的干员昵称重复了")
            self.lineEditPlayerName.setText(self.player_now.name)
            return
        ok = QMessageBox.question(
            self,
            "确认",
            f"确定要将干员 {self.player_now.name} 改名为 {name} 吗？",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if ok != QMessageBox.Yes:
            self.lineEditPlayerName.setText(self.player_now.name)
            return
        old_name = self.player_now.name
        self.player_now.name = name
        del self.players[old_name]
        self.players[name] = self.player_now
        self.comboBoxSelPlayer.setItemText(self.comboBoxSelPlayer.currentIndex(), name)
        self.comboBoxSelPlayer.setCurrentText(name)
        self.load_player(name)
        logger.info(f"Player {self.player_now.name} renamed to {name}")
        QMessageBox.information(
            self,
            "成功",
            "干员昵称修改成功\n注意: avatar文件夹内的头像文件名不会自动修改, 请手动修改",
        )

    @Slot()
    def on_lineEditPlayerNote_editingFinished(self):
        note = self.lineEditPlayerNote.text()
        if note == self.player_now.note:
            return
        self.player_now.note = note
        logger.info(f"Player {self.player_now.name} note updated: {note}")

    @Slot(int)
    def on_comboBoxStartOperator_currentIndexChanged(self, index: int):
        name = self.comboBoxStartOperator.currentText()
        self.record.start_operator = name
        self.sync_obs_player_info(True)
        logger.info(f"Start operator updated: {name}")

    @Slot(int)
    def on_comboBoxStartTeam_currentIndexChanged(self, index: int):
        name = self.comboBoxStartTeam.currentText()
        self.record.start_team = name
        self.sync_obs_player_info(True)
        logger.info(f"Start team updated: {name}")

    # listRecord 删除
    def __list_del_item(self):
        row = self.listRecord.currentRow()
        cnt = self.listRecord.count()
        if cnt == 0:
            return
        if row == -1:
            row = cnt - 1
        self.listRecord.takeItem(row)
        self.record.data.pop(row)
        self.record.time = int(datetime.datetime.now().timestamp())
        self.listRecord.setCurrentRow(max(row - 1, 0))
        self.recalc_score()

    @Slot(QPoint)  # listRecord 右键菜单
    def on_listRecord_customContextMenuRequested(self, pos: QPoint):
        menu = QMenu()
        menu.addAction("删除", self.__list_del_item)
        menu.exec(self.listRecord.mapToGlobal(pos))

    def recalc_score(self):
        score = self.record.base_score
        score_multi = []
        for i in range(self.listRecord.count()):
            item = self.listRecord.item(i)
            text = item.text()
            if "x" in text:
                score_multi.append(float(text.split("x")[-1]))
            elif "+" in text:
                score += int(text.split("+")[-1])
            elif "-" in text:
                score -= int(text.split("-")[-1])
        for mul in score_multi:
            score *= mul
        self.labelScore.setText(f"{score:.4f}".rstrip("0").rstrip("."))
        self.record.score = score
        self.update_player_info()
        logger.info(f"Score recalculated: {score:.4f}")
        if self.connected:
            self.obs.fake.set_score(f"{score:.4f}".rstrip("0").rstrip("."))
        ###### 以下为额外逻辑 ######
        six, five, four = 0, 0, 0
        for text in self.record.data:
            if "六星" in text:
                six += 1
            elif "五星" in text:
                five += 1
            elif "四星" in text:
                four += 1
        self.labelHeaderTemp.setText(f"// 六星: {six} 五星: {five} 四星: {four} //")

    def add_score_change(
        self, info1: str, info2: str, change: float, is_multi: bool = False
    ):
        text = info1
        if info2:
            text += f" {info2}"
        if is_multi:
            text += f" x{change+1:.4f}".rstrip("0").rstrip(".")
            info2 = f"最终乘算 x{change+1:.4f}".rstrip("0").rstrip(".")
            change = 0
        else:
            text += f" {change:+}"
        self.listRecord.addItem(text)
        self.record.data.append(text)
        self.record.valid = True
        self.record.time = int(datetime.datetime.now().timestamp())
        logger.info(f"Score change added: {text}")
        self.recalc_score()
        if self.connected and self.checkBoxEnLowers.isChecked():
            self.obs.fake.display_lower(
                info1.split(" ")[0],
                info2,
                change,
                duration=OBS_TOAST_DURATION,
                plus_bk_path=os.path.join(RESOURCE_PATH, OBS_TOAST_PLUS_IMG_NAME),
                minus_bk_path=os.path.join(RESOURCE_PATH, OBS_TOAST_MINUS_IMG_NAME),
            )

    @Slot()
    def on_spinBoxBaseScore_editingFinished(self):
        self.record.base_score = self.spinBoxBaseScore.value()
        self.record.time = int(datetime.datetime.now().timestamp())
        self.record.valid = True
        logger.info(f"Base score changed to {self.record.base_score}")
        self.recalc_score()
        if self.connected and self.checkBoxEnLowers.isChecked():
            self.obs.fake.display_lower(
                "基础分数",
                f"+{self.record.base_score}",
                0,
                duration=OBS_TOAST_DURATION,
                plus_bk_path=os.path.join(RESOURCE_PATH, OBS_TOAST_PLUS_IMG_NAME),
                minus_bk_path=os.path.join(RESOURCE_PATH, OBS_TOAST_MINUS_IMG_NAME),
            )

    @Slot()
    def on_pushButtonConnect_clicked(self):
        if self.connected:
            self.obs.stop()
            self.pushButtonConnect.setText("连接OBS")
            self.connected = False
            self.labelConState.setText("/// PRTS 未连接 ///")
            self.labelConState.setStyleSheet("")
        else:
            addr = self.lineEditServer.text()
            port = self.spinBoxConPort.value()
            try:
                self.obs = ReqClientExQThread(addr, port, "", timeout=5)
            except Exception as e:
                logger.error(f"OBS Client connection failed: {e}")
                QMessageBox.warning(
                    self,
                    "连接失败",
                    f"无法连接到: {addr}:{port}\n发生错误: {e}\n"
                    "请检查OBS Websocket服务器是否已启动并设置正确的端口号\n(请不要开启身份验证!)",
                )
                return
            self.pushButtonConnect.setText("断开OBS")
            self.connected = True
            self.labelConState.setText("/// PRTS 已连接 ///")
            self.labelConState.setStyleSheet("color: #93bd7a")
            self.obs.set_pause(self.checkBoxPause.isChecked())
            self.sync_obs_player_info()

    @Slot()
    def on_pushButtonClrLowers_clicked(self):
        if not self.connected:
            logger.warning("OBS not connected")
            return
        self.obs.clear()

    @Slot()
    def on_checkBoxPause_toggled(self):
        if not self.connected:
            return
        self.obs.set_pause(self.checkBoxPause.isChecked())
        if not self.checkBoxPause.isChecked():
            self.sync_obs_player_info()

    ############## 以下为分数逻辑 ##############

    @Slot(int)
    def on_comboBoxKillSp_currentIndexChanged(self, index: int):
        text = self.comboBoxKillSp.currentText()
        self.checkBoxKillSpPerfect.setEnabled(text in ["鸭速公路<紧急>"])
        self.checkBoxKillSpPerfect.setChecked(False)
        if "信号灯" in text or "劫虚济实" in text or "叙事邀约" in text:
            self.checkBoxKillSpPerfect.setChecked(True)
        self.spinBoxKillSp.setEnabled(
            "狭路相逢" not in text
            and "叙事邀约" not in text
            and "战场侧面" not in text
            and "信号灯" not in text
            and "劫虚济实" not in text
        )

    @Slot(int)
    def on_comboBoxEmerg_currentIndexChanged(self, index: int):
        text = self.comboBoxEmerg.currentText()
        self.checkBoxEmergBswLessFour.setChecked(False)
        self.pushButtonSubmitEmerg.setEnabled("—" not in text)
        if "溃乱魔典" in text or "大棋一盘" in text or "BOSS" in text or "—" in text:
            self.checkBoxEmergBswLessFour.setEnabled(False)
        else:
            self.checkBoxEmergBswLessFour.setEnabled(True)

    @Slot()
    def on_pushButtonSubmitCustom_clicked(self):
        text = self.lineEditCustomScore.text()
        if not text:
            QMessageBox.warning(self, "不许黑幕", "请给出打分理由")
            return
        self.add_score_change(text, "", self.spinBoxCustomScore.value())

    @Slot()
    def on_pushButtonSubmitTemp_clicked(self):
        if self.radioButtonTempSix.isChecked():
            score = 50
            text = "六星干员"
        elif self.radioButtonTempFive.isChecked():
            score = 20
            text = "五星干员"
        elif self.radioButtonTempFour.isChecked():
            score = 10
            text = "四星干员"
        else:
            return
        self.add_score_change("临时招募", text, score)

    @Slot()
    def on_pushButtonSubmitEmerg_clicked(self):
        text = (
            self.comboBoxEmerg.currentText()
            .split("<")[0]
            .replace("【", "")
            .replace("】", "")
        )
        if text.startswith("—"):
            return
        score_dict = {
            "溃乱魔典": 30,
            "大棋一盘": 20,
            "猩红甬道": 40,
            "假象对冲": 30,
            "朽败考察": 20,
            "年代断层": 0,
            "计划耕种": 70,
            "寄人城池下": 50,
            "通道封锁": 30,
            "无罪净土": 30,
            "巫咒同盟": 30,
            "残损学院": 20,
            "谋求共识": 70,
            "神圣的渴求": 40,
            "三层BOSS关": 30,
            "四层普通紧急": 0,
            "五层普通紧急": 0,
            "六层普通紧急": 0,
        }
        score = score_dict[text]
        text2 = ""
        if "BOSS" not in text:
            if "<" in self.comboBoxEmerg.currentText():
                score += 20
                text2 += "特殊年代"
            if (
                self.checkBoxEmergBswLessFour.isChecked()
                and "溃乱魔典" not in text
                and "大棋一盘" not in text
            ):
                score += 15
                if text2 != "":
                    text2 += "/"
                text2 += "低部署"
        else:
            if "<" in self.comboBoxEmerg.currentText():
                score += 30
                text2 += "卫国前夜"
        if score == 0:
            return
        self.add_score_change(text, text2, score)

    @Slot()
    def on_pushButtonSubmitKillSp_clicked(self):
        val = self.spinBoxKillSp.value()
        perfect = self.checkBoxKillSpPerfect.isChecked()
        text = self.comboBoxKillSp.currentText()
        text1 = text
        text2 = "无漏" if perfect else ""
        if text == "普通关卡":
            score = 10 * val
            text1 = "特殊击杀"
            text2 = f"{val}只"
        elif "信号灯" in text or "劫虚济实" in text:
            score = 50 if "紧急" in text else 25
        elif "战场侧面" in text:
            score = 40 if "紧急" in text else 20
        elif text == "鸭速公路<紧急>":
            score = 20 * val
            text2 = f"特殊击杀{val}只"
            if perfect:
                score += 40
                text2 += "/无漏"
        elif "狭路相逢" in text:
            score = 10
            text2 = "未使用过的组合"
        elif text == "叙事邀约":
            score = 40
        else:
            return
        if score == 0:
            return
        self.add_score_change(text1, text2, score)

    @Slot()
    def on_pushButtonEarlyEmerg_clicked(self):
        val = self.spinBoxEarlyEmerg.value()
        if val == 0:
            return
        score = 20 * val
        self.add_score_change("跨层紧急作战", f"{val}树洞藏品", score)

    @Slot()
    def on_pushButtonSubmitMoneyOverflow_clicked(self):
        val = self.spinBoxMoneyOverflow.value()
        if val == 0:
            return
        score = -50 * val
        self.add_score_change("取钱超支", f"{val}点", score)

    @Slot()
    def on_pushButtonSubmitEnding_clicked(self):
        text1 = self.comboBoxEnding1.currentText()
        text2 = self.comboBoxEnding2.currentText()
        text3 = self.comboBoxEnding3.currentText()
        score = (
            {0: 0, 1: 20, 2: 70}[self.comboBoxEnding1.currentIndex()]
            + {0: 0, 1: 120, 2: 140, 3: 190}[self.comboBoxEnding2.currentIndex()]
            + {0: 0, 1: 170, 2: 200, 3: 250}[self.comboBoxEnding3.currentIndex()]
        )
        text = text1
        if text2 != "未达成":
            text = text2
            if self.checkBoxEndingEnd2Sp.isChecked():
                score += 20
                text += " (SP)"
        if text3 != "未达成":
            text = text3
            if self.checkBoxEndingEnd3Sp.isChecked():
                score += 50
                text += " (SP)"
        if score == 0:
            return
        self.add_score_change("达成结局", text, score)

    @Slot()
    def on_pushButtonSubmitSum_clicked(self):
        ter = self.spinBoxSumTreasure.value()
        emerg = self.spinBoxSumEmerg.value()
        bbtsy = self.checkBoxSumHasBbtsy.isChecked()
        score = -6 * ter + -15 * emerg + (20 if bbtsy else 0)
        self.add_score_change(
            "最终结算",
            f"藏品:{ter} 紧急:{emerg}" + (" (誓言)" if bbtsy else ""),
            score,
        )

    @Slot()
    def on_pushButtonSubmitBan_clicked(self):
        mul = 0
        if self.radioButtonWsde2.isChecked():
            self.add_score_change("抓取维什戴尔", "独立乘算", -0.2, is_multi=True)
        if self.radioButtonWsde3.isChecked():
            mul += 0.0711

        def get_ban_count(checkBox: QCheckBox):
            if checkBox.checkState() == Qt.CheckState.PartiallyChecked:
                return 1
            elif checkBox.checkState() == Qt.CheckState.Checked:
                return 2
            return 0

        mul += 0.03 * (
            get_ban_count(self.checkBoxBanCjayfl)
            + get_ban_count(self.checkBoxBanKalsit)
            + get_ban_count(self.checkBoxBanYns)
            + get_ban_count(self.checkBoxBanSuxin)
            + get_ban_count(self.checkBoxBanWeba)
            + get_ban_count(self.checkBoxBanNifu)
        )
        mul += 0.05 * (
            get_ban_count(self.checkBoxBanLogos)
            + get_ban_count(self.checkBoxBanAskl)
            + get_ban_count(self.checkBoxBanQlsyd)
            + get_ban_count(self.checkBoxBanKuiying)
        )
        if mul == 0:
            return
        self.add_score_change("禁用干员", "最终乘算", mul, is_multi=True)

    @Slot()
    def on_pushButtonClearBan_clicked(self):
        for widget in self.frameBan.findChildren(QCheckBox):
            widget.setCheckState(Qt.CheckState.Unchecked)


def clear_splash():
    if "NUITKA_ONEFILE_PARENT" in os.environ:
        splash_filename = os.path.join(
            tempfile.gettempdir(),
            "onefile_%d_splash_feedback.tmp" % int(os.environ["NUITKA_ONEFILE_PARENT"]),
        )
        if os.path.exists(splash_filename):
            os.unlink(splash_filename)


def main() -> int:
    argv = sys.argv
    argv += [
        "-platform",
        "windows:darkmode=2",
        "--style",
        "Windows",
    ]
    app = QApplication(argv)
    win = MainWindow()
    qdarktheme.setup_theme(
        theme="dark",
        custom_colors={
            "primary": "#FF5252",
            "background": "#1F1C1C",
            "foreground": "#F5F5F5",
        },
    )
    win.show()
    clear_splash()
    return app.exec()


if __name__ == "__main__":
    main()
