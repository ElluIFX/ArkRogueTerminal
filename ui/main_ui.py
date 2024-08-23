# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QListView, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(886, 800)
        MainWindow.setMinimumSize(QSize(886, 800))
        MainWindow.setMaximumSize(QSize(886, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_7 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_7 = QHBoxLayout(self.frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, 0, 0)
        self.frameAvatar = QFrame(self.frame)
        self.frameAvatar.setObjectName(u"frameAvatar")
        self.frameAvatar.setMinimumSize(QSize(120, 120))
        self.frameAvatar.setFrameShape(QFrame.StyledPanel)
        self.frameAvatar.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frameAvatar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.labelAvatar = QLabel(self.frameAvatar)
        self.labelAvatar.setObjectName(u"labelAvatar")
        self.labelAvatar.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.labelAvatar.setFont(font1)
        self.labelAvatar.setScaledContents(True)
        self.labelAvatar.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.labelAvatar)


        self.verticalLayout_21.addWidget(self.frameAvatar)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_21.addItem(self.verticalSpacer)


        self.horizontalLayout_6.addLayout(self.verticalLayout_21)

        self.horizontalSpacer_3 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        font2 = QFont()
        font2.setPointSize(9)
        font2.setBold(False)
        font2.setItalic(False)
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font2)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEditPlayerName = QLineEdit(self.frame)
        self.lineEditPlayerName.setObjectName(u"lineEditPlayerName")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPlayerName.sizePolicy().hasHeightForWidth())
        self.lineEditPlayerName.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setPointSize(10)
        self.lineEditPlayerName.setFont(font3)
        self.lineEditPlayerName.setFocusPolicy(Qt.ClickFocus)
        self.lineEditPlayerName.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEditPlayerName)

        self.lineEditPlayerNote = QLineEdit(self.frame)
        self.lineEditPlayerNote.setObjectName(u"lineEditPlayerNote")
        sizePolicy.setHeightForWidth(self.lineEditPlayerNote.sizePolicy().hasHeightForWidth())
        self.lineEditPlayerNote.setSizePolicy(sizePolicy)
        self.lineEditPlayerNote.setFont(font3)
        self.lineEditPlayerNote.setFocusPolicy(Qt.ClickFocus)
        self.lineEditPlayerNote.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lineEditPlayerNote)

        self.labelPlayerUUID = QLabel(self.frame)
        self.labelPlayerUUID.setObjectName(u"labelPlayerUUID")
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(False)
        font4.setItalic(False)
        self.labelPlayerUUID.setFont(font4)
        self.labelPlayerUUID.setFrameShape(QFrame.Box)
        self.labelPlayerUUID.setScaledContents(False)
        self.labelPlayerUUID.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelPlayerUUID)

        self.labelPlayerLastSaveTime = QLabel(self.frame)
        self.labelPlayerLastSaveTime.setObjectName(u"labelPlayerLastSaveTime")
        self.labelPlayerLastSaveTime.setFont(font4)
        self.labelPlayerLastSaveTime.setFrameShape(QFrame.Box)
        self.labelPlayerLastSaveTime.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelPlayerLastSaveTime)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_14)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_12)

        self.label_28 = QLabel(self.frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)
        self.label_28.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_29)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.labelPlayerRecordNum = QLabel(self.frame)
        self.labelPlayerRecordNum.setObjectName(u"labelPlayerRecordNum")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.labelPlayerRecordNum.setFont(font5)
        self.labelPlayerRecordNum.setFrameShape(QFrame.Box)
        self.labelPlayerRecordNum.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelPlayerRecordNum)

        self.labelPlayerMaxRecord = QLabel(self.frame)
        self.labelPlayerMaxRecord.setObjectName(u"labelPlayerMaxRecord")
        self.labelPlayerMaxRecord.setFont(font5)
        self.labelPlayerMaxRecord.setFrameShape(QFrame.Box)
        self.labelPlayerMaxRecord.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.labelPlayerMaxRecord)

        self.comboBoxStartTeam = QComboBox(self.frame)
        self.comboBoxStartTeam.addItem("")
        self.comboBoxStartTeam.setObjectName(u"comboBoxStartTeam")
        self.comboBoxStartTeam.setMaxVisibleItems(20)

        self.verticalLayout_4.addWidget(self.comboBoxStartTeam)

        self.comboBoxStartOperator = QComboBox(self.frame)
        self.comboBoxStartOperator.addItem("")
        self.comboBoxStartOperator.setObjectName(u"comboBoxStartOperator")
        self.comboBoxStartOperator.setMaxVisibleItems(20)

        self.verticalLayout_4.addWidget(self.comboBoxStartOperator)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 1)
        self.verticalLayout_4.setStretch(3, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalLayout_5.setStretch(1, 1)
        self.horizontalLayout_5.setStretch(3, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.comboBoxSelPlayer = QComboBox(self.frame)
        self.comboBoxSelPlayer.setObjectName(u"comboBoxSelPlayer")
        font6 = QFont()
        font6.setPointSize(9)
        self.comboBoxSelPlayer.setFont(font6)
        self.comboBoxSelPlayer.setFocusPolicy(Qt.ClickFocus)
        self.comboBoxSelPlayer.setMaxVisibleItems(20)

        self.horizontalLayout_4.addWidget(self.comboBoxSelPlayer)

        self.pushButtonAddPlayer = QPushButton(self.frame)
        self.pushButtonAddPlayer.setObjectName(u"pushButtonAddPlayer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButtonAddPlayer.sizePolicy().hasHeightForWidth())
        self.pushButtonAddPlayer.setSizePolicy(sizePolicy1)
        self.pushButtonAddPlayer.setMaximumSize(QSize(50, 28))
        font7 = QFont()
        font7.setPointSize(9)
        font7.setItalic(False)
        font7.setUnderline(False)
        font7.setStrikeOut(False)
        self.pushButtonAddPlayer.setFont(font7)
        self.pushButtonAddPlayer.setFocusPolicy(Qt.ClickFocus)
        self.pushButtonAddPlayer.setStyleSheet(u"color: #94bf79")

        self.horizontalLayout_4.addWidget(self.pushButtonAddPlayer)

        self.pushButtonDelPlayer = QPushButton(self.frame)
        self.pushButtonDelPlayer.setObjectName(u"pushButtonDelPlayer")
        sizePolicy1.setHeightForWidth(self.pushButtonDelPlayer.sizePolicy().hasHeightForWidth())
        self.pushButtonDelPlayer.setSizePolicy(sizePolicy1)
        self.pushButtonDelPlayer.setMaximumSize(QSize(50, 28))
        self.pushButtonDelPlayer.setFont(font7)
        self.pushButtonDelPlayer.setFocusPolicy(Qt.ClickFocus)
        self.pushButtonDelPlayer.setStyleSheet(u"color: #d86a74")

        self.horizontalLayout_4.addWidget(self.pushButtonDelPlayer)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.comboBoxSelRecord = QComboBox(self.frame)
        self.comboBoxSelRecord.setObjectName(u"comboBoxSelRecord")
        self.comboBoxSelRecord.setMinimumSize(QSize(70, 0))
        self.comboBoxSelRecord.setFocusPolicy(Qt.ClickFocus)
        self.comboBoxSelRecord.setMaxVisibleItems(20)
        self.comboBoxSelRecord.setFrame(True)

        self.horizontalLayout_4.addWidget(self.comboBoxSelRecord)

        self.pushButtonClrRecord = QPushButton(self.frame)
        self.pushButtonClrRecord.setObjectName(u"pushButtonClrRecord")
        sizePolicy1.setHeightForWidth(self.pushButtonClrRecord.sizePolicy().hasHeightForWidth())
        self.pushButtonClrRecord.setSizePolicy(sizePolicy1)
        self.pushButtonClrRecord.setMaximumSize(QSize(16777215, 28))
        self.pushButtonClrRecord.setFont(font7)
        self.pushButtonClrRecord.setFocusPolicy(Qt.ClickFocus)
        self.pushButtonClrRecord.setStyleSheet(u"color: #d86a74")

        self.horizontalLayout_4.addWidget(self.pushButtonClrRecord)

        self.horizontalLayout_4.setStretch(1, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_6.setStretch(2, 1)

        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout_7.addLayout(self.verticalLayout_6)


        self.verticalLayout_7.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.verticalLayout_19 = QVBoxLayout(self.frame_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Plain)
        self.verticalLayout_8 = QVBoxLayout(self.frame_4)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 4, 4, 4)
        self.label_25 = QLabel(self.frame_4)
        self.label_25.setObjectName(u"label_25")
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setItalic(False)
        self.label_25.setFont(font8)
        self.label_25.setStyleSheet(u"color: #CC6E6E")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_25)

        self.labelHeaderTemp = QLabel(self.frame_4)
        self.labelHeaderTemp.setObjectName(u"labelHeaderTemp")
        self.labelHeaderTemp.setFont(font8)
        self.labelHeaderTemp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.labelHeaderTemp)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.radioButtonTempSix = QRadioButton(self.frame_4)
        self.radioButtonTempSix.setObjectName(u"radioButtonTempSix")

        self.horizontalLayout_11.addWidget(self.radioButtonTempSix)

        self.radioButtonTempFive = QRadioButton(self.frame_4)
        self.radioButtonTempFive.setObjectName(u"radioButtonTempFive")

        self.horizontalLayout_11.addWidget(self.radioButtonTempFive)

        self.radioButtonTempFour = QRadioButton(self.frame_4)
        self.radioButtonTempFour.setObjectName(u"radioButtonTempFour")

        self.horizontalLayout_11.addWidget(self.radioButtonTempFour)

        self.pushButtonSubmitTemp = QPushButton(self.frame_4)
        self.pushButtonSubmitTemp.setObjectName(u"pushButtonSubmitTemp")

        self.horizontalLayout_11.addWidget(self.pushButtonSubmitTemp)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 4)
        self.horizontalLayout_11.setStretch(2, 4)
        self.horizontalLayout_11.setStretch(3, 4)

        self.verticalLayout_8.addLayout(self.horizontalLayout_11)

        self.verticalLayout_8.setStretch(2, 1)

        self.horizontalLayout_22.addWidget(self.frame_4)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Plain)
        self.verticalLayout_13 = QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(4, 4, 4, 4)
        self.label_21 = QLabel(self.frame_9)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font8)
        self.label_21.setStyleSheet(u"color: #CC6E6E")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_21)

        self.comboBoxEmerg = QComboBox(self.frame_9)
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.addItem("")
        self.comboBoxEmerg.setObjectName(u"comboBoxEmerg")
        self.comboBoxEmerg.setMaxVisibleItems(20)

        self.verticalLayout_13.addWidget(self.comboBoxEmerg)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.checkBoxEmergBswLessFour = QCheckBox(self.frame_9)
        self.checkBoxEmergBswLessFour.setObjectName(u"checkBoxEmergBswLessFour")
        self.checkBoxEmergBswLessFour.setEnabled(False)
        self.checkBoxEmergBswLessFour.setStyleSheet(u"color: #EF9A9A")
        self.checkBoxEmergBswLessFour.setCheckable(True)

        self.horizontalLayout_16.addWidget(self.checkBoxEmergBswLessFour)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_4)

        self.pushButtonSubmitEmerg = QPushButton(self.frame_9)
        self.pushButtonSubmitEmerg.setObjectName(u"pushButtonSubmitEmerg")

        self.horizontalLayout_16.addWidget(self.pushButtonSubmitEmerg)


        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.verticalLayout_13.setStretch(1, 1)
        self.verticalLayout_13.setStretch(2, 1)

        self.horizontalLayout_22.addWidget(self.frame_9)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.verticalLayout_10 = QVBoxLayout(self.frame_6)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(4, 4, 4, 4)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font8)
        self.label_11.setStyleSheet(u"color: #CC6E6E")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.comboBoxKillSp = QComboBox(self.frame_6)
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.addItem("")
        self.comboBoxKillSp.setObjectName(u"comboBoxKillSp")

        self.horizontalLayout_12.addWidget(self.comboBoxKillSp)

        self.labelKillSp = QLabel(self.frame_6)
        self.labelKillSp.setObjectName(u"labelKillSp")
        self.labelKillSp.setFont(font2)
        self.labelKillSp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.labelKillSp)

        self.spinBoxKillSp = QSpinBox(self.frame_6)
        self.spinBoxKillSp.setObjectName(u"spinBoxKillSp")
        self.spinBoxKillSp.setMaximum(999)

        self.horizontalLayout_12.addWidget(self.spinBoxKillSp)

        self.checkBoxKillSpPerfect = QCheckBox(self.frame_6)
        self.checkBoxKillSpPerfect.setObjectName(u"checkBoxKillSpPerfect")
        self.checkBoxKillSpPerfect.setEnabled(False)
        self.checkBoxKillSpPerfect.setCheckable(True)

        self.horizontalLayout_12.addWidget(self.checkBoxKillSpPerfect)

        self.pushButtonSubmitKillSp = QPushButton(self.frame_6)
        self.pushButtonSubmitKillSp.setObjectName(u"pushButtonSubmitKillSp")

        self.horizontalLayout_12.addWidget(self.pushButtonSubmitKillSp)

        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(2, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.verticalLayout_10.setStretch(1, 1)

        self.verticalLayout_18.addWidget(self.frame_6)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, -1, -1, 0)
        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Plain)
        self.verticalLayout_14 = QVBoxLayout(self.frame_10)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(4, 4, 4, 4)
        self.label_22 = QLabel(self.frame_10)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font8)
        self.label_22.setStyleSheet(u"color: #CC6E6E")
        self.label_22.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_22)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.labelKillSp_2 = QLabel(self.frame_10)
        self.labelKillSp_2.setObjectName(u"labelKillSp_2")
        self.labelKillSp_2.setFont(font2)
        self.labelKillSp_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.labelKillSp_2)

        self.spinBoxEarlyEmerg = QSpinBox(self.frame_10)
        self.spinBoxEarlyEmerg.setObjectName(u"spinBoxEarlyEmerg")
        self.spinBoxEarlyEmerg.setMaximum(999)

        self.horizontalLayout_17.addWidget(self.spinBoxEarlyEmerg)

        self.pushButtonEarlyEmerg = QPushButton(self.frame_10)
        self.pushButtonEarlyEmerg.setObjectName(u"pushButtonEarlyEmerg")

        self.horizontalLayout_17.addWidget(self.pushButtonEarlyEmerg)

        self.horizontalLayout_17.setStretch(1, 1)

        self.verticalLayout_14.addLayout(self.horizontalLayout_17)

        self.verticalLayout_14.setStretch(1, 1)

        self.horizontalLayout_25.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Plain)
        self.verticalLayout_22 = QVBoxLayout(self.frame_11)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(4, 4, 4, 4)
        self.label_31 = QLabel(self.frame_11)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font8)
        self.label_31.setStyleSheet(u"color: #CC6E6E")
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_31)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.labelKillSp_3 = QLabel(self.frame_11)
        self.labelKillSp_3.setObjectName(u"labelKillSp_3")
        self.labelKillSp_3.setFont(font2)
        self.labelKillSp_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.labelKillSp_3)

        self.spinBoxMoneyOverflow = QSpinBox(self.frame_11)
        self.spinBoxMoneyOverflow.setObjectName(u"spinBoxMoneyOverflow")
        self.spinBoxMoneyOverflow.setMaximum(999)

        self.horizontalLayout_26.addWidget(self.spinBoxMoneyOverflow)

        self.pushButtonSubmitMoneyOverflow = QPushButton(self.frame_11)
        self.pushButtonSubmitMoneyOverflow.setObjectName(u"pushButtonSubmitMoneyOverflow")

        self.horizontalLayout_26.addWidget(self.pushButtonSubmitMoneyOverflow)

        self.horizontalLayout_26.setStretch(1, 1)

        self.verticalLayout_22.addLayout(self.horizontalLayout_26)

        self.verticalLayout_22.setStretch(1, 1)

        self.horizontalLayout_25.addWidget(self.frame_11)


        self.verticalLayout_18.addLayout(self.horizontalLayout_25)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Plain)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(4, 4, 4, 4)
        self.label_18 = QLabel(self.frame_8)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"color: #CC6E6E")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_18)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.comboBoxEnding1 = QComboBox(self.frame_8)
        self.comboBoxEnding1.addItem("")
        self.comboBoxEnding1.addItem("")
        self.comboBoxEnding1.addItem("")
        self.comboBoxEnding1.setObjectName(u"comboBoxEnding1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBoxEnding1.sizePolicy().hasHeightForWidth())
        self.comboBoxEnding1.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.comboBoxEnding1)

        self.label_19 = QLabel(self.frame_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font8)
        self.label_19.setStyleSheet(u"color: rgb(255, 85, 0)")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_19)

        self.comboBoxEnding2 = QComboBox(self.frame_8)
        self.comboBoxEnding2.addItem("")
        self.comboBoxEnding2.addItem("")
        self.comboBoxEnding2.addItem("")
        self.comboBoxEnding2.addItem("")
        self.comboBoxEnding2.setObjectName(u"comboBoxEnding2")
        sizePolicy2.setHeightForWidth(self.comboBoxEnding2.sizePolicy().hasHeightForWidth())
        self.comboBoxEnding2.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.comboBoxEnding2)

        self.label_20 = QLabel(self.frame_8)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font8)
        self.label_20.setStyleSheet(u"color: rgb(255, 85, 0)")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.label_20)

        self.comboBoxEnding3 = QComboBox(self.frame_8)
        self.comboBoxEnding3.addItem("")
        self.comboBoxEnding3.addItem("")
        self.comboBoxEnding3.addItem("")
        self.comboBoxEnding3.addItem("")
        self.comboBoxEnding3.setObjectName(u"comboBoxEnding3")
        sizePolicy2.setHeightForWidth(self.comboBoxEnding3.sizePolicy().hasHeightForWidth())
        self.comboBoxEnding3.setSizePolicy(sizePolicy2)

        self.horizontalLayout_15.addWidget(self.comboBoxEnding3)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(2, 1)
        self.horizontalLayout_15.setStretch(4, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.checkBoxEndingEnd2Sp = QCheckBox(self.frame_8)
        self.checkBoxEndingEnd2Sp.setObjectName(u"checkBoxEndingEnd2Sp")
        self.checkBoxEndingEnd2Sp.setEnabled(True)
        self.checkBoxEndingEnd2Sp.setStyleSheet(u"color: #EF9A9A")
        self.checkBoxEndingEnd2Sp.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.checkBoxEndingEnd2Sp)

        self.checkBoxEndingEnd3Sp = QCheckBox(self.frame_8)
        self.checkBoxEndingEnd3Sp.setObjectName(u"checkBoxEndingEnd3Sp")
        self.checkBoxEndingEnd3Sp.setEnabled(True)
        self.checkBoxEndingEnd3Sp.setStyleSheet(u"color: #EF9A9A")
        self.checkBoxEndingEnd3Sp.setCheckable(True)

        self.horizontalLayout_14.addWidget(self.checkBoxEndingEnd3Sp)

        self.pushButtonSubmitEnding = QPushButton(self.frame_8)
        self.pushButtonSubmitEnding.setObjectName(u"pushButtonSubmitEnding")

        self.horizontalLayout_14.addWidget(self.pushButtonSubmitEnding)

        self.horizontalLayout_14.setStretch(0, 2)
        self.horizontalLayout_14.setStretch(1, 2)

        self.verticalLayout_12.addLayout(self.horizontalLayout_14)

        self.verticalLayout_12.setStretch(1, 1)
        self.verticalLayout_12.setStretch(2, 1)

        self.verticalLayout_18.addWidget(self.frame_8)

        self.frameBan = QFrame(self.frame_2)
        self.frameBan.setObjectName(u"frameBan")
        self.frameBan.setFrameShape(QFrame.StyledPanel)
        self.frameBan.setFrameShadow(QFrame.Plain)
        self.verticalLayout_15 = QVBoxLayout(self.frameBan)
        self.verticalLayout_15.setSpacing(1)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(4, 4, 4, 4)
        self.label_23 = QLabel(self.frameBan)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font8)
        self.label_23.setStyleSheet(u"color: #CC6E6E")
        self.label_23.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_23)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.checkBoxBanLogos = QCheckBox(self.frameBan)
        self.checkBoxBanLogos.setObjectName(u"checkBoxBanLogos")
        self.checkBoxBanLogos.setTristate(True)

        self.horizontalLayout_18.addWidget(self.checkBoxBanLogos)

        self.checkBoxBanAskl = QCheckBox(self.frameBan)
        self.checkBoxBanAskl.setObjectName(u"checkBoxBanAskl")
        self.checkBoxBanAskl.setTristate(True)

        self.horizontalLayout_18.addWidget(self.checkBoxBanAskl)

        self.checkBoxBanQlsyd = QCheckBox(self.frameBan)
        self.checkBoxBanQlsyd.setObjectName(u"checkBoxBanQlsyd")
        self.checkBoxBanQlsyd.setTristate(True)

        self.horizontalLayout_18.addWidget(self.checkBoxBanQlsyd)

        self.checkBoxBanKuiying = QCheckBox(self.frameBan)
        self.checkBoxBanKuiying.setObjectName(u"checkBoxBanKuiying")
        self.checkBoxBanKuiying.setTristate(True)

        self.horizontalLayout_18.addWidget(self.checkBoxBanKuiying)

        self.checkBoxBanWeba = QCheckBox(self.frameBan)
        self.checkBoxBanWeba.setObjectName(u"checkBoxBanWeba")
        self.checkBoxBanWeba.setTristate(True)

        self.horizontalLayout_18.addWidget(self.checkBoxBanWeba)


        self.verticalLayout_15.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.checkBoxBanCjayfl = QCheckBox(self.frameBan)
        self.checkBoxBanCjayfl.setObjectName(u"checkBoxBanCjayfl")
        self.checkBoxBanCjayfl.setTristate(True)

        self.horizontalLayout_19.addWidget(self.checkBoxBanCjayfl)

        self.checkBoxBanKalsit = QCheckBox(self.frameBan)
        self.checkBoxBanKalsit.setObjectName(u"checkBoxBanKalsit")
        self.checkBoxBanKalsit.setTristate(True)

        self.horizontalLayout_19.addWidget(self.checkBoxBanKalsit)

        self.checkBoxBanYns = QCheckBox(self.frameBan)
        self.checkBoxBanYns.setObjectName(u"checkBoxBanYns")
        self.checkBoxBanYns.setTristate(True)

        self.horizontalLayout_19.addWidget(self.checkBoxBanYns)

        self.checkBoxBanSuxin = QCheckBox(self.frameBan)
        self.checkBoxBanSuxin.setObjectName(u"checkBoxBanSuxin")
        self.checkBoxBanSuxin.setTristate(True)

        self.horizontalLayout_19.addWidget(self.checkBoxBanSuxin)

        self.checkBoxBanNifu = QCheckBox(self.frameBan)
        self.checkBoxBanNifu.setObjectName(u"checkBoxBanNifu")
        self.checkBoxBanNifu.setTristate(True)

        self.horizontalLayout_19.addWidget(self.checkBoxBanNifu)


        self.verticalLayout_15.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, -1, -1)
        self.label_30 = QLabel(self.frameBan)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: #EF9A9A")
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_30)

        self.radioButtonWsde1 = QRadioButton(self.frameBan)
        self.radioButtonWsde1.setObjectName(u"radioButtonWsde1")
        self.radioButtonWsde1.setChecked(True)

        self.horizontalLayout_24.addWidget(self.radioButtonWsde1)

        self.radioButtonWsde2 = QRadioButton(self.frameBan)
        self.radioButtonWsde2.setObjectName(u"radioButtonWsde2")

        self.horizontalLayout_24.addWidget(self.radioButtonWsde2)

        self.radioButtonWsde3 = QRadioButton(self.frameBan)
        self.radioButtonWsde3.setObjectName(u"radioButtonWsde3")

        self.horizontalLayout_24.addWidget(self.radioButtonWsde3)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_5)

        self.pushButtonClearBan = QPushButton(self.frameBan)
        self.pushButtonClearBan.setObjectName(u"pushButtonClearBan")

        self.horizontalLayout_24.addWidget(self.pushButtonClearBan)

        self.label_27 = QLabel(self.frameBan)
        self.label_27.setObjectName(u"label_27")
        font9 = QFont()
        font9.setPointSize(10)
        font9.setBold(True)
        font9.setItalic(False)
        self.label_27.setFont(font9)
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_27)

        self.pushButtonSubmitBan = QPushButton(self.frameBan)
        self.pushButtonSubmitBan.setObjectName(u"pushButtonSubmitBan")

        self.horizontalLayout_24.addWidget(self.pushButtonSubmitBan)


        self.horizontalLayout_20.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_20.setStretch(0, 1)

        self.verticalLayout_15.addLayout(self.horizontalLayout_20)

        self.verticalLayout_15.setStretch(1, 1)
        self.verticalLayout_15.setStretch(2, 1)
        self.verticalLayout_15.setStretch(3, 1)

        self.verticalLayout_18.addWidget(self.frameBan)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Plain)
        self.verticalLayout_11 = QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(4, 4, 4, 4)
        self.label_15 = QLabel(self.frame_7)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font8)
        self.label_15.setStyleSheet(u"color: #CC6E6E")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_15)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_16 = QLabel(self.frame_7)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font2)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_16)

        self.spinBoxSumTreasure = QSpinBox(self.frame_7)
        self.spinBoxSumTreasure.setObjectName(u"spinBoxSumTreasure")
        self.spinBoxSumTreasure.setMaximum(999)

        self.horizontalLayout_13.addWidget(self.spinBoxSumTreasure)

        self.label_17 = QLabel(self.frame_7)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font2)
        self.label_17.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_17)

        self.spinBoxSumEmerg = QSpinBox(self.frame_7)
        self.spinBoxSumEmerg.setObjectName(u"spinBoxSumEmerg")
        self.spinBoxSumEmerg.setMaximum(999)

        self.horizontalLayout_13.addWidget(self.spinBoxSumEmerg)

        self.checkBoxSumHasBbtsy = QCheckBox(self.frame_7)
        self.checkBoxSumHasBbtsy.setObjectName(u"checkBoxSumHasBbtsy")
        self.checkBoxSumHasBbtsy.setEnabled(True)
        self.checkBoxSumHasBbtsy.setStyleSheet(u"color: #EF9A9A")
        self.checkBoxSumHasBbtsy.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.checkBoxSumHasBbtsy)

        self.pushButtonSubmitSum = QPushButton(self.frame_7)
        self.pushButtonSubmitSum.setObjectName(u"pushButtonSubmitSum")

        self.horizontalLayout_13.addWidget(self.pushButtonSubmitSum)

        self.horizontalLayout_13.setStretch(1, 1)
        self.horizontalLayout_13.setStretch(3, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.verticalLayout_11.setStretch(1, 1)

        self.verticalLayout_18.addWidget(self.frame_7)


        self.horizontalLayout_23.addLayout(self.verticalLayout_18)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Plain)
        self.verticalLayout_20 = QVBoxLayout(self.frame_13)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(4, 4, 4, 4)
        self.label_26 = QLabel(self.frame_13)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font8)
        self.label_26.setStyleSheet(u"color: #CC6E6E")
        self.label_26.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_26)

        self.spinBoxBaseScore = QSpinBox(self.frame_13)
        self.spinBoxBaseScore.setObjectName(u"spinBoxBaseScore")
        self.spinBoxBaseScore.setAlignment(Qt.AlignCenter)
        self.spinBoxBaseScore.setMaximum(10000)

        self.verticalLayout_20.addWidget(self.spinBoxBaseScore)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_2)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Plain)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(4, 4, 4, 4)
        self.label_24 = QLabel(self.frame_12)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font8)
        self.label_24.setStyleSheet(u"color: #CC6E6E")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_24)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lineEditCustomScore = QLineEdit(self.frame_12)
        self.lineEditCustomScore.setObjectName(u"lineEditCustomScore")

        self.horizontalLayout_21.addWidget(self.lineEditCustomScore)

        self.spinBoxCustomScore = QSpinBox(self.frame_12)
        self.spinBoxCustomScore.setObjectName(u"spinBoxCustomScore")
        self.spinBoxCustomScore.setMinimum(-999)
        self.spinBoxCustomScore.setMaximum(999)

        self.horizontalLayout_21.addWidget(self.spinBoxCustomScore)

        self.pushButtonSubmitCustom = QPushButton(self.frame_12)
        self.pushButtonSubmitCustom.setObjectName(u"pushButtonSubmitCustom")

        self.horizontalLayout_21.addWidget(self.pushButtonSubmitCustom)

        self.horizontalLayout_21.setStretch(0, 2)
        self.horizontalLayout_21.setStretch(1, 1)

        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.verticalLayout_16.setStretch(1, 1)

        self.verticalLayout_17.addWidget(self.frame_12)

        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Plain)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(4, 4, 4, 4)
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font8)
        self.label_9.setStyleSheet(u"color: #CC6E6E")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)

        self.listRecord = QListWidget(self.frame_5)
        self.listRecord.setObjectName(u"listRecord")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.listRecord.sizePolicy().hasHeightForWidth())
        self.listRecord.setSizePolicy(sizePolicy3)
        font10 = QFont()
        font10.setPointSize(8)
        font10.setBold(True)
        self.listRecord.setFont(font10)
        self.listRecord.setFrameShadow(QFrame.Plain)
        self.listRecord.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listRecord.setProperty("showDropIndicator", False)
        self.listRecord.setDragEnabled(False)
        self.listRecord.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.listRecord.setDefaultDropAction(Qt.MoveAction)
        self.listRecord.setAlternatingRowColors(True)
        self.listRecord.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listRecord.setMovement(QListView.Static)
        self.listRecord.setSpacing(2)
        self.listRecord.setSortingEnabled(False)

        self.verticalLayout_9.addWidget(self.listRecord)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.frame_5)
        self.label_8.setObjectName(u"label_8")
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)
        font11.setItalic(False)
        self.label_8.setFont(font11)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.labelScore = QLabel(self.frame_5)
        self.labelScore.setObjectName(u"labelScore")
        self.labelScore.setFont(font11)
        self.labelScore.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.labelScore)

        self.horizontalLayout_10.setStretch(1, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_10)

        self.verticalLayout_9.setStretch(1, 1)

        self.verticalLayout_17.addWidget(self.frame_5)

        self.verticalLayout_17.setStretch(2, 1)

        self.horizontalLayout_23.addLayout(self.verticalLayout_17)

        self.horizontalLayout_23.setStretch(0, 1)

        self.verticalLayout_19.addLayout(self.horizontalLayout_23)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.checkBoxPause = QCheckBox(self.frame_3)
        self.checkBoxPause.setObjectName(u"checkBoxPause")
        self.checkBoxPause.setFont(font6)
        self.checkBoxPause.setFocusPolicy(Qt.ClickFocus)
        self.checkBoxPause.setCheckable(True)
        self.checkBoxPause.setChecked(False)

        self.horizontalLayout_9.addWidget(self.checkBoxPause)

        self.checkBoxEnLowers = QCheckBox(self.frame_3)
        self.checkBoxEnLowers.setObjectName(u"checkBoxEnLowers")
        self.checkBoxEnLowers.setFont(font6)
        self.checkBoxEnLowers.setFocusPolicy(Qt.ClickFocus)
        self.checkBoxEnLowers.setChecked(True)

        self.horizontalLayout_9.addWidget(self.checkBoxEnLowers)

        self.pushButtonClrLowers = QPushButton(self.frame_3)
        self.pushButtonClrLowers.setObjectName(u"pushButtonClrLowers")
        self.pushButtonClrLowers.setFont(font6)
        self.pushButtonClrLowers.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_9.addWidget(self.pushButtonClrLowers)


        self.horizontalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.labelConState = QLabel(self.frame_3)
        self.labelConState.setObjectName(u"labelConState")
        self.labelConState.setFont(font9)
        self.labelConState.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelConState)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_2)

        self.lineEditServer = QLineEdit(self.frame_3)
        self.lineEditServer.setObjectName(u"lineEditServer")
        sizePolicy.setHeightForWidth(self.lineEditServer.sizePolicy().hasHeightForWidth())
        self.lineEditServer.setSizePolicy(sizePolicy)
        self.lineEditServer.setMinimumSize(QSize(100, 0))
        self.lineEditServer.setFont(font3)
        self.lineEditServer.setFocusPolicy(Qt.ClickFocus)
        self.lineEditServer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.lineEditServer)

        self.spinBoxConPort = QSpinBox(self.frame_3)
        self.spinBoxConPort.setObjectName(u"spinBoxConPort")
        self.spinBoxConPort.setMinimumSize(QSize(60, 0))
        self.spinBoxConPort.setFocusPolicy(Qt.ClickFocus)
        self.spinBoxConPort.setMaximum(99999)
        self.spinBoxConPort.setValue(4455)

        self.horizontalLayout_8.addWidget(self.spinBoxConPort)

        self.pushButtonConnect = QPushButton(self.frame_3)
        self.pushButtonConnect.setObjectName(u"pushButtonConnect")
        self.pushButtonConnect.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_8.addWidget(self.pushButtonConnect)


        self.horizontalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(2, 99)
        self.horizontalLayout.setStretch(4, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.verticalLayout_7.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7f57\u5fb7\u5c9b\u88c1\u5224\u7ec8\u7aef Beta", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u3000\u5e72\u5458\u4fe1\u606f\u5361\u3000\u2014\u2014", None))
        self.labelAvatar.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u5934\u50cf", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u6635\u79f0:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5907\u6ce8:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"UUID:", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u6700\u540e\u4fee\u6539:", None))
        self.lineEditPlayerName.setText(QCoreApplication.translate("MainWindow", u"\uff2e/A", None))
        self.lineEditPlayerNote.setText(QCoreApplication.translate("MainWindow", u"\uff2e/A", None))
        self.labelPlayerUUID.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.labelPlayerLastSaveTime.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6548\u8bb0\u5f55:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6700\u9ad8\u5206:", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u5c40\u5206\u961f:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u5c40\u5e72\u5458:", None))
        self.labelPlayerRecordNum.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelPlayerMaxRecord.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBoxStartTeam.setItemText(0, QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))

        self.comboBoxStartOperator.setItemText(0, QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e72\u5458\u9009\u62e9:", None))
        self.pushButtonAddPlayer.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButtonDelPlayer.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u69fd\u4f4d:", None))
        self.pushButtonClrRecord.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u96f6\u6b64\u8bb0\u5f55", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u3000\u8ba1\u5206\u677f\u3000\u2014\u2014", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u4e34\u65f6\u62db\u52df", None))
        self.labelHeaderTemp.setText(QCoreApplication.translate("MainWindow", u"\u516d\u661f: 0 \u4e94\u661f: 0 \u56db\u661f: 0", None))
        self.radioButtonTempSix.setText(QCoreApplication.translate("MainWindow", u"\u516d\u661f", None))
        self.radioButtonTempFive.setText(QCoreApplication.translate("MainWindow", u"\u4e94\u661f", None))
        self.radioButtonTempFour.setText(QCoreApplication.translate("MainWindow", u"\u56db\u661f", None))
        self.pushButtonSubmitTemp.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u5173\u5361/BOSS (\u4e0d\u8df3\u5173,\u540c\u5173\u5361\u66f4\u9ad8\u5206\u5148\u5220\u9664\u8bb0\u5f55)", None))
        self.comboBoxEmerg.setItemText(0, QCoreApplication.translate("MainWindow", u"\u6e83\u4e71\u9b54\u5178", None))
        self.comboBoxEmerg.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5927\u68cb\u4e00\u76d8", None))
        self.comboBoxEmerg.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5927\u68cb\u4e00\u76d8<\u82e6\u96be>", None))
        self.comboBoxEmerg.setItemText(3, QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2193 \u56db\u5c42 \u2193\u2014\u2014", None))
        self.comboBoxEmerg.setItemText(4, QCoreApplication.translate("MainWindow", u"\u3010\u56db\u5c42\u666e\u901a\u7d27\u6025\u3011", None))
        self.comboBoxEmerg.setItemText(5, QCoreApplication.translate("MainWindow", u"\u7329\u7ea2\u752c\u9053", None))
        self.comboBoxEmerg.setItemText(6, QCoreApplication.translate("MainWindow", u"\u7329\u7ea2\u752c\u9053<\u5929\u707e/\u82e6\u96be/\u91d1\u878d>", None))
        self.comboBoxEmerg.setItemText(7, QCoreApplication.translate("MainWindow", u"\u5047\u8c61\u5bf9\u51b2", None))
        self.comboBoxEmerg.setItemText(8, QCoreApplication.translate("MainWindow", u"\u5047\u8c61\u5bf9\u51b2<\u5947\u89c2/\u9b54\u738b>", None))
        self.comboBoxEmerg.setItemText(9, QCoreApplication.translate("MainWindow", u"\u673d\u8d25\u8003\u5bdf", None))
        self.comboBoxEmerg.setItemText(10, QCoreApplication.translate("MainWindow", u"\u673d\u8d25\u8003\u5bdf<\u91d1\u878d/\u9b54\u738b>", None))
        self.comboBoxEmerg.setItemText(11, QCoreApplication.translate("MainWindow", u"\u5e74\u4ee3\u65ad\u5c42<\u9b54\u738b/\u5929\u707e/\u91d1\u878d>", None))
        self.comboBoxEmerg.setItemText(12, QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2193 \u4e94\u5c42 \u2193\u2014\u2014", None))
        self.comboBoxEmerg.setItemText(13, QCoreApplication.translate("MainWindow", u"\u3010\u4e94\u5c42\u666e\u901a\u7d27\u6025\u3011", None))
        self.comboBoxEmerg.setItemText(14, QCoreApplication.translate("MainWindow", u"\u8ba1\u5212\u8015\u79cd", None))
        self.comboBoxEmerg.setItemText(15, QCoreApplication.translate("MainWindow", u"\u8ba1\u5212\u8015\u79cd<\u82e6\u96be/\u5947\u89c2>", None))
        self.comboBoxEmerg.setItemText(16, QCoreApplication.translate("MainWindow", u"\u5bc4\u4eba\u57ce\u6c60\u4e0b", None))
        self.comboBoxEmerg.setItemText(17, QCoreApplication.translate("MainWindow", u"\u5bc4\u4eba\u57ce\u6c60\u4e0b<\u91d1\u878d/\u5947\u89c2>", None))
        self.comboBoxEmerg.setItemText(18, QCoreApplication.translate("MainWindow", u"\u901a\u9053\u5c01\u9501", None))
        self.comboBoxEmerg.setItemText(19, QCoreApplication.translate("MainWindow", u"\u901a\u9053\u5c01\u9501<\u5947\u89c2>", None))
        self.comboBoxEmerg.setItemText(20, QCoreApplication.translate("MainWindow", u"\u65e0\u7f6a\u51c0\u571f", None))
        self.comboBoxEmerg.setItemText(21, QCoreApplication.translate("MainWindow", u"\u65e0\u7f6a\u51c0\u571f<\u5947\u89c2>", None))
        self.comboBoxEmerg.setItemText(22, QCoreApplication.translate("MainWindow", u"\u5deb\u5492\u540c\u76df", None))
        self.comboBoxEmerg.setItemText(23, QCoreApplication.translate("MainWindow", u"\u5deb\u5492\u540c\u76df<\u5947\u89c2>", None))
        self.comboBoxEmerg.setItemText(24, QCoreApplication.translate("MainWindow", u"\u6b8b\u635f\u5b66\u9662", None))
        self.comboBoxEmerg.setItemText(25, QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2193 \u516d\u5c42 \u2193\u2014\u2014", None))
        self.comboBoxEmerg.setItemText(26, QCoreApplication.translate("MainWindow", u"\u3010\u516d\u5c42\u666e\u901a\u7d27\u6025\u3011", None))
        self.comboBoxEmerg.setItemText(27, QCoreApplication.translate("MainWindow", u"\u8c0b\u6c42\u5171\u8bc6", None))
        self.comboBoxEmerg.setItemText(28, QCoreApplication.translate("MainWindow", u"\u8c0b\u6c42\u5171\u8bc6<\u91d1\u878d/\u5947\u89c2>", None))
        self.comboBoxEmerg.setItemText(29, QCoreApplication.translate("MainWindow", u"\u795e\u5723\u7684\u6e34\u6c42", None))
        self.comboBoxEmerg.setItemText(30, QCoreApplication.translate("MainWindow", u"\u795e\u5723\u7684\u6e34\u6c42<\u5947\u89c2/\u5929\u707e>", None))
        self.comboBoxEmerg.setItemText(31, QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2193 BOSS \u2193\u2014\u2014", None))
        self.comboBoxEmerg.setItemText(32, QCoreApplication.translate("MainWindow", u"\u4e09\u5c42BOSS\u5173", None))
        self.comboBoxEmerg.setItemText(33, QCoreApplication.translate("MainWindow", u"\u4e09\u5c42BOSS\u5173<\u536b\u56fd\u524d\u591c>", None))

        self.checkBoxEmergBswLessFour.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u7f72\u4f4d\u4e0d\u591a\u4e8e4", None))
        self.pushButtonSubmitEmerg.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u901a\u5173\u9690\u85cf\u5173\u5361/\u8fbe\u6210\u7279\u6b8a\u51fb\u6740(\u9e2d/\u72d7/\u718a/\u9f20)", None))
        self.comboBoxKillSp.setItemText(0, QCoreApplication.translate("MainWindow", u"\u666e\u901a\u5173\u5361", None))
        self.comboBoxKillSp.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4fe1\u53f7\u706f", None))
        self.comboBoxKillSp.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4fe1\u53f7\u706f<\u7d27\u6025>", None))
        self.comboBoxKillSp.setItemText(3, QCoreApplication.translate("MainWindow", u"\u52ab\u865a\u6d4e\u5b9e", None))
        self.comboBoxKillSp.setItemText(4, QCoreApplication.translate("MainWindow", u"\u52ab\u865a\u6d4e\u5b9e<\u7d27\u6025>", None))
        self.comboBoxKillSp.setItemText(5, QCoreApplication.translate("MainWindow", u"\u6218\u573a\u4fa7\u9762", None))
        self.comboBoxKillSp.setItemText(6, QCoreApplication.translate("MainWindow", u"\u6218\u573a\u4fa7\u9762<\u7d27\u6025>", None))
        self.comboBoxKillSp.setItemText(7, QCoreApplication.translate("MainWindow", u"\u9e2d\u901f\u516c\u8def<\u7d27\u6025>", None))
        self.comboBoxKillSp.setItemText(8, QCoreApplication.translate("MainWindow", u"\u72ed\u8def\u76f8\u9022<\u4e09\u7ea7/\u4f7f\u7528\u672a\u4f7f\u7528\u8fc7\u7684\u5e72\u5458>", None))
        self.comboBoxKillSp.setItemText(9, QCoreApplication.translate("MainWindow", u"\u53d9\u4e8b\u9080\u7ea6", None))

        self.labelKillSp.setText(QCoreApplication.translate("MainWindow", u"\u7279\u6b8a\u51fb\u6740", None))
        self.spinBoxKillSp.setPrefix("")
        self.checkBoxKillSpPerfect.setText(QCoreApplication.translate("MainWindow", u"\u65e0\u6f0f", None))
        self.pushButtonSubmitKillSp.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u6811\u6d1e\u8de8\u5c42\u906d\u9047\u7d27\u6025\u4f5c\u6218", None))
        self.labelKillSp_2.setText(QCoreApplication.translate("MainWindow", u"\u6811\u6d1e\u85cf\u54c1\u6570", None))
        self.spinBoxEarlyEmerg.setPrefix("")
        self.pushButtonEarlyEmerg.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u94b1\u8d85\u652f", None))
        self.labelKillSp_3.setText(QCoreApplication.translate("MainWindow", u"\u8d85\u51fa60\u7684\u70b9\u6570", None))
        self.spinBoxMoneyOverflow.setPrefix("")
        self.pushButtonSubmitMoneyOverflow.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4 (\u4ec5\u4e00\u6b21)", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8fbe\u6210\u7ed3\u5c40", None))
        self.comboBoxEnding1.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u6388\u8bfe", None))
        self.comboBoxEnding1.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u6388\u8bfe<\u6df7\u4e71>", None))
        self.comboBoxEnding1.setItemText(2, QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u6388\u8bfe<\u6df7\u4e71/\u65e0\u6f0f>", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.comboBoxEnding2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u672a\u8fbe\u6210", None))
        self.comboBoxEnding2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u671d\u8c12", None))
        self.comboBoxEnding2.setItemText(2, QCoreApplication.translate("MainWindow", u"\u671d\u8c12<\u6df7\u4e71>", None))
        self.comboBoxEnding2.setItemText(3, QCoreApplication.translate("MainWindow", u"\u671d\u8c12<\u6df7\u4e71/\u65e0\u6f0f>", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u2192", None))
        self.comboBoxEnding3.setItemText(0, QCoreApplication.translate("MainWindow", u"\u672a\u8fbe\u6210", None))
        self.comboBoxEnding3.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5723\u57ce", None))
        self.comboBoxEnding3.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5723\u57ce<\u6df7\u4e71>", None))
        self.comboBoxEnding3.setItemText(3, QCoreApplication.translate("MainWindow", u"\u5723\u57ce<\u6df7\u4e71/\u65e0\u6f0f>", None))

        self.checkBoxEndingEnd2Sp.setText(QCoreApplication.translate("MainWindow", u"\u91d1\u878d/\u5947\u89c2/\u62e5\u6324\u901a\u5173\u4e8c\u7ed3\u5c40", None))
        self.checkBoxEndingEnd3Sp.setText(QCoreApplication.translate("MainWindow", u"\u5947\u89c2/\u62e5\u6324/\u9b54\u738b\u901a\u5173\u4e09\u7ed3\u5c40", None))
        self.pushButtonSubmitEnding.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4 (\u4ec5\u4e00\u6b21)", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Ban\u4f4d\u7ed3\u7b97 (\u9009\u62e9\u4e3a\u672a\u6293\u53d6,\u9700\u8fc7\u4e94\u5c42BOSS,\"-\"\u4e3a\u4e00\u6b21\u5f97\u5206,\"\u221a\"\u4e3a\u4e24\u6b21\u5f97\u5206)", None))
        self.checkBoxBanLogos.setText(QCoreApplication.translate("MainWindow", u"Logos", None))
        self.checkBoxBanAskl.setText(QCoreApplication.translate("MainWindow", u"\u963f\u65af\u5361\u4f26", None))
        self.checkBoxBanQlsyd.setText(QCoreApplication.translate("MainWindow", u"\u9e92\u9e9fS\u591c\u5200", None))
        self.checkBoxBanKuiying.setText(QCoreApplication.translate("MainWindow", u"\u5080\u5f71", None))
        self.checkBoxBanWeba.setText(QCoreApplication.translate("MainWindow", u"\u4e4c\u5c14\u6bd4\u5b89", None))
        self.checkBoxBanCjayfl.setText(QCoreApplication.translate("MainWindow", u"\u7eaf\u70ec\u827e\u96c5\u6cd5\u62c9", None))
        self.checkBoxBanKalsit.setText(QCoreApplication.translate("MainWindow", u"\u51ef\u5c14\u5e0c", None))
        self.checkBoxBanYns.setText(QCoreApplication.translate("MainWindow", u"\u4f0a\u5185\u65af", None))
        self.checkBoxBanSuxin.setText(QCoreApplication.translate("MainWindow", u"\u5851\u5fc3", None))
        self.checkBoxBanNifu.setText(QCoreApplication.translate("MainWindow", u"\u59ae\u8299", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u7ef4\u4ec0\u6234\u5c14\uff1a", None))
        self.radioButtonWsde1.setText(QCoreApplication.translate("MainWindow", u"\u672a\u62db\u52df ", None))
        self.radioButtonWsde2.setText(QCoreApplication.translate("MainWindow", u"\u62db\u52df ", None))
        self.radioButtonWsde3.setText(QCoreApplication.translate("MainWindow", u"\u653e\u5f03\u535a\u58eb\u94f6\u5370 ", None))
        self.pushButtonClearBan.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.pushButtonSubmitBan.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4 (\u4ec5\u4e00\u6b21)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u6700\u7ec8\u7ed3\u7b97", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u6301\u6709\u85cf\u54c1", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u901a\u5173\u7d27\u6025", None))
        self.checkBoxSumHasBbtsy.setText(QCoreApplication.translate("MainWindow", u"\u6301\u6709<\u5df4\u522b\u5854\u8a93\u8a00>", None))
        self.pushButtonSubmitSum.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u4ea4 (\u4ec5\u4e00\u6b21)", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u5206\u6570", None))
        self.spinBoxBaseScore.setSuffix("")
        self.spinBoxBaseScore.setPrefix("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u589e\u51cf", None))
        self.lineEditCustomScore.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7406\u7531", None))
        self.pushButtonSubmitCustom.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8be6\u7ec6\u8bb0\u5f55 (\u53f3\u952e\u8bb0\u5f55\u53ef\u5220\u9664)", None))
#if QT_CONFIG(tooltip)
        self.listRecord.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u603b\u5206:", None))
        self.labelScore.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.checkBoxPause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505c\u5237\u65b0", None))
        self.checkBoxEnLowers.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u5f39\u51fa\u901a\u77e5", None))
        self.pushButtonClrLowers.setText(QCoreApplication.translate("MainWindow", u"\u522b\u5f39\u901a\u77e5\u4e86", None))
        self.labelConState.setText(QCoreApplication.translate("MainWindow", u"/// PRTS \u672a\u8fde\u63a5 ///", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u670d\u52a1\u5668:", None))
        self.lineEditServer.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.pushButtonConnect.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5OBS", None))
    # retranslateUi

