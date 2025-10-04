import datetime
import os
import re
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
    QCheckBox,  # noqa: F401
    QComboBox,
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
VERSION = "1.3.2"
MINIMUM_DB_VERSION = "1.3.0"
AVATAR_SIZE = 140  # 软件内头像大小
OBS_AVATAR_SIZE = 224  # OBS头像大小
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
    base_score: float = 0  # 基础分数
    score: float = 0  # 总分
    start_operator: str = ""  # 开局干员
    start_team: str = ""  # 开局队伍
    cup: str = ""  # 杯数
    team: str = ""  # 队伍
    select: str = ""  # 选择
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
            f"罗德岛裁判终端 Beta - 那啥杯#2/萨卡兹的无终奇语 - {VERSION} by Ellu"
        )
        self.setWindowIcon(QIcon(os.path.join(PATH, "icon.png")))

        self.pushButtonSyncOBS.setEnabled(False)

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

        self.register_team_score_change()

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
        clear = False
        with shelve.open(DATABASE_PATH) as db:
            if "__version__" in db and db["__version__"] != VERSION:
                logger.warning(
                    f"Database version mismatch, expect {VERSION}, got {db['__version__']}"
                )
                a, b, c = db["__version__"].split(".")
                a1, b1, c1 = int(a), int(b), int(c)
                a, b, c = MINIMUM_DB_VERSION.split(".")
                a2, b2, c2 = int(a), int(b), int(c)
                if a1 < a2 or b1 < b2 or c1 < c2:
                    logger.error(
                        "Database version lower than minimum version, clear database"
                    )
                    ret = QMessageBox.question(
                        self,
                        "数据库版本过低",
                        "数据库版本低于兼容版本, 是否清除数据库?\n(如不清除,软件将退出)",
                        QMessageBox.Yes | QMessageBox.No,
                        QMessageBox.Yes,
                    )
                    if ret != QMessageBox.Yes:
                        sys.exit(0)
                    clear = True
        with shelve.open(DATABASE_PATH, "n" if clear else "r") as db:
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
            self.obs.a.set_player(self.player_now.name, self.avatar_obs_path)
        self.obs.a.set_metadata(
            os.path.join(START_TEAM_PATH, f"{self.record.start_team}.png")
            if self.record.start_team
            else "",
            os.path.join(START_OPERATOR_PATH, f"{self.record.start_operator}.png")
            if self.record.start_operator
            else "",
            self.record.cup,
            self.record.team,
            self.record.select,
            self.lineEditSpeaker.text(),
        )

    def sync_obs_score(self):
        return
        if not self.connected:
            return
        details = [item for item in self.record.data if "<无效>" not in item]
        total = self.record.score
        self.obs.a.display_score(details, total)

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
        self.sync_obs_score()
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
            self.labelAvatar.setText(
                "未找到头像\n请将同名图片放入\nark_data/avatar\n文件夹中"
            )
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
        if len(self.record.data) == 0 or not self.record.data[0].startswith("基础分数"):
            self.record.data.insert(0, "基础分数 0")
        for item in self.record.data:
            self.listRecord.addItem(item)

        def load_op(combo: QComboBox, op: str):
            if op in [combo.itemText(i) for i in range(combo.count())]:
                combo.setCurrentText(op)
            else:
                combo.setCurrentIndex(0)

        load_op(self.comboBoxStartOperator, self.record.start_operator)

        if self.record.start_team in [
            self.comboBoxStartTeam.itemText(i)
            for i in range(self.comboBoxStartTeam.count())
        ]:
            self.comboBoxStartTeam.setCurrentText(self.record.start_team)
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
        self.record.data.append("基础分数 0")
        self.record.base_score = 0
        self.record.score = 0
        self.record.time = 0
        self.record.start_operator = ""
        self.record.start_team = ""
        self.spinBoxBaseScore.setValue(0)
        self.listRecord.clear()
        self.listRecord.addItem(f"基础分数 {self.record.base_score}")
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
        if name == "未知":
            name = ""
        self.record.start_operator = name
        logger.info(f"Start operator updated: {name}")

    @Slot(int)
    def on_comboBoxStartTeam_currentIndexChanged(self, index: int):
        name = self.comboBoxStartTeam.currentText()
        if name == "未知":
            name = ""
        self.record.start_team = name
        logger.info(f"Start team updated: {name}")

    @Slot(int)
    def on_comboBoxCup_currentIndexChanged(self, index: int):
        self.record.cup = self.comboBoxCup.currentText()
        logger.info(f"Cup updated: {self.record.cup}")

    @Slot()
    def on_lineEditPlayerTeam_textChanged(self):
        self.record.team = self.lineEditPlayerTeam.text().strip()
        logger.info(f"Team updated: {self.record.team}")

    @Slot()
    def on_lineEditPlayerSelect_textChanged(self):
        self.record.select = self.lineEditPlayerSelect.text().strip()
        logger.info(f"Select updated: {self.record.select}")

    @Slot()
    def on_pushButtonSyncOBS_clicked(self):
        self.sync_obs_player_info()
        self.sync_obs_score()

    # listRecord 删除
    def __list_del_item(self):
        row = self.listRecord.currentRow()
        cnt = self.listRecord.count()
        if cnt == 0:
            return
        if row == -1:
            row = cnt - 1
        if self.listRecord.item(row).text().startswith("基础分数"):
            return
        self.listRecord.takeItem(row)
        self.record.data.pop(row)
        self.record.time = int(datetime.datetime.now().timestamp())
        self.listRecord.setCurrentRow(max(row - 1, 0))
        self.recalc_score()

    @Slot(QPoint)  # listRecord 右键菜单
    def on_listRecord_customContextMenuRequested(self, pos: QPoint):
        # 如果列表没有选中项目则拒绝
        menu = QMenu()
        menu.addAction("删除", self.__list_del_item)
        if self.listRecord.currentRow() == -1 or (
            self.listRecord.item(self.listRecord.currentRow())
            .text()
            .startswith("基础分数")
        ):
            menu.actions()[0].setEnabled(False)
        menu.exec(self.listRecord.mapToGlobal(pos))

    def recalc_score(self):
        score = self.record.base_score
        score_multi = []
        for i in range(self.listRecord.count()):
            item = self.listRecord.item(i)
            text = item.text()
            if "<无效>" in text:
                continue
            if text.startswith("基础分数"):
                continue
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
        self.sync_obs_score()
        ###### 以下为额外逻辑 ######
        six, five, four = 0, 0, 0
        for text in self.record.data:
            if "六星" in text:
                six += 1
            elif "五星" in text:
                five += 1
            elif "四星" in text:
                four += 1
        self.labelHeaderTemp.setText(f"[总数] 六星: {six} 五星: {five} 四星: {four}")
        kill = 0
        for text in self.record.data:
            if "特殊击杀" in text:  # 特殊击杀 X只
                kill += int(re.findall(r"(\d+)只", text)[0])
        self.labelHeaderkillSp.setText(f"[总数] 击杀 {kill} 只鸭/狗/熊")

    def add_score_change(
        self, text: str, change: float, is_multi: bool = False, invalid: bool = False
    ):
        if is_multi:
            text += f" 最终x{change+1:.4f}".rstrip("0").rstrip(".")
            change = 0
        else:
            text += f" {change:+}"
        if invalid:
            text = f"<无效> {text}"
        self.listRecord.addItem(text)
        self.listRecord.setCurrentRow(self.listRecord.count() - 1)
        self.record.data.append(text)
        self.record.valid = True
        self.record.time = int(datetime.datetime.now().timestamp())
        logger.info(f"Score change added: {text}")
        self.recalc_score()

    def invalid_score_record(self, key: str):
        for i in range(1, self.listRecord.count()):
            if self.listRecord.item(i).text().startswith(key):
                item = self.listRecord.item(i)
                item.setText(f"<无效> {item.text()}")
                self.record.data[i] = f"<无效> {self.record.data[i]}"
                break

    @Slot()
    def on_spinBoxBaseScore_editingFinished(self):
        self.record.base_score = self.spinBoxBaseScore.value()
        if self.record.data[0].startswith("基础分数"):
            self.record.data[0] = f"基础分数 {self.record.base_score}"
        else:
            self.record.data.insert(0, f"基础分数 {self.record.base_score}")
        self.record.time = int(datetime.datetime.now().timestamp())
        self.record.valid = True
        if self.listRecord.count() > 0:
            item = self.listRecord.item(0)
            if item.text().startswith("基础分数"):
                item.setText(f"基础分数 {self.record.base_score}")
            else:
                self.listRecord.insertItem(0, f"基础分数 {self.record.base_score}")
        else:
            self.listRecord.addItem(f"基础分数 {self.record.base_score}")
        logger.info(f"Base score changed to {self.record.base_score}")
        self.recalc_score()

    @Slot()
    def on_pushButtonConnect_clicked(self):
        if self.connected:
            self.obs.stop()
            self.pushButtonConnect.setText("连接OBS")
            self.connected = False
            self.labelConState.setText("/// PRTS 未连接 ///")
            self.labelConState.setStyleSheet("")
            self.pushButtonSyncOBS.setEnabled(False)
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
            self.sync_obs_score()
            self.pushButtonSyncOBS.setEnabled(True)

    @Slot()
    def on_checkBoxPause_toggled(self):
        if not self.connected:
            return
        self.obs.set_pause(self.checkBoxPause.isChecked())
        if not self.checkBoxPause.isChecked():
            self.sync_obs_player_info()
            self.sync_obs_score()

    ############## 以下为分数逻辑 ##############

    @Slot(int)
    def on_comboBoxEmerg_currentIndexChanged(self, index: int):
        text = self.comboBoxEmerg.currentText()
        self.pushButtonSubmitEmerg.setEnabled("—" not in text)

    @Slot(int)
    def on_comboBoxEnding_currentIndexChanged(self, index: int):
        text = self.comboBoxEnding.currentText()
        self.comboBoxEndingEx.clear()
        if text not in ["圣城", "授法", "不容拒绝"]:
            for i in ["普通", "紧急"]:
                self.comboBoxEndingEx.addItem(i)
        else:
            if text == "圣城":
                pass
            elif text == "授法":
                for i in ["通关", "击杀一阶段", "击杀二阶段"]:
                    self.comboBoxEndingEx.addItem(i)
            else:
                for i in ["终结的骨架", "终结的躯体", "终结的实相"]:
                    self.comboBoxEndingEx.addItem(i)
        self.comboBoxEndingEx.setCurrentIndex(0)
        if self.comboBoxEndingEx.count() == 0:
            self.comboBoxEndingEx.setEnabled(False)
        else:
            self.comboBoxEndingEx.setEnabled(True)
        self.checkBoxEndingChaos.setChecked(False)

    @Slot()
    def on_pushButtonSubmitCustom_clicked(self):
        text = self.lineEditCustomScore.text()
        if not text:
            QMessageBox.warning(self, "不许黑幕", "请给出打分理由")
            return
        self.add_score_change(text, self.spinBoxCustomScore.value())

    @Slot()
    def on_pushButtonSubmitTemp_clicked(self):
        if self.radioButtonTempSix.isChecked():
            score = 30
            text = "临招六星"
        elif self.radioButtonTempFive.isChecked():
            score = 20
            text = "临招五星"
        elif self.radioButtonTempFour.isChecked():
            score = 10
            text = "临招四星"
        else:
            return
        self.add_score_change(text, score)

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
        sp_score_dict = {
            "紧急劫虚济实无漏": 20,
            "紧急战场侧面": 50,
            "斩首": 10,
            "奉献": 10,
            "或然面纱": 20,
            "离歌的庭院": 40,
            "赴敌者": 40,
            "王冠之下": 40,
        }
        emer_score_dict = {
            "大棋一盘": 10,
            "溃乱魔典": 15,
            "机动队": 15,
            "假想对冲": 10,
            "年代断层": 15,
            "猩红甬道": 25,
            "混沌": 35,
            "神出鬼没": 50,
            "争议频发": 60,
            "通道封锁": 20,
            "寄人城池下": 30,
            "计划耕种": 50,
            "莱茵卫士": 70,
            "建制": 80,
            "神圣的渴求": 50,
            "谋求共识": 60,
            "外道": 70,
            "洞天福地": 100,
        }
        if text in sp_score_dict:
            score = sp_score_dict[text]
            emer = False
        elif text in emer_score_dict:
            score = emer_score_dict[text]
            emer = True
        else:
            raise ValueError(f"事件 {text} 未找到")
        if emer:
            text = f"紧急: {text}"
            # 检索所有已存在的紧急记录
            emer_list = []

            def parse_emer_score(text: str):
                return int(re.findall(r"\+(\d+)", text)[0])

            for item in self.record.data:
                if item.startswith("紧急: "):
                    emer_list.append(
                        (item.split("+")[0].strip(), parse_emer_score(item))
                    )

            # 按加分从高到低排序
            emer_list.sort(key=lambda x: x[1], reverse=True)
            logger.info(f"紧急记录: {emer_list} 本次: {text}")

            if sum(1 for item in emer_list if item[0] == text) >= 2:
                self.add_score_change(text, score, invalid=True)
                return

            if len(emer_list) >= 10:
                if emer_list[-1][1] >= score:  # 最低分已经高于本次分数
                    self.add_score_change(text, score, invalid=True)
                    return
                # 无效化最低分记录
                self.invalid_score_record(emer_list[-1][0])

        self.add_score_change(text, score)

    @Slot()
    def on_pushButtonSubmitKillSp_clicked(self):
        val = self.spinBoxKillSp.value()
        score = 20 * val
        self.add_score_change(f"特殊击杀{val}只", score)

    @Slot()
    def on_pushButtonSubmitEnding_clicked(self):
        text = self.comboBoxEnding.currentText()
        textex = self.comboBoxEndingEx.currentText()
        if not textex:
            all = text
        else:
            all = f"{text} ({textex})"
        score = {
            "紧急授课 (普通)": 50,
            "紧急授课 (紧急)": 80,
            "朝谒 (普通)": 100,
            "朝谒 (紧急)": 150,
            "思维矫正 (普通)": 150,
            "思维矫正 (紧急)": 180,
            "魂灵朝谒 (普通)": 200,
            "魂灵朝谒 (紧急)": 250,
            "圣城": 100,
            "授法 (通关)": 150,
            "授法 (击杀一阶段)": 300,
            "授法 (击杀二阶段)": 100,
            "不容拒绝 (终结的骨架)": 350,
            "不容拒绝 (终结的躯体)": 400,
            "不容拒绝 (终结的实相)": 650,
        }[all]
        chaos = self.checkBoxEndingChaos.isChecked()
        if chaos:
            if text in ["紧急授课", "朝谒", "思维矫正"]:
                score += 10
            elif text == "圣城":
                score += 20
            elif text == "魂灵朝谒":
                score += 40
            elif text == "授法":
                score += 80
            elif text == "不容拒绝":
                score += 150 if "终结的实相" in all else 100
        title = f"结局: {all}" + (" (混乱)" if chaos else "")
        self.add_score_change(title, score)

    @Slot()
    def on_pushButtonSubmitSp_clicked(self):
        if self.radioButtonSpDsb.isChecked():
            self.add_score_change('"大啥杯"进入六层关底', 0.3, True)
        elif self.radioButtonSpSsef.isChecked():
            self.add_score_change("似是而非补偿分", 100)
        elif self.radioButtonSpRed.isChecked():
            self.add_score_change("技术违规", -500)

    def recalc_team_score(self, _=None):
        score = (
            self.doubleSpinBoxTeamScore_1.value()
            + self.doubleSpinBoxTeamScore_2.value()
            + self.doubleSpinBoxTeamScore_3.value()
            + self.doubleSpinBoxTeamScore_4.value()
            + self.doubleSpinBoxTeamScore_5.value()
        )
        if self.checkBoxTeam4End.isChecked():
            score += 1000
        if self.spinBoxTeamGdxz.value() > 0:
            score += {
                1: 300,
                2: 500,
                3: 700,
            }.get(self.spinBoxTeamGdxz.value(), 700)
        score -= 100 * self.spinBoxTeamQqcz.value()
        score -= 300 * self.spinBoxTeamDup.value()
        score -= 600 * self.spinBoxTeamDupEw.value()
        self.labelTeamScore.setText(f"{score:.4f}".rstrip("0").rstrip("."))

    def register_team_score_change(self):
        for spinbox in [
            self.doubleSpinBoxTeamScore_1,
            self.doubleSpinBoxTeamScore_2,
            self.doubleSpinBoxTeamScore_3,
            self.doubleSpinBoxTeamScore_4,
            self.doubleSpinBoxTeamScore_5,
        ]:
            spinbox.valueChanged.connect(self.recalc_team_score)
        self.spinBoxTeamGdxz.valueChanged.connect(self.recalc_team_score)
        self.spinBoxTeamQqcz.valueChanged.connect(self.recalc_team_score)
        self.spinBoxTeamDup.valueChanged.connect(self.recalc_team_score)
        self.spinBoxTeamDupEw.valueChanged.connect(self.recalc_team_score)
        self.checkBoxTeam4End.stateChanged.connect(self.recalc_team_score)


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
    additional_qss = (
        "QToolTip {"
        "   color: rgb(228, 231, 235);"
        "   background-color: rgb(32, 33, 36);"
        "   border: 1px solid rgb(63, 64, 66);"
        "   border-radius: 4px;"
        "}"
        "QSlider::add-page:horizontal {"
        "   background: #36ff8888;"
        "}"
        "QSlider::sub-page:horizontal {"
        "   background: #368888ff;"
        "}"
    )
    qdarktheme.setup_theme(
        theme="dark",
        custom_colors={
            "primary": "#FF5252",
            "background": "#1F1C1C",
            "foreground": "#F5F5F5",
        },
        additional_qss=additional_qss,
    )
    win.show()
    clear_splash()
    return app.exec()


if __name__ == "__main__":
    main()
