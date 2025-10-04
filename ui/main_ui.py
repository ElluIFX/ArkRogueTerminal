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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QButtonGroup, QCheckBox,
    QComboBox, QDoubleSpinBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QListView,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(950, 867)
        MainWindow.setMinimumSize(QSize(950, 800))
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

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font2)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_14)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font2)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_12)


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
        font3.setPointSize(9)
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

        self.labelPlayerRecordNum = QLabel(self.frame)
        self.labelPlayerRecordNum.setObjectName(u"labelPlayerRecordNum")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.labelPlayerRecordNum.setFont(font5)
        self.labelPlayerRecordNum.setFrameShape(QFrame.Box)
        self.labelPlayerRecordNum.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelPlayerRecordNum)

        self.labelPlayerMaxRecord = QLabel(self.frame)
        self.labelPlayerMaxRecord.setObjectName(u"labelPlayerMaxRecord")
        self.labelPlayerMaxRecord.setFont(font5)
        self.labelPlayerMaxRecord.setFrameShape(QFrame.Box)
        self.labelPlayerMaxRecord.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelPlayerMaxRecord)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)

        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_30)

        self.label_31 = QLabel(self.frame)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_31)

        self.label_38 = QLabel(self.frame)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)
        self.label_38.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_38)

        self.label_43 = QLabel(self.frame)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font2)
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_43)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.comboBoxCup = QComboBox(self.frame)
        self.comboBoxCup.addItem("")
        self.comboBoxCup.addItem("")
        self.comboBoxCup.setObjectName(u"comboBoxCup")
        self.comboBoxCup.setMaxVisibleItems(20)

        self.verticalLayout_4.addWidget(self.comboBoxCup)

        self.lineEditPlayerTeam = QLineEdit(self.frame)
        self.lineEditPlayerTeam.setObjectName(u"lineEditPlayerTeam")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEditPlayerTeam.sizePolicy().hasHeightForWidth())
        self.lineEditPlayerTeam.setSizePolicy(sizePolicy1)
        self.lineEditPlayerTeam.setFont(font3)
        self.lineEditPlayerTeam.setFocusPolicy(Qt.ClickFocus)
        self.lineEditPlayerTeam.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lineEditPlayerTeam)

        self.lineEditPlayerSelect = QLineEdit(self.frame)
        self.lineEditPlayerSelect.setObjectName(u"lineEditPlayerSelect")
        sizePolicy1.setHeightForWidth(self.lineEditPlayerSelect.sizePolicy().hasHeightForWidth())
        self.lineEditPlayerSelect.setSizePolicy(sizePolicy1)
        self.lineEditPlayerSelect.setFont(font3)
        self.lineEditPlayerSelect.setFocusPolicy(Qt.ClickFocus)
        self.lineEditPlayerSelect.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lineEditPlayerSelect)

        self.lineEditSpeaker = QLineEdit(self.frame)
        self.lineEditSpeaker.setObjectName(u"lineEditSpeaker")
        sizePolicy1.setHeightForWidth(self.lineEditSpeaker.sizePolicy().hasHeightForWidth())
        self.lineEditSpeaker.setSizePolicy(sizePolicy1)
        self.lineEditSpeaker.setFont(font3)
        self.lineEditSpeaker.setFocusPolicy(Qt.ClickFocus)
        self.lineEditSpeaker.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lineEditSpeaker)


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
        self.comboBoxSelPlayer.setFont(font3)
        self.comboBoxSelPlayer.setFocusPolicy(Qt.ClickFocus)
        self.comboBoxSelPlayer.setMaxVisibleItems(20)

        self.horizontalLayout_4.addWidget(self.comboBoxSelPlayer)

        self.pushButtonAddPlayer = QPushButton(self.frame)
        self.pushButtonAddPlayer.setObjectName(u"pushButtonAddPlayer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButtonAddPlayer.sizePolicy().hasHeightForWidth())
        self.pushButtonAddPlayer.setSizePolicy(sizePolicy2)
        self.pushButtonAddPlayer.setMaximumSize(QSize(50, 28))
        font6 = QFont()
        font6.setPointSize(9)
        font6.setItalic(False)
        font6.setUnderline(False)
        font6.setStrikeOut(False)
        self.pushButtonAddPlayer.setFont(font6)
        self.pushButtonAddPlayer.setFocusPolicy(Qt.ClickFocus)
        self.pushButtonAddPlayer.setStyleSheet(u"color: #94bf79")

        self.horizontalLayout_4.addWidget(self.pushButtonAddPlayer)

        self.pushButtonDelPlayer = QPushButton(self.frame)
        self.pushButtonDelPlayer.setObjectName(u"pushButtonDelPlayer")
        sizePolicy2.setHeightForWidth(self.pushButtonDelPlayer.sizePolicy().hasHeightForWidth())
        self.pushButtonDelPlayer.setSizePolicy(sizePolicy2)
        self.pushButtonDelPlayer.setMaximumSize(QSize(50, 28))
        self.pushButtonDelPlayer.setFont(font6)
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
        sizePolicy2.setHeightForWidth(self.pushButtonClrRecord.sizePolicy().hasHeightForWidth())
        self.pushButtonClrRecord.setSizePolicy(sizePolicy2)
        self.pushButtonClrRecord.setMaximumSize(QSize(16777215, 28))
        self.pushButtonClrRecord.setFont(font6)
        self.pushButtonClrRecord.setFocusPolicy(Qt.ClickFocus)
        self.pushButtonClrRecord.setStyleSheet(u"color: #d86a74")

        self.horizontalLayout_4.addWidget(self.pushButtonClrRecord)

        self.pushButtonSyncOBS = QPushButton(self.frame)
        self.pushButtonSyncOBS.setObjectName(u"pushButtonSyncOBS")
        sizePolicy2.setHeightForWidth(self.pushButtonSyncOBS.sizePolicy().hasHeightForWidth())
        self.pushButtonSyncOBS.setSizePolicy(sizePolicy2)
        self.pushButtonSyncOBS.setMaximumSize(QSize(16777215, 28))
        font7 = QFont()
        font7.setBold(True)
        self.pushButtonSyncOBS.setFont(font7)
        self.pushButtonSyncOBS.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout_4.addWidget(self.pushButtonSyncOBS)

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

        self.labelHeaderkillSp = QLabel(self.frame_6)
        self.labelHeaderkillSp.setObjectName(u"labelHeaderkillSp")
        self.labelHeaderkillSp.setFont(font8)
        self.labelHeaderkillSp.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.labelHeaderkillSp)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.labelKillSp = QLabel(self.frame_6)
        self.labelKillSp.setObjectName(u"labelKillSp")
        self.labelKillSp.setFont(font2)
        self.labelKillSp.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.labelKillSp)

        self.spinBoxKillSp = QSpinBox(self.frame_6)
        self.spinBoxKillSp.setObjectName(u"spinBoxKillSp")
        self.spinBoxKillSp.setMaximum(999)

        self.horizontalLayout_12.addWidget(self.spinBoxKillSp)

        self.pushButtonSubmitKillSp = QPushButton(self.frame_6)
        self.pushButtonSubmitKillSp.setObjectName(u"pushButtonSubmitKillSp")

        self.horizontalLayout_12.addWidget(self.pushButtonSubmitKillSp)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 1)

        self.verticalLayout_10.addLayout(self.horizontalLayout_12)

        self.verticalLayout_10.setStretch(2, 1)

        self.horizontalLayout_22.addWidget(self.frame_6)


        self.verticalLayout_18.addLayout(self.horizontalLayout_22)

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

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
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
        self.comboBoxEmerg.setObjectName(u"comboBoxEmerg")
        self.comboBoxEmerg.setMaxVisibleItems(20)

        self.horizontalLayout_16.addWidget(self.comboBoxEmerg)

        self.pushButtonSubmitEmerg = QPushButton(self.frame_9)
        self.pushButtonSubmitEmerg.setObjectName(u"pushButtonSubmitEmerg")

        self.horizontalLayout_16.addWidget(self.pushButtonSubmitEmerg)

        self.horizontalLayout_16.setStretch(0, 1)

        self.verticalLayout_13.addLayout(self.horizontalLayout_16)

        self.verticalLayout_13.setStretch(1, 1)

        self.verticalLayout_18.addWidget(self.frame_9)

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
        self.comboBoxEnding = QComboBox(self.frame_8)
        self.comboBoxEnding.addItem("")
        self.comboBoxEnding.addItem("")
        self.comboBoxEnding.addItem("")
        self.comboBoxEnding.addItem("")
        self.comboBoxEnding.addItem("")
        self.comboBoxEnding.addItem("")
        self.comboBoxEnding.addItem("")
        self.comboBoxEnding.setObjectName(u"comboBoxEnding")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.comboBoxEnding.sizePolicy().hasHeightForWidth())
        self.comboBoxEnding.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.comboBoxEnding)

        self.comboBoxEndingEx = QComboBox(self.frame_8)
        self.comboBoxEndingEx.addItem("")
        self.comboBoxEndingEx.addItem("")
        self.comboBoxEndingEx.setObjectName(u"comboBoxEndingEx")
        sizePolicy3.setHeightForWidth(self.comboBoxEndingEx.sizePolicy().hasHeightForWidth())
        self.comboBoxEndingEx.setSizePolicy(sizePolicy3)

        self.horizontalLayout_15.addWidget(self.comboBoxEndingEx)

        self.checkBoxEndingChaos = QCheckBox(self.frame_8)
        self.checkBoxEndingChaos.setObjectName(u"checkBoxEndingChaos")
        self.checkBoxEndingChaos.setEnabled(True)
        self.checkBoxEndingChaos.setStyleSheet(u"color: #EF9A9A")
        self.checkBoxEndingChaos.setCheckable(True)

        self.horizontalLayout_15.addWidget(self.checkBoxEndingChaos)

        self.pushButtonSubmitEnding = QPushButton(self.frame_8)
        self.pushButtonSubmitEnding.setObjectName(u"pushButtonSubmitEnding")

        self.horizontalLayout_15.addWidget(self.pushButtonSubmitEnding)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 1)

        self.verticalLayout_12.addLayout(self.horizontalLayout_15)

        self.verticalLayout_12.setStretch(1, 1)

        self.verticalLayout_18.addWidget(self.frame_8)

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
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 5, -1)
        self.radioButtonSpDsb = QRadioButton(self.frame_7)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioButtonSpDsb)
        self.radioButtonSpDsb.setObjectName(u"radioButtonSpDsb")
        self.radioButtonSpDsb.setChecked(True)

        self.gridLayout.addWidget(self.radioButtonSpDsb, 0, 0, 1, 1)

        self.radioButtonSpSsef = QRadioButton(self.frame_7)
        self.buttonGroup.addButton(self.radioButtonSpSsef)
        self.radioButtonSpSsef.setObjectName(u"radioButtonSpSsef")

        self.gridLayout.addWidget(self.radioButtonSpSsef, 1, 0, 1, 1)

        self.radioButtonSpRed = QRadioButton(self.frame_7)
        self.buttonGroup.addButton(self.radioButtonSpRed)
        self.radioButtonSpRed.setObjectName(u"radioButtonSpRed")

        self.gridLayout.addWidget(self.radioButtonSpRed, 0, 1, 1, 1)


        self.horizontalLayout_13.addLayout(self.gridLayout)

        self.pushButtonSubmitSp = QPushButton(self.frame_7)
        self.pushButtonSubmitSp.setObjectName(u"pushButtonSubmitSp")

        self.horizontalLayout_13.addWidget(self.pushButtonSubmitSp)

        self.horizontalLayout_13.setStretch(0, 1)

        self.verticalLayout_11.addLayout(self.horizontalLayout_13)

        self.verticalLayout_11.setStretch(1, 1)

        self.verticalLayout_18.addWidget(self.frame_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_2)

        self.verticalLayout_18.setStretch(4, 1)

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

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, -1, -1, 6)
        self.spinBoxBaseScore = QSpinBox(self.frame_13)
        self.spinBoxBaseScore.setObjectName(u"spinBoxBaseScore")
        self.spinBoxBaseScore.setAlignment(Qt.AlignCenter)
        self.spinBoxBaseScore.setMaximum(10000)

        self.horizontalLayout_14.addWidget(self.spinBoxBaseScore)

        self.pushButtonXXX = QPushButton(self.frame_13)
        self.pushButtonXXX.setObjectName(u"pushButtonXXX")

        self.horizontalLayout_14.addWidget(self.pushButtonXXX)

        self.horizontalLayout_14.setStretch(0, 1)

        self.verticalLayout_20.addLayout(self.horizontalLayout_14)


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
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.listRecord.sizePolicy().hasHeightForWidth())
        self.listRecord.setSizePolicy(sizePolicy4)
        font9 = QFont()
        font9.setPointSize(8)
        font9.setBold(True)
        self.listRecord.setFont(font9)
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
        font10 = QFont()
        font10.setPointSize(14)
        font10.setBold(True)
        font10.setItalic(False)
        self.label_8.setFont(font10)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.labelScore = QLabel(self.frame_5)
        self.labelScore.setObjectName(u"labelScore")
        self.labelScore.setFont(font10)
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

        self.frame_14 = QFrame(self.centralwidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Plain)
        self.verticalLayout_23 = QVBoxLayout(self.frame_14)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_2 = QLabel(self.frame_14)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_2)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Plain)
        self.verticalLayout_25 = QVBoxLayout(self.frame_15)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(4, 4, 4, 4)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, -1, -1, 0)
        self.doubleSpinBoxTeamScore_1 = QDoubleSpinBox(self.frame_15)
        self.doubleSpinBoxTeamScore_1.setObjectName(u"doubleSpinBoxTeamScore_1")
        self.doubleSpinBoxTeamScore_1.setAlignment(Qt.AlignCenter)
        self.doubleSpinBoxTeamScore_1.setMaximum(10000.000000000000000)

        self.horizontalLayout_28.addWidget(self.doubleSpinBoxTeamScore_1)

        self.label_32 = QLabel(self.frame_15)
        self.label_32.setObjectName(u"label_32")
        sizePolicy5 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy5)
        self.label_32.setFont(font)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_32)

        self.doubleSpinBoxTeamScore_2 = QDoubleSpinBox(self.frame_15)
        self.doubleSpinBoxTeamScore_2.setObjectName(u"doubleSpinBoxTeamScore_2")
        self.doubleSpinBoxTeamScore_2.setAlignment(Qt.AlignCenter)
        self.doubleSpinBoxTeamScore_2.setMaximum(10000.000000000000000)

        self.horizontalLayout_28.addWidget(self.doubleSpinBoxTeamScore_2)

        self.label_33 = QLabel(self.frame_15)
        self.label_33.setObjectName(u"label_33")
        sizePolicy5.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy5)
        self.label_33.setFont(font)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_33)

        self.doubleSpinBoxTeamScore_3 = QDoubleSpinBox(self.frame_15)
        self.doubleSpinBoxTeamScore_3.setObjectName(u"doubleSpinBoxTeamScore_3")
        self.doubleSpinBoxTeamScore_3.setAlignment(Qt.AlignCenter)
        self.doubleSpinBoxTeamScore_3.setMaximum(10000.000000000000000)

        self.horizontalLayout_28.addWidget(self.doubleSpinBoxTeamScore_3)

        self.label_34 = QLabel(self.frame_15)
        self.label_34.setObjectName(u"label_34")
        sizePolicy5.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy5)
        self.label_34.setFont(font)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_34)

        self.doubleSpinBoxTeamScore_4 = QDoubleSpinBox(self.frame_15)
        self.doubleSpinBoxTeamScore_4.setObjectName(u"doubleSpinBoxTeamScore_4")
        self.doubleSpinBoxTeamScore_4.setAlignment(Qt.AlignCenter)
        self.doubleSpinBoxTeamScore_4.setMaximum(10000.000000000000000)

        self.horizontalLayout_28.addWidget(self.doubleSpinBoxTeamScore_4)

        self.label_35 = QLabel(self.frame_15)
        self.label_35.setObjectName(u"label_35")
        sizePolicy5.setHeightForWidth(self.label_35.sizePolicy().hasHeightForWidth())
        self.label_35.setSizePolicy(sizePolicy5)
        self.label_35.setFont(font)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_35)

        self.doubleSpinBoxTeamScore_5 = QDoubleSpinBox(self.frame_15)
        self.doubleSpinBoxTeamScore_5.setObjectName(u"doubleSpinBoxTeamScore_5")
        self.doubleSpinBoxTeamScore_5.setAlignment(Qt.AlignCenter)
        self.doubleSpinBoxTeamScore_5.setMaximum(10000.000000000000000)

        self.horizontalLayout_28.addWidget(self.doubleSpinBoxTeamScore_5)

        self.label_37 = QLabel(self.frame_15)
        self.label_37.setObjectName(u"label_37")
        sizePolicy5.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy5)
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_37)

        self.horizontalLayout_28.setStretch(0, 2)
        self.horizontalLayout_28.setStretch(2, 2)
        self.horizontalLayout_28.setStretch(4, 2)
        self.horizontalLayout_28.setStretch(6, 2)
        self.horizontalLayout_28.setStretch(8, 2)

        self.verticalLayout_24.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, -1, -1, 0)
        self.checkBoxTeam4End = QCheckBox(self.frame_15)
        self.checkBoxTeam4End.setObjectName(u"checkBoxTeam4End")
        sizePolicy6 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.checkBoxTeam4End.sizePolicy().hasHeightForWidth())
        self.checkBoxTeam4End.setSizePolicy(sizePolicy6)

        self.horizontalLayout_29.addWidget(self.checkBoxTeam4End)

        self.label_36 = QLabel(self.frame_15)
        self.label_36.setObjectName(u"label_36")
        sizePolicy5.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy5)
        self.label_36.setFont(font)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_36)

        self.spinBoxTeamGdxz = QSpinBox(self.frame_15)
        self.spinBoxTeamGdxz.setObjectName(u"spinBoxTeamGdxz")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.spinBoxTeamGdxz.sizePolicy().hasHeightForWidth())
        self.spinBoxTeamGdxz.setSizePolicy(sizePolicy7)
        self.spinBoxTeamGdxz.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxTeamGdxz.setAlignment(Qt.AlignCenter)
        self.spinBoxTeamGdxz.setMaximum(10000)

        self.horizontalLayout_29.addWidget(self.spinBoxTeamGdxz)

        self.label_40 = QLabel(self.frame_15)
        self.label_40.setObjectName(u"label_40")
        sizePolicy5.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy5)
        self.label_40.setFont(font)
        self.label_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_40)

        self.spinBoxTeamQqcz = QSpinBox(self.frame_15)
        self.spinBoxTeamQqcz.setObjectName(u"spinBoxTeamQqcz")
        sizePolicy7.setHeightForWidth(self.spinBoxTeamQqcz.sizePolicy().hasHeightForWidth())
        self.spinBoxTeamQqcz.setSizePolicy(sizePolicy7)
        self.spinBoxTeamQqcz.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxTeamQqcz.setAlignment(Qt.AlignCenter)
        self.spinBoxTeamQqcz.setMaximum(10000)

        self.horizontalLayout_29.addWidget(self.spinBoxTeamQqcz)

        self.label_41 = QLabel(self.frame_15)
        self.label_41.setObjectName(u"label_41")
        sizePolicy5.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy5)
        self.label_41.setFont(font)
        self.label_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_41)

        self.spinBoxTeamDup = QSpinBox(self.frame_15)
        self.spinBoxTeamDup.setObjectName(u"spinBoxTeamDup")
        sizePolicy7.setHeightForWidth(self.spinBoxTeamDup.sizePolicy().hasHeightForWidth())
        self.spinBoxTeamDup.setSizePolicy(sizePolicy7)
        self.spinBoxTeamDup.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxTeamDup.setAlignment(Qt.AlignCenter)
        self.spinBoxTeamDup.setMaximum(10000)

        self.horizontalLayout_29.addWidget(self.spinBoxTeamDup)

        self.label_42 = QLabel(self.frame_15)
        self.label_42.setObjectName(u"label_42")
        sizePolicy5.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy5)
        self.label_42.setFont(font)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_42)

        self.spinBoxTeamDupEw = QSpinBox(self.frame_15)
        self.spinBoxTeamDupEw.setObjectName(u"spinBoxTeamDupEw")
        sizePolicy7.setHeightForWidth(self.spinBoxTeamDupEw.sizePolicy().hasHeightForWidth())
        self.spinBoxTeamDupEw.setSizePolicy(sizePolicy7)
        self.spinBoxTeamDupEw.setMaximumSize(QSize(16777215, 16777215))
        self.spinBoxTeamDupEw.setAlignment(Qt.AlignCenter)
        self.spinBoxTeamDupEw.setMaximum(10000)

        self.horizontalLayout_29.addWidget(self.spinBoxTeamDupEw)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_8)


        self.verticalLayout_24.addLayout(self.horizontalLayout_29)


        self.verticalLayout_25.addLayout(self.verticalLayout_24)


        self.horizontalLayout_30.addWidget(self.frame_15)

        self.label_39 = QLabel(self.frame_14)
        self.label_39.setObjectName(u"label_39")
        sizePolicy5.setHeightForWidth(self.label_39.sizePolicy().hasHeightForWidth())
        self.label_39.setSizePolicy(sizePolicy5)
        self.label_39.setFont(font10)
        self.label_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_39)

        self.labelTeamScore = QLabel(self.frame_14)
        self.labelTeamScore.setObjectName(u"labelTeamScore")
        self.labelTeamScore.setFont(font10)
        self.labelTeamScore.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.labelTeamScore)

        self.horizontalLayout_30.setStretch(0, 5)
        self.horizontalLayout_30.setStretch(2, 2)

        self.verticalLayout_23.addLayout(self.horizontalLayout_30)


        self.verticalLayout_7.addWidget(self.frame_14)

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
        self.checkBoxPause.setFont(font3)
        self.checkBoxPause.setFocusPolicy(Qt.ClickFocus)
        self.checkBoxPause.setCheckable(True)
        self.checkBoxPause.setChecked(False)

        self.horizontalLayout_9.addWidget(self.checkBoxPause)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.horizontalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.labelConState = QLabel(self.frame_3)
        self.labelConState.setObjectName(u"labelConState")
        font11 = QFont()
        font11.setPointSize(10)
        font11.setBold(True)
        font11.setItalic(False)
        self.labelConState.setFont(font11)
        self.labelConState.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.labelConState)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lineEditServer = QLineEdit(self.frame_3)
        self.lineEditServer.setObjectName(u"lineEditServer")
        sizePolicy.setHeightForWidth(self.lineEditServer.sizePolicy().hasHeightForWidth())
        self.lineEditServer.setSizePolicy(sizePolicy)
        self.lineEditServer.setMinimumSize(QSize(100, 0))
        font12 = QFont()
        font12.setPointSize(10)
        self.lineEditServer.setFont(font12)
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

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.horizontalLayout.setStretch(4, 2)

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
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6709\u6548\u8bb0\u5f55:", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6700\u9ad8\u5206:", None))
        self.lineEditPlayerName.setText("")
        self.lineEditPlayerName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u65e0\u6635\u79f0", None))
        self.lineEditPlayerNote.setText("")
        self.lineEditPlayerNote.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u65e0\u5907\u6ce8", None))
        self.labelPlayerUUID.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.labelPlayerLastSaveTime.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.labelPlayerRecordNum.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.labelPlayerMaxRecord.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u5c40\u5206\u961f:", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u5c40\u5e72\u5458:", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u676f\u7ea7:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u6240\u5c5e\u961f\u4f0d:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u76f8\u9047\u9009\u62e9:", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u8bf4:", None))
        self.comboBoxStartTeam.setItemText(0, QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))

        self.comboBoxStartOperator.setItemText(0, QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))

        self.comboBoxCup.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5927\u5565\u676f", None))
        self.comboBoxCup.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5565\u676f", None))

        self.lineEditPlayerTeam.setText("")
        self.lineEditPlayerTeam.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.lineEditPlayerSelect.setText("")
        self.lineEditPlayerSelect.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u672a\u77e5", None))
        self.lineEditSpeaker.setText("")
        self.lineEditSpeaker.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u672a\u8bbe\u7f6e, \u7528\u9017\u53f7\u5206\u9694", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5e72\u5458\u9009\u62e9:", None))
        self.pushButtonAddPlayer.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.pushButtonDelPlayer.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u69fd\u4f4d:", None))
        self.pushButtonClrRecord.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u96f6\u6b64\u8bb0\u5f55", None))
        self.pushButtonSyncOBS.setText(QCoreApplication.translate("MainWindow", u"\u540c\u6b65OBS", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u3000\u4e2a\u4eba \u8ba1\u5206\u677f\u3000\u2014\u2014", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u4e34\u65f6\u62db\u52df", None))
        self.labelHeaderTemp.setText(QCoreApplication.translate("MainWindow", u"[\u603b\u6570] \u516d\u661f: 0 \u4e94\u661f: 0 \u56db\u661f: 0", None))
        self.radioButtonTempSix.setText(QCoreApplication.translate("MainWindow", u"\u516d\u661f", None))
        self.radioButtonTempFive.setText(QCoreApplication.translate("MainWindow", u"\u4e94\u661f", None))
        self.radioButtonTempFour.setText(QCoreApplication.translate("MainWindow", u"\u56db\u661f", None))
        self.pushButtonSubmitTemp.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u7279\u6b8a\u51fb\u6740", None))
        self.labelHeaderkillSp.setText(QCoreApplication.translate("MainWindow", u"[\u603b\u6570] \u51fb\u6740 0 \u53ea\u9e2d/\u72d7/\u718a", None))
        self.labelKillSp.setText(QCoreApplication.translate("MainWindow", u"\u672c\u6b21\u51fb\u6740 ", None))
        self.spinBoxKillSp.setSuffix(QCoreApplication.translate("MainWindow", u"\u53ea", None))
        self.spinBoxKillSp.setPrefix("")
        self.pushButtonSubmitKillSp.setText(QCoreApplication.translate("MainWindow", u"\u589e\u52a0", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u7d27\u6025/\u9690\u85cf\u5173\u5361 (\u4e0d\u5305\u62ec\u62f1\u95e8\u901a\u5173)", None))
        self.comboBoxEmerg.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5927\u68cb\u4e00\u76d8", None))
        self.comboBoxEmerg.setItemText(1, QCoreApplication.translate("MainWindow", u"\u6e83\u4e71\u9b54\u5178", None))
        self.comboBoxEmerg.setItemText(2, QCoreApplication.translate("MainWindow", u"\u673a\u52a8\u961f", None))
        self.comboBoxEmerg.setItemText(3, QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2193 \u56db\u5c42 \u2193\u2014\u2014", None))
        self.comboBoxEmerg.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5047\u60f3\u5bf9\u51b2", None))
        self.comboBoxEmerg.setItemText(5, QCoreApplication.translate("MainWindow", u"\u5e74\u4ee3\u65ad\u5c42", None))
        self.comboBoxEmerg.setItemText(6, QCoreApplication.translate("MainWindow", u"\u7329\u7ea2\u752c\u9053", None))
        self.comboBoxEmerg.setItemText(7, QCoreApplication.translate("MainWindow", u"\u6df7\u6c8c", None))
        self.comboBoxEmerg.setItemText(8, QCoreApplication.translate("MainWindow", u"\u795e\u51fa\u9b3c\u6ca1", None))
        self.comboBoxEmerg.setItemText(9, QCoreApplication.translate("MainWindow", u"\u4e89\u8bae\u9891\u53d1", None))
        self.comboBoxEmerg.setItemText(10, QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2193 \u4e94\u5c42 \u2193\u2014\u2014", None))
        self.comboBoxEmerg.setItemText(11, QCoreApplication.translate("MainWindow", u"\u901a\u9053\u5c01\u9501", None))
        self.comboBoxEmerg.setItemText(12, QCoreApplication.translate("MainWindow", u"\u5bc4\u4eba\u57ce\u6c60\u4e0b", None))
        self.comboBoxEmerg.setItemText(13, QCoreApplication.translate("MainWindow", u"\u8ba1\u5212\u8015\u79cd", None))
        self.comboBoxEmerg.setItemText(14, QCoreApplication.translate("MainWindow", u"\u83b1\u8335\u536b\u58eb", None))
        self.comboBoxEmerg.setItemText(15, QCoreApplication.translate("MainWindow", u"\u5efa\u5236", None))
        self.comboBoxEmerg.setItemText(16, QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2193 \u516d\u5c42 \u2193\u2014\u2014", None))
        self.comboBoxEmerg.setItemText(17, QCoreApplication.translate("MainWindow", u"\u795e\u5723\u7684\u6e34\u6c42", None))
        self.comboBoxEmerg.setItemText(18, QCoreApplication.translate("MainWindow", u"\u8c0b\u6c42\u5171\u8bc6", None))
        self.comboBoxEmerg.setItemText(19, QCoreApplication.translate("MainWindow", u"\u5916\u9053", None))
        self.comboBoxEmerg.setItemText(20, QCoreApplication.translate("MainWindow", u"\u6d1e\u5929\u798f\u5730", None))
        self.comboBoxEmerg.setItemText(21, QCoreApplication.translate("MainWindow", u"\u2014\u2014\u2193 \u9690\u85cf \u2193\u2014\u2014", None))
        self.comboBoxEmerg.setItemText(22, QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u52ab\u865a\u6d4e\u5b9e\u65e0\u6f0f", None))
        self.comboBoxEmerg.setItemText(23, QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u6218\u573a\u4fa7\u9762", None))
        self.comboBoxEmerg.setItemText(24, QCoreApplication.translate("MainWindow", u"\u65a9\u9996", None))
        self.comboBoxEmerg.setItemText(25, QCoreApplication.translate("MainWindow", u"\u5949\u732e", None))
        self.comboBoxEmerg.setItemText(26, QCoreApplication.translate("MainWindow", u"\u6216\u7136\u9762\u7eb1", None))
        self.comboBoxEmerg.setItemText(27, QCoreApplication.translate("MainWindow", u"\u79bb\u6b4c\u7684\u5ead\u9662", None))
        self.comboBoxEmerg.setItemText(28, QCoreApplication.translate("MainWindow", u"\u8d74\u654c\u8005", None))
        self.comboBoxEmerg.setItemText(29, QCoreApplication.translate("MainWindow", u"\u738b\u51a0\u4e4b\u4e0b", None))

        self.pushButtonSubmitEmerg.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u8fbe\u6210\u7ed3\u5c40", None))
        self.comboBoxEnding.setItemText(0, QCoreApplication.translate("MainWindow", u"\u7d27\u6025\u6388\u8bfe", None))
        self.comboBoxEnding.setItemText(1, QCoreApplication.translate("MainWindow", u"\u671d\u8c12", None))
        self.comboBoxEnding.setItemText(2, QCoreApplication.translate("MainWindow", u"\u601d\u7ef4\u77eb\u6b63", None))
        self.comboBoxEnding.setItemText(3, QCoreApplication.translate("MainWindow", u"\u9b42\u7075\u671d\u8c12", None))
        self.comboBoxEnding.setItemText(4, QCoreApplication.translate("MainWindow", u"\u5723\u57ce", None))
        self.comboBoxEnding.setItemText(5, QCoreApplication.translate("MainWindow", u"\u6388\u6cd5", None))
        self.comboBoxEnding.setItemText(6, QCoreApplication.translate("MainWindow", u"\u4e0d\u5bb9\u62d2\u7edd", None))

        self.comboBoxEndingEx.setItemText(0, QCoreApplication.translate("MainWindow", u"\u666e\u901a", None))
        self.comboBoxEndingEx.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7d27\u6025", None))

        self.checkBoxEndingChaos.setText(QCoreApplication.translate("MainWindow", u"\u6df7\u4e71\u901a\u5173", None))
        self.pushButtonSubmitEnding.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u7279\u6b8a\u4e58\u7b97/\u52a0\u5206/\u6263\u5206", None))
        self.radioButtonSpDsb.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5565\u676f\u8fdb\u5165\u516d\u5c42\u5173\u5e95", None))
        self.radioButtonSpSsef.setText(QCoreApplication.translate("MainWindow", u"\u4f3c\u662f\u800c\u975e\u8865\u507f\u5206", None))
#if QT_CONFIG(tooltip)
        self.radioButtonSpRed.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u2460\u85cf\u54c1\u6c60\u4e2d\u6709\u201d\u963f\u7eb3\u8428\u7faf\u78e8\u201c\u6216\u201d\u65e0\u7ec8\u4e4b\u94a5\u201c\u3002</p><p>\u2461\u5728\u62e5\u6709\u201d\u7edd\u671b/\u62ef\u6551/\u505c\u6b62\u201c\u7684\u60c5\u51b5\u4e0b\u8fdb\u5165\u81f3\u5c11\u4e24\u4e2a\u4e0d\u671f\u800c\u9047\u4f46\u672a\u9047\u89c1\u4e8b\u4ef6\u201c\u5b64\u6ce8\u4e00\u63b7\u201d\u3002</p><p>\u2462\u6301\u6709\u201c\u7247\u74e3\u201d\u8fdb\u5165\u4e94\u5c42\u65f6\u4e0d\u5b58\u5728\u201c\u72ed\u8def\u76f8\u9022\u201d\u8282\u70b9\u3002</p><p>\u901a\u5173\u65f6\u82e5\u2460\u2461\u2462\u4e2d\u7684\u4efb\u610f\u4e00\u6761\u90fd\u4e0d\u6ee1\u8db3\u5219\u6263 500 \u5206</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButtonSpRed.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u7b97\u6263\u5206 (\u9f20\u6807\u60ac\u505c\u770b\u7ec6\u5219)", None))
        self.pushButtonSubmitSp.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u57fa\u7840\u5206\u6570", None))
        self.spinBoxBaseScore.setSuffix("")
        self.spinBoxBaseScore.setPrefix("")
        self.pushButtonXXX.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u81ea\u5b9a\u4e49\u589e\u51cf (\u5c42\u6570\u5206\u7528\u8fd9\u4e2a)", None))
        self.lineEditCustomScore.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7406\u7531", None))
        self.pushButtonSubmitCustom.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u8be6\u7ec6\u8bb0\u5f55 (\u53f3\u952e\u8bb0\u5f55\u53ef\u5220\u9664)", None))
#if QT_CONFIG(tooltip)
        self.listRecord.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u603b\u5206:", None))
        self.labelScore.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u2014\u2014\u3000\u961f\u4f0d \u8ba1\u7b97\u5668\u3000\u2014\u2014", None))
        self.doubleSpinBoxTeamScore_1.setSuffix("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.doubleSpinBoxTeamScore_2.setSuffix("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.doubleSpinBoxTeamScore_3.setSuffix("")
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.doubleSpinBoxTeamScore_4.setSuffix("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.doubleSpinBoxTeamScore_5.setSuffix("")
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.checkBoxTeam4End.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5f53\u961f\u4f0d\u6210\u529f\u6218\u80dc\u201d\u201c\u963f\u7c73\u5a05\u201d\uff0c\u7089\u82af\u7ec8\u66f2\u201c\u201d\u594e\u9686\uff0c\u6469\u8bc3\u8428\u57f5\u6743\u5316\u201c\u201d\u7279\u96f7\u897f\u65af\uff0c\u9ed1\u51a0\u5c0a\u4e3b\u201c\u201d\u5f17\u83b1\u8499\u7279\uff0c\u8bf8\u601d\u4e4b\u89e3\u7b54\u201c\u65f6+1000 \u5206\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.checkBoxTeam4End.setText(QCoreApplication.translate("MainWindow", u"\u96c6\u9f50\u56db\u4e2a\u7ed3\u5c40", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(tooltip)
        self.spinBoxTeamGdxz.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5f53\u961f\u4f0d\u9009\u624b\u6301\u6709\u201d\u6eda\u52a8\u5148\u7956\u201c\u901a\u5173\u56db\u7ed3\u5c40\u6216\u4e94\u7ed3\u5c40\u65f6\uff0c\u7b2c\u4e00\u4f4d\u4e3a\u961f\u4f0d\u8d62\u5f97 300 \u5206\uff0c\u7b2c\u4e8c\u7b2c\u4e09\u4f4d 200 \u5206\uff0c\u7b2c\u56db\u7b2c\u4e94\u4f4d 0 \u5206\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.spinBoxTeamGdxz.setSuffix(QCoreApplication.translate("MainWindow", u"\u4e2a", None))
        self.spinBoxTeamGdxz.setPrefix(QCoreApplication.translate("MainWindow", u"\u6eda\u52a8\u5148\u7956", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(tooltip)
        self.spinBoxTeamQqcz.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u5546\u5e97\u53d6\u94b1\u89c4\u5219\u4e3a\u5168\u961f\u5171\u4eab\u4f59\u989d\uff0c\u4f59\u989d\u603b\u6570\u4e3a 999\u3002\u82e5\u8d85\u51fa 999 \u70b9\uff0c\u6bcf\u8d85\u51fa\u4e00\u70b9\u4fbf\u6263\u9664\u961f\u4f0d\u603b\u5206 100 \u5206\u3002</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.spinBoxTeamQqcz.setSuffix(QCoreApplication.translate("MainWindow", u"\u70b9", None))
        self.spinBoxTeamQqcz.setPrefix(QCoreApplication.translate("MainWindow", u"\u53d6\u94b1\u8d85\u652f", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.spinBoxTeamDup.setSuffix(QCoreApplication.translate("MainWindow", u"\u4e2a", None))
        self.spinBoxTeamDup.setPrefix(QCoreApplication.translate("MainWindow", u"\u91cd\u590d\u516d\u661f", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.spinBoxTeamDupEw.setSuffix(QCoreApplication.translate("MainWindow", u"\u4e2a", None))
        self.spinBoxTeamDupEw.setPrefix(QCoreApplication.translate("MainWindow", u"\u91cd\u590dew ", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.labelTeamScore.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.checkBoxPause.setText(QCoreApplication.translate("MainWindow", u"\u6682\u505cOBS\u4fe1\u606f\u540c\u6b65", None))
        self.labelConState.setText(QCoreApplication.translate("MainWindow", u"/// PRTS \u672a\u8fde\u63a5 ///", None))
        self.lineEditServer.setText(QCoreApplication.translate("MainWindow", u"localhost", None))
        self.pushButtonConnect.setText(QCoreApplication.translate("MainWindow", u"\u8fde\u63a5OBS", None))
    # retranslateUi

