import datetime
import os
import shelve
import sys
import tempfile
import time
import uuid
from copy import copy
from dataclasses import dataclass

from loguru import logger
from PySide6 import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtMultimedia import *
from PySide6.QtMultimediaWidgets import *
from PySide6.QtWidgets import *

from log_redirect import redirect_logging
from ui import MainUITemplate

"""
qdarktheme import after QT
"""
import qdarktheme

UUID_NAMESPACE = uuid.UUID("1b671a64-40d5-491e-99b0-da01ff1f3341")
VERSION = "0.3.0"
AVATAR_SIZE = 128  # 软件内头像大小
OBS_AVATAR_SIZE = 512  # OBS头像大小
DARK_THEME = True  # 是否使用暗色主题
MAX_SLOT = 16  # 最大记录槽位
DEFAULT_NOTE = "无备注信息"  # 默认备注信息
DATA_DIR_NAME = "ark_data"  # 数据文件夹
AVATAR_DIR_NAME = "avatar"  # 头像文件夹
OBS_TEMP_DIR_NAME = "obs_temp"  # OBS素材临时文件夹
LOGFILE_NAME = "log.txt"  # 日志文件名
DATABASE_NAME = "players.db"  # 数据库前缀
DATABASE_BACKUP_NAME = "players_backup.db"  # 数据库备份前缀

PATH = os.path.dirname(os.path.abspath(__file__))  # 打包后的临时路径
ARGV_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))  # 实际上的运行路径

DATA_PATH = os.path.join(ARGV_PATH, DATA_DIR_NAME)
AVATAR_PATH = os.path.join(DATA_PATH, AVATAR_DIR_NAME)
OBS_TEMP_PATH = os.path.join(DATA_PATH, OBS_TEMP_DIR_NAME)
DATABASE_PATH = os.path.join(DATA_PATH, DATABASE_NAME)
DATABASE_BACKUP_PATH = os.path.join(DATA_PATH, DATABASE_BACKUP_NAME)
LOGFILE_PATH = os.path.join(DATA_PATH, LOGFILE_NAME)

if not os.path.exists(DATA_PATH):
    os.makedirs(DATA_PATH)
if not os.path.exists(AVATAR_PATH):
    os.makedirs(AVATAR_PATH)
if not os.path.exists(OBS_TEMP_PATH):
    os.makedirs(OBS_TEMP_PATH)

logger.remove()
logger.add(LOGFILE_PATH, level="DEBUG")
if os.path.samefile(PATH, ARGV_PATH):  # 直接运行
    logger.add(sys.stderr, level="DEBUG")

redirect_logging("DEBUG")

generate_uuid = lambda name: str(
    uuid.uuid5(UUID_NAMESPACE, name + str(datetime.datetime.now()))
)


@dataclass
class Record:
    data: list[str]  # 记录数据
    base_score: int = 0  # 基础分
    score: int = 0  # 总分
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
    "超大杯, 信我!",
    generate_uuid("临时招募·迷迭香"),
    [Record(list()) for _ in range(MAX_SLOT)],
)


class MainWindow(QMainWindow, MainUITemplate):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle(f"罗德岛裁判终端 Beta - 萨米肉鸽 - {VERSION} by Ellu")
        self.setWindowIcon(QIcon(os.path.join(PATH, "icon.png")))

        self.players: dict[str, Player] = {}

        for i in range(MAX_SLOT):
            self.comboBoxSelRecord.addItem(f"{i+1}")
        self.frameAvatar.setMinimumSize(AVATAR_SIZE + 8, AVATAR_SIZE + 8)

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
        self.save_database()
        event.accept()

    def load_database(self):
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
        t0 = time.perf_counter()
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
        t1 = time.perf_counter()
        logger.info(f"Database saved, cost {t1-t0:.5f}s")
        # logger.debug(f"Players={self.players}")

    def update_player_info(self):
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

    def load_player(self, name: str):
        if name not in self.players:
            logger.warning(f"Player {name} not found")
            return
        logger.info(f"Loading player {name}")
        self.player_now = self.players[name]
        self.load_avatar()
        self.update_player_info()
        self.comboBoxSelRecord.setCurrentIndex(-1)
        self.comboBoxSelRecord.setCurrentIndex(0)
        # will call on_comboBoxSelRecord_currentIndexChanged

    def load_avatar(self):
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
            OBS_TEMP_PATH, f"resized_avatar_{self.player_now.uuid}.png"
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
        logger.info(f"Loading record {index+1} for {self.player_now.name}")
        self.record = self.player_now.records[index]
        self.listRecord.clear()
        for item in self.record.data:
            self.listRecord.addItem(item)
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
        score_multi = 0
        for i in range(self.listRecord.count()):
            item = self.listRecord.item(i)
            text = item.text()
            if "x" in text:
                score_multi += float(text.split("x")[-1])
            elif "+" in text:
                score += int(text.split("+")[-1])
            elif "-" in text:
                score -= int(text.split("-")[-1])
        if score_multi != 0:
            score *= 1 + score_multi
        self.labelScore.setText(f"{score:.4f}".rstrip("0").rstrip("."))
        self.record.score = score
        self.update_player_info()
        logger.info(f"Score recalculated: {score:.4f}")
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
            text += f" x{change:.4f}".rstrip("0").rstrip(".")
        else:
            text += f" {change:+}"
        self.listRecord.addItem(text)
        self.record.data.append(text)
        self.record.valid = True
        self.record.time = int(datetime.datetime.now().timestamp())
        logger.info(f"Score change added: {text}")
        self.recalc_score()

    @Slot()
    def on_spinBoxBaseScore_editingFinished(self):
        self.record.base_score = self.spinBoxBaseScore.value()
        logger.info(f"Base score changed to {self.record.base_score}")
        self.recalc_score()

    ############## 以下为分数逻辑 ##############

    @Slot(int)
    def on_comboBoxKillSp_currentIndexChanged(self, index: int):
        text = self.comboBoxKillSp.currentText()
        self.checkBoxKillSpPerfect.setEnabled(text in ["正义使者", "英雄无名"])
        if text == "豪华车队":
            self.labelKillSp.setText("击杀熊")
            self.spinBoxKillSp.setValue(1)
            self.spinBoxKillSp.setEnabled(False)
        else:
            self.spinBoxKillSp.setEnabled(True)
            self.spinBoxKillSp.setValue(0)
            self.labelKillSp.setText(
                "击杀敌人" if text == "英雄无名" else "击杀狗/鸭/熊"
            )

    def __check_slzt(self):
        self.checkBoxEndingNoSlzt.setEnabled(
            self.comboBoxEnding2.currentText() == "自深处的一瞥"
            and self.comboBoxEnding3.currentText() == "终始"
        )

    @Slot(int)
    def on_comboBoxEnding2_currentIndexChanged(self, index: int):
        self.__check_slzt()

    @Slot(int)
    def on_comboBoxEnding3_currentIndexChanged(self, index: int):
        self.__check_slzt()

    @Slot(int)
    def on_comboBoxEmerg_currentIndexChanged(self, index: int):
        text = self.comboBoxEmerg.currentText()
        con = text in ["冰海疑影", "乐理之灾", "公司纠葛", "人造物狂欢节", "亡者行军"]
        self.checkBoxEmergHasLw.setEnabled(con)
        if not con:
            self.checkBoxEmergHasLw.setChecked(False)

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
        text = self.comboBoxEmerg.currentText()
        add = self.checkBoxEmergHasLw.isChecked()
        score_dict = {
            "冰海疑影": 30 if add else 20,
            "公司纠葛": 30 if add else 20,
            "坍缩体的午后": 20,
            "人造物狂欢节": 110 if add else 90,
            "本能污染": 50,
            "亡者行军": 70 if add else 50,
            "乐理之灾": 55 if add else 35,
            "生灵的终点": 90,
            "BOSS-大地醒转": 50,
            "BOSS-呼吸": 50,
            "BOSS-夺树者": 50,
        }
        self.add_score_change(
            ("紧急关卡" if not text.startswith("BOSS-") else "隐藏BOSS")
            + (" (路网无漏)" if add else ""),
            text.replace("BOSS-", ""),
            score_dict[text],
        )

    @Slot()
    def on_pushButtonSubmitKillSp_clicked(self):
        val = self.spinBoxKillSp.value()
        perfect = self.checkBoxKillSpPerfect.isChecked()
        text = self.comboBoxKillSp.currentText()
        if text == "普通关卡":
            score = 20 * val
            text1 = "击杀狗/鸭/熊"
            text2 = f"{val}只"
        elif text == "豪华车队":
            score = 40 * val
            text1 = "豪华车队"
            text2 = "击杀熊"
        elif text == "正义使者":
            text1 = "正义使者"
            if perfect:
                score = 200
                text2 = "无漏通关"
            else:
                score = 70 + 30 * val
                text2 = f"狗/鸭/熊{val}只"
        elif text == "英雄无名":
            text1 = "英雄无名"
            if perfect:
                score = 150
                text2 = "无漏通关"
            else:
                score = 30 + 15 * val
                text2 = f"击杀{val}敌人"
        else:
            return
        if score == 0:
            return
        self.add_score_change(text1, text2, score)

    @Slot()
    def on_pushButtonSubmitEndStage_clicked(self):
        text = self.comboBoxEndStage.currentText()
        score_dict = {
            "萨米之熵": 30,
            "深寒造像": 150,
            "园丁": 100,
            "虚无之偶": 120,
            "迈入永恒": 150,
            "哨兵": 300,
            "时光之沙": 100,
        }
        self.add_score_change("结局关卡", text, score_dict[text])

    @Slot()
    def on_pushButtonSubmitEnding_clicked(self):
        text1 = self.comboBoxEnding1.currentText()
        text2 = self.comboBoxEnding2.currentText()
        text3 = self.comboBoxEnding3.currentText()
        score = 0
        if (
            text3 == "终始"
            and text2 == "自深处的一瞥"
            and self.checkBoxEndingNoSlzt.isChecked()
        ):
            score += 150
        if (text3 == "终始" or text2 == "自深处的一瞥") and text1 == "直至冬夜降临":
            score += 100
        if (
            text3 == "终始" or text2 == "自深处的一瞥"
        ) and text1 == "越过群山<深寒造像>":
            score += 100
        text = text1
        if text2 != "未达成":
            text = text2
        if text3 != "未达成":
            text = text3
        self.add_score_change("达成结局", text, score)

    @Slot()
    def on_pushButtonSubmitSum_clicked(self):
        ter = self.spinBoxSumTreasure.value()
        table = self.spinBoxSumTable.value()
        wyzl = self.checkBoxSumHasWyzl.isChecked()
        score = 10 * ter + 5 * table + (50 if wyzl else 0)
        self.add_score_change(
            "最终结算",
            f"藏品:{ter} 密文板:{table}" + (" 无垠赠礼" if wyzl else ""),
            score,
        )

    @Slot()
    def on_pushButtonSubmitBan_clicked(self):
        mul = 0
        if self.checkBoxBanWsde.isChecked():
            mul += 0.08
        if self.checkBoxBanJmdkss.isChecked() and self.checkBoxBanQlryd.isChecked():
            mul += 0.06
        elif self.checkBoxBanJmdkss.isChecked():
            mul += 0.02
        elif self.checkBoxBanQlryd.isChecked():
            mul += 0.02
        mul += 0.03 * (
            int(self.checkBoxBanJian.isChecked())
            + int(self.checkBoxBanMen.isChecked())
            + int(self.checkBoxBanAl.isChecked())
            + int(self.checkBoxBanYns.isChecked())
        )
        mul += 0.02 * (
            int(self.checkBoxBanYywc.isChecked())
            + int(self.checkBoxBanCjayfl.isChecked())
            + int(self.checkBoxBanLogos.isChecked())
            + int(self.checkBoxBanLy.isChecked())
        )
        if mul == 0:
            return
        self.add_score_change("禁用干员", "最终乘算", mul, is_multi=True)

    @Slot()
    def on_pushButtonReverseBan_clicked(self):
        # 反选全部checkbox
        for widget in self.frameBan.findChildren(QCheckBox):
            widget.setChecked(not widget.isChecked())


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
    if DARK_THEME:
        argv += [
            "-platform",
            "windows:darkmode=2",
            "--style",
            "Windows",
        ]  # or "Fusion" ?
    app = QApplication(argv)
    win = MainWindow()
    qdarktheme.setup_theme(theme="dark" if DARK_THEME else "light")
    win.show()
    clear_splash()
    return app.exec()


if __name__ == "__main__":
    main()
