# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'magisterka_guiXFjfOj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from AnalogGaugeWidget import AnalogGaugeWidget
from QChartViewPointer import QChartView

import icons_rc
import zdjecia_rc
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1920, 1080)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QSize(1920, 1080))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setContextMenuPolicy(Qt.NoContextMenu)
        MainWindow.setAcceptDrops(False)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"QToolTip {\n"
"	border: 3px solid rgb(0, 0, 127)i;\n"
"    padding: 5px;\n"
"    border-radius: 10px;\n"
"    opacity: 200;\n"
"	background-color: rgb(15, 14, 28);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QMessageBox {\n"
"	background-color: rgb(35, 32, 47);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"border: 10px solid rgb(0, 0, 0)i;\n"
"}")
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu_container = QFrame(self.centralwidget)
        self.side_menu_container.setObjectName(u"side_menu_container")
        self.side_menu_container.setMinimumSize(QSize(50, 0))
        self.side_menu_container.setMaximumSize(QSize(250, 16777215))
        self.side_menu_container.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color:rgb(39, 36, 44);\n"
"}")
        self.side_menu_container.setFrameShape(QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.side_menu_container)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_menu = QFrame(self.side_menu_container)
        self.slide_menu.setObjectName(u"slide_menu")
        self.slide_menu.setMinimumSize(QSize(0, 0))
        self.slide_menu.setMaximumSize(QSize(300, 16777215))
        self.slide_menu.setStyleSheet(u"QFrame\n"
"{\n"
"background-color:transparent;\n"
"border:none;\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton\n"
"{\n"
"border:none;\n"
"}")
        self.slide_menu.setFrameShape(QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.slide_menu)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.slide_menu)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"border-top-left-radius:0px;\n"
"border-bottom-left-radius:30px;\n"
"background-color:rgb(0, 0, 0);\n"
"}\n"
"QLabel\n"
"{\n"
"border:none;\n"
"}\n"
"QFrame::hover{\n"
"background-color:rgb(94, 92, 100);\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_3)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 9, 0, 9)
        self.Run_AirSim = QPushButton(self.frame_3)
        self.Run_AirSim.setObjectName(u"Run_AirSim")
        self.Run_AirSim.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-drone-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Run_AirSim.setIcon(icon)
        self.Run_AirSim.setIconSize(QSize(64, 64))

        self.verticalLayout_16.addWidget(self.Run_AirSim, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_5 = QFrame(self.slide_menu)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy1)
        self.frame_5.setStyleSheet(u"QFrame\n"
"{\n"
"border-top-left-radius:40px;\n"
"border-bottom-left-radius:40px;\n"
"color:rgb(246, 245, 244);\n"
"}\n"
"QLabel\n"
"{\n"
"border:none;\n"
"}\n"
"QPushButton\n"
"{\n"
"border:none;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Home_frame = QFrame(self.frame_5)
        self.Home_frame.setObjectName(u"Home_frame")
        self.Home_frame.setToolTipDuration(-1)
        self.Home_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(1, 5, 44, 255), stop:1 rgba(16, 14, 27, 255));\n"
"}\n"
"QFrame::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}\n"
"QLabel\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.Home_frame.setFrameShape(QFrame.StyledPanel)
        self.Home_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.Home_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.Home_button = QPushButton(self.Home_frame)
        self.Home_button.setObjectName(u"Home_button")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-home-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Home_button.setIcon(icon1)
        self.Home_button.setIconSize(QSize(64, 64))
        self.Home_button.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.Home_button, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.Home = QLabel(self.Home_frame)
        self.Home.setObjectName(u"Home")

        self.horizontalLayout_7.addWidget(self.Home)

        self.Home.raise_()
        self.Home_button.raise_()

        self.verticalLayout_6.addWidget(self.Home_frame)

        self.VR_frame = QFrame(self.frame_5)
        self.VR_frame.setObjectName(u"VR_frame")
        self.VR_frame.setToolTipDuration(-1)
        self.VR_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"}\n"
"QFrame::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}\n"
"QLabel\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.VR_frame.setFrameShape(QFrame.StyledPanel)
        self.VR_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.VR_frame)
        self.horizontalLayout_41.setSpacing(0)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.VR_Button = QPushButton(self.VR_frame)
        self.VR_Button.setObjectName(u"VR_Button")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-vr-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_Button.setIcon(icon2)
        self.VR_Button.setIconSize(QSize(64, 64))
        self.VR_Button.setCheckable(True)

        self.horizontalLayout_41.addWidget(self.VR_Button)

        self.VR = QLabel(self.VR_frame)
        self.VR.setObjectName(u"VR")

        self.horizontalLayout_41.addWidget(self.VR, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.VR_frame)

        self.Settings_frame = QFrame(self.frame_5)
        self.Settings_frame.setObjectName(u"Settings_frame")
        self.Settings_frame.setToolTipDuration(-1)
        self.Settings_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"}\n"
"QFrame::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}\n"
"QLabel\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.Settings_frame.setFrameShape(QFrame.StyledPanel)
        self.Settings_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.Settings_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.Settings_button = QPushButton(self.Settings_frame)
        self.Settings_button.setObjectName(u"Settings_button")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-settings-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Settings_button.setIcon(icon3)
        self.Settings_button.setIconSize(QSize(64, 64))
        self.Settings_button.setCheckable(True)

        self.horizontalLayout_8.addWidget(self.Settings_button, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.Settings = QLabel(self.Settings_frame)
        self.Settings.setObjectName(u"Settings")

        self.horizontalLayout_8.addWidget(self.Settings, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.Settings_frame)

        self.Parametry_frame = QFrame(self.frame_5)
        self.Parametry_frame.setObjectName(u"Parametry_frame")
        self.Parametry_frame.setToolTipDuration(-1)
        self.Parametry_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"}\n"
"QFrame::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}\n"
"QLabel\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.Parametry_frame.setFrameShape(QFrame.StyledPanel)
        self.Parametry_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.Parametry_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.Parametry_button = QPushButton(self.Parametry_frame)
        self.Parametry_button.setObjectName(u"Parametry_button")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-drone-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Parametry_button.setIcon(icon4)
        self.Parametry_button.setIconSize(QSize(64, 64))
        self.Parametry_button.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.Parametry_button, 0, Qt.AlignLeft)

        self.Parametry = QLabel(self.Parametry_frame)
        self.Parametry.setObjectName(u"Parametry")

        self.horizontalLayout_9.addWidget(self.Parametry, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.Parametry_frame)

        self.Przewodnik_frame = QFrame(self.frame_5)
        self.Przewodnik_frame.setObjectName(u"Przewodnik_frame")
        self.Przewodnik_frame.setToolTipDuration(-1)
        self.Przewodnik_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"}\n"
"QFrame::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}\n"
"QLabel\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.Przewodnik_frame.setFrameShape(QFrame.StyledPanel)
        self.Przewodnik_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.Przewodnik_frame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.Przewodnik_button = QPushButton(self.Przewodnik_frame)
        self.Przewodnik_button.setObjectName(u"Przewodnik_button")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-task-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Przewodnik_button.setIcon(icon5)
        self.Przewodnik_button.setIconSize(QSize(64, 64))
        self.Przewodnik_button.setCheckable(True)

        self.horizontalLayout_10.addWidget(self.Przewodnik_button, 0, Qt.AlignLeft)

        self.Przewodnik = QLabel(self.Przewodnik_frame)
        self.Przewodnik.setObjectName(u"Przewodnik")

        self.horizontalLayout_10.addWidget(self.Przewodnik, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.Przewodnik_frame)

        self.Misje_frame = QFrame(self.frame_5)
        self.Misje_frame.setObjectName(u"Misje_frame")
        self.Misje_frame.setToolTipDuration(-1)
        self.Misje_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"}\n"
"QFrame::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}\n"
"QLabel\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.Misje_frame.setFrameShape(QFrame.StyledPanel)
        self.Misje_frame.setFrameShadow(QFrame.Sunken)
        self.Misje_frame.setLineWidth(1)
        self.Misje_frame.setMidLineWidth(0)
        self.horizontalLayout_11 = QHBoxLayout(self.Misje_frame)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.Misje_button = QPushButton(self.Misje_frame)
        self.Misje_button.setObjectName(u"Misje_button")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-charts-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Misje_button.setIcon(icon6)
        self.Misje_button.setIconSize(QSize(64, 64))
        self.Misje_button.setCheckable(True)

        self.horizontalLayout_11.addWidget(self.Misje_button, 0, Qt.AlignLeft)

        self.Misje = QLabel(self.Misje_frame)
        self.Misje.setObjectName(u"Misje")

        self.horizontalLayout_11.addWidget(self.Misje, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.Misje_frame)

        self.Analiza_frame = QFrame(self.frame_5)
        self.Analiza_frame.setObjectName(u"Analiza_frame")
        self.Analiza_frame.setToolTipDuration(-1)
        self.Analiza_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"}\n"
"QFrame::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}\n"
"QLabel\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.Analiza_frame.setFrameShape(QFrame.NoFrame)
        self.Analiza_frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_12 = QHBoxLayout(self.Analiza_frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.Analiza_button = QPushButton(self.Analiza_frame)
        self.Analiza_button.setObjectName(u"Analiza_button")
        self.Analiza_button.setFocusPolicy(Qt.StrongFocus)
        self.Analiza_button.setAcceptDrops(False)
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-analysis-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Analiza_button.setIcon(icon7)
        self.Analiza_button.setIconSize(QSize(64, 64))
        self.Analiza_button.setCheckable(True)
        self.Analiza_button.setFlat(False)

        self.horizontalLayout_12.addWidget(self.Analiza_button, 0, Qt.AlignLeft)

        self.Analiza = QLabel(self.Analiza_frame)
        self.Analiza.setObjectName(u"Analiza")
        self.Analiza.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.Analiza, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.Analiza_frame)

        self.Informacje_frame = QFrame(self.frame_5)
        self.Informacje_frame.setObjectName(u"Informacje_frame")
        self.Informacje_frame.setToolTipDuration(-1)
        self.Informacje_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"border-bottom-left-radius:0px;\n"
"}\n"
"QFrame::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}\n"
"QLabel\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"")
        self.Informacje_frame.setFrameShape(QFrame.StyledPanel)
        self.Informacje_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.Informacje_frame)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Informacje_button = QPushButton(self.Informacje_frame)
        self.Informacje_button.setObjectName(u"Informacje_button")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-info-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Informacje_button.setIcon(icon8)
        self.Informacje_button.setIconSize(QSize(64, 64))
        self.Informacje_button.setCheckable(True)

        self.horizontalLayout_13.addWidget(self.Informacje_button, 0, Qt.AlignLeft)

        self.Informacje = QLabel(self.Informacje_frame)
        self.Informacje.setObjectName(u"Informacje")

        self.horizontalLayout_13.addWidget(self.Informacje, 0, Qt.AlignHCenter)


        self.verticalLayout_6.addWidget(self.Informacje_frame)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout_2.addWidget(self.slide_menu)


        self.horizontalLayout.addWidget(self.side_menu_container)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setMaximumSize(QSize(1900, 16777215))
        self.main_body.setStyleSheet(u"QFrame{\n"
"border:none;\n"
"}")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMaximumSize(QSize(16777215, 100))
        self.header_frame.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(1, 5, 44, 255), stop:1 rgba(16, 14, 27, 255));\n"
"}\n"
"QPushButton\n"
"{\n"
"background-color:transparent;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgb(71, 79, 136);\n"
"}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.header_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Menu_button = QPushButton(self.frame)
        self.Menu_button.setObjectName(u"Menu_button")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-menu-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_button.setIcon(icon9)
        self.Menu_button.setIconSize(QSize(40, 40))
        self.Menu_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.Menu_button)

        self.Clear_button = QPushButton(self.frame)
        self.Clear_button.setObjectName(u"Clear_button")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-clear-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Clear_button.setIcon(icon10)
        self.Clear_button.setIconSize(QSize(40, 40))
        self.Clear_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.Clear_button)

        self.Camera_button = QPushButton(self.frame)
        self.Camera_button.setObjectName(u"Camera_button")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-camera-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Camera_button.setIcon(icon11)
        self.Camera_button.setIconSize(QSize(40, 40))
        self.Camera_button.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.Camera_button)


        self.horizontalLayout_43.addWidget(self.frame)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer)

        self.frame_2 = QFrame(self.header_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(200, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.Min = QPushButton(self.frame_2)
        self.Min.setObjectName(u"Min")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Min.sizePolicy().hasHeightForWidth())
        self.Min.setSizePolicy(sizePolicy3)
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-minimize-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Min.setIcon(icon12)
        self.Min.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.Min)

        self.Max = QPushButton(self.frame_2)
        self.Max.setObjectName(u"Max")
        sizePolicy3.setHeightForWidth(self.Max.sizePolicy().hasHeightForWidth())
        self.Max.setSizePolicy(sizePolicy3)
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-resize-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Max.setIcon(icon13)
        self.Max.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.Max)

        self.Close = QPushButton(self.frame_2)
        self.Close.setObjectName(u"Close")
        sizePolicy3.setHeightForWidth(self.Close.sizePolicy().hasHeightForWidth())
        self.Close.setSizePolicy(sizePolicy3)
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close.setIcon(icon14)
        self.Close.setIconSize(QSize(32, 32))

        self.horizontalLayout_5.addWidget(self.Close)


        self.horizontalLayout_43.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.main_body)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1421, 700))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"QStackedWidget\n"
"{\n"
"	background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(1, 5, 44, 255), stop:1 rgba(16, 14, 27, 255));\n"
"color:rgb(255, 255, 255);\n"
"border:none;\n"
"}\n"
"")
        self.stackedWidget.setLineWidth(0)
        self.Home_page = QWidget()
        self.Home_page.setObjectName(u"Home_page")
        self.Home_page.setStyleSheet(u"border-image: url(:/Zdjecia/Zdjecia/Zrzut ekranu (3).png) 0 0 0 0 stretch stretch;\n"
"")
        self.stackedWidget.addWidget(self.Home_page)
        self.Settings_page = QWidget()
        self.Settings_page.setObjectName(u"Settings_page")
        self.Settings_page.setStyleSheet(u"background-color:transparent;\n"
"background-repeat: no-repeat;\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(255, 255, 255);")
        self.horizontalLayout_39 = QHBoxLayout(self.Settings_page)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.frame_7 = QFrame(self.Settings_page)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy3.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy3)
        self.frame_7.setMinimumSize(QSize(1000, 0))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_7)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_27 = QLabel(self.frame_7)
        self.label_27.setObjectName(u"label_27")
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_27.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_27, 0, Qt.AlignHCenter)

        self.WyborMapy_frame = QFrame(self.frame_7)
        self.WyborMapy_frame.setObjectName(u"WyborMapy_frame")
        self.WyborMapy_frame.setStyleSheet(u"QFrame{\n"
"	border-top: 1px solid rgb(36, 31, 49);\n"
"	border-right: rgb(255, 255, 255);\n"
"	border-bottom: 1px solid rgb(36, 31, 49);\n"
"	border-left: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"}")
        self.WyborMapy_frame.setFrameShape(QFrame.StyledPanel)
        self.WyborMapy_frame.setFrameShadow(QFrame.Raised)
        self.WyborMapy_frame.setLineWidth(1)
        self.verticalLayout_7 = QVBoxLayout(self.WyborMapy_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.Blocks_frame = QFrame(self.WyborMapy_frame)
        self.Blocks_frame.setObjectName(u"Blocks_frame")
        self.Blocks_frame.setStyleSheet(u"")
        self.Blocks_frame.setFrameShape(QFrame.StyledPanel)
        self.Blocks_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Blocks_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Btn_Blocks = QRadioButton(self.Blocks_frame)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.Btn_Blocks)
        self.Btn_Blocks.setObjectName(u"Btn_Blocks")
        self.Btn_Blocks.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_6.addWidget(self.Btn_Blocks)

        self.Title_Blocks = QLabel(self.Blocks_frame)
        self.Title_Blocks.setObjectName(u"Title_Blocks")
        font2 = QFont()
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.Title_Blocks.setFont(font2)

        self.horizontalLayout_6.addWidget(self.Title_Blocks)

        self.Opis_Blocks = QLabel(self.Blocks_frame)
        self.Opis_Blocks.setObjectName(u"Opis_Blocks")
        self.Opis_Blocks.setMaximumSize(QSize(200, 16777215))
        self.Opis_Blocks.setWordWrap(True)

        self.horizontalLayout_6.addWidget(self.Opis_Blocks)

        self.Zdj_Blocks = QLabel(self.Blocks_frame)
        self.Zdj_Blocks.setObjectName(u"Zdj_Blocks")
        self.Zdj_Blocks.setMaximumSize(QSize(170, 16777215))
        self.Zdj_Blocks.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/rsz_blocks.png"))
        self.Zdj_Blocks.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.Zdj_Blocks)


        self.verticalLayout_7.addWidget(self.Blocks_frame)

        self.AbandonedPark_frame = QFrame(self.WyborMapy_frame)
        self.AbandonedPark_frame.setObjectName(u"AbandonedPark_frame")
        self.AbandonedPark_frame.setFrameShape(QFrame.StyledPanel)
        self.AbandonedPark_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.AbandonedPark_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.Btn_Aband = QRadioButton(self.AbandonedPark_frame)
        self.buttonGroup.addButton(self.Btn_Aband)
        self.Btn_Aband.setObjectName(u"Btn_Aband")
        self.Btn_Aband.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_14.addWidget(self.Btn_Aband)

        self.Title_Aband = QLabel(self.AbandonedPark_frame)
        self.Title_Aband.setObjectName(u"Title_Aband")
        self.Title_Aband.setFont(font2)

        self.horizontalLayout_14.addWidget(self.Title_Aband)

        self.Opis_Aband = QLabel(self.AbandonedPark_frame)
        self.Opis_Aband.setObjectName(u"Opis_Aband")
        self.Opis_Aband.setMaximumSize(QSize(200, 16777215))
        self.Opis_Aband.setTextFormat(Qt.AutoText)
        self.Opis_Aband.setWordWrap(True)
        self.Opis_Aband.setMargin(0)

        self.horizontalLayout_14.addWidget(self.Opis_Aband)

        self.Zdj_Aband = QLabel(self.AbandonedPark_frame)
        self.Zdj_Aband.setObjectName(u"Zdj_Aband")
        self.Zdj_Aband.setMinimumSize(QSize(170, 0))
        self.Zdj_Aband.setMaximumSize(QSize(170, 16777215))
        self.Zdj_Aband.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/rsz_abandonedpark.png"))
        self.Zdj_Aband.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.Zdj_Aband)


        self.verticalLayout_7.addWidget(self.AbandonedPark_frame)

        self.ZhangJiajie_frame = QFrame(self.WyborMapy_frame)
        self.ZhangJiajie_frame.setObjectName(u"ZhangJiajie_frame")
        self.ZhangJiajie_frame.setFrameShape(QFrame.StyledPanel)
        self.ZhangJiajie_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.ZhangJiajie_frame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.btn_ZJ = QRadioButton(self.ZhangJiajie_frame)
        self.buttonGroup.addButton(self.btn_ZJ)
        self.btn_ZJ.setObjectName(u"btn_ZJ")
        self.btn_ZJ.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_15.addWidget(self.btn_ZJ)

        self.Title_ZJ = QLabel(self.ZhangJiajie_frame)
        self.Title_ZJ.setObjectName(u"Title_ZJ")
        self.Title_ZJ.setFont(font2)

        self.horizontalLayout_15.addWidget(self.Title_ZJ)

        self.Opis_ZJ = QLabel(self.ZhangJiajie_frame)
        self.Opis_ZJ.setObjectName(u"Opis_ZJ")
        self.Opis_ZJ.setMaximumSize(QSize(200, 16777215))
        self.Opis_ZJ.setWordWrap(True)

        self.horizontalLayout_15.addWidget(self.Opis_ZJ)

        self.Zdj_ZJ = QLabel(self.ZhangJiajie_frame)
        self.Zdj_ZJ.setObjectName(u"Zdj_ZJ")
        self.Zdj_ZJ.setMinimumSize(QSize(170, 0))
        self.Zdj_ZJ.setMaximumSize(QSize(170, 16777215))
        self.Zdj_ZJ.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/rsz_zhangjiajie.png"))
        self.Zdj_ZJ.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.Zdj_ZJ)


        self.verticalLayout_7.addWidget(self.ZhangJiajie_frame)

        self.MSbuild_frame = QFrame(self.WyborMapy_frame)
        self.MSbuild_frame.setObjectName(u"MSbuild_frame")
        self.MSbuild_frame.setFrameShape(QFrame.StyledPanel)
        self.MSbuild_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.MSbuild_frame)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.btn_MSBuild = QRadioButton(self.MSbuild_frame)
        self.buttonGroup.addButton(self.btn_MSBuild)
        self.btn_MSBuild.setObjectName(u"btn_MSBuild")
        self.btn_MSBuild.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_MSBuild)

        self.Title_MSBuild = QLabel(self.MSbuild_frame)
        self.Title_MSBuild.setObjectName(u"Title_MSBuild")
        self.Title_MSBuild.setFont(font2)

        self.horizontalLayout_19.addWidget(self.Title_MSBuild)

        self.Opis_MSBuild = QLabel(self.MSbuild_frame)
        self.Opis_MSBuild.setObjectName(u"Opis_MSBuild")
        self.Opis_MSBuild.setMaximumSize(QSize(200, 16777215))
        self.Opis_MSBuild.setWordWrap(True)

        self.horizontalLayout_19.addWidget(self.Opis_MSBuild)

        self.Zdj_MSBuild = QLabel(self.MSbuild_frame)
        self.Zdj_MSBuild.setObjectName(u"Zdj_MSBuild")
        self.Zdj_MSBuild.setMinimumSize(QSize(170, 0))
        self.Zdj_MSBuild.setMaximumSize(QSize(170, 16777215))
        self.Zdj_MSBuild.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/rsz_msbuild2018.png"))
        self.Zdj_MSBuild.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.Zdj_MSBuild)


        self.verticalLayout_7.addWidget(self.MSbuild_frame)

        self.Landscape_frame = QFrame(self.WyborMapy_frame)
        self.Landscape_frame.setObjectName(u"Landscape_frame")
        self.Landscape_frame.setFrameShape(QFrame.StyledPanel)
        self.Landscape_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.Landscape_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.Btn_Land = QRadioButton(self.Landscape_frame)
        self.buttonGroup.addButton(self.Btn_Land)
        self.Btn_Land.setObjectName(u"Btn_Land")
        self.Btn_Land.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_17.addWidget(self.Btn_Land)

        self.label = QLabel(self.Landscape_frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)
        self.label.setMargin(0)

        self.horizontalLayout_17.addWidget(self.label)

        self.label_7 = QLabel(self.Landscape_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(200, 16777215))
        self.label_7.setWordWrap(True)

        self.horizontalLayout_17.addWidget(self.label_7)

        self.label_26 = QLabel(self.Landscape_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(170, 0))
        self.label_26.setMaximumSize(QSize(170, 16777215))
        self.label_26.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/rsz_screenshot_from_2023-08-19_13-08-47.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_26.setMargin(-5)

        self.horizontalLayout_17.addWidget(self.label_26)


        self.verticalLayout_7.addWidget(self.Landscape_frame)

        self.AirSimNH_frame = QFrame(self.WyborMapy_frame)
        self.AirSimNH_frame.setObjectName(u"AirSimNH_frame")
        self.AirSimNH_frame.setFrameShape(QFrame.StyledPanel)
        self.AirSimNH_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.AirSimNH_frame)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Btn_AirSimNH = QRadioButton(self.AirSimNH_frame)
        self.buttonGroup.addButton(self.Btn_AirSimNH)
        self.Btn_AirSimNH.setObjectName(u"Btn_AirSimNH")
        self.Btn_AirSimNH.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_16.addWidget(self.Btn_AirSimNH)

        self.Title_AirSimNH = QLabel(self.AirSimNH_frame)
        self.Title_AirSimNH.setObjectName(u"Title_AirSimNH")
        self.Title_AirSimNH.setFont(font2)

        self.horizontalLayout_16.addWidget(self.Title_AirSimNH)

        self.Opis_AirSimNH = QLabel(self.AirSimNH_frame)
        self.Opis_AirSimNH.setObjectName(u"Opis_AirSimNH")
        self.Opis_AirSimNH.setMaximumSize(QSize(200, 16777215))
        self.Opis_AirSimNH.setWordWrap(True)

        self.horizontalLayout_16.addWidget(self.Opis_AirSimNH)

        self.Zdj_AirSimNH = QLabel(self.AirSimNH_frame)
        self.Zdj_AirSimNH.setObjectName(u"Zdj_AirSimNH")
        self.Zdj_AirSimNH.setMinimumSize(QSize(170, 0))
        self.Zdj_AirSimNH.setMaximumSize(QSize(170, 16777215))
        self.Zdj_AirSimNH.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/rsz_airsimnh.png"))
        self.Zdj_AirSimNH.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.Zdj_AirSimNH)


        self.verticalLayout_7.addWidget(self.AirSimNH_frame)

        self.Africa_frame = QFrame(self.WyborMapy_frame)
        self.Africa_frame.setObjectName(u"Africa_frame")
        self.Africa_frame.setFrameShape(QFrame.StyledPanel)
        self.Africa_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.Africa_frame)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.Btn_Africa = QRadioButton(self.Africa_frame)
        self.buttonGroup.addButton(self.Btn_Africa)
        self.Btn_Africa.setObjectName(u"Btn_Africa")
        self.Btn_Africa.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_18.addWidget(self.Btn_Africa)

        self.Title_Africa = QLabel(self.Africa_frame)
        self.Title_Africa.setObjectName(u"Title_Africa")
        self.Title_Africa.setFont(font2)

        self.horizontalLayout_18.addWidget(self.Title_Africa)

        self.Opis_Africa = QLabel(self.Africa_frame)
        self.Opis_Africa.setObjectName(u"Opis_Africa")
        self.Opis_Africa.setMaximumSize(QSize(200, 16777215))
        self.Opis_Africa.setWordWrap(True)

        self.horizontalLayout_18.addWidget(self.Opis_Africa)

        self.Zdj_Africa = QLabel(self.Africa_frame)
        self.Zdj_Africa.setObjectName(u"Zdj_Africa")
        self.Zdj_Africa.setMinimumSize(QSize(170, 0))
        self.Zdj_Africa.setMaximumSize(QSize(170, 16777215))
        self.Zdj_Africa.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/rsz_africa.png"))
        self.Zdj_Africa.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.Zdj_Africa)


        self.verticalLayout_7.addWidget(self.Africa_frame)


        self.verticalLayout_8.addWidget(self.WyborMapy_frame)


        self.horizontalLayout_39.addWidget(self.frame_7)

        self.frame_15 = QFrame(self.Settings_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_15)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_103 = QFrame(self.frame_15)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_103)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_237 = QLabel(self.frame_103)
        self.label_237.setObjectName(u"label_237")
        font4 = QFont()
        font4.setPointSize(13)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_237.setFont(font4)

        self.verticalLayout_59.addWidget(self.label_237, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_104 = QFrame(self.frame_103)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setStyleSheet(u"QFrame{\n"
"	border-top: 1px solid rgb(36, 31, 49);\n"
"	border-right: rgb(255, 255, 255);\n"
"	border-bottom: 1px solid rgb(36, 31, 49);\n"
"	border-left: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"}")
        self.frame_104.setFrameShape(QFrame.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_105 = QHBoxLayout(self.frame_104)
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.frame_105 = QFrame(self.frame_104)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Raised)
        self.verticalLayout_53 = QVBoxLayout(self.frame_105)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_238 = QLabel(self.frame_105)
        self.label_238.setObjectName(u"label_238")
        self.label_238.setFont(font3)

        self.verticalLayout_53.addWidget(self.label_238)

        self.comboBox_4 = QComboBox(self.frame_105)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        font5 = QFont()
        font5.setFamily(u"Microsoft YaHei UI")
        font5.setPointSize(12)
        font5.setBold(True)
        font5.setWeight(75)
        self.comboBox_4.setFont(font5)

        self.verticalLayout_53.addWidget(self.comboBox_4)


        self.horizontalLayout_105.addWidget(self.frame_105)

        self.frame_106 = QFrame(self.frame_104)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setFrameShape(QFrame.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_106)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_239 = QLabel(self.frame_106)
        self.label_239.setObjectName(u"label_239")
        self.label_239.setFont(font3)

        self.verticalLayout_57.addWidget(self.label_239)

        self.comboBox_5 = QComboBox(self.frame_106)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setFont(font5)

        self.verticalLayout_57.addWidget(self.comboBox_5)


        self.horizontalLayout_105.addWidget(self.frame_106)


        self.verticalLayout_59.addWidget(self.frame_104)

        self.label_244 = QLabel(self.frame_103)
        self.label_244.setObjectName(u"label_244")
        self.label_244.setFont(font4)

        self.verticalLayout_59.addWidget(self.label_244, 0, Qt.AlignHCenter)

        self.frame_107 = QFrame(self.frame_103)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setStyleSheet(u"QFrame{\n"
"	border-top: 1px solid rgb(36, 31, 49);\n"
"	border-right: rgb(255, 255, 255);\n"
"	border-bottom: 1px solid rgb(36, 31, 49);\n"
"	border-left: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"}")
        self.frame_107.setFrameShape(QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Raised)
        self.verticalLayout_58 = QVBoxLayout(self.frame_107)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_241 = QLabel(self.frame_107)
        self.label_241.setObjectName(u"label_241")
        self.label_241.setFont(font3)

        self.verticalLayout_58.addWidget(self.label_241, 0, Qt.AlignHCenter)

        self.comboBox_6 = QComboBox(self.frame_107)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setFont(font5)

        self.verticalLayout_58.addWidget(self.comboBox_6, 0, Qt.AlignHCenter)


        self.verticalLayout_59.addWidget(self.frame_107)


        self.verticalLayout_20.addWidget(self.frame_103)

        self.WyborRozd_frame = QFrame(self.frame_15)
        self.WyborRozd_frame.setObjectName(u"WyborRozd_frame")
        self.WyborRozd_frame.setMaximumSize(QSize(16777215, 600))
        self.WyborRozd_frame.setStyleSheet(u"QFrame{\n"
"	border-top: 1px solid rgb(36, 31, 49);\n"
"	border-right: rgb(255, 255, 255);\n"
"	border-bottom: 1px solid rgb(36, 31, 49);\n"
"	border-left: rgb(255, 255, 255);\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"}")
        self.WyborRozd_frame.setFrameShape(QFrame.StyledPanel)
        self.WyborRozd_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.WyborRozd_frame)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_28 = QLabel(self.WyborRozd_frame)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font4)

        self.verticalLayout_14.addWidget(self.label_28, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.x1920_frame = QFrame(self.WyborRozd_frame)
        self.x1920_frame.setObjectName(u"x1920_frame")
        self.x1920_frame.setFrameShape(QFrame.StyledPanel)
        self.x1920_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.x1920_frame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.x1920_btn = QRadioButton(self.x1920_frame)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.x1920_btn)
        self.x1920_btn.setObjectName(u"x1920_btn")
        self.x1920_btn.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_20.addWidget(self.x1920_btn)

        self.label_19 = QLabel(self.x1920_frame)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_20.addWidget(self.label_19)


        self.verticalLayout_14.addWidget(self.x1920_frame)

        self.x1680x1050_frame = QFrame(self.WyborRozd_frame)
        self.x1680x1050_frame.setObjectName(u"x1680x1050_frame")
        self.x1680x1050_frame.setFrameShape(QFrame.StyledPanel)
        self.x1680x1050_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.x1680x1050_frame)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.x1680x1050_btn = QRadioButton(self.x1680x1050_frame)
        self.buttonGroup_2.addButton(self.x1680x1050_btn)
        self.x1680x1050_btn.setObjectName(u"x1680x1050_btn")
        self.x1680x1050_btn.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_33.addWidget(self.x1680x1050_btn)

        self.label_20 = QLabel(self.x1680x1050_frame)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_33.addWidget(self.label_20)


        self.verticalLayout_14.addWidget(self.x1680x1050_frame)

        self.x1200x800_frame = QFrame(self.WyborRozd_frame)
        self.x1200x800_frame.setObjectName(u"x1200x800_frame")
        self.x1200x800_frame.setFrameShape(QFrame.StyledPanel)
        self.x1200x800_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.x1200x800_frame)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.x1200x800_btn = QRadioButton(self.x1200x800_frame)
        self.buttonGroup_2.addButton(self.x1200x800_btn)
        self.x1200x800_btn.setObjectName(u"x1200x800_btn")
        self.x1200x800_btn.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_34.addWidget(self.x1200x800_btn)

        self.label_21 = QLabel(self.x1200x800_frame)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_34.addWidget(self.label_21)


        self.verticalLayout_14.addWidget(self.x1200x800_frame)

        self.x1600x900_frame = QFrame(self.WyborRozd_frame)
        self.x1600x900_frame.setObjectName(u"x1600x900_frame")
        self.x1600x900_frame.setFrameShape(QFrame.StyledPanel)
        self.x1600x900_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.x1600x900_frame)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.x1600x900_btn = QRadioButton(self.x1600x900_frame)
        self.buttonGroup_2.addButton(self.x1600x900_btn)
        self.x1600x900_btn.setObjectName(u"x1600x900_btn")
        self.x1600x900_btn.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_35.addWidget(self.x1600x900_btn)

        self.label_22 = QLabel(self.x1600x900_frame)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_35.addWidget(self.label_22)


        self.verticalLayout_14.addWidget(self.x1600x900_frame)

        self.x1366x768_frame = QFrame(self.WyborRozd_frame)
        self.x1366x768_frame.setObjectName(u"x1366x768_frame")
        self.x1366x768_frame.setFrameShape(QFrame.StyledPanel)
        self.x1366x768_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.x1366x768_frame)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.x1366x768_btn = QRadioButton(self.x1366x768_frame)
        self.buttonGroup_2.addButton(self.x1366x768_btn)
        self.x1366x768_btn.setObjectName(u"x1366x768_btn")
        self.x1366x768_btn.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_36.addWidget(self.x1366x768_btn)

        self.label_23 = QLabel(self.x1366x768_frame)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_36.addWidget(self.label_23)


        self.verticalLayout_14.addWidget(self.x1366x768_frame)

        self.x1440x900_frame = QFrame(self.WyborRozd_frame)
        self.x1440x900_frame.setObjectName(u"x1440x900_frame")
        self.x1440x900_frame.setFrameShape(QFrame.StyledPanel)
        self.x1440x900_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.x1440x900_frame)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.x1440x900_btn = QRadioButton(self.x1440x900_frame)
        self.buttonGroup_2.addButton(self.x1440x900_btn)
        self.x1440x900_btn.setObjectName(u"x1440x900_btn")
        self.x1440x900_btn.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_37.addWidget(self.x1440x900_btn)

        self.label_24 = QLabel(self.x1440x900_frame)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_37.addWidget(self.label_24)


        self.verticalLayout_14.addWidget(self.x1440x900_frame)

        self.x1024x720_frame = QFrame(self.WyborRozd_frame)
        self.x1024x720_frame.setObjectName(u"x1024x720_frame")
        self.x1024x720_frame.setFrameShape(QFrame.StyledPanel)
        self.x1024x720_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_38 = QHBoxLayout(self.x1024x720_frame)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.x1024x720_btn = QRadioButton(self.x1024x720_frame)
        self.buttonGroup_2.addButton(self.x1024x720_btn)
        self.x1024x720_btn.setObjectName(u"x1024x720_btn")
        self.x1024x720_btn.setStyleSheet(u"\n"
"QRadioButton::indicator {\n"
"width: 38px;\n"
"height: 38px;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-50.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"image: url(:/icons/Icons/Magisterka_python(1)/icons8-check-501.png);\n"
"margin-left: 8px;\n"
"margin-top: 5px;\n"
"margin-bottom: 5px;\n"
"}")

        self.horizontalLayout_38.addWidget(self.x1024x720_btn)

        self.label_25 = QLabel(self.x1024x720_frame)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_38.addWidget(self.label_25)


        self.verticalLayout_14.addWidget(self.x1024x720_frame)


        self.verticalLayout_20.addWidget(self.WyborRozd_frame)


        self.horizontalLayout_39.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.Settings_page)
        self.Parameters_page = QWidget()
        self.Parameters_page.setObjectName(u"Parameters_page")
        self.Parameters_page.setStyleSheet(u"background-color:transparent;\n"
"background-repeat: no-repeat;\n"
"color: rgb(255, 255, 255);")
        self.verticalLayout_13 = QVBoxLayout(self.Parameters_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(-1, 1, 8, 1)
        self.frame_14 = QFrame(self.Parameters_page)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(20, 10, 281, 419))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_16)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_31 = QLabel(self.frame_16)
        self.label_31.setObjectName(u"label_31")

        self.gridLayout.addWidget(self.label_31, 4, 2, 1, 1)

        self.Predkosc_X = QLCDNumber(self.frame_16)
        self.Predkosc_X.setObjectName(u"Predkosc_X")
        font6 = QFont()
        font6.setPointSize(12)
        self.Predkosc_X.setFont(font6)
        self.Predkosc_X.setDigitCount(6)

        self.gridLayout.addWidget(self.Predkosc_X, 3, 1, 1, 1)

        self.Pozycja_X = QLCDNumber(self.frame_16)
        self.Pozycja_X.setObjectName(u"Pozycja_X")
        self.Pozycja_X.setFont(font6)
        self.Pozycja_X.setDigitCount(6)
        self.Pozycja_X.setProperty("value", 0.000000000000000)

        self.gridLayout.addWidget(self.Pozycja_X, 0, 1, 1, 1)

        self.Pochylenie = QLCDNumber(self.frame_16)
        self.Pochylenie.setObjectName(u"Pochylenie")
        self.Pochylenie.setFont(font6)
        self.Pochylenie.setDigitCount(6)

        self.gridLayout.addWidget(self.Pochylenie, 8, 1, 1, 1)

        self.Przechylenie = QLCDNumber(self.frame_16)
        self.Przechylenie.setObjectName(u"Przechylenie")
        self.Przechylenie.setFont(font6)
        self.Przechylenie.setDigitCount(6)

        self.gridLayout.addWidget(self.Przechylenie, 7, 1, 1, 1)

        self.label_10 = QLabel(self.frame_16)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 1, 2, 1, 1)

        self.label_3 = QLabel(self.frame_16)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 8, 2, 1, 1)

        self.Predkosc_Y = QLCDNumber(self.frame_16)
        self.Predkosc_Y.setObjectName(u"Predkosc_Y")
        self.Predkosc_Y.setFont(font6)
        self.Predkosc_Y.setDigitCount(6)

        self.gridLayout.addWidget(self.Predkosc_Y, 4, 1, 1, 1)

        self.label_5 = QLabel(self.frame_16)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 9, 2, 1, 1)

        self.label_32 = QLabel(self.frame_16)
        self.label_32.setObjectName(u"label_32")

        self.gridLayout.addWidget(self.label_32, 5, 2, 1, 1)

        self.label_68 = QLabel(self.frame_16)
        self.label_68.setObjectName(u"label_68")

        self.gridLayout.addWidget(self.label_68, 12, 2, 1, 1)

        self.Wysokosc = QLCDNumber(self.frame_16)
        self.Wysokosc.setObjectName(u"Wysokosc")
        self.Wysokosc.setFont(font6)
        self.Wysokosc.setDigitCount(6)

        self.gridLayout.addWidget(self.Wysokosc, 2, 1, 1, 1)

        self.Emotion = QLCDNumber(self.frame_16)
        self.Emotion.setObjectName(u"Emotion")
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setPointSize(12)
        self.Emotion.setFont(font7)
        self.Emotion.setDigitCount(6)

        self.gridLayout.addWidget(self.Emotion, 11, 1, 1, 1)

        self.label_30 = QLabel(self.frame_16)
        self.label_30.setObjectName(u"label_30")

        self.gridLayout.addWidget(self.label_30, 3, 2, 1, 1)

        self.Predkosc_Z = QLCDNumber(self.frame_16)
        self.Predkosc_Z.setObjectName(u"Predkosc_Z")
        self.Predkosc_Z.setFont(font6)
        self.Predkosc_Z.setDigitCount(6)

        self.gridLayout.addWidget(self.Predkosc_Z, 5, 1, 1, 1)

        self.Czas = QLCDNumber(self.frame_16)
        self.Czas.setObjectName(u"Czas")
        self.Czas.setFont(font6)
        self.Czas.setDigitCount(6)

        self.gridLayout.addWidget(self.Czas, 10, 1, 1, 1)

        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 10, 2, 1, 1)

        self.pozycja_Y = QLCDNumber(self.frame_16)
        self.pozycja_Y.setObjectName(u"pozycja_Y")
        self.pozycja_Y.setFont(font6)
        self.pozycja_Y.setDigitCount(6)

        self.gridLayout.addWidget(self.pozycja_Y, 1, 1, 1, 1)

        self.label_9 = QLabel(self.frame_16)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 0, 2, 1, 1)

        self.Heart_rate = QLCDNumber(self.frame_16)
        self.Heart_rate.setObjectName(u"Heart_rate")
        self.Heart_rate.setFont(font6)
        self.Heart_rate.setDigitCount(6)

        self.gridLayout.addWidget(self.Heart_rate, 12, 1, 1, 1)

        self.Predkosc = QLCDNumber(self.frame_16)
        self.Predkosc.setObjectName(u"Predkosc")
        self.Predkosc.setFont(font6)
        self.Predkosc.setDigitCount(6)

        self.gridLayout.addWidget(self.Predkosc, 6, 1, 1, 1)

        self.label_39 = QLabel(self.frame_16)
        self.label_39.setObjectName(u"label_39")

        self.gridLayout.addWidget(self.label_39, 7, 2, 1, 1)

        self.label_29 = QLabel(self.frame_16)
        self.label_29.setObjectName(u"label_29")

        self.gridLayout.addWidget(self.label_29, 2, 2, 1, 1)

        self.label_33 = QLabel(self.frame_16)
        self.label_33.setObjectName(u"label_33")

        self.gridLayout.addWidget(self.label_33, 6, 2, 1, 1)

        self.Odchylenie = QLCDNumber(self.frame_16)
        self.Odchylenie.setObjectName(u"Odchylenie")
        self.Odchylenie.setFont(font6)
        self.Odchylenie.setDigitCount(6)

        self.gridLayout.addWidget(self.Odchylenie, 9, 1, 1, 1)

        self.label_34 = QLabel(self.frame_16)
        self.label_34.setObjectName(u"label_34")
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_34.setFont(font8)

        self.gridLayout.addWidget(self.label_34, 0, 0, 1, 1)

        self.label_35 = QLabel(self.frame_16)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font8)

        self.gridLayout.addWidget(self.label_35, 1, 0, 1, 1)

        self.label_36 = QLabel(self.frame_16)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font8)

        self.gridLayout.addWidget(self.label_36, 2, 0, 1, 1)

        self.label_37 = QLabel(self.frame_16)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font8)

        self.gridLayout.addWidget(self.label_37, 3, 0, 1, 1)

        self.label_38 = QLabel(self.frame_16)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font8)

        self.gridLayout.addWidget(self.label_38, 4, 0, 1, 1)

        self.label_40 = QLabel(self.frame_16)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font8)

        self.gridLayout.addWidget(self.label_40, 5, 0, 1, 1)

        self.label_41 = QLabel(self.frame_16)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font8)

        self.gridLayout.addWidget(self.label_41, 6, 0, 1, 1)

        self.label_42 = QLabel(self.frame_16)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setFont(font8)

        self.gridLayout.addWidget(self.label_42, 7, 0, 1, 1)

        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font8)

        self.gridLayout.addWidget(self.label_2, 8, 0, 1, 1)

        self.label_4 = QLabel(self.frame_16)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font8)

        self.gridLayout.addWidget(self.label_4, 9, 0, 1, 1)

        self.label_6 = QLabel(self.frame_16)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font8)

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.label_69 = QLabel(self.frame_16)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font8)

        self.gridLayout.addWidget(self.label_69, 12, 0, 1, 1)

        self.label_67 = QLabel(self.frame_16)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font8)

        self.gridLayout.addWidget(self.label_67, 11, 0, 1, 1)

        self.stackedWidget_mapy = QStackedWidget(self.frame_14)
        self.stackedWidget_mapy.setObjectName(u"stackedWidget_mapy")
        self.stackedWidget_mapy.setGeometry(QRect(320, 10, 526, 400))
        self.stackedWidget_mapy.setMinimumSize(QSize(526, 400))
        self.AirSimNH_mapa = QWidget()
        self.AirSimNH_mapa.setObjectName(u"AirSimNH_mapa")
        self.AirSimNH_mapa.setMinimumSize(QSize(526, 400))
        self.AirSimNH_mapa.setStyleSheet(u"")
        self.AirSimNH_GV = QGraphicsView(self.AirSimNH_mapa)
        self.AirSimNH_GV.setObjectName(u"AirSimNH_GV")
        self.AirSimNH_GV.setGeometry(QRect(0, 0, 526, 400))
        self.AirSimNH_GV.setMinimumSize(QSize(526, 400))
        self.stackedWidget_mapy.addWidget(self.AirSimNH_mapa)
        self.Aband_mapa = QWidget()
        self.Aband_mapa.setObjectName(u"Aband_mapa")
        self.Aband_mapa.setStyleSheet(u"border-image: url(:/Zdjecia/Zdjecia/AbandonedPark.png);")
        self.stackedWidget_mapy.addWidget(self.Aband_mapa)
        self.Africa_Mapa = QWidget()
        self.Africa_Mapa.setObjectName(u"Africa_Mapa")
        self.Africa_Mapa.setStyleSheet(u"border-image: url(:/Zdjecia/Zdjecia/Africa.png);")
        self.stackedWidget_mapy.addWidget(self.Africa_Mapa)
        self.Blocks_mapa = QWidget()
        self.Blocks_mapa.setObjectName(u"Blocks_mapa")
        self.Blocks_mapa.setStyleSheet(u"border-image: url(:/Zdjecia/Zdjecia/Blocks.png);")
        self.stackedWidget_mapy.addWidget(self.Blocks_mapa)
        self.Lands_mapa = QWidget()
        self.Lands_mapa.setObjectName(u"Lands_mapa")
        self.Lands_mapa.setStyleSheet(u"border-image: url(:/Zdjecia/Zdjecia/Landscape.png);")
        self.stackedWidget_mapy.addWidget(self.Lands_mapa)
        self.ZJ_mapa = QWidget()
        self.ZJ_mapa.setObjectName(u"ZJ_mapa")
        self.ZJ_mapa.setStyleSheet(u"border-image: url(:/Zdjecia/Zdjecia/ZJ.png);")
        self.stackedWidget_mapy.addWidget(self.ZJ_mapa)
        self.MSBuild_mapa = QWidget()
        self.MSBuild_mapa.setObjectName(u"MSBuild_mapa")
        self.MSBuild_mapa.setStyleSheet(u"border-image: url(:/Zdjecia/Zdjecia/MSBuild.png);")
        self.stackedWidget_mapy.addWidget(self.MSBuild_mapa)
        self.WynikMisji_frame = QFrame(self.frame_14)
        self.WynikMisji_frame.setObjectName(u"WynikMisji_frame")
        self.WynikMisji_frame.setGeometry(QRect(240, 890, 441, 82))
        self.WynikMisji_frame.setFrameShape(QFrame.StyledPanel)
        self.WynikMisji_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_40 = QHBoxLayout(self.WynikMisji_frame)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.WynikMisji_obraz = QLabel(self.WynikMisji_frame)
        self.WynikMisji_obraz.setObjectName(u"WynikMisji_obraz")
        self.WynikMisji_obraz.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-congratulation-64.png"))
        self.WynikMisji_obraz.setScaledContents(True)

        self.horizontalLayout_40.addWidget(self.WynikMisji_obraz)

        self.WynikMisji_podpis = QLabel(self.WynikMisji_frame)
        self.WynikMisji_podpis.setObjectName(u"WynikMisji_podpis")
        font9 = QFont()
        font9.setPointSize(13)
        self.WynikMisji_podpis.setFont(font9)
        self.WynikMisji_podpis.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.WynikMisji_podpis.setWordWrap(False)

        self.horizontalLayout_40.addWidget(self.WynikMisji_podpis)

        self.frame_35 = QFrame(self.frame_14)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(860, 10, 276, 861))
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_35)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frame_13 = QFrame(self.frame_35)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_13)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")
        font10 = QFont()
        font10.setFamily(u"Segoe UI Variable Display Semib")
        font10.setPointSize(12)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_18.setFont(font10)

        self.verticalLayout_19.addWidget(self.label_18, 0, Qt.AlignHCenter)

        self.widget_3 = AnalogGaugeWidget(self.frame_13)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(240, 240))
        self.widget_3.setStyleSheet(u"background-color: rgb(0, 0, 255);")

        self.verticalLayout_19.addWidget(self.widget_3)


        self.verticalLayout_21.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.frame_35)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_13 = QLabel(self.frame_12)
        self.label_13.setObjectName(u"label_13")
        font11 = QFont()
        font11.setFamily(u"Segoe UI Variable Text Semibold")
        font11.setPointSize(12)
        font11.setBold(True)
        font11.setWeight(75)
        self.label_13.setFont(font11)

        self.verticalLayout_17.addWidget(self.label_13, 0, Qt.AlignHCenter)

        self.widget_2 = AnalogGaugeWidget(self.frame_12)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(240, 240))
        self.widget_2.setStyleSheet(u"background-color: rgb(0, 0, 255);")

        self.verticalLayout_17.addWidget(self.widget_2)


        self.verticalLayout_21.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_35)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_11)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        font12 = QFont()
        font12.setFamily(u"Segoe UI Variable Display Semib")
        font12.setPointSize(12)
        self.label_12.setFont(font12)

        self.verticalLayout_18.addWidget(self.label_12, 0, Qt.AlignHCenter)

        self.widget = AnalogGaugeWidget(self.frame_11)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(240, 240))
        self.widget.setStyleSheet(u"background-color: rgb(0, 0, 255);")

        self.verticalLayout_18.addWidget(self.widget)


        self.verticalLayout_21.addWidget(self.frame_11)

        self.label_66 = QLabel(self.frame_14)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setGeometry(QRect(30, 430, 801, 91))
        font13 = QFont()
        font13.setFamily(u"OCR A Extended")
        font13.setPointSize(15)
        self.label_66.setFont(font13)
        self.label_66.setAlignment(Qt.AlignCenter)
        self.label_66.setWordWrap(True)
        self.frame_40 = QFrame(self.frame_14)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setGeometry(QRect(40, 520, 801, 401))
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.Misje_male = QTableWidget(self.frame_40)
        if (self.Misje_male.columnCount() < 4):
            self.Misje_male.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.Misje_male.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.Misje_male.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.Misje_male.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.Misje_male.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.Misje_male.rowCount() < 10):
            self.Misje_male.setRowCount(10)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.Misje_male.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.Misje_male.setItem(0, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.Misje_male.setItem(0, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.Misje_male.setItem(0, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.Misje_male.setItem(0, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.Misje_male.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.Misje_male.setItem(1, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.Misje_male.setItem(1, 2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.Misje_male.setItem(1, 3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.Misje_male.setItem(2, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.Misje_male.setItem(2, 1, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.Misje_male.setItem(2, 2, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.Misje_male.setItem(2, 3, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.Misje_male.setItem(3, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.Misje_male.setItem(3, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.Misje_male.setItem(3, 2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.Misje_male.setItem(3, 3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.Misje_male.setItem(4, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.Misje_male.setItem(4, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.Misje_male.setItem(4, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.Misje_male.setItem(4, 3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.Misje_male.setItem(5, 0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.Misje_male.setItem(5, 1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.Misje_male.setItem(5, 2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.Misje_male.setItem(5, 3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.Misje_male.setItem(6, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.Misje_male.setItem(6, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.Misje_male.setItem(6, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.Misje_male.setItem(6, 3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.Misje_male.setItem(7, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.Misje_male.setItem(7, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.Misje_male.setItem(7, 2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.Misje_male.setItem(7, 3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.Misje_male.setItem(8, 0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.Misje_male.setItem(8, 1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.Misje_male.setItem(8, 2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.Misje_male.setItem(8, 3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.Misje_male.setItem(9, 0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.Misje_male.setItem(9, 1, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.Misje_male.setItem(9, 2, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.Misje_male.setItem(9, 3, __qtablewidgetitem53)
        self.Misje_male.setObjectName(u"Misje_male")
        self.Misje_male.setGeometry(QRect(9, 9, 791, 321))
        self.Misje_male.setStyleSheet(u"QHeaderView::section\n"
"{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QTableCornerButton::section\n"
"{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.frame_41 = QFrame(self.frame_40)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setGeometry(QRect(10, 340, 791, 50))
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.Misje_Button = QPushButton(self.frame_41)
        self.Misje_Button.setObjectName(u"Misje_Button")
        self.Misje_Button.setMaximumSize(QSize(200, 200))
        font14 = QFont()
        font14.setFamily(u"Impact")
        font14.setPointSize(12)
        self.Misje_Button.setFont(font14)
        self.Misje_Button.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(30, 32, 34);\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"border-radius:20px;\n"
"border: 3px;\n"
"}\n"
"")
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-get-set-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Misje_Button.setIcon(icon15)
        self.Misje_Button.setIconSize(QSize(32, 32))
        self.Misje_Button.setFlat(True)

        self.horizontalLayout_45.addWidget(self.Misje_Button)

        self.Wykresy = QPushButton(self.frame_41)
        self.Wykresy.setObjectName(u"Wykresy")
        self.Wykresy.setMaximumSize(QSize(200, 200))
        self.Wykresy.setFont(font14)
        self.Wykresy.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(30, 32, 34);\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"border-radius:20px;\n"
"border: 3px;\n"
"}\n"
"")
        self.Wykresy.setIcon(icon6)
        self.Wykresy.setIconSize(QSize(32, 32))
        self.Wykresy.setFlat(True)

        self.horizontalLayout_45.addWidget(self.Wykresy)

        self.VR_wspolne = QPushButton(self.frame_41)
        self.VR_wspolne.setObjectName(u"VR_wspolne")
        self.VR_wspolne.setMaximumSize(QSize(200, 200))
        self.VR_wspolne.setFont(font14)
        self.VR_wspolne.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(30, 32, 34);\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"border-radius:20px;\n"
"border: 3px;\n"
"}\n"
"")
        icon16 = QIcon()
        icon16.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-vr-glasses-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_wspolne.setIcon(icon16)
        self.VR_wspolne.setIconSize(QSize(32, 32))
        self.VR_wspolne.setFlat(True)

        self.horizontalLayout_45.addWidget(self.VR_wspolne)

        self.Save = QPushButton(self.frame_41)
        self.Save.setObjectName(u"Save")
        self.Save.setMaximumSize(QSize(200, 16777215))
        self.Save.setFont(font14)
        self.Save.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(30, 32, 34);\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"border-radius:20px;\n"
"border: 3px;\n"
"}\n"
"")
        icon17 = QIcon()
        icon17.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-save-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save.setIcon(icon17)
        self.Save.setIconSize(QSize(32, 32))

        self.horizontalLayout_45.addWidget(self.Save)

        self.label_70 = QLabel(self.frame_40)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(0, 10, 801, 331))
        self.label_70.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Operator_dron.png"))
        self.line = QFrame(self.frame_14)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(1140, 0, 1, 1021))
        self.line.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.frame_42 = QFrame(self.frame_14)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setGeometry(QRect(1140, 0, 362, 390))
        font15 = QFont()
        font15.setPointSize(14)
        self.frame_42.setFont(font15)
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.frame_42)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.frame_43 = QFrame(self.frame_42)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_117 = QLabel(self.frame_43)
        self.label_117.setObjectName(u"label_117")
        font16 = QFont()
        font16.setPointSize(20)
        font16.setBold(True)
        font16.setItalic(False)
        font16.setUnderline(False)
        font16.setWeight(75)
        font16.setStrikeOut(False)
        font16.setKerning(False)
        self.label_117.setFont(font16)

        self.horizontalLayout_46.addWidget(self.label_117)

        self.pushButton_12 = QPushButton(self.frame_43)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(64, 64))
        self.pushButton_12.setMaximumSize(QSize(64, 64))
        self.pushButton_12.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	border-image: url(:/icons/Icons/Magisterka_python(1)/icons8-controller-50.png);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	border-image: url(:/icons/Icons/Magisterka_python(1)/icons8-controller-50(1).png);\n"
"}")
        self.pushButton_12.setIconSize(QSize(61, 64))
        self.pushButton_12.setAutoRepeat(False)

        self.horizontalLayout_46.addWidget(self.pushButton_12)


        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.frame_43)

        self.label_118 = QLabel(self.frame_42)
        self.label_118.setObjectName(u"label_118")
        self.label_118.setFont(font15)

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_118)

        self.label_119 = QLabel(self.frame_42)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font15)
        self.label_119.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.label_119)

        self.label_120 = QLabel(self.frame_42)
        self.label_120.setObjectName(u"label_120")
        self.label_120.setFont(font15)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_120)

        self.label_121 = QLabel(self.frame_42)
        self.label_121.setObjectName(u"label_121")
        self.label_121.setFont(font15)
        self.label_121.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_121)

        self.label_122 = QLabel(self.frame_42)
        self.label_122.setObjectName(u"label_122")
        self.label_122.setFont(font15)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_122)

        self.label_123 = QLabel(self.frame_42)
        self.label_123.setObjectName(u"label_123")
        self.label_123.setFont(font15)
        self.label_123.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_123)

        self.label_124 = QLabel(self.frame_42)
        self.label_124.setObjectName(u"label_124")
        self.label_124.setFont(font15)

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_124)

        self.label_125 = QLabel(self.frame_42)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setFont(font15)
        self.label_125.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.label_125)

        self.label_126 = QLabel(self.frame_42)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setFont(font15)

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_126)

        self.label_127 = QLabel(self.frame_42)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setFont(font15)
        self.label_127.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.label_127)

        self.label_128 = QLabel(self.frame_42)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setFont(font15)

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_128)

        self.label_129 = QLabel(self.frame_42)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setFont(font15)
        self.label_129.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.label_129)

        self.label_130 = QLabel(self.frame_42)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setFont(font15)

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_130)

        self.label_131 = QLabel(self.frame_42)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setFont(font15)
        self.label_131.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.label_131)

        self.label_132 = QLabel(self.frame_42)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setFont(font15)

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_132)

        self.label_133 = QLabel(self.frame_42)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setFont(font15)
        self.label_133.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.label_133)

        self.label_134 = QLabel(self.frame_42)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setFont(font15)

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_134)

        self.label_135 = QLabel(self.frame_42)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setFont(font15)
        self.label_135.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.label_135)

        self.label_136 = QLabel(self.frame_42)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setFont(font15)

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_136)

        self.label_137 = QLabel(self.frame_42)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setFont(font15)
        self.label_137.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.label_137)

        self.label_71 = QLabel(self.frame_14)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(1150, 410, 341, 331))
        self.label_71.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Sterowanie.png"))
        self.label_71.setScaledContents(True)
        self.line_2 = QFrame(self.frame_14)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(1140, 390, 351, 1))
        self.line_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)
        self.line_3 = QFrame(self.frame_14)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setGeometry(QRect(1140, 760, 351, 1))
        self.line_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)
        self.frame_44 = QFrame(self.frame_14)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setGeometry(QRect(1140, 760, 351, 171))
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.frame_45 = QFrame(self.frame_44)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_45)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_138 = QLabel(self.frame_45)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setFont(font14)

        self.verticalLayout_22.addWidget(self.label_138, 0, Qt.AlignHCenter)

        self.label_142 = QLabel(self.frame_45)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-angry-50.png"))

        self.verticalLayout_22.addWidget(self.label_142, 0, Qt.AlignHCenter)

        self.label_140 = QLabel(self.frame_45)
        self.label_140.setObjectName(u"label_140")

        self.verticalLayout_22.addWidget(self.label_140, 0, Qt.AlignHCenter)

        self.emocje_LED = QLabel(self.frame_45)
        self.emocje_LED.setObjectName(u"emocje_LED")
        self.emocje_LED.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-red-circle-48.png"))
        self.emocje_LED.setScaledContents(True)

        self.verticalLayout_22.addWidget(self.emocje_LED, 0, Qt.AlignHCenter)


        self.horizontalLayout_47.addWidget(self.frame_45)

        self.line_4 = QFrame(self.frame_44)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_47.addWidget(self.line_4)

        self.frame_46 = QFrame(self.frame_44)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.frame_46.setLineWidth(1)
        self.verticalLayout_23 = QVBoxLayout(self.frame_46)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_139 = QLabel(self.frame_46)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setFont(font14)

        self.verticalLayout_23.addWidget(self.label_139, 0, Qt.AlignHCenter)

        self.label_143 = QLabel(self.frame_46)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-heart-rate-50.png"))

        self.verticalLayout_23.addWidget(self.label_143, 0, Qt.AlignHCenter)

        self.label_141 = QLabel(self.frame_46)
        self.label_141.setObjectName(u"label_141")
        font17 = QFont()
        font17.setFamily(u"MS Gothic")
        font17.setPointSize(12)
        font17.setBold(True)
        font17.setWeight(75)
        self.label_141.setFont(font17)

        self.verticalLayout_23.addWidget(self.label_141, 0, Qt.AlignHCenter)

        self.tetno_LED = QLabel(self.frame_46)
        self.tetno_LED.setObjectName(u"tetno_LED")
        self.tetno_LED.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-red-circle-48.png"))
        self.tetno_LED.setScaledContents(True)

        self.verticalLayout_23.addWidget(self.tetno_LED, 0, Qt.AlignHCenter)


        self.horizontalLayout_47.addWidget(self.frame_46)

        self.line_5 = QFrame(self.frame_14)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(1160, 930, 118, 3))
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_13.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.Parameters_page)
        self.VR_page = QWidget()
        self.VR_page.setObjectName(u"VR_page")
        self.VR_page.setStyleSheet(u"color:rgb(255,255,255);\n"
"background-color:transparent;")
        self.frame_34 = QFrame(self.VR_page)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setGeometry(QRect(9, 9, 240, 590))
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_34)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_33 = QFrame(self.frame_34)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_33)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.VR_landscape = QPushButton(self.frame_33)
        self.VR_landscape.setObjectName(u"VR_landscape")
        self.VR_landscape.setMinimumSize(QSize(64, 64))
        self.VR_landscape.setMaximumSize(QSize(128, 128))
        self.VR_landscape.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Zdjecia/Zdjecia/rsz_landscapemountains.png);\n"
"border-radius:10px;\n"
"\n"
"\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	image: url(:/icons/Icons/Magisterka_python(1)/icons8-vr-glasses-64.png);\n"
"\n"
"}\n"
"\n"
"")
        self.VR_landscape.setIconSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.VR_landscape, 1, 1, 1, 1)

        self.VR_abandoned = QPushButton(self.frame_33)
        self.VR_abandoned.setObjectName(u"VR_abandoned")
        self.VR_abandoned.setMinimumSize(QSize(64, 64))
        self.VR_abandoned.setMaximumSize(QSize(128, 128))
        self.VR_abandoned.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius:10px;\n"
"	border-image: url(:/Zdjecia/Zdjecia/rsz_africa.png);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	image: url(:/icons/Icons/Magisterka_python(1)/icons8-vr-glasses-64.png);\n"
"}")
        self.VR_abandoned.setIconSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.VR_abandoned, 2, 2, 1, 1)

        self.VR_africa = QPushButton(self.frame_33)
        self.VR_africa.setObjectName(u"VR_africa")
        self.VR_africa.setMinimumSize(QSize(64, 64))
        self.VR_africa.setMaximumSize(QSize(128, 128))
        self.VR_africa.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius:10px;\n"
"	border-image: url(:/Zdjecia/Zdjecia/rsz_abandonedpark.png);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	image: url(:/icons/Icons/Magisterka_python(1)/icons8-vr-glasses-64.png);\n"
"}")
        self.VR_africa.setIconSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.VR_africa, 2, 1, 1, 1)

        self.VR_MSBuild = QPushButton(self.frame_33)
        self.VR_MSBuild.setObjectName(u"VR_MSBuild")
        self.VR_MSBuild.setMinimumSize(QSize(64, 64))
        self.VR_MSBuild.setMaximumSize(QSize(128, 128))
        self.VR_MSBuild.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius:10px;\n"
"	border-image: url(:/Zdjecia/Zdjecia/rsz_msbuild2018.png);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	image: url(:/icons/Icons/Magisterka_python(1)/icons8-vr-glasses-64.png);\n"
"}")
        self.VR_MSBuild.setIconSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.VR_MSBuild, 2, 0, 1, 1)

        self.VR_AirSimNH = QPushButton(self.frame_33)
        self.VR_AirSimNH.setObjectName(u"VR_AirSimNH")
        self.VR_AirSimNH.setMinimumSize(QSize(64, 64))
        self.VR_AirSimNH.setMaximumSize(QSize(128, 128))
        self.VR_AirSimNH.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius:10px;\n"
"	border-image: url(:/Zdjecia/Zdjecia/rsz_airsimnh.png);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	image: url(:/icons/Icons/Magisterka_python(1)/icons8-vr-glasses-64.png);\n"
"}")
        self.VR_AirSimNH.setIconSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.VR_AirSimNH, 1, 2, 1, 1)

        self.VR_blocks = QPushButton(self.frame_33)
        self.VR_blocks.setObjectName(u"VR_blocks")
        self.VR_blocks.setMinimumSize(QSize(64, 64))
        self.VR_blocks.setMaximumSize(QSize(128, 128))
        self.VR_blocks.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-radius:10px;\n"
"	border-image: url(:/Zdjecia/Zdjecia/rsz_blocks.png);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	image: url(:/icons/Icons/Magisterka_python(1)/icons8-vr-glasses-64.png);\n"
"}")
        self.VR_blocks.setIconSize(QSize(64, 64))

        self.gridLayout_2.addWidget(self.VR_blocks, 1, 0, 1, 1)

        self.label_64 = QLabel(self.frame_33)
        self.label_64.setObjectName(u"label_64")
        font18 = QFont()
        font18.setFamily(u"Segoe UI Black")
        font18.setPointSize(14)
        font18.setBold(True)
        font18.setWeight(75)
        self.label_64.setFont(font18)
        self.label_64.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_64, 0, 0, 1, 3)


        self.verticalLayout_3.addWidget(self.frame_33)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_10)

        self.label_65 = QLabel(self.frame_34)
        self.label_65.setObjectName(u"label_65")
        font19 = QFont()
        font19.setPointSize(12)
        font19.setBold(True)
        font19.setItalic(False)
        font19.setWeight(75)
        self.label_65.setFont(font19)
        self.label_65.setScaledContents(True)
        self.label_65.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_65)

        self.Actualmap = QLineEdit(self.frame_34)
        self.Actualmap.setObjectName(u"Actualmap")
        font20 = QFont()
        font20.setFamily(u"Lucida Console")
        font20.setPointSize(14)
        self.Actualmap.setFont(font20)
        self.Actualmap.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.Actualmap)

        self.frame_36 = QFrame(self.frame_34)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_36)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")

        self.verticalLayout_3.addWidget(self.frame_36)

        self.Wykresy_2 = QPushButton(self.frame_34)
        self.Wykresy_2.setObjectName(u"Wykresy_2")
        self.Wykresy_2.setMaximumSize(QSize(200, 200))
        self.Wykresy_2.setFont(font14)
        self.Wykresy_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(30, 32, 34);\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"border-radius:20px;\n"
"border: 3px;\n"
"}\n"
"")
        self.Wykresy_2.setIcon(icon6)
        self.Wykresy_2.setIconSize(QSize(32, 32))
        self.Wykresy_2.setFlat(True)

        self.verticalLayout_3.addWidget(self.Wykresy_2, 0, Qt.AlignHCenter)

        self.Save_2 = QPushButton(self.frame_34)
        self.Save_2.setObjectName(u"Save_2")
        self.Save_2.setMinimumSize(QSize(180, 50))
        self.Save_2.setMaximumSize(QSize(200, 16777215))
        self.Save_2.setFont(font14)
        self.Save_2.setStyleSheet(u"QPushButton:hover{\n"
"	background-color: rgb(30, 32, 34);\n"
"}\n"
"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"border-radius:20px;\n"
"border: 3px;\n"
"}\n"
"")
        self.Save_2.setIconSize(QSize(32, 32))

        self.verticalLayout_3.addWidget(self.Save_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_9 = QSpacerItem(20, 101, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer_9)

        self.VR_start = QPushButton(self.frame_34)
        self.VR_start.setObjectName(u"VR_start")
        self.VR_start.setStyleSheet(u"QPushButton\n"
"{\n"
"	background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"background-color:rgb(50, 48, 52);\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-vr-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_start.setIcon(icon18)
        self.VR_start.setIconSize(QSize(64, 64))

        self.verticalLayout_3.addWidget(self.VR_start)

        self.frame_37 = QFrame(self.VR_page)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setGeometry(QRect(320, 40, 362, 390))
        self.frame_37.setFont(font15)
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_37)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_44 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_86 = QLabel(self.frame_38)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font16)

        self.horizontalLayout_44.addWidget(self.label_86)

        self.pushButton_11 = QPushButton(self.frame_38)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setMinimumSize(QSize(64, 64))
        self.pushButton_11.setMaximumSize(QSize(64, 64))
        self.pushButton_11.setStyleSheet(u"QPushButton\n"
"{\n"
"	\n"
"	border-image: url(:/icons/Icons/Magisterka_python(1)/icons8-controller-50.png);\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton::hover\n"
"{\n"
"	border-image: url(:/icons/Icons/Magisterka_python(1)/icons8-controller-50(1).png);\n"
"}")
        self.pushButton_11.setIconSize(QSize(61, 64))
        self.pushButton_11.setAutoRepeat(False)

        self.horizontalLayout_44.addWidget(self.pushButton_11)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.frame_38)

        self.label_72 = QLabel(self.frame_37)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font15)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_72)

        self.label_73 = QLabel(self.frame_37)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font15)
        self.label_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_73)

        self.label_74 = QLabel(self.frame_37)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font15)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_74)

        self.label_75 = QLabel(self.frame_37)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font15)
        self.label_75.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.label_75)

        self.label_76 = QLabel(self.frame_37)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font15)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_76)

        self.label_77 = QLabel(self.frame_37)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font15)
        self.label_77.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.label_77)

        self.label_78 = QLabel(self.frame_37)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font15)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_78)

        self.label_79 = QLabel(self.frame_37)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font15)
        self.label_79.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.label_79)

        self.label_80 = QLabel(self.frame_37)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font15)

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_80)

        self.label_81 = QLabel(self.frame_37)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font15)
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.label_81)

        self.label_82 = QLabel(self.frame_37)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font15)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_82)

        self.label_83 = QLabel(self.frame_37)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font15)
        self.label_83.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.label_83)

        self.label_84 = QLabel(self.frame_37)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font15)

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_84)

        self.label_85 = QLabel(self.frame_37)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font15)
        self.label_85.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.label_85)

        self.label_87 = QLabel(self.frame_37)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font15)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_87)

        self.label_89 = QLabel(self.frame_37)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font15)
        self.label_89.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.label_89)

        self.label_88 = QLabel(self.frame_37)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font15)

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_88)

        self.label_90 = QLabel(self.frame_37)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font15)
        self.label_90.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.label_90)

        self.label_91 = QLabel(self.frame_37)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font15)

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_91)

        self.label_92 = QLabel(self.frame_37)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font15)
        self.label_92.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.label_92)

        self.frame_39 = QFrame(self.VR_page)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setGeometry(QRect(320, 430, 391, 431))
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_39)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_113 = QLabel(self.frame_39)
        self.label_113.setObjectName(u"label_113")
        font21 = QFont()
        font21.setPointSize(11)
        font21.setBold(True)
        font21.setWeight(75)
        self.label_113.setFont(font21)

        self.gridLayout_3.addWidget(self.label_113, 10, 2, 1, 1)

        self.label_102 = QLabel(self.frame_39)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font21)

        self.gridLayout_3.addWidget(self.label_102, 0, 2, 1, 1)

        self.label_110 = QLabel(self.frame_39)
        self.label_110.setObjectName(u"label_110")

        self.gridLayout_3.addWidget(self.label_110, 4, 4, 1, 1)

        self.label_104 = QLabel(self.frame_39)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setFont(font21)

        self.gridLayout_3.addWidget(self.label_104, 9, 2, 1, 1)

        self.pozycja_Y_2 = QLCDNumber(self.frame_39)
        self.pozycja_Y_2.setObjectName(u"pozycja_Y_2")
        self.pozycja_Y_2.setFont(font6)
        self.pozycja_Y_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.pozycja_Y_2, 1, 3, 1, 1)

        self.label_96 = QLabel(self.frame_39)
        self.label_96.setObjectName(u"label_96")

        self.gridLayout_3.addWidget(self.label_96, 5, 4, 1, 1)

        self.Predkosc_2 = QLCDNumber(self.frame_39)
        self.Predkosc_2.setObjectName(u"Predkosc_2")
        self.Predkosc_2.setFont(font6)
        self.Predkosc_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Predkosc_2, 6, 3, 1, 1)

        self.Przechylenie_2 = QLCDNumber(self.frame_39)
        self.Przechylenie_2.setObjectName(u"Przechylenie_2")
        self.Przechylenie_2.setFont(font6)
        self.Przechylenie_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Przechylenie_2, 7, 3, 1, 1)

        self.label_103 = QLabel(self.frame_39)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font21)

        self.gridLayout_3.addWidget(self.label_103, 8, 2, 1, 1)

        self.Wysokosc_2 = QLCDNumber(self.frame_39)
        self.Wysokosc_2.setObjectName(u"Wysokosc_2")
        self.Wysokosc_2.setFont(font6)
        self.Wysokosc_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Wysokosc_2, 2, 3, 1, 1)

        self.label_109 = QLabel(self.frame_39)
        self.label_109.setObjectName(u"label_109")

        self.gridLayout_3.addWidget(self.label_109, 7, 4, 1, 1)

        self.Odchylenie_2 = QLCDNumber(self.frame_39)
        self.Odchylenie_2.setObjectName(u"Odchylenie_2")
        self.Odchylenie_2.setFont(font6)
        self.Odchylenie_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Odchylenie_2, 9, 3, 1, 1)

        self.label_107 = QLabel(self.frame_39)
        self.label_107.setObjectName(u"label_107")

        self.gridLayout_3.addWidget(self.label_107, 2, 4, 1, 1)

        self.label_111 = QLabel(self.frame_39)
        self.label_111.setObjectName(u"label_111")

        self.gridLayout_3.addWidget(self.label_111, 0, 4, 1, 1)

        self.Czas_2 = QLCDNumber(self.frame_39)
        self.Czas_2.setObjectName(u"Czas_2")
        self.Czas_2.setFont(font6)
        self.Czas_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Czas_2, 10, 3, 1, 1)

        self.label_106 = QLabel(self.frame_39)
        self.label_106.setObjectName(u"label_106")

        self.gridLayout_3.addWidget(self.label_106, 6, 4, 1, 1)

        self.label_95 = QLabel(self.frame_39)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font21)

        self.gridLayout_3.addWidget(self.label_95, 4, 2, 1, 1)

        self.label_105 = QLabel(self.frame_39)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font21)

        self.gridLayout_3.addWidget(self.label_105, 2, 2, 1, 1)

        self.label_114 = QLabel(self.frame_39)
        self.label_114.setObjectName(u"label_114")

        self.gridLayout_3.addWidget(self.label_114, 1, 4, 1, 1)

        self.label_94 = QLabel(self.frame_39)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font21)

        self.gridLayout_3.addWidget(self.label_94, 5, 2, 1, 1)

        self.Pochylenie_2 = QLCDNumber(self.frame_39)
        self.Pochylenie_2.setObjectName(u"Pochylenie_2")
        self.Pochylenie_2.setFont(font6)
        self.Pochylenie_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Pochylenie_2, 8, 3, 1, 1)

        self.Predkosc_Z_2 = QLCDNumber(self.frame_39)
        self.Predkosc_Z_2.setObjectName(u"Predkosc_Z_2")
        self.Predkosc_Z_2.setFont(font6)
        self.Predkosc_Z_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Predkosc_Z_2, 5, 3, 1, 1)

        self.label_99 = QLabel(self.frame_39)
        self.label_99.setObjectName(u"label_99")

        self.gridLayout_3.addWidget(self.label_99, 10, 4, 1, 1)

        self.label_93 = QLabel(self.frame_39)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font21)

        self.gridLayout_3.addWidget(self.label_93, 6, 2, 1, 1)

        self.label_112 = QLabel(self.frame_39)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setFont(font21)

        self.gridLayout_3.addWidget(self.label_112, 7, 2, 1, 1)

        self.Predkosc_Y_2 = QLCDNumber(self.frame_39)
        self.Predkosc_Y_2.setObjectName(u"Predkosc_Y_2")
        self.Predkosc_Y_2.setFont(font6)
        self.Predkosc_Y_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Predkosc_Y_2, 4, 3, 1, 1)

        self.Pozycja_X_2 = QLCDNumber(self.frame_39)
        self.Pozycja_X_2.setObjectName(u"Pozycja_X_2")
        self.Pozycja_X_2.setFont(font6)
        self.Pozycja_X_2.setDigitCount(6)
        self.Pozycja_X_2.setProperty("value", 0.000000000000000)

        self.gridLayout_3.addWidget(self.Pozycja_X_2, 0, 3, 1, 1)

        self.label_100 = QLabel(self.frame_39)
        self.label_100.setObjectName(u"label_100")

        self.gridLayout_3.addWidget(self.label_100, 3, 4, 1, 1)

        self.label_98 = QLabel(self.frame_39)
        self.label_98.setObjectName(u"label_98")

        self.gridLayout_3.addWidget(self.label_98, 8, 4, 1, 1)

        self.Predkosc_X_2 = QLCDNumber(self.frame_39)
        self.Predkosc_X_2.setObjectName(u"Predkosc_X_2")
        self.Predkosc_X_2.setFont(font6)
        self.Predkosc_X_2.setDigitCount(6)

        self.gridLayout_3.addWidget(self.Predkosc_X_2, 3, 3, 1, 1)

        self.label_97 = QLabel(self.frame_39)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font21)

        self.gridLayout_3.addWidget(self.label_97, 3, 2, 1, 1)

        self.label_101 = QLabel(self.frame_39)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font21)

        self.gridLayout_3.addWidget(self.label_101, 1, 2, 1, 1)

        self.label_108 = QLabel(self.frame_39)
        self.label_108.setObjectName(u"label_108")

        self.gridLayout_3.addWidget(self.label_108, 9, 4, 1, 1)

        self.stackedWidget.addWidget(self.VR_page)
        self.Tutorial_page = QWidget()
        self.Tutorial_page.setObjectName(u"Tutorial_page")
        self.Tutorial_page.setStyleSheet(u"background-color:transparent;\n"
"background-repeat: no-repeat;\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout_102 = QHBoxLayout(self.Tutorial_page)
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.frame_9 = QFrame(self.Tutorial_page)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy4)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.frame_9)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy5)
        self.frame_18.setMaximumSize(QSize(700, 16777215))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_18)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.frame_19 = QFrame(self.frame_18)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_14 = QLabel(self.frame_19)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-arrow-left-58.png"))
        self.label_14.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_14)

        self.label_43 = QLabel(self.frame_19)
        self.label_43.setObjectName(u"label_43")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy6)
        self.label_43.setWordWrap(True)

        self.horizontalLayout_21.addWidget(self.label_43)


        self.verticalLayout_5.addWidget(self.frame_19)

        self.verticalSpacer_2 = QSpacerItem(20, 21, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.frame_20 = QFrame(self.frame_18)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(16777215, 80))
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_44 = QLabel(self.frame_20)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-arrow-left-58.png"))
        self.label_44.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_44, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_45 = QLabel(self.frame_20)
        self.label_45.setObjectName(u"label_45")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy7)
        self.label_45.setWordWrap(True)

        self.horizontalLayout_22.addWidget(self.label_45)


        self.verticalLayout_5.addWidget(self.frame_20)

        self.verticalSpacer_3 = QSpacerItem(20, 34, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.frame_17 = QFrame(self.frame_18)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_42 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(-1, -1, -1, 35)
        self.label_62 = QLabel(self.frame_17)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-arrow-left-58.png"))
        self.label_62.setScaledContents(True)

        self.horizontalLayout_42.addWidget(self.label_62, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.label_63 = QLabel(self.frame_17)
        self.label_63.setObjectName(u"label_63")
        sizePolicy7.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy7)
        self.label_63.setWordWrap(True)

        self.horizontalLayout_42.addWidget(self.label_63, 0, Qt.AlignVCenter)


        self.verticalLayout_5.addWidget(self.frame_17)

        self.verticalSpacer_11 = QSpacerItem(20, 3, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_11)

        self.frame_21 = QFrame(self.frame_18)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_46 = QLabel(self.frame_21)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-arrow-left-58.png"))
        self.label_46.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.label_46)

        self.label_47 = QLabel(self.frame_21)
        self.label_47.setObjectName(u"label_47")
        sizePolicy6.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy6)
        self.label_47.setWordWrap(True)

        self.horizontalLayout_23.addWidget(self.label_47)


        self.verticalLayout_5.addWidget(self.frame_21)

        self.verticalSpacer_4 = QSpacerItem(20, 37, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.frame_22 = QFrame(self.frame_18)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_48 = QLabel(self.frame_22)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-arrow-left-58.png"))
        self.label_48.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_48, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_49 = QLabel(self.frame_22)
        self.label_49.setObjectName(u"label_49")
        sizePolicy6.setHeightForWidth(self.label_49.sizePolicy().hasHeightForWidth())
        self.label_49.setSizePolicy(sizePolicy6)
        self.label_49.setWordWrap(True)

        self.horizontalLayout_24.addWidget(self.label_49)


        self.verticalLayout_5.addWidget(self.frame_22)

        self.verticalSpacer_5 = QSpacerItem(20, 18, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_5)

        self.frame_23 = QFrame(self.frame_18)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_50 = QLabel(self.frame_23)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-arrow-left-58.png"))
        self.label_50.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.label_50, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_51 = QLabel(self.frame_23)
        self.label_51.setObjectName(u"label_51")
        sizePolicy6.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy6)
        self.label_51.setWordWrap(True)

        self.horizontalLayout_25.addWidget(self.label_51)


        self.verticalLayout_5.addWidget(self.frame_23)

        self.verticalSpacer_6 = QSpacerItem(20, 17, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_6)

        self.frame_24 = QFrame(self.frame_18)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_52 = QLabel(self.frame_24)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-arrow-left-58.png"))
        self.label_52.setScaledContents(True)

        self.horizontalLayout_26.addWidget(self.label_52, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_53 = QLabel(self.frame_24)
        self.label_53.setObjectName(u"label_53")
        sizePolicy6.setHeightForWidth(self.label_53.sizePolicy().hasHeightForWidth())
        self.label_53.setSizePolicy(sizePolicy6)
        self.label_53.setWordWrap(True)

        self.horizontalLayout_26.addWidget(self.label_53)


        self.verticalLayout_5.addWidget(self.frame_24)

        self.verticalSpacer_7 = QSpacerItem(20, 19, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.frame_25 = QFrame(self.frame_18)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_54 = QLabel(self.frame_25)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-arrow-left-58.png"))
        self.label_54.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.label_54)

        self.label_55 = QLabel(self.frame_25)
        self.label_55.setObjectName(u"label_55")
        sizePolicy6.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy6)
        self.label_55.setWordWrap(True)

        self.horizontalLayout_27.addWidget(self.label_55)


        self.verticalLayout_5.addWidget(self.frame_25)

        self.verticalSpacer_8 = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_5.addItem(self.verticalSpacer_8)


        self.horizontalLayout_31.addWidget(self.frame_18)


        self.horizontalLayout_102.addWidget(self.frame_9)

        self.frame_80 = QFrame(self.Tutorial_page)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setMinimumSize(QSize(500, 0))
        self.frame_80.setMaximumSize(QSize(16777215, 1000))
        self.frame_80.setFrameShape(QFrame.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_80)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_10 = QFrame(self.frame_80)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_103 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.label_210 = QLabel(self.frame_10)
        self.label_210.setObjectName(u"label_210")
        font22 = QFont()
        font22.setPointSize(16)
        font22.setBold(True)
        font22.setWeight(75)
        self.label_210.setFont(font22)

        self.horizontalLayout_103.addWidget(self.label_210, 0, Qt.AlignHCenter)

        self.pushButton = QPushButton(self.frame_10)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font9)
        icon19 = QIcon()
        icon19.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-right-arrow-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon19)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_103.addWidget(self.pushButton, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_51.addWidget(self.frame_10)

        self.frame_93 = QFrame(self.frame_80)
        self.frame_93.setObjectName(u"frame_93")
        self.frame_93.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_93.setFrameShape(QFrame.StyledPanel)
        self.frame_93.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_101 = QHBoxLayout(self.frame_93)
        self.horizontalLayout_101.setSpacing(0)
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.horizontalLayout_101.setContentsMargins(0, 0, 0, 0)
        self.label_208 = QLabel(self.frame_93)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setFont(font)
        self.label_208.setWordWrap(True)

        self.horizontalLayout_101.addWidget(self.label_208)

        self.label_222 = QLabel(self.frame_93)
        self.label_222.setObjectName(u"label_222")
        self.label_222.setMaximumSize(QSize(64, 64))
        self.label_222.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-drone-60.png"))
        self.label_222.setScaledContents(True)

        self.horizontalLayout_101.addWidget(self.label_222)


        self.verticalLayout_51.addWidget(self.frame_93)

        self.frame_92 = QFrame(self.frame_80)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_92.setFrameShape(QFrame.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_100 = QHBoxLayout(self.frame_92)
        self.horizontalLayout_100.setSpacing(0)
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.horizontalLayout_100.setContentsMargins(0, 0, 0, 0)
        self.label_209 = QLabel(self.frame_92)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setFont(font)
        self.label_209.setWordWrap(True)

        self.horizontalLayout_100.addWidget(self.label_209)

        self.label_225 = QLabel(self.frame_92)
        self.label_225.setObjectName(u"label_225")
        self.label_225.setMaximumSize(QSize(160, 70))
        self.label_225.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Sterowanie.png"))
        self.label_225.setScaledContents(True)

        self.horizontalLayout_100.addWidget(self.label_225)


        self.verticalLayout_51.addWidget(self.frame_92)

        self.frame_91 = QFrame(self.frame_80)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_91.setFrameShape(QFrame.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_99 = QHBoxLayout(self.frame_91)
        self.horizontalLayout_99.setSpacing(0)
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.horizontalLayout_99.setContentsMargins(0, 0, 0, 0)
        self.label_211 = QLabel(self.frame_91)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setFont(font)
        self.label_211.setWordWrap(True)

        self.horizontalLayout_99.addWidget(self.label_211)

        self.label_223 = QLabel(self.frame_91)
        self.label_223.setObjectName(u"label_223")
        self.label_223.setMaximumSize(QSize(100, 60))
        self.label_223.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-12-16 131624.png"))
        self.label_223.setScaledContents(True)

        self.horizontalLayout_99.addWidget(self.label_223)


        self.verticalLayout_51.addWidget(self.frame_91)

        self.frame_90 = QFrame(self.frame_80)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_90.setFrameShape(QFrame.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_98 = QHBoxLayout(self.frame_90)
        self.horizontalLayout_98.setSpacing(0)
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.horizontalLayout_98.setContentsMargins(0, 0, 0, 0)
        self.label_212 = QLabel(self.frame_90)
        self.label_212.setObjectName(u"label_212")
        self.label_212.setFont(font)
        self.label_212.setWordWrap(True)

        self.horizontalLayout_98.addWidget(self.label_212)

        self.label_224 = QLabel(self.frame_90)
        self.label_224.setObjectName(u"label_224")
        self.label_224.setMaximumSize(QSize(200, 60))
        self.label_224.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-11-13 113106.png"))
        self.label_224.setScaledContents(True)

        self.horizontalLayout_98.addWidget(self.label_224)


        self.verticalLayout_51.addWidget(self.frame_90)

        self.frame_89 = QFrame(self.frame_80)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_89.setFrameShape(QFrame.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_97 = QHBoxLayout(self.frame_89)
        self.horizontalLayout_97.setSpacing(0)
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.horizontalLayout_97.setContentsMargins(0, 0, 0, 0)
        self.label_213 = QLabel(self.frame_89)
        self.label_213.setObjectName(u"label_213")
        self.label_213.setFont(font)
        self.label_213.setWordWrap(True)

        self.horizontalLayout_97.addWidget(self.label_213)


        self.verticalLayout_51.addWidget(self.frame_89)

        self.frame_88 = QFrame(self.frame_80)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_88.setFrameShape(QFrame.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_96 = QHBoxLayout(self.frame_88)
        self.horizontalLayout_96.setSpacing(0)
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalLayout_96.setContentsMargins(0, 0, 0, 0)
        self.label_214 = QLabel(self.frame_88)
        self.label_214.setObjectName(u"label_214")
        self.label_214.setFont(font)
        self.label_214.setWordWrap(True)

        self.horizontalLayout_96.addWidget(self.label_214)

        self.label_227 = QLabel(self.frame_88)
        self.label_227.setObjectName(u"label_227")
        self.label_227.setMaximumSize(QSize(200, 60))
        self.label_227.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-11-13 214559.png"))
        self.label_227.setScaledContents(True)

        self.horizontalLayout_96.addWidget(self.label_227)


        self.verticalLayout_51.addWidget(self.frame_88)

        self.frame_87 = QFrame(self.frame_80)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_87.setFrameShape(QFrame.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_94 = QHBoxLayout(self.frame_87)
        self.horizontalLayout_94.setSpacing(0)
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalLayout_94.setContentsMargins(0, 0, 0, 0)
        self.label_215 = QLabel(self.frame_87)
        self.label_215.setObjectName(u"label_215")
        self.label_215.setFont(font)
        self.label_215.setWordWrap(True)

        self.horizontalLayout_94.addWidget(self.label_215)


        self.verticalLayout_51.addWidget(self.frame_87)

        self.frame_86 = QFrame(self.frame_80)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_86.setFrameShape(QFrame.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_95 = QHBoxLayout(self.frame_86)
        self.horizontalLayout_95.setSpacing(0)
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalLayout_95.setContentsMargins(0, 0, 0, 0)
        self.label_216 = QLabel(self.frame_86)
        self.label_216.setObjectName(u"label_216")
        self.label_216.setFont(font)
        self.label_216.setWordWrap(True)

        self.horizontalLayout_95.addWidget(self.label_216)

        self.label_226 = QLabel(self.frame_86)
        self.label_226.setObjectName(u"label_226")
        self.label_226.setMaximumSize(QSize(200, 60))
        self.label_226.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-12-17 133628.png"))
        self.label_226.setScaledContents(True)

        self.horizontalLayout_95.addWidget(self.label_226)


        self.verticalLayout_51.addWidget(self.frame_86)

        self.frame_85 = QFrame(self.frame_80)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_85.setFrameShape(QFrame.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_93 = QHBoxLayout(self.frame_85)
        self.horizontalLayout_93.setSpacing(0)
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.horizontalLayout_93.setContentsMargins(0, 0, 0, 0)
        self.label_217 = QLabel(self.frame_85)
        self.label_217.setObjectName(u"label_217")
        self.label_217.setFont(font)
        self.label_217.setWordWrap(True)

        self.horizontalLayout_93.addWidget(self.label_217)

        self.label_228 = QLabel(self.frame_85)
        self.label_228.setObjectName(u"label_228")
        self.label_228.setMaximumSize(QSize(64, 64))
        self.label_228.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-automatic-64.png"))
        self.label_228.setScaledContents(True)

        self.horizontalLayout_93.addWidget(self.label_228)


        self.verticalLayout_51.addWidget(self.frame_85)

        self.frame_84 = QFrame(self.frame_80)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_84.setFrameShape(QFrame.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_92 = QHBoxLayout(self.frame_84)
        self.horizontalLayout_92.setSpacing(0)
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalLayout_92.setContentsMargins(0, 0, 0, 0)
        self.label_218 = QLabel(self.frame_84)
        self.label_218.setObjectName(u"label_218")
        self.label_218.setFont(font)
        self.label_218.setScaledContents(False)
        self.label_218.setWordWrap(True)

        self.horizontalLayout_92.addWidget(self.label_218)

        self.label_229 = QLabel(self.frame_84)
        self.label_229.setObjectName(u"label_229")
        self.label_229.setMaximumSize(QSize(64, 64))
        self.label_229.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-landing-64.png"))
        self.label_229.setScaledContents(True)

        self.horizontalLayout_92.addWidget(self.label_229)


        self.verticalLayout_51.addWidget(self.frame_84)

        self.frame_83 = QFrame(self.frame_80)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_83.setFrameShape(QFrame.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_91 = QHBoxLayout(self.frame_83)
        self.horizontalLayout_91.setSpacing(0)
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.horizontalLayout_91.setContentsMargins(0, 0, 0, 0)
        self.label_219 = QLabel(self.frame_83)
        self.label_219.setObjectName(u"label_219")
        self.label_219.setFont(font)
        self.label_219.setWordWrap(True)

        self.horizontalLayout_91.addWidget(self.label_219)

        self.label_230 = QLabel(self.frame_83)
        self.label_230.setObjectName(u"label_230")
        self.label_230.setMaximumSize(QSize(200, 60))
        self.label_230.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-11-09 092944.png"))
        self.label_230.setScaledContents(True)

        self.horizontalLayout_91.addWidget(self.label_230)


        self.verticalLayout_51.addWidget(self.frame_83)

        self.frame_82 = QFrame(self.frame_80)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_82.setFrameShape(QFrame.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_90 = QHBoxLayout(self.frame_82)
        self.horizontalLayout_90.setSpacing(0)
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.horizontalLayout_90.setContentsMargins(0, 0, 0, 0)
        self.label_220 = QLabel(self.frame_82)
        self.label_220.setObjectName(u"label_220")
        self.label_220.setFont(font)
        self.label_220.setWordWrap(True)

        self.horizontalLayout_90.addWidget(self.label_220)

        self.label_231 = QLabel(self.frame_82)
        self.label_231.setObjectName(u"label_231")
        self.label_231.setMaximumSize(QSize(200, 60))
        self.label_231.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-11-10 131231.png"))
        self.label_231.setScaledContents(True)

        self.horizontalLayout_90.addWidget(self.label_231)


        self.verticalLayout_51.addWidget(self.frame_82)

        self.frame_81 = QFrame(self.frame_80)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:30px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_81.setFrameShape(QFrame.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_81)
        self.horizontalLayout_83.setSpacing(0)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_83.setContentsMargins(0, 0, 0, 0)
        self.label_221 = QLabel(self.frame_81)
        self.label_221.setObjectName(u"label_221")
        self.label_221.setFont(font)
        self.label_221.setScaledContents(True)
        self.label_221.setWordWrap(True)

        self.horizontalLayout_83.addWidget(self.label_221, 0, Qt.AlignVCenter)

        self.label_232 = QLabel(self.frame_81)
        self.label_232.setObjectName(u"label_232")
        self.label_232.setMaximumSize(QSize(64, 64))
        self.label_232.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-analysis-50.png"))
        self.label_232.setScaledContents(True)

        self.horizontalLayout_83.addWidget(self.label_232)


        self.verticalLayout_51.addWidget(self.frame_81)


        self.horizontalLayout_102.addWidget(self.frame_80)

        self.frame_94 = QFrame(self.Tutorial_page)
        self.frame_94.setObjectName(u"frame_94")
        self.frame_94.setFrameShape(QFrame.StyledPanel)
        self.frame_94.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_94)
        self.verticalLayout_52.setSpacing(0)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_233 = QLabel(self.frame_94)
        self.label_233.setObjectName(u"label_233")
        self.label_233.setMinimumSize(QSize(480, 370))
        self.label_233.setMaximumSize(QSize(480, 370))
        self.label_233.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-12-19 194237.png"))
        self.label_233.setScaledContents(True)

        self.verticalLayout_52.addWidget(self.label_233)

        self.label_235 = QLabel(self.frame_94)
        self.label_235.setObjectName(u"label_235")
        self.label_235.setMinimumSize(QSize(480, 220))
        self.label_235.setMaximumSize(QSize(480, 16777215))
        self.label_235.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-12-19 195443.png"))
        self.label_235.setScaledContents(True)

        self.verticalLayout_52.addWidget(self.label_235)

        self.label_234 = QLabel(self.frame_94)
        self.label_234.setObjectName(u"label_234")
        self.label_234.setMinimumSize(QSize(480, 400))
        self.label_234.setMaximumSize(QSize(480, 370))
        self.label_234.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-12-19 194254.png"))
        self.label_234.setScaledContents(True)

        self.verticalLayout_52.addWidget(self.label_234)


        self.horizontalLayout_102.addWidget(self.frame_94)

        self.stackedWidget.addWidget(self.Tutorial_page)
        self.Mission_page = QWidget()
        self.Mission_page.setObjectName(u"Mission_page")
        self.Mission_page.setStyleSheet(u"background-color:transparent;\n"
"background-repeat: no-repeat;\n"
"color: rgb(255, 255, 255);")
        self.frame_26 = QFrame(self.Mission_page)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setGeometry(QRect(0, -1, 1330, 1024))
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy8)
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_26)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 90)
        self.frame_47 = QFrame(self.frame_26)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setMaximumSize(QSize(600, 400))
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_47)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_115 = QLabel(self.frame_47)
        self.label_115.setObjectName(u"label_115")
        font23 = QFont()
        font23.setFamily(u"Microsoft YaHei UI")
        font23.setPointSize(18)
        font23.setBold(True)
        font23.setWeight(75)
        self.label_115.setFont(font23)

        self.verticalLayout_24.addWidget(self.label_115, 0, Qt.AlignHCenter)

        self.comboBox = QComboBox(self.frame_47)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font5)

        self.verticalLayout_24.addWidget(self.comboBox, 0, Qt.AlignHCenter)

        self.stackedWidget_2 = QStackedWidget(self.frame_47)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page0 = QWidget()
        self.page0.setObjectName(u"page0")
        self.horizontalLayout_48 = QHBoxLayout(self.page0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.chart0 = QChartView(self.page0)
        self.chart0.setObjectName(u"chart0")
        self.chart0.setStyleSheet(u"background-color: rgb(0, 10, 0);")

        self.horizontalLayout_48.addWidget(self.chart0)

        self.stackedWidget_2.addWidget(self.page0)
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.horizontalLayout_49 = QHBoxLayout(self.page1)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.chart1 = QChartView(self.page1)
        self.chart1.setObjectName(u"chart1")
        self.chart1.setStyleSheet(u"background-color: rgb(110, 0, 0);")

        self.horizontalLayout_49.addWidget(self.chart1)

        self.stackedWidget_2.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.horizontalLayout_50 = QHBoxLayout(self.page2)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.chart2 = QChartView(self.page2)
        self.chart2.setObjectName(u"chart2")
        self.chart2.setStyleSheet(u"background-color: rgb(30, 30, 30);")

        self.horizontalLayout_50.addWidget(self.chart2)

        self.stackedWidget_2.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.horizontalLayout_51 = QHBoxLayout(self.page3)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.chart3 = QChartView(self.page3)
        self.chart3.setObjectName(u"chart3")
        self.chart3.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.horizontalLayout_51.addWidget(self.chart3)

        self.stackedWidget_2.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.horizontalLayout_52 = QHBoxLayout(self.page4)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.chart4 = QChartView(self.page4)
        self.chart4.setObjectName(u"chart4")
        self.chart4.setMinimumSize(QSize(0, 0))
        self.chart4.setMaximumSize(QSize(564, 382))
        self.chart4.setStyleSheet(u"background-color: rgb(0, 0, 127);")

        self.horizontalLayout_52.addWidget(self.chart4)

        self.stackedWidget_2.addWidget(self.page4)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.horizontalLayout_53 = QHBoxLayout(self.page5)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.chart5 = QChartView(self.page5)
        self.chart5.setObjectName(u"chart5")
        self.chart5.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_53.addWidget(self.chart5)

        self.stackedWidget_2.addWidget(self.page5)
        self.page6 = QWidget()
        self.page6.setObjectName(u"page6")
        self.horizontalLayout_54 = QHBoxLayout(self.page6)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.chart6 = QChartView(self.page6)
        self.chart6.setObjectName(u"chart6")
        self.chart6.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_54.addWidget(self.chart6)

        self.stackedWidget_2.addWidget(self.page6)
        self.page7 = QWidget()
        self.page7.setObjectName(u"page7")
        self.horizontalLayout_55 = QHBoxLayout(self.page7)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.chart7 = QChartView(self.page7)
        self.chart7.setObjectName(u"chart7")
        self.chart7.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_55.addWidget(self.chart7)

        self.stackedWidget_2.addWidget(self.page7)
        self.page8 = QWidget()
        self.page8.setObjectName(u"page8")
        self.verticalLayout_28 = QVBoxLayout(self.page8)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.chart8 = QChartView(self.page8)
        self.chart8.setObjectName(u"chart8")
        self.chart8.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_28.addWidget(self.chart8)

        self.stackedWidget_2.addWidget(self.page8)
        self.page9 = QWidget()
        self.page9.setObjectName(u"page9")
        self.horizontalLayout_56 = QHBoxLayout(self.page9)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.chart9 = QChartView(self.page9)
        self.chart9.setObjectName(u"chart9")
        self.chart9.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_56.addWidget(self.chart9)

        self.stackedWidget_2.addWidget(self.page9)
        self.page10 = QWidget()
        self.page10.setObjectName(u"page10")
        self.horizontalLayout_57 = QHBoxLayout(self.page10)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.chart10 = QChartView(self.page10)
        self.chart10.setObjectName(u"chart10")
        self.chart10.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_57.addWidget(self.chart10)

        self.stackedWidget_2.addWidget(self.page10)

        self.verticalLayout_24.addWidget(self.stackedWidget_2)


        self.gridLayout_4.addWidget(self.frame_47, 0, 0, 1, 1)

        self.frame_49 = QFrame(self.frame_26)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setMaximumSize(QSize(600, 400))
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_49)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_144 = QLabel(self.frame_49)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setFont(font23)

        self.verticalLayout_26.addWidget(self.label_144, 0, Qt.AlignHCenter)

        self.widget_6 = QChartView(self.frame_49)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMinimumSize(QSize(564, 382))
        self.widget_6.setMaximumSize(QSize(564, 382))
        self.widget_6.setStyleSheet(u"background-color: rgb(85, 85, 255);")

        self.verticalLayout_26.addWidget(self.widget_6)


        self.gridLayout_4.addWidget(self.frame_49, 0, 2, 1, 1)

        self.frame_48 = QFrame(self.frame_26)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setMaximumSize(QSize(600, 400))
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_48)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_116 = QLabel(self.frame_48)
        self.label_116.setObjectName(u"label_116")
        self.label_116.setFont(font23)

        self.verticalLayout_25.addWidget(self.label_116, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.widget_5 = QChartView(self.frame_48)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(564, 382))
        self.widget_5.setStyleSheet(u"background-color: rgb(85, 85, 255);")

        self.verticalLayout_25.addWidget(self.widget_5, 0, Qt.AlignTop)


        self.gridLayout_4.addWidget(self.frame_48, 1, 0, 1, 1)

        self.frame_50 = QFrame(self.frame_26)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(600, 400))
        self.frame_50.setFrameShape(QFrame.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_50)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_145 = QLabel(self.frame_50)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setFont(font23)

        self.verticalLayout_27.addWidget(self.label_145, 0, Qt.AlignHCenter)

        self.comboBox_2 = QComboBox(self.frame_50)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setFont(font5)

        self.verticalLayout_27.addWidget(self.comboBox_2, 0, Qt.AlignHCenter)

        self.stackedWidget_3 = QStackedWidget(self.frame_50)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(0, 0))
        self.page0_2 = QWidget()
        self.page0_2.setObjectName(u"page0_2")
        self.horizontalLayout_58 = QHBoxLayout(self.page0_2)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.chart0_2 = QChartView(self.page0_2)
        self.chart0_2.setObjectName(u"chart0_2")
        self.chart0_2.setMaximumSize(QSize(16777215, 16777215))
        self.chart0_2.setStyleSheet(u"background-color: rgb(0, 10, 0);")

        self.horizontalLayout_58.addWidget(self.chart0_2)

        self.stackedWidget_3.addWidget(self.page0_2)
        self.page1_2 = QWidget()
        self.page1_2.setObjectName(u"page1_2")
        self.horizontalLayout_59 = QHBoxLayout(self.page1_2)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.chart1_2 = QChartView(self.page1_2)
        self.chart1_2.setObjectName(u"chart1_2")
        self.chart1_2.setStyleSheet(u"background-color: rgb(110, 0, 0);")

        self.horizontalLayout_59.addWidget(self.chart1_2)

        self.stackedWidget_3.addWidget(self.page1_2)
        self.page2_2 = QWidget()
        self.page2_2.setObjectName(u"page2_2")
        self.horizontalLayout_60 = QHBoxLayout(self.page2_2)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.chart2_2 = QChartView(self.page2_2)
        self.chart2_2.setObjectName(u"chart2_2")
        self.chart2_2.setStyleSheet(u"background-color: rgb(30, 30, 30);")

        self.horizontalLayout_60.addWidget(self.chart2_2)

        self.stackedWidget_3.addWidget(self.page2_2)
        self.page3_2 = QWidget()
        self.page3_2.setObjectName(u"page3_2")
        self.horizontalLayout_61 = QHBoxLayout(self.page3_2)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.chart3_2 = QChartView(self.page3_2)
        self.chart3_2.setObjectName(u"chart3_2")
        self.chart3_2.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.horizontalLayout_61.addWidget(self.chart3_2)

        self.stackedWidget_3.addWidget(self.page3_2)
        self.page4_2 = QWidget()
        self.page4_2.setObjectName(u"page4_2")
        self.horizontalLayout_62 = QHBoxLayout(self.page4_2)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.chart4_2 = QChartView(self.page4_2)
        self.chart4_2.setObjectName(u"chart4_2")
        self.chart4_2.setStyleSheet(u"background-color: rgb(0, 0, 127);")

        self.horizontalLayout_62.addWidget(self.chart4_2)

        self.stackedWidget_3.addWidget(self.page4_2)
        self.page5_2 = QWidget()
        self.page5_2.setObjectName(u"page5_2")
        self.horizontalLayout_63 = QHBoxLayout(self.page5_2)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.chart5_2 = QChartView(self.page5_2)
        self.chart5_2.setObjectName(u"chart5_2")
        self.chart5_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_63.addWidget(self.chart5_2)

        self.stackedWidget_3.addWidget(self.page5_2)
        self.page6_2 = QWidget()
        self.page6_2.setObjectName(u"page6_2")
        self.horizontalLayout_64 = QHBoxLayout(self.page6_2)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.chart6_2 = QChartView(self.page6_2)
        self.chart6_2.setObjectName(u"chart6_2")
        self.chart6_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_64.addWidget(self.chart6_2)

        self.stackedWidget_3.addWidget(self.page6_2)
        self.page7_2 = QWidget()
        self.page7_2.setObjectName(u"page7_2")
        self.horizontalLayout_65 = QHBoxLayout(self.page7_2)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.chart7_2 = QChartView(self.page7_2)
        self.chart7_2.setObjectName(u"chart7_2")
        self.chart7_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_65.addWidget(self.chart7_2)

        self.stackedWidget_3.addWidget(self.page7_2)
        self.page8_2 = QWidget()
        self.page8_2.setObjectName(u"page8_2")
        self.verticalLayout_29 = QVBoxLayout(self.page8_2)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.chart8_2 = QChartView(self.page8_2)
        self.chart8_2.setObjectName(u"chart8_2")
        self.chart8_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_29.addWidget(self.chart8_2)

        self.stackedWidget_3.addWidget(self.page8_2)
        self.page9_2 = QWidget()
        self.page9_2.setObjectName(u"page9_2")
        self.horizontalLayout_66 = QHBoxLayout(self.page9_2)
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.chart9_2 = QChartView(self.page9_2)
        self.chart9_2.setObjectName(u"chart9_2")
        self.chart9_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_66.addWidget(self.chart9_2)

        self.stackedWidget_3.addWidget(self.page9_2)
        self.page10_2 = QWidget()
        self.page10_2.setObjectName(u"page10_2")
        self.horizontalLayout_67 = QHBoxLayout(self.page10_2)
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.chart10_2 = QChartView(self.page10_2)
        self.chart10_2.setObjectName(u"chart10_2")
        self.chart10_2.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_67.addWidget(self.chart10_2)

        self.stackedWidget_3.addWidget(self.page10_2)

        self.verticalLayout_27.addWidget(self.stackedWidget_3)


        self.gridLayout_4.addWidget(self.frame_50, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.Mission_page)
        self.Analyze_page = QWidget()
        self.Analyze_page.setObjectName(u"Analyze_page")
        self.Analyze_page.setStyleSheet(u"background-color:transparent;\n"
"background-repeat: no-repeat;\n"
"color: rgb(255, 255, 255);")
        self.frame_52 = QFrame(self.Analyze_page)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setGeometry(QRect(730, 82, 690, 418))
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_52)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_174 = QLabel(self.frame_52)
        self.label_174.setObjectName(u"label_174")
        font24 = QFont()
        font24.setFamily(u"Microsoft YaHei UI")
        font24.setPointSize(13)
        font24.setBold(True)
        font24.setWeight(75)
        self.label_174.setFont(font24)

        self.verticalLayout_45.addWidget(self.label_174, 0, Qt.AlignHCenter)

        self.frame_72 = QFrame(self.frame_52)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setFrameShape(QFrame.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_82 = QHBoxLayout(self.frame_72)
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.horizontalLayout_82.setContentsMargins(-1, -1, -1, 0)
        self.label_188 = QLabel(self.frame_72)
        self.label_188.setObjectName(u"label_188")
        font25 = QFont()
        font25.setFamily(u"Microsoft YaHei UI")
        font25.setPointSize(12)
        self.label_188.setFont(font25)

        self.horizontalLayout_82.addWidget(self.label_188, 0, Qt.AlignHCenter)

        self.label_189 = QLabel(self.frame_72)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setFont(font25)

        self.horizontalLayout_82.addWidget(self.label_189, 0, Qt.AlignHCenter)


        self.verticalLayout_45.addWidget(self.frame_72)

        self.frame_71 = QFrame(self.frame_52)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_81 = QHBoxLayout(self.frame_71)
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.frame_67 = QFrame(self.frame_71)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_80 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_80.setSpacing(30)
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        sizePolicy1.setHeightForWidth(self.frame_68.sizePolicy().hasHeightForWidth())
        self.frame_68.setSizePolicy(sizePolicy1)
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_68)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_179 = QLabel(self.frame_68)
        self.label_179.setObjectName(u"label_179")
        font26 = QFont()
        font26.setFamily(u"MS Reference Sans Serif")
        font26.setBold(True)
        font26.setWeight(75)
        self.label_179.setFont(font26)

        self.verticalLayout_40.addWidget(self.label_179, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_180 = QLabel(self.frame_68)
        self.label_180.setObjectName(u"label_180")
        self.label_180.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-heart-rate-50.png"))

        self.verticalLayout_40.addWidget(self.label_180, 0, Qt.AlignHCenter)

        self.label_181 = QLabel(self.frame_68)
        self.label_181.setObjectName(u"label_181")
        self.label_181.setFont(font5)

        self.verticalLayout_40.addWidget(self.label_181, 0, Qt.AlignHCenter)


        self.horizontalLayout_80.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.frame_67)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setFrameShape(QFrame.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_69)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_182 = QLabel(self.frame_69)
        self.label_182.setObjectName(u"label_182")
        self.label_182.setFont(font26)

        self.verticalLayout_43.addWidget(self.label_182, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_183 = QLabel(self.frame_69)
        self.label_183.setObjectName(u"label_183")
        self.label_183.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-heart-rate-50.png"))

        self.verticalLayout_43.addWidget(self.label_183, 0, Qt.AlignHCenter)

        self.label_184 = QLabel(self.frame_69)
        self.label_184.setObjectName(u"label_184")
        self.label_184.setFont(font5)

        self.verticalLayout_43.addWidget(self.label_184, 0, Qt.AlignHCenter)


        self.horizontalLayout_80.addWidget(self.frame_69)

        self.frame_70 = QFrame(self.frame_67)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_70)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_185 = QLabel(self.frame_70)
        self.label_185.setObjectName(u"label_185")
        self.label_185.setFont(font26)

        self.verticalLayout_44.addWidget(self.label_185, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_186 = QLabel(self.frame_70)
        self.label_186.setObjectName(u"label_186")
        self.label_186.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-heart-rate-50.png"))

        self.verticalLayout_44.addWidget(self.label_186, 0, Qt.AlignHCenter)

        self.label_187 = QLabel(self.frame_70)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setFont(font5)

        self.verticalLayout_44.addWidget(self.label_187, 0, Qt.AlignHCenter)


        self.horizontalLayout_80.addWidget(self.frame_70)


        self.horizontalLayout_81.addWidget(self.frame_67)

        self.line_7 = QFrame(self.frame_71)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_7.setFrameShape(QFrame.VLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_81.addWidget(self.line_7)

        self.frame_53 = QFrame(self.frame_71)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_78 = QHBoxLayout(self.frame_53)
        self.horizontalLayout_78.setSpacing(30)
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_54)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_146 = QLabel(self.frame_54)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setFont(font26)

        self.verticalLayout_31.addWidget(self.label_146, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_147 = QLabel(self.frame_54)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-heart-rate-50.png"))

        self.verticalLayout_31.addWidget(self.label_147, 0, Qt.AlignHCenter)

        self.label_148 = QLabel(self.frame_54)
        self.label_148.setObjectName(u"label_148")
        self.label_148.setFont(font5)

        self.verticalLayout_31.addWidget(self.label_148, 0, Qt.AlignHCenter)


        self.horizontalLayout_78.addWidget(self.frame_54)

        self.frame_55 = QFrame(self.frame_53)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_55)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_149 = QLabel(self.frame_55)
        self.label_149.setObjectName(u"label_149")
        self.label_149.setFont(font26)

        self.verticalLayout_32.addWidget(self.label_149, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_150 = QLabel(self.frame_55)
        self.label_150.setObjectName(u"label_150")
        self.label_150.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-heart-rate-50.png"))

        self.verticalLayout_32.addWidget(self.label_150, 0, Qt.AlignHCenter)

        self.label_151 = QLabel(self.frame_55)
        self.label_151.setObjectName(u"label_151")
        self.label_151.setFont(font5)

        self.verticalLayout_32.addWidget(self.label_151, 0, Qt.AlignHCenter)


        self.horizontalLayout_78.addWidget(self.frame_55)

        self.frame_56 = QFrame(self.frame_53)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_56)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_152 = QLabel(self.frame_56)
        self.label_152.setObjectName(u"label_152")
        self.label_152.setFont(font26)

        self.verticalLayout_33.addWidget(self.label_152, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_153 = QLabel(self.frame_56)
        self.label_153.setObjectName(u"label_153")
        self.label_153.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-heart-rate-50.png"))

        self.verticalLayout_33.addWidget(self.label_153, 0, Qt.AlignHCenter)

        self.label_154 = QLabel(self.frame_56)
        self.label_154.setObjectName(u"label_154")
        self.label_154.setFont(font5)

        self.verticalLayout_33.addWidget(self.label_154, 0, Qt.AlignHCenter)


        self.horizontalLayout_78.addWidget(self.frame_56)


        self.horizontalLayout_81.addWidget(self.frame_53)


        self.verticalLayout_45.addWidget(self.frame_71)

        self.line_6 = QFrame(self.frame_52)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_45.addWidget(self.line_6)

        self.label_155 = QLabel(self.frame_52)
        self.label_155.setObjectName(u"label_155")
        self.label_155.setFont(font24)

        self.verticalLayout_45.addWidget(self.label_155, 0, Qt.AlignHCenter)

        self.frame_63 = QFrame(self.frame_52)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_79 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.frame_57 = QFrame(self.frame_63)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_57)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_156 = QLabel(self.frame_57)
        self.label_156.setObjectName(u"label_156")
        self.label_156.setFont(font26)

        self.verticalLayout_34.addWidget(self.label_156, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_157 = QLabel(self.frame_57)
        self.label_157.setObjectName(u"label_157")
        font27 = QFont()
        font27.setPointSize(5)
        self.label_157.setFont(font27)
        self.label_157.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-angry-50.png"))

        self.verticalLayout_34.addWidget(self.label_157, 0, Qt.AlignHCenter)

        self.label_158 = QLabel(self.frame_57)
        self.label_158.setObjectName(u"label_158")
        self.label_158.setFont(font5)

        self.verticalLayout_34.addWidget(self.label_158, 0, Qt.AlignHCenter)


        self.horizontalLayout_79.addWidget(self.frame_57)

        self.frame_58 = QFrame(self.frame_63)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_58)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_159 = QLabel(self.frame_58)
        self.label_159.setObjectName(u"label_159")
        self.label_159.setFont(font26)

        self.verticalLayout_35.addWidget(self.label_159, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_160 = QLabel(self.frame_58)
        self.label_160.setObjectName(u"label_160")
        self.label_160.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-disgusting-50.png"))

        self.verticalLayout_35.addWidget(self.label_160, 0, Qt.AlignHCenter)

        self.label_161 = QLabel(self.frame_58)
        self.label_161.setObjectName(u"label_161")
        self.label_161.setFont(font5)

        self.verticalLayout_35.addWidget(self.label_161, 0, Qt.AlignHCenter)


        self.horizontalLayout_79.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_63)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_59)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_162 = QLabel(self.frame_59)
        self.label_162.setObjectName(u"label_162")
        self.label_162.setFont(font26)

        self.verticalLayout_36.addWidget(self.label_162, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_163 = QLabel(self.frame_59)
        self.label_163.setObjectName(u"label_163")
        self.label_163.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-shocked-50.png"))

        self.verticalLayout_36.addWidget(self.label_163, 0, Qt.AlignHCenter)

        self.label_164 = QLabel(self.frame_59)
        self.label_164.setObjectName(u"label_164")
        self.label_164.setFont(font5)

        self.verticalLayout_36.addWidget(self.label_164, 0, Qt.AlignHCenter)


        self.horizontalLayout_79.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_63)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_60)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_165 = QLabel(self.frame_60)
        self.label_165.setObjectName(u"label_165")
        self.label_165.setFont(font26)

        self.verticalLayout_37.addWidget(self.label_165, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_166 = QLabel(self.frame_60)
        self.label_166.setObjectName(u"label_166")
        self.label_166.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-happy-50.png"))

        self.verticalLayout_37.addWidget(self.label_166, 0, Qt.AlignHCenter)

        self.label_167 = QLabel(self.frame_60)
        self.label_167.setObjectName(u"label_167")
        self.label_167.setFont(font5)

        self.verticalLayout_37.addWidget(self.label_167, 0, Qt.AlignHCenter)


        self.horizontalLayout_79.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_63)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_61)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_168 = QLabel(self.frame_61)
        self.label_168.setObjectName(u"label_168")
        self.label_168.setFont(font26)

        self.verticalLayout_38.addWidget(self.label_168, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_169 = QLabel(self.frame_61)
        self.label_169.setObjectName(u"label_169")
        self.label_169.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-surprised-50 (1).png"))

        self.verticalLayout_38.addWidget(self.label_169, 0, Qt.AlignHCenter)

        self.label_170 = QLabel(self.frame_61)
        self.label_170.setObjectName(u"label_170")
        self.label_170.setFont(font5)

        self.verticalLayout_38.addWidget(self.label_170, 0, Qt.AlignHCenter)


        self.horizontalLayout_79.addWidget(self.frame_61)

        self.frame_66 = QFrame(self.frame_63)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_66)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_176 = QLabel(self.frame_66)
        self.label_176.setObjectName(u"label_176")
        self.label_176.setFont(font26)

        self.verticalLayout_42.addWidget(self.label_176, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_177 = QLabel(self.frame_66)
        self.label_177.setObjectName(u"label_177")
        self.label_177.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-sad-50.png"))

        self.verticalLayout_42.addWidget(self.label_177, 0, Qt.AlignHCenter)

        self.label_178 = QLabel(self.frame_66)
        self.label_178.setObjectName(u"label_178")
        self.label_178.setFont(font5)

        self.verticalLayout_42.addWidget(self.label_178, 0, Qt.AlignHCenter)


        self.horizontalLayout_79.addWidget(self.frame_66)

        self.frame_62 = QFrame(self.frame_63)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_62)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_171 = QLabel(self.frame_62)
        self.label_171.setObjectName(u"label_171")
        self.label_171.setFont(font26)

        self.verticalLayout_39.addWidget(self.label_171, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_172 = QLabel(self.frame_62)
        self.label_172.setObjectName(u"label_172")
        self.label_172.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-neutral-50.png"))

        self.verticalLayout_39.addWidget(self.label_172, 0, Qt.AlignHCenter)

        self.label_173 = QLabel(self.frame_62)
        self.label_173.setObjectName(u"label_173")
        self.label_173.setFont(font5)

        self.verticalLayout_39.addWidget(self.label_173, 0, Qt.AlignHCenter)


        self.horizontalLayout_79.addWidget(self.frame_62)


        self.verticalLayout_45.addWidget(self.frame_63)

        self.frame_64 = QFrame(self.Analyze_page)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setGeometry(QRect(160, 550, 556, 341))
        self.frame_64.setStyleSheet(u"")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_56 = QVBoxLayout(self.frame_64)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_65)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_236 = QLabel(self.frame_65)
        self.label_236.setObjectName(u"label_236")
        font28 = QFont()
        font28.setFamily(u"Microsoft YaHei UI")
        font28.setPointSize(23)
        font28.setBold(True)
        font28.setWeight(75)
        self.label_236.setFont(font28)
        self.label_236.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_55.addWidget(self.label_236)


        self.verticalLayout_56.addWidget(self.frame_65)

        self.frame_102 = QFrame(self.frame_64)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_106 = QHBoxLayout(self.frame_102)
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.label_250 = QLabel(self.frame_102)
        self.label_250.setObjectName(u"label_250")
        self.label_250.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-forward-button-50.png"))

        self.horizontalLayout_106.addWidget(self.label_250, 0, Qt.AlignHCenter)

        self.frame_95 = QFrame(self.frame_102)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setFrameShape(QFrame.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_95)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.procenty = QLabel(self.frame_95)
        self.procenty.setObjectName(u"procenty")
        self.procenty.setMinimumSize(QSize(400, 0))
        self.procenty.setFont(font5)
        self.procenty.setWordWrap(True)

        self.verticalLayout_60.addWidget(self.procenty)


        self.horizontalLayout_106.addWidget(self.frame_95, 0, Qt.AlignLeft)


        self.verticalLayout_56.addWidget(self.frame_102)

        self.frame_96 = QFrame(self.frame_64)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_104 = QHBoxLayout(self.frame_96)
        self.horizontalLayout_104.setSpacing(0)
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalLayout_104.setContentsMargins(-1, -1, -1, 9)
        self.label_240 = QLabel(self.frame_96)
        self.label_240.setObjectName(u"label_240")
        self.label_240.setMinimumSize(QSize(100, 100))
        self.label_240.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-info-64.png"))
        self.label_240.setScaledContents(True)

        self.horizontalLayout_104.addWidget(self.label_240, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.komunikat = QLabel(self.frame_96)
        self.komunikat.setObjectName(u"komunikat")
        self.komunikat.setMinimumSize(QSize(420, 0))
        self.komunikat.setFont(font5)
        self.komunikat.setWordWrap(True)

        self.horizontalLayout_104.addWidget(self.komunikat, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_56.addWidget(self.frame_96)

        self.frame_51 = QFrame(self.Analyze_page)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setGeometry(QRect(120, 90, 600, 400))
        self.frame_51.setMaximumSize(QSize(600, 400))
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_51)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_175 = QLabel(self.frame_51)
        self.label_175.setObjectName(u"label_175")
        self.label_175.setFont(font23)

        self.verticalLayout_30.addWidget(self.label_175, 0, Qt.AlignHCenter)

        self.comboBox_3 = QComboBox(self.frame_51)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setFont(font5)

        self.verticalLayout_30.addWidget(self.comboBox_3, 0, Qt.AlignHCenter)

        self.stackedWidget_4 = QStackedWidget(self.frame_51)
        self.stackedWidget_4.setObjectName(u"stackedWidget_4")
        self.stackedWidget_4.setMinimumSize(QSize(0, 0))
        self.page0_3 = QWidget()
        self.page0_3.setObjectName(u"page0_3")
        self.horizontalLayout_68 = QHBoxLayout(self.page0_3)
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.chart0_3 = QChartView(self.page0_3)
        self.chart0_3.setObjectName(u"chart0_3")
        self.chart0_3.setMaximumSize(QSize(16777215, 16777215))
        self.chart0_3.setStyleSheet(u"background-color: rgb(0, 10, 0);")

        self.horizontalLayout_68.addWidget(self.chart0_3)

        self.stackedWidget_4.addWidget(self.page0_3)
        self.page1_3 = QWidget()
        self.page1_3.setObjectName(u"page1_3")
        self.horizontalLayout_69 = QHBoxLayout(self.page1_3)
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.chart1_3 = QChartView(self.page1_3)
        self.chart1_3.setObjectName(u"chart1_3")
        self.chart1_3.setStyleSheet(u"background-color: rgb(110, 0, 0);")

        self.horizontalLayout_69.addWidget(self.chart1_3)

        self.stackedWidget_4.addWidget(self.page1_3)
        self.page2_3 = QWidget()
        self.page2_3.setObjectName(u"page2_3")
        self.horizontalLayout_70 = QHBoxLayout(self.page2_3)
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.chart2_3 = QChartView(self.page2_3)
        self.chart2_3.setObjectName(u"chart2_3")
        self.chart2_3.setStyleSheet(u"background-color: rgb(30, 30, 30);")

        self.horizontalLayout_70.addWidget(self.chart2_3)

        self.stackedWidget_4.addWidget(self.page2_3)
        self.page3_3 = QWidget()
        self.page3_3.setObjectName(u"page3_3")
        self.horizontalLayout_71 = QHBoxLayout(self.page3_3)
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.chart3_3 = QChartView(self.page3_3)
        self.chart3_3.setObjectName(u"chart3_3")
        self.chart3_3.setStyleSheet(u"background-color: rgb(85, 255, 0);")

        self.horizontalLayout_71.addWidget(self.chart3_3)

        self.stackedWidget_4.addWidget(self.page3_3)
        self.page4_3 = QWidget()
        self.page4_3.setObjectName(u"page4_3")
        self.horizontalLayout_72 = QHBoxLayout(self.page4_3)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.chart4_3 = QChartView(self.page4_3)
        self.chart4_3.setObjectName(u"chart4_3")
        self.chart4_3.setStyleSheet(u"background-color: rgb(0, 0, 127);")

        self.horizontalLayout_72.addWidget(self.chart4_3)

        self.stackedWidget_4.addWidget(self.page4_3)
        self.page5_3 = QWidget()
        self.page5_3.setObjectName(u"page5_3")
        self.horizontalLayout_73 = QHBoxLayout(self.page5_3)
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.chart5_3 = QChartView(self.page5_3)
        self.chart5_3.setObjectName(u"chart5_3")
        self.chart5_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_73.addWidget(self.chart5_3)

        self.stackedWidget_4.addWidget(self.page5_3)
        self.page6_3 = QWidget()
        self.page6_3.setObjectName(u"page6_3")
        self.horizontalLayout_74 = QHBoxLayout(self.page6_3)
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.chart6_3 = QChartView(self.page6_3)
        self.chart6_3.setObjectName(u"chart6_3")
        self.chart6_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_74.addWidget(self.chart6_3)

        self.stackedWidget_4.addWidget(self.page6_3)
        self.page7_3 = QWidget()
        self.page7_3.setObjectName(u"page7_3")
        self.horizontalLayout_75 = QHBoxLayout(self.page7_3)
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.chart7_3 = QChartView(self.page7_3)
        self.chart7_3.setObjectName(u"chart7_3")
        self.chart7_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_75.addWidget(self.chart7_3)

        self.stackedWidget_4.addWidget(self.page7_3)
        self.page8_3 = QWidget()
        self.page8_3.setObjectName(u"page8_3")
        self.verticalLayout_41 = QVBoxLayout(self.page8_3)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.chart8_3 = QChartView(self.page8_3)
        self.chart8_3.setObjectName(u"chart8_3")
        self.chart8_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.verticalLayout_41.addWidget(self.chart8_3)

        self.stackedWidget_4.addWidget(self.page8_3)
        self.page9_3 = QWidget()
        self.page9_3.setObjectName(u"page9_3")
        self.horizontalLayout_76 = QHBoxLayout(self.page9_3)
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.chart9_3 = QChartView(self.page9_3)
        self.chart9_3.setObjectName(u"chart9_3")
        self.chart9_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_76.addWidget(self.chart9_3)

        self.stackedWidget_4.addWidget(self.page9_3)
        self.page10_3 = QWidget()
        self.page10_3.setObjectName(u"page10_3")
        self.horizontalLayout_77 = QHBoxLayout(self.page10_3)
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.chart10_3 = QChartView(self.page10_3)
        self.chart10_3.setObjectName(u"chart10_3")
        self.chart10_3.setStyleSheet(u"background-color: rgb(0, 0, 0);")

        self.horizontalLayout_77.addWidget(self.chart10_3)

        self.stackedWidget_4.addWidget(self.page10_3)

        self.verticalLayout_30.addWidget(self.stackedWidget_4)

        self.frame_97 = QFrame(self.Analyze_page)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setGeometry(QRect(820, 550, 591, 357))
        self.frame_97.setStyleSheet(u"")
        self.frame_97.setFrameShape(QFrame.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_97)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_98 = QFrame(self.frame_97)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setFrameShape(QFrame.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_107 = QHBoxLayout(self.frame_98)
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.label_242 = QLabel(self.frame_98)
        self.label_242.setObjectName(u"label_242")
        font29 = QFont()
        font29.setFamily(u"Microsoft YaHei UI")
        font29.setPointSize(20)
        font29.setBold(True)
        font29.setWeight(75)
        self.label_242.setFont(font29)
        self.label_242.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_107.addWidget(self.label_242)


        self.verticalLayout_54.addWidget(self.frame_98)

        self.frame_99 = QFrame(self.frame_97)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_108 = QHBoxLayout(self.frame_99)
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.label_243 = QLabel(self.frame_99)
        self.label_243.setObjectName(u"label_243")
        self.label_243.setFont(font5)
        self.label_243.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_108.addWidget(self.label_243)


        self.verticalLayout_54.addWidget(self.frame_99)

        self.frame_100 = QFrame(self.frame_97)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setFrameShape(QFrame.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_109 = QHBoxLayout(self.frame_100)
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.label_246 = QLabel(self.frame_100)
        self.label_246.setObjectName(u"label_246")
        self.label_246.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-help-50.png"))

        self.horizontalLayout_109.addWidget(self.label_246, 0, Qt.AlignHCenter)

        self.rada = QLabel(self.frame_100)
        self.rada.setObjectName(u"rada")
        self.rada.setMinimumSize(QSize(400, 106))
        font30 = QFont()
        font30.setFamily(u"Microsoft YaHei UI")
        font30.setPointSize(11)
        font30.setBold(True)
        font30.setWeight(75)
        self.rada.setFont(font30)
        self.rada.setWordWrap(True)

        self.horizontalLayout_109.addWidget(self.rada)


        self.verticalLayout_54.addWidget(self.frame_100)

        self.frame_101 = QFrame(self.frame_97)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setFrameShape(QFrame.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_110 = QHBoxLayout(self.frame_101)
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.label_248 = QLabel(self.frame_101)
        self.label_248.setObjectName(u"label_248")
        self.label_248.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-creativity-and-resourcefulness-50.png"))

        self.horizontalLayout_110.addWidget(self.label_248, 0, Qt.AlignHCenter)

        self.mysl = QLabel(self.frame_101)
        self.mysl.setObjectName(u"mysl")
        self.mysl.setMinimumSize(QSize(400, 0))
        font31 = QFont()
        font31.setFamily(u"Microsoft YaHei UI")
        font31.setPointSize(12)
        font31.setBold(False)
        font31.setItalic(True)
        font31.setWeight(50)
        self.mysl.setFont(font31)
        self.mysl.setWordWrap(True)

        self.horizontalLayout_110.addWidget(self.mysl)


        self.verticalLayout_54.addWidget(self.frame_101)

        self.Autor = QLabel(self.frame_97)
        self.Autor.setObjectName(u"Autor")
        self.Autor.setMinimumSize(QSize(150, 0))
        font32 = QFont()
        font32.setPointSize(11)
        self.Autor.setFont(font32)
        self.Autor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_54.addWidget(self.Autor, 0, Qt.AlignRight)

        self.line_8 = QFrame(self.Analyze_page)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(120, 510, 1301, 3))
        self.line_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)
        self.line_9 = QFrame(self.Analyze_page)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(803, 514, 5, 405))
        self.line_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)
        self.stackedWidget.addWidget(self.Analyze_page)
        self.Info_page = QWidget()
        self.Info_page.setObjectName(u"Info_page")
        self.Info_page.setStyleSheet(u"background-color:transparent;\n"
"background-repeat: no-repeat;\n"
"color: rgb(255, 255, 255);")
        self.horizontalLayout_88 = QHBoxLayout(self.Info_page)
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.frame_27 = QFrame(self.Info_page)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_27)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.frame_27)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_4)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_59 = QLabel(self.frame_4)
        self.label_59.setObjectName(u"label_59")
        font33 = QFont()
        font33.setPointSize(20)
        font33.setBold(True)
        font33.setWeight(75)
        self.label_59.setFont(font33)

        self.verticalLayout_12.addWidget(self.label_59, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_4)

        self.frame_28 = QFrame(self.frame_27)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_15 = QLabel(self.frame_28)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(225, 16777215))
        self.label_15.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Obraz1.png"))
        self.label_15.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_15, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_56 = QLabel(self.frame_28)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_56.setWordWrap(True)

        self.horizontalLayout_29.addWidget(self.label_56, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_28)

        self.frame_31 = QFrame(self.frame_27)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_31)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_60 = QLabel(self.frame_31)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font33)

        self.verticalLayout_10.addWidget(self.label_60)


        self.verticalLayout_2.addWidget(self.frame_31)

        self.frame_29 = QFrame(self.frame_27)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_16 = QLabel(self.frame_29)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(225, 16777215))
        self.label_16.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Obraz2.png"))
        self.label_16.setScaledContents(True)

        self.horizontalLayout_28.addWidget(self.label_16, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_57 = QLabel(self.frame_29)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_57.setWordWrap(True)

        self.horizontalLayout_28.addWidget(self.label_57, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_29)

        self.frame_32 = QFrame(self.frame_27)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_32)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_61 = QLabel(self.frame_32)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font33)

        self.verticalLayout_11.addWidget(self.label_61, 0, Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.frame_32)

        self.frame_30 = QFrame(self.frame_27)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_17 = QLabel(self.frame_30)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(225, 16777215))
        self.label_17.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Obraz3.png"))
        self.label_17.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.label_17, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_58 = QLabel(self.frame_30)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"font: 75 9pt \"MS Shell Dlg 2\";")
        self.label_58.setWordWrap(True)

        self.horizontalLayout_4.addWidget(self.label_58, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_30)


        self.horizontalLayout_88.addWidget(self.frame_27)

        self.frame_73 = QFrame(self.Info_page)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_73)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_190 = QLabel(self.frame_73)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setFont(font33)

        self.verticalLayout_46.addWidget(self.label_190, 0, Qt.AlignHCenter)

        self.label_195 = QLabel(self.frame_73)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_195, 0, Qt.AlignHCenter)

        self.Khamisi = QFrame(self.frame_73)
        self.Khamisi.setObjectName(u"Khamisi")
        self.Khamisi.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.Khamisi.setFrameShape(QFrame.StyledPanel)
        self.Khamisi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.Khamisi)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_191 = QLabel(self.Khamisi)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setMaximumSize(QSize(50, 150))
        self.label_191.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/Zrzut ekranu 2023-12-17 180557.png"))
        self.label_191.setScaledContents(True)

        self.horizontalLayout_32.addWidget(self.label_191)

        self.frame_75 = QFrame(self.Khamisi)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_75.setFrameShape(QFrame.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_75)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_77 = QFrame(self.frame_75)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_77.setFrameShape(QFrame.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_77)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_193 = QLabel(self.frame_77)
        self.label_193.setObjectName(u"label_193")
        font34 = QFont()
        font34.setFamily(u"Berlin Sans FB")
        font34.setPointSize(10)
        self.label_193.setFont(font34)
        self.label_193.setStyleSheet(u"QLabel::hover{\n"
"	color: rgb(85, 255, 255);\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.verticalLayout_47.addWidget(self.label_193, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_77)

        self.frame_79 = QFrame(self.frame_75)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_79.setFrameShape(QFrame.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_84 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_194 = QLabel(self.frame_79)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setFont(font34)
        self.label_194.setStyleSheet(u"QLabel::hover{\n"
"	color: rgb(85, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.horizontalLayout_84.addWidget(self.label_194, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_79)

        self.frame_78 = QFrame(self.frame_75)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_78.setFrameShape(QFrame.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_78)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.label_192 = QLabel(self.frame_78)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setFont(font34)
        self.label_192.setStyleSheet(u"QLabel::hover{\n"
"	color: rgb(85, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.verticalLayout_48.addWidget(self.label_192, 0, Qt.AlignHCenter)


        self.verticalLayout_9.addWidget(self.frame_78)


        self.horizontalLayout_32.addWidget(self.frame_75)


        self.verticalLayout_46.addWidget(self.Khamisi)

        self.label_200 = QLabel(self.frame_73)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_200, 0, Qt.AlignHCenter)

        self.Khamisi_2 = QFrame(self.frame_73)
        self.Khamisi_2.setObjectName(u"Khamisi_2")
        self.Khamisi_2.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.Khamisi_2.setFrameShape(QFrame.StyledPanel)
        self.Khamisi_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_89 = QHBoxLayout(self.Khamisi_2)
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.label_196 = QLabel(self.Khamisi_2)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setMaximumSize(QSize(64, 64))
        self.label_196.setFrameShape(QFrame.Panel)
        self.label_196.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-vr-glasses-64.png"))

        self.horizontalLayout_89.addWidget(self.label_196)

        self.frame_76 = QFrame(self.Khamisi_2)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.frame_76)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_197 = QLabel(self.frame_76)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setFont(font34)
        self.label_197.setStyleSheet(u"QLabel::hover{\n"
"	color: rgb(85, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.verticalLayout_49.addWidget(self.label_197, 0, Qt.AlignHCenter)


        self.horizontalLayout_89.addWidget(self.frame_76)


        self.verticalLayout_46.addWidget(self.Khamisi_2)

        self.label_201 = QLabel(self.frame_73)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_201, 0, Qt.AlignHCenter)

        self.Khamisi_3 = QFrame(self.frame_73)
        self.Khamisi_3.setObjectName(u"Khamisi_3")
        self.Khamisi_3.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.Khamisi_3.setFrameShape(QFrame.StyledPanel)
        self.Khamisi_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_86 = QHBoxLayout(self.Khamisi_3)
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_199 = QLabel(self.Khamisi_3)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setMaximumSize(QSize(70, 90))
        self.label_199.setFrameShape(QFrame.Panel)
        self.label_199.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/godlo_wat.png"))
        self.label_199.setScaledContents(True)

        self.horizontalLayout_86.addWidget(self.label_199)

        self.label_198 = QLabel(self.Khamisi_3)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setFont(font34)
        self.label_198.setStyleSheet(u"QLabel::hover{\n"
"	color: rgb(85, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.horizontalLayout_86.addWidget(self.label_198, 0, Qt.AlignHCenter)


        self.verticalLayout_46.addWidget(self.Khamisi_3)

        self.label_204 = QLabel(self.frame_73)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_204, 0, Qt.AlignHCenter)

        self.Khamisi_4 = QFrame(self.frame_73)
        self.Khamisi_4.setObjectName(u"Khamisi_4")
        self.Khamisi_4.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.Khamisi_4.setFrameShape(QFrame.StyledPanel)
        self.Khamisi_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_85 = QHBoxLayout(self.Khamisi_4)
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.label_203 = QLabel(self.Khamisi_4)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setMaximumSize(QSize(70, 70))
        self.label_203.setFrameShape(QFrame.Panel)
        self.label_203.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/wml.png"))
        self.label_203.setScaledContents(True)

        self.horizontalLayout_85.addWidget(self.label_203)

        self.frame_74 = QFrame(self.Khamisi_4)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame_74.setFrameShape(QFrame.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_74)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_202 = QLabel(self.frame_74)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setFont(font34)
        self.label_202.setStyleSheet(u"QLabel::hover{\n"
"	color: rgb(85, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.verticalLayout_50.addWidget(self.label_202, 0, Qt.AlignHCenter)


        self.horizontalLayout_85.addWidget(self.frame_74)


        self.verticalLayout_46.addWidget(self.Khamisi_4)

        self.label_207 = QLabel(self.frame_73)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setFont(font3)

        self.verticalLayout_46.addWidget(self.label_207, 0, Qt.AlignHCenter)

        self.Khamisi_5 = QFrame(self.frame_73)
        self.Khamisi_5.setObjectName(u"Khamisi_5")
        self.Khamisi_5.setStyleSheet(u"QFrame::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"border-radius:40px;\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.Khamisi_5.setFrameShape(QFrame.StyledPanel)
        self.Khamisi_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_87 = QHBoxLayout(self.Khamisi_5)
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_205 = QLabel(self.Khamisi_5)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setMaximumSize(QSize(70, 90))
        self.label_205.setFrameShape(QFrame.Panel)
        self.label_205.setPixmap(QPixmap(u":/Zdjecia/Zdjecia/github.png"))
        self.label_205.setScaledContents(True)

        self.horizontalLayout_87.addWidget(self.label_205)

        self.label_206 = QLabel(self.Khamisi_5)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setFont(font34)
        self.label_206.setStyleSheet(u"QLabel::hover{\n"
"	color: rgb(85, 255, 255);\n"
"	\n"
"	background-color: rgb(0, 85, 255);\n"
"\n"
"}")

        self.horizontalLayout_87.addWidget(self.label_206, 0, Qt.AlignHCenter)


        self.verticalLayout_46.addWidget(self.Khamisi_5)


        self.horizontalLayout_88.addWidget(self.frame_73)

        self.stackedWidget.addWidget(self.Info_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame_6 = QFrame(self.main_body)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame\n"
"{\n"
"	background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(1, 5, 44, 255), stop:1 rgba(16, 14, 27, 255));\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label_11)

        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setMaximumSize(QSize(10, 10))
        self.frame_8.setStyleSheet(u"border-image: url(:/icons/Icons/Magisterka_python(1)/icons8-page-size-50.png);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_30.addWidget(self.frame_8)


        self.verticalLayout.addWidget(self.frame_6)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Analiza_button.pressed.connect(self.Analiza_frame.repaint)

        self.Analiza_button.setDefault(False)
        self.stackedWidget.setCurrentIndex(6)
        self.stackedWidget_mapy.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.stackedWidget_4.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.frame_3.setToolTip(QCoreApplication.translate("MainWindow", u"W\u0142\u0105cz AirSim w celu badania zdolno\u015bci manualnych", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Run_AirSim.setToolTip(QCoreApplication.translate("MainWindow", u"W\u0142\u0105cz AirSim w celu badania zdolno\u015bci manualnych", None))
#endif // QT_CONFIG(tooltip)
        self.Run_AirSim.setText("")
#if QT_CONFIG(tooltip)
        self.Home_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Strona startowa", None))
#endif // QT_CONFIG(tooltip)
        self.Home_button.setText("")
        self.Home.setText(QCoreApplication.translate("MainWindow", u"Strona startowa", None))
#if QT_CONFIG(tooltip)
        self.VR_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Pulpit sterowania badaniem w VR", None))
#endif // QT_CONFIG(tooltip)
        self.VR_Button.setText("")
        self.VR.setText(QCoreApplication.translate("MainWindow", u"Badanie VR", None))
#if QT_CONFIG(tooltip)
        self.Settings_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
#endif // QT_CONFIG(tooltip)
        self.Settings_button.setText("")
        self.Settings.setText(QCoreApplication.translate("MainWindow", u"Ustawienia", None))
#if QT_CONFIG(tooltip)
        self.Parametry_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Parametry Drona ", None))
#endif // QT_CONFIG(tooltip)
        self.Parametry_button.setText("")
        self.Parametry.setText(QCoreApplication.translate("MainWindow", u"Parametry", None))
#if QT_CONFIG(tooltip)
        self.Przewodnik_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Opis programu", None))
#endif // QT_CONFIG(tooltip)
        self.Przewodnik_button.setText("")
        self.Przewodnik.setText(QCoreApplication.translate("MainWindow", u"Przewodnik", None))
#if QT_CONFIG(tooltip)
        self.Misje_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Wykresy", None))
#endif // QT_CONFIG(tooltip)
        self.Misje_button.setText("")
        self.Misje.setText(QCoreApplication.translate("MainWindow", u"Wykresy", None))
#if QT_CONFIG(tooltip)
        self.Analiza_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Analiza danych biometrycznych", None))
#endif // QT_CONFIG(tooltip)
        self.Analiza_button.setText("")
        self.Analiza.setText(QCoreApplication.translate("MainWindow", u"Analiza", None))
#if QT_CONFIG(tooltip)
        self.Informacje_frame.setToolTip(QCoreApplication.translate("MainWindow", u"Informacje o projekcie", None))
#endif // QT_CONFIG(tooltip)
        self.Informacje_button.setText("")
        self.Informacje.setText(QCoreApplication.translate("MainWindow", u"Informacje", None))
#if QT_CONFIG(tooltip)
        self.Menu_button.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Menu_button.setText("")
#if QT_CONFIG(tooltip)
        self.Clear_button.setToolTip(QCoreApplication.translate("MainWindow", u"Zamknij poprzednie instancje ", None))
#endif // QT_CONFIG(tooltip)
        self.Clear_button.setText("")
#if QT_CONFIG(tooltip)
        self.Camera_button.setToolTip(QCoreApplication.translate("MainWindow", u"Podgl\u0105d kamerki u\u017cywanej do badania rozpoznania emocji", None))
#endif // QT_CONFIG(tooltip)
        self.Camera_button.setText("")
#if QT_CONFIG(tooltip)
        self.Min.setToolTip(QCoreApplication.translate("MainWindow", u"Zminimalizuj", None))
#endif // QT_CONFIG(tooltip)
        self.Min.setText("")
        self.Max.setText("")
#if QT_CONFIG(tooltip)
        self.Close.setToolTip(QCoreApplication.translate("MainWindow", u"Zamknij ", None))
#endif // QT_CONFIG(tooltip)
        self.Close.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Wybierz jedn\u0105 z poni\u017cszych map", None))
        self.Btn_Blocks.setText("")
        self.Title_Blocks.setText(QCoreApplication.translate("MainWindow", u"Blocks", None))
        self.Opis_Blocks.setText(QCoreApplication.translate("MainWindow", u"Bazowa mapa udost\u0119pniana przez AirSim przy instalacji. Wydajna lecz bardzo skromna graficznie.", None))
#if QT_CONFIG(tooltip)
        self.Zdj_Blocks.setToolTip(QCoreApplication.translate("MainWindow", u"Blocks", None))
#endif // QT_CONFIG(tooltip)
        self.Zdj_Blocks.setText("")
        self.Btn_Aband.setText("")
        self.Title_Aband.setText(QCoreApplication.translate("MainWindow", u"Abandoned Park", None))
        self.Opis_Aband.setText(QCoreApplication.translate("MainWindow", u"Bardzo \u0142adna mapa, lecz wyst\u0119puj\u0105 problemy z jej instalacj\u0105, do celu projektu niezalecana.", None))
#if QT_CONFIG(tooltip)
        self.Zdj_Aband.setToolTip(QCoreApplication.translate("MainWindow", u"Abandoned Park", None))
#endif // QT_CONFIG(tooltip)
        self.Zdj_Aband.setText("")
        self.btn_ZJ.setText("")
        self.Title_ZJ.setText(QCoreApplication.translate("MainWindow", u"ZhangJiajie", None))
        self.Opis_ZJ.setText(QCoreApplication.translate("MainWindow", u"\u0141adna mapa, lecz niewydajna i niezalecana do celu projektu. ", None))
#if QT_CONFIG(tooltip)
        self.Zdj_ZJ.setToolTip(QCoreApplication.translate("MainWindow", u"ZhangJiajie", None))
#endif // QT_CONFIG(tooltip)
        self.Zdj_ZJ.setText("")
        self.btn_MSBuild.setText("")
        self.Title_MSBuild.setText(QCoreApplication.translate("MainWindow", u"MSBuild", None))
        self.Opis_MSBuild.setText(QCoreApplication.translate("MainWindow", u"Prosta mapa, dzia\u0142a p\u0142ynnie.", None))
#if QT_CONFIG(tooltip)
        self.Zdj_MSBuild.setToolTip(QCoreApplication.translate("MainWindow", u"MSBuild", None))
#endif // QT_CONFIG(tooltip)
        self.Zdj_MSBuild.setText("")
        self.Btn_Land.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Landscape Mountains", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"G\u00f3rski krajobraz, mog\u0105cy mie\u0107 zastosowanie w celu oceny orientacji przestrzennej.", None))
#if QT_CONFIG(tooltip)
        self.label_26.setToolTip(QCoreApplication.translate("MainWindow", u"Landscape Mountains", None))
#endif // QT_CONFIG(tooltip)
        self.label_26.setText("")
        self.Btn_AirSimNH.setText("")
        self.Title_AirSimNH.setText(QCoreApplication.translate("MainWindow", u"Neighbourhood", None))
        self.Opis_AirSimNH.setText(QCoreApplication.translate("MainWindow", u"Zalecana mapa, wi\u0119kszo\u015b\u0107 zada\u0144 badawczych zosta\u0142a wykonana z przeznaczeniem na t\u0105 map\u0119. ", None))
#if QT_CONFIG(tooltip)
        self.Zdj_AirSimNH.setToolTip(QCoreApplication.translate("MainWindow", u"AirSimNH", None))
#endif // QT_CONFIG(tooltip)
        self.Zdj_AirSimNH.setText("")
        self.Btn_Africa.setText("")
        self.Title_Africa.setText(QCoreApplication.translate("MainWindow", u"Africa", None))
        self.Opis_Africa.setText(QCoreApplication.translate("MainWindow", u"Bardzo bogata graficznie ale bardzo zasoboch\u0142onna, niezalecana do projektu. ", None))
#if QT_CONFIG(tooltip)
        self.Zdj_Africa.setToolTip(QCoreApplication.translate("MainWindow", u"Africa", None))
#endif // QT_CONFIG(tooltip)
        self.Zdj_Africa.setText("")
        self.label_237.setText(QCoreApplication.translate("MainWindow", u"Wyb\u00f3r portu czujnika t\u0119tna:", None))
        self.label_238.setText(QCoreApplication.translate("MainWindow", u"Numer portu", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"COM0", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"COM1", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"COM2", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", u"COM3", None))
        self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", u"COM4", None))
        self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", u"COM5", None))
        self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", u"COM6", None))
        self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", u"COM7", None))
        self.comboBox_4.setItemText(8, QCoreApplication.translate("MainWindow", u"COM8", None))
        self.comboBox_4.setItemText(9, QCoreApplication.translate("MainWindow", u"COM9", None))
        self.comboBox_4.setItemText(10, QCoreApplication.translate("MainWindow", u"COM10", None))
        self.comboBox_4.setItemText(11, QCoreApplication.translate("MainWindow", u"COM11", None))
        self.comboBox_4.setItemText(12, QCoreApplication.translate("MainWindow", u"COM12", None))
        self.comboBox_4.setItemText(13, QCoreApplication.translate("MainWindow", u"COM13", None))
        self.comboBox_4.setItemText(14, QCoreApplication.translate("MainWindow", u"COM14", None))
        self.comboBox_4.setItemText(15, QCoreApplication.translate("MainWindow", u"COM15", None))
        self.comboBox_4.setItemText(16, QCoreApplication.translate("MainWindow", u"COM16", None))
        self.comboBox_4.setItemText(17, QCoreApplication.translate("MainWindow", u"COM17", None))
        self.comboBox_4.setItemText(18, QCoreApplication.translate("MainWindow", u"COM18", None))
        self.comboBox_4.setItemText(19, QCoreApplication.translate("MainWindow", u"COM19", None))
        self.comboBox_4.setItemText(20, QCoreApplication.translate("MainWindow", u"COM20", None))
        self.comboBox_4.setItemText(21, QCoreApplication.translate("MainWindow", u"COM21", None))
        self.comboBox_4.setItemText(22, QCoreApplication.translate("MainWindow", u"COM22", None))
        self.comboBox_4.setItemText(23, QCoreApplication.translate("MainWindow", u"COM23", None))
        self.comboBox_4.setItemText(24, QCoreApplication.translate("MainWindow", u"COM24", None))
        self.comboBox_4.setItemText(25, QCoreApplication.translate("MainWindow", u"COM25", None))
        self.comboBox_4.setItemText(26, QCoreApplication.translate("MainWindow", u"COM26", None))
        self.comboBox_4.setItemText(27, QCoreApplication.translate("MainWindow", u"COM27", None))
        self.comboBox_4.setItemText(28, QCoreApplication.translate("MainWindow", u"COM28", None))
        self.comboBox_4.setItemText(29, QCoreApplication.translate("MainWindow", u"COM29", None))
        self.comboBox_4.setItemText(30, QCoreApplication.translate("MainWindow", u"COM30", None))

        self.label_239.setText(QCoreApplication.translate("MainWindow", u"Baudrate ", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainWindow", u"75", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"110", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"134", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainWindow", u"150", None))
        self.comboBox_5.setItemText(4, QCoreApplication.translate("MainWindow", u"300", None))
        self.comboBox_5.setItemText(5, QCoreApplication.translate("MainWindow", u"600", None))
        self.comboBox_5.setItemText(6, QCoreApplication.translate("MainWindow", u"1200", None))
        self.comboBox_5.setItemText(7, QCoreApplication.translate("MainWindow", u"1800", None))
        self.comboBox_5.setItemText(8, QCoreApplication.translate("MainWindow", u"2400", None))
        self.comboBox_5.setItemText(9, QCoreApplication.translate("MainWindow", u"4800", None))
        self.comboBox_5.setItemText(10, QCoreApplication.translate("MainWindow", u"7200", None))
        self.comboBox_5.setItemText(11, QCoreApplication.translate("MainWindow", u"9600", None))
        self.comboBox_5.setItemText(12, QCoreApplication.translate("MainWindow", u"14400", None))
        self.comboBox_5.setItemText(13, QCoreApplication.translate("MainWindow", u"19200", None))
        self.comboBox_5.setItemText(14, QCoreApplication.translate("MainWindow", u"38400", None))
        self.comboBox_5.setItemText(15, QCoreApplication.translate("MainWindow", u"57600", None))
        self.comboBox_5.setItemText(16, QCoreApplication.translate("MainWindow", u"115200", None))
        self.comboBox_5.setItemText(17, QCoreApplication.translate("MainWindow", u"128000", None))

        self.label_244.setText(QCoreApplication.translate("MainWindow", u"Wyb\u00f3r numeru kamerki", None))
        self.label_241.setText(QCoreApplication.translate("MainWindow", u"Indeks kamerki", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"0", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainWindow", u"3", None))
        self.comboBox_6.setItemText(4, QCoreApplication.translate("MainWindow", u"4", None))
        self.comboBox_6.setItemText(5, QCoreApplication.translate("MainWindow", u"5", None))
        self.comboBox_6.setItemText(6, QCoreApplication.translate("MainWindow", u"6", None))
        self.comboBox_6.setItemText(7, QCoreApplication.translate("MainWindow", u"7", None))
        self.comboBox_6.setItemText(8, QCoreApplication.translate("MainWindow", u"8", None))
        self.comboBox_6.setItemText(9, QCoreApplication.translate("MainWindow", u"9", None))
        self.comboBox_6.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Rozdzielczo\u015b\u0107 AIRSIM:", None))
        self.x1920_btn.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"1920x1080", None))
        self.x1680x1050_btn.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"1680x1050", None))
        self.x1200x800_btn.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"1200x800", None))
        self.x1600x900_btn.setText("")
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"1600x900", None))
        self.x1366x768_btn.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"1366x768", None))
        self.x1440x900_btn.setText("")
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"1440x900", None))
        self.x1024x720_btn.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"1024x720", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Stopnie", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Stopnie", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Ud/min", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sekundy", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Stopnie", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Pozycja X", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Pozycja Y", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Wysoko\u015b\u0107", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107 X", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107 Y", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107 Z", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Przechylenie", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pochylenie", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Odchylenie", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Czas", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"T\u0119tno", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Emocja", None))
        self.WynikMisji_obraz.setText("")
        self.WynikMisji_podpis.setText(QCoreApplication.translate("MainWindow", u"Gratulacje! Misja zako\u0144czona powodzeniem!", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Czas [s]", None))
#if QT_CONFIG(tooltip)
        self.widget_3.setToolTip(QCoreApplication.translate("MainWindow", u"Pozosta\u0142y czas na wykonanie misji", None))
#endif // QT_CONFIG(tooltip)
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Wysoko\u015b\u0107 [m]", None))
#if QT_CONFIG(tooltip)
        self.widget_2.setToolTip(QCoreApplication.translate("MainWindow", u"Wska\u017anik wysoko\u015bci ", None))
#endif // QT_CONFIG(tooltip)
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107 [m/s]", None))
#if QT_CONFIG(tooltip)
        self.widget.setToolTip(QCoreApplication.translate("MainWindow", u"Wska\u017anik pr\u0119dko\u015bci ", None))
#endif // QT_CONFIG(tooltip)
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Tre\u015b\u0107 misji ", None))
        ___qtablewidgetitem = self.Misje_male.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Tre\u015b\u0107 misji ", None));
        ___qtablewidgetitem1 = self.Misje_male.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Margines b\u0142\u0119du", None));
        ___qtablewidgetitem2 = self.Misje_male.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Przewidziany czas", None));
        ___qtablewidgetitem3 = self.Misje_male.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Wynik", None));
        ___qtablewidgetitem4 = self.Misje_male.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Poziom 1 ", None));
        ___qtablewidgetitem5 = self.Misje_male.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Poziom 2", None));
        ___qtablewidgetitem6 = self.Misje_male.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Poziom 3", None));
        ___qtablewidgetitem7 = self.Misje_male.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Poziom 4", None));
        ___qtablewidgetitem8 = self.Misje_male.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Poziom 5", None));
        ___qtablewidgetitem9 = self.Misje_male.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Poziom 6", None));
        ___qtablewidgetitem10 = self.Misje_male.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Poziom 7", None));
        ___qtablewidgetitem11 = self.Misje_male.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Poziom 8", None));
        ___qtablewidgetitem12 = self.Misje_male.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Poziom 9", None));
        ___qtablewidgetitem13 = self.Misje_male.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Poziom 10 ", None));

        __sortingEnabled = self.Misje_male.isSortingEnabled()
        self.Misje_male.setSortingEnabled(False)
        ___qtablewidgetitem14 = self.Misje_male.item(0, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Pole\u0107 na wsp\u00f3\u0142rz\u0119dne (30,-30)", None));
        ___qtablewidgetitem15 = self.Misje_male.item(0, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"+-(10,10)", None));
        ___qtablewidgetitem16 = self.Misje_male.item(0, 2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem17 = self.Misje_male.item(0, 3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem18 = self.Misje_male.item(1, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"B\u0119d\u0105c w pu\u0142apie wysoko\u015bci (20,25) pole\u0107 na wsp\u00f3\u0142rz\u0119dne (-15,15)", None));
        ___qtablewidgetitem19 = self.Misje_male.item(1, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"H=2.5m, +-(5,5)", None));
        ___qtablewidgetitem20 = self.Misje_male.item(1, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem21 = self.Misje_male.item(1, 3)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem22 = self.Misje_male.item(2, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Wyl\u0105duj we wsp\u00f3\u0142rz\u0119dnych (10,10) ", None));
        ___qtablewidgetitem23 = self.Misje_male.item(2, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"+-(5,5)", None));
        ___qtablewidgetitem24 = self.Misje_male.item(2, 2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem25 = self.Misje_male.item(2, 3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem26 = self.Misje_male.item(3, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Pole\u0107 na wsp\u00f3\u0142rz\u0119dne (30,30) i osi\u0105gnij wysoko\u015b\u0107 50 metr\u00f3w", None));
        ___qtablewidgetitem27 = self.Misje_male.item(3, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"H=2.5m +-(5,5)", None));
        ___qtablewidgetitem28 = self.Misje_male.item(3, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem29 = self.Misje_male.item(3, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem30 = self.Misje_male.item(4, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Pole\u0107 na wsp\u00f3\u0142rz\u0119dne (-20,-20) osi\u0105gaj\u0105c pr\u0119dko\u015b\u0107 20 wez\u0142\u00f3w/s", None));
        ___qtablewidgetitem31 = self.Misje_male.item(4, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"+-(10,10)", None));
        ___qtablewidgetitem32 = self.Misje_male.item(4, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem33 = self.Misje_male.item(4, 3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem34 = self.Misje_male.item(5, 0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Wyl\u0105duj we wsp\u00f3\u0142rz\u0119dnych (0,0)", None));
        ___qtablewidgetitem35 = self.Misje_male.item(5, 1)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"+-(2.5,2.5)", None));
        ___qtablewidgetitem36 = self.Misje_male.item(5, 2)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"20s", None));
        ___qtablewidgetitem37 = self.Misje_male.item(5, 3)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem38 = self.Misje_male.item(6, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Pole\u0107 na wsp\u00f3\u0142rz\u0119dne (15,15) {wiatr 2m/s)", None));
        ___qtablewidgetitem39 = self.Misje_male.item(6, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"+-(10,10)", None));
        ___qtablewidgetitem40 = self.Misje_male.item(6, 2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem41 = self.Misje_male.item(6, 3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem42 = self.Misje_male.item(7, 0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Pole\u0107 na wsp\u00f3\u0142rz\u0119dne (-10,-10) i zawi\u015bnij w pu\u0142apie (15,20) {wiatr 2w\u0119z\u0142\u00f3w/s)", None));
        ___qtablewidgetitem43 = self.Misje_male.item(7, 1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"+-(5,5)", None));
        ___qtablewidgetitem44 = self.Misje_male.item(7, 2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem45 = self.Misje_male.item(7, 3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem46 = self.Misje_male.item(8, 0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Pole\u0107 na wsp\u00f3\u0142rz\u0119dne (-45,-20) nie przekraczaj\u0105c wysoko\u015bci 20 {wiatr 5 w\u0119z\u0142\u00f3w/s)", None));
        ___qtablewidgetitem47 = self.Misje_male.item(8, 1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"+-(5,5)", None));
        ___qtablewidgetitem48 = self.Misje_male.item(8, 2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem49 = self.Misje_male.item(8, 3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        ___qtablewidgetitem50 = self.Misje_male.item(9, 0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Wyl\u0105duj we wsp\u00f3\u0142rz\u0119dnych (0,0) {wiatr 7.5 w\u0119z\u0142\u00f3w/s}", None));
        ___qtablewidgetitem51 = self.Misje_male.item(9, 1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"+-(4,4)", None));
        ___qtablewidgetitem52 = self.Misje_male.item(9, 2)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"30s", None));
        ___qtablewidgetitem53 = self.Misje_male.item(9, 3)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Niezaliczona", None));
        self.Misje_male.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.Misje_male.setToolTip(QCoreApplication.translate("MainWindow", u"Misje", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Misje_Button.setToolTip(QCoreApplication.translate("MainWindow", u"Rozpocznij badanie zdolno\u015bci manualnych", None))
#endif // QT_CONFIG(tooltip)
        self.Misje_Button.setText(QCoreApplication.translate("MainWindow", u"     Czas na misje!", None))
#if QT_CONFIG(tooltip)
        self.Wykresy.setToolTip(QCoreApplication.translate("MainWindow", u"Wygeneruj wykresy i przekieruj do nich", None))
#endif // QT_CONFIG(tooltip)
        self.Wykresy.setText(QCoreApplication.translate("MainWindow", u"    Wygeneruj wykresy", None))
#if QT_CONFIG(tooltip)
        self.VR_wspolne.setToolTip(QCoreApplication.translate("MainWindow", u"Wygeneruj wykresy i przekieruj do nich", None))
#endif // QT_CONFIG(tooltip)
        self.VR_wspolne.setText(QCoreApplication.translate("MainWindow", u"Przejd\u017a do badania VR", None))
#if QT_CONFIG(tooltip)
        self.Save.setToolTip(QCoreApplication.translate("MainWindow", u"Zapisz dane do pliku ", None))
#endif // QT_CONFIG(tooltip)
        self.Save.setText(QCoreApplication.translate("MainWindow", u"      Zapisz dane do pliku ", None))
        self.label_70.setText("")
#if QT_CONFIG(tooltip)
        self.frame_42.setToolTip(QCoreApplication.translate("MainWindow", u"Przypisanie poszczeg\u00f3lnych klawiszy", None))
#endif // QT_CONFIG(tooltip)
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Sterowanie", None))
        self.pushButton_12.setText("")
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Pomoc", None))
        self.label_120.setText(QCoreApplication.translate("MainWindow", u"F10", None))
        self.label_121.setText(QCoreApplication.translate("MainWindow", u"Opcje pogody", None))
        self.label_122.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.label_123.setText(QCoreApplication.translate("MainWindow", u"Widok FPV", None))
        self.label_124.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_125.setText(QCoreApplication.translate("MainWindow", u"Widok \"Le\u0107 ze mn\u0105\"", None))
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"\\", None))
        self.label_127.setText(QCoreApplication.translate("MainWindow", u"Widok \"obserwator naziemny\"", None))
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_129.setText(QCoreApplication.translate("MainWindow", u"Widok \"Zza drona\"", None))
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_131.setText(QCoreApplication.translate("MainWindow", u"R\u0119czne sterowanie kamer\u0105 ", None))
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_133.setText(QCoreApplication.translate("MainWindow", u"W\u0142\u0105cz nagrywanie", None))
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.label_135.setText(QCoreApplication.translate("MainWindow", u"Pokazywanie toru trasy ", None))
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"Backspace", None))
        self.label_137.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
#if QT_CONFIG(tooltip)
        self.label_71.setToolTip(QCoreApplication.translate("MainWindow", u"Sterowanie kontrolerem ", None))
#endif // QT_CONFIG(tooltip)
        self.label_71.setText("")
#if QT_CONFIG(tooltip)
        self.frame_45.setToolTip(QCoreApplication.translate("MainWindow", u"Twoja obecna emocja odczytana z kamerki ", None))
#endif // QT_CONFIG(tooltip)
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"Twoja emocja", None))
        self.label_142.setText("")
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"Zdenerwowany", None))
        self.emocje_LED.setText("")
#if QT_CONFIG(tooltip)
        self.frame_46.setToolTip(QCoreApplication.translate("MainWindow", u"Twoje obecne t\u0119tno ", None))
#endif // QT_CONFIG(tooltip)
        self.label_139.setText(QCoreApplication.translate("MainWindow", u"Twoje t\u0119tno", None))
        self.label_143.setText("")
        self.label_141.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tetno_LED.setText("")
#if QT_CONFIG(tooltip)
        self.VR_landscape.setToolTip(QCoreApplication.translate("MainWindow", u"Landscape Mountains", None))
#endif // QT_CONFIG(tooltip)
        self.VR_landscape.setText("")
#if QT_CONFIG(tooltip)
        self.VR_abandoned.setToolTip(QCoreApplication.translate("MainWindow", u"Abandoned Park", None))
#endif // QT_CONFIG(tooltip)
        self.VR_abandoned.setText("")
#if QT_CONFIG(tooltip)
        self.VR_africa.setToolTip(QCoreApplication.translate("MainWindow", u"Africa", None))
#endif // QT_CONFIG(tooltip)
        self.VR_africa.setText("")
#if QT_CONFIG(tooltip)
        self.VR_MSBuild.setToolTip(QCoreApplication.translate("MainWindow", u"MSBuild2018", None))
#endif // QT_CONFIG(tooltip)
        self.VR_MSBuild.setText("")
#if QT_CONFIG(tooltip)
        self.VR_AirSimNH.setToolTip(QCoreApplication.translate("MainWindow", u"AirSimNH", None))
#endif // QT_CONFIG(tooltip)
        self.VR_AirSimNH.setText("")
#if QT_CONFIG(tooltip)
        self.VR_blocks.setToolTip(QCoreApplication.translate("MainWindow", u"Blocks", None))
#endif // QT_CONFIG(tooltip)
        self.VR_blocks.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Wyb\u00f3r mapy VR", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Aktualnie wybrana mapa:", None))
#if QT_CONFIG(tooltip)
        self.Wykresy_2.setToolTip(QCoreApplication.translate("MainWindow", u"Tworzy i przekierowywuje do okna wykres\u00f3w", None))
#endif // QT_CONFIG(tooltip)
        self.Wykresy_2.setText(QCoreApplication.translate("MainWindow", u"    Wygeneruj wykresy", None))
#if QT_CONFIG(tooltip)
        self.Save_2.setToolTip(QCoreApplication.translate("MainWindow", u"Oce\u0144 predyspozycje ", None))
#endif // QT_CONFIG(tooltip)
        self.Save_2.setText(QCoreApplication.translate("MainWindow", u"Dokonaj oceny", None))
#if QT_CONFIG(tooltip)
        self.VR_start.setToolTip(QCoreApplication.translate("MainWindow", u"Rozpoczyna badanie w wirtualnej rzeczywisto\u015bci", None))
#endif // QT_CONFIG(tooltip)
        self.VR_start.setText(QCoreApplication.translate("MainWindow", u"Rozpocznij badanie", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Sterowanie", None))
        self.pushButton_11.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"F1", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Pomoc", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"F10", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Opcje pogody", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Widok FPV", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Widok \"Le\u0107 ze mn\u0105\"", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\\", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Widok \"obserwator naziemny\"", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Widok \"Zza drona\"", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"R\u0119czne sterowanie kamer\u0105 ", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"W\u0142\u0105cz nagrywanie", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Pokazywanie toru trasy ", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Backspace", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Czas badania", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Pozycja X", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Odchylenie", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Pochylenie", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Stopnie", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107 Y", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Wysoko\u015b\u0107", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"m", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107 Z", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"Sekundy", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Przechylenie", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"m/s", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Stopnie", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Pr\u0119dko\u015b\u0107 X", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Pozycja Y", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Stopnie", None))
        self.label_14.setText("")
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Tu znajduje si\u0119 strona startowa projektu, nic szczeg\u00f3lnego pr\u00f3cz tytu\u0142u", None))
        self.label_44.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Tu znajduje sie panel symulacji badania w wirtualnej rzeczywistosci ", None))
        self.label_62.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Tu znajduj\u0105 si\u0119 takie ustawienia, jak wyb\u00f3r mapy", None))
        self.label_46.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Tu znajduj\u0105 si\u0119 parametry drona, wraz z zadaniem jakie pilot powinien wykona\u0107", None))
        self.label_48.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Tu znajduje si\u0119, kr\u00f3tkie opisanie tego co powinien robi\u0107 badany oraz gdzie si\u0119 znajduj\u0105 poszczeg\u00f3lne informacje", None))
        self.label_50.setText("")
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Tu znajduj\u0105 si\u0119 wykresy wygenerowane po badaniu", None))
        self.label_52.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Tu znajduje si\u0119 zobrazowanie danych, kt\u00f3re zosta\u0142y poddane analizie w trakcie oceny predyspozycji", None))
        self.label_54.setText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Informacje o projekcie oraz autorach i idei projektu", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"Aby przej\u015b\u0107 dalej, naci\u015bnij: ", None))
        self.pushButton.setText("")
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"W\u0142\u0105cz symulator poprzez wci\u015bni\u0119cie przycisku z ikon\u0105 platformy czterowirnikowej ", None))
        self.label_222.setText("")
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"Po wczytaniu symulatora zapoznaj si\u0119 z instrukcjami dotycz\u0105cymi sterowania i po\u015bwi\u0119\u0107 chwil\u0119 na trening umiej\u0119tno\u015bci sterowania BSP w AirSim ", None))
        self.label_225.setText("")
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"Sprawd\u017a czy diody sygnalizuj\u0105ce przesy\u0142anie warto\u015bci t\u0119tna jak i sprawdzanie emocji s\u0105 koloru zielonego ", None))
        self.label_223.setText("")
        self.label_212.setText(QCoreApplication.translate("MainWindow", u"Rozpocznij badanie poprzez naci\u015bni\u0119cie przycisku \u201eCzas na misje!\u201d", None))
        self.label_224.setText("")
        self.label_213.setText(QCoreApplication.translate("MainWindow", u"Ka\u017cde zadanie jest poprzedzone wyg\u0142oszeniem tre\u015bci misji, jednak\u017ce je\u015bli nie zapami\u0119tasz jej tre\u015bci to b\u0119dzie ona wy\u015bwietlana w aplikacji ", None))
        self.label_214.setText(QCoreApplication.translate("MainWindow", u"Po zako\u0144czeniu ostatniego zadania pojawi si\u0119 okienko z pytaniem,Wyb\u00f3r opcji \u201eTak!\u201d spowoduje automatyczne przej\u015bcie do strony z badaniem w wirtualnej rzeczywisto\u015bci ", None))
        self.label_227.setText("")
        self.label_215.setText(QCoreApplication.translate("MainWindow", u"Po przej\u015bciu do strony z badaniem w VR (ang. Virtual Reality \u2013 wirtualna rzeczywisto\u015b\u0107) wybierz map\u0119, na kt\u00f3rej chcesz odby\u0107 badanie. Jednak\u017ce, miej na uwadze \u017ce wyb\u00f3r innej mapy ni\u017c \u201eAirSimNH\u201d nie jest zalecane", None))
        self.label_216.setText(QCoreApplication.translate("MainWindow", u"Aby rozpocz\u0105\u0107 badanie kliknij dwukrotnie w przycisk z podpisem \u201eRozpocznij badanie\u201d ", None))
        self.label_226.setText("")
        self.label_217.setText(QCoreApplication.translate("MainWindow", u"Nast\u0119pnie naci\u015bnij przycisk automatycznego prze\u0142\u0105czania pomi\u0119dzy poziomami w oknie \u201ePoziomy \u2013 Wirtualna rzeczywisto\u015b\u0107\u201d ", None))
        self.label_228.setText("")
        self.label_218.setText(QCoreApplication.translate("MainWindow", u"Wykonaj tyle poziom\u00f3w ile dasz rad\u0119, gdy poczujesz si\u0119 s\u0142abo natychmiast zdejmij gogle VR i naci\u015bnij przycisk s\u0142u\u017c\u0105cy do zako\u0144czenia badania", None))
        self.label_229.setText("")
        self.label_219.setText(QCoreApplication.translate("MainWindow", u"Po zako\u0144czeniu badania zapisz dane do pliku u\u017cywajac do tego celu  przycisku", None))
        self.label_230.setText("")
        self.label_220.setText(QCoreApplication.translate("MainWindow", u"Nast\u0119pnie wygeneruj wykresy i wynik badania na podstawie danych zapisanych do pliku", None))
        self.label_231.setText("")
        self.label_221.setText(QCoreApplication.translate("MainWindow", u"Po naci\u015bni\u0119ciu powy\u017cszego przycisku u\u017cytkownik zostanie automatycznie przekierowany do strony z wykresami, aby dosta\u0107 si\u0119 do wyniku badania nale\u017cy wybra\u0107 stron\u0119 ze statystykami i wynikiem badania. Przekierowanie do strony nast\u0105pi po naci\u015bni\u0119ciu przycisku  w menu bocznym", None))
        self.label_232.setText("")
        self.label_233.setText("")
        self.label_235.setText("")
        self.label_234.setText("")
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Zmiany t\u0119tna przez ca\u0142e badanie", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Wszystkie poziomy", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Poziom 1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Poziom 2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Poziom 3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Poziom 4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Poziom 5", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Poziom 6", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Poziom 7", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Poziom 8", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Poziom 9", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Poziom 10", None))

#if QT_CONFIG(tooltip)
        self.stackedWidget_2.setToolTip(QCoreApplication.translate("MainWindow", u"Zmiany t\u0119tna przez ca\u0142e badanie ", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.frame_49.setToolTip(QCoreApplication.translate("MainWindow", u"Udzia\u0142 poszczeg\u00f3lnych emocji w og\u00f3le", None))
#endif // QT_CONFIG(tooltip)
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"Podzia\u0142 procentowy emocji ", None))
#if QT_CONFIG(tooltip)
        self.frame_48.setToolTip(QCoreApplication.translate("MainWindow", u"\u015arednie warto\u015bci t\u0119tna na poszczeg\u00f3lnych poziomach", None))
#endif // QT_CONFIG(tooltip)
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"T\u0119tno w zale\u017cno\u015bci od poziomu", None))
#if QT_CONFIG(tooltip)
        self.frame_50.setToolTip(QCoreApplication.translate("MainWindow", u"Dok\u0142adne charakterystyki obrazuj\u0105ce zmiany emocji w poszczeg\u00f3lnych etapach badania", None))
#endif // QT_CONFIG(tooltip)
        self.label_145.setText(QCoreApplication.translate("MainWindow", u"Zmiany emocji  przez ca\u0142e badanie", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Wszystkie poziomy", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Poziom 1", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Poziom 2", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Poziom 3", None))
        self.comboBox_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Poziom 4", None))
        self.comboBox_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Poziom 5", None))
        self.comboBox_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Poziom 6", None))
        self.comboBox_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Poziom 7", None))
        self.comboBox_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Poziom 8", None))
        self.comboBox_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Poziom 9", None))
        self.comboBox_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Poziom 10", None))

        self.label_174.setText(QCoreApplication.translate("MainWindow", u"Warto\u015bci charakterystyczne dla t\u0119tna: ", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"Badanie VR", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"Badanie zdolno\u015bci manualnych ", None))
#if QT_CONFIG(tooltip)
        self.frame_68.setToolTip(QCoreApplication.translate("MainWindow", u"Maksymalne t\u0119tno zaobserwowane w trakcie badania VR ", None))
#endif // QT_CONFIG(tooltip)
        self.label_179.setText(QCoreApplication.translate("MainWindow", u"MAX", None))
        self.label_180.setText("")
        self.label_181.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_69.setToolTip(QCoreApplication.translate("MainWindow", u"Minimalne t\u0119tno zaobserwowane w trakcie badania w VR ", None))
#endif // QT_CONFIG(tooltip)
        self.label_182.setText(QCoreApplication.translate("MainWindow", u"MIN", None))
        self.label_183.setText("")
        self.label_184.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_70.setToolTip(QCoreApplication.translate("MainWindow", u"\u015arednie t\u0119tno zaobserwowane w trakcie badania w VR", None))
#endif // QT_CONFIG(tooltip)
        self.label_185.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNIA", None))
        self.label_186.setText("")
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_54.setToolTip(QCoreApplication.translate("MainWindow", u"Maksymalne t\u0119tno zaobserwowane w trakcie badania zdolno\u015bci manualnych ", None))
#endif // QT_CONFIG(tooltip)
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"MAX", None))
        self.label_147.setText("")
        self.label_148.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_55.setToolTip(QCoreApplication.translate("MainWindow", u"Minimalne t\u0119tno zaobserwowane w trakcie badania zdolno\u015bci manualnych ", None))
#endif // QT_CONFIG(tooltip)
        self.label_149.setText(QCoreApplication.translate("MainWindow", u"MIN", None))
        self.label_150.setText("")
        self.label_151.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_56.setToolTip(QCoreApplication.translate("MainWindow", u"\u015arednie t\u0119tno zaobserwowane w trakcie badania zdolno\u015bci manualnych", None))
#endif // QT_CONFIG(tooltip)
        self.label_152.setText(QCoreApplication.translate("MainWindow", u"\u015aREDNIA", None))
        self.label_153.setText("")
        self.label_154.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_155.setText(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wyst\u0105pie\u0144 poszczeg\u00f3lnych emocji: ", None))
#if QT_CONFIG(tooltip)
        self.frame_57.setToolTip(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wyst\u0105pie\u0144 \"zdenerwowanej twarzy\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_156.setText(QCoreApplication.translate("MainWindow", u"W\u015bciek\u0142y", None))
        self.label_157.setText("")
        self.label_158.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_58.setToolTip(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wyst\u0105pie\u0144 \"obrzydzonej twarzy\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_159.setText(QCoreApplication.translate("MainWindow", u"Obrzydzony", None))
        self.label_160.setText("")
        self.label_161.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_59.setToolTip(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wyst\u0105pie\u0144 \"przestraszonej twarzy\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_162.setText(QCoreApplication.translate("MainWindow", u"Przestraszony", None))
        self.label_163.setText("")
        self.label_164.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_60.setToolTip(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wyst\u0105pie\u0144 \"szcz\u0119\u015bliwej twarzy\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_165.setText(QCoreApplication.translate("MainWindow", u"Szcz\u0119\u015bliwy", None))
        self.label_166.setText("")
        self.label_167.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_61.setToolTip(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wyst\u0105pie\u0144 \"zaskoczonej twarzy\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_168.setText(QCoreApplication.translate("MainWindow", u"Zaskoczona", None))
        self.label_169.setText("")
        self.label_170.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_66.setToolTip(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wyst\u0105pie\u0144 \"smutnej twarzy\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_176.setText(QCoreApplication.translate("MainWindow", u"Smutna", None))
        self.label_177.setText("")
        self.label_178.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_62.setToolTip(QCoreApplication.translate("MainWindow", u"Ilo\u015b\u0107 wyst\u0105pie\u0144 \"neutralnej twarzy\"", None))
#endif // QT_CONFIG(tooltip)
        self.label_171.setText(QCoreApplication.translate("MainWindow", u"Neutralna", None))
        self.label_172.setText("")
        self.label_173.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(tooltip)
        self.frame_64.setToolTip(QCoreApplication.translate("MainWindow", u"Predykcje", None))
#endif // QT_CONFIG(tooltip)
        self.label_236.setText(QCoreApplication.translate("MainWindow", u"Ocena twoich predyspozycji: ", None))
        self.label_250.setText("")
        self.procenty.setText(QCoreApplication.translate("MainWindow", u"Wedle komputera nadajesz si\u0119 do bycia operatorem BSP w 0 procentach", None))
        self.label_240.setText("")
        self.komunikat.setText(QCoreApplication.translate("MainWindow", u"Komputer oceni\u0142, \u017ce nie kontrolujesz emocji i nie radzisz sobie z presj\u0105 wynikaj\u0105c\u0105 z postawionych bada\u0144, poniewa\u017c twoje t\u0119tno wykaza\u0142o bardzo du\u017c\u0105 zmienno\u015b\u0107", None))
#if QT_CONFIG(tooltip)
        self.frame_51.setToolTip(QCoreApplication.translate("MainWindow", u"Wykresy obrazuj\u0105ce przebieg danych w trakcie badania w VR", None))
#endif // QT_CONFIG(tooltip)
        self.label_175.setText(QCoreApplication.translate("MainWindow", u"Zmiany t\u0119tna  przez ca\u0142e badanie w VR", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", u"Wszystkie poziomy", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"Poziom 1", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"Poziom 2", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", u"Poziom 3", None))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", u"Poziom 4", None))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", u"Poziom 5", None))
        self.comboBox_3.setItemText(6, QCoreApplication.translate("MainWindow", u"Poziom 6", None))
        self.comboBox_3.setItemText(7, QCoreApplication.translate("MainWindow", u"Poziom 7", None))
        self.comboBox_3.setItemText(8, QCoreApplication.translate("MainWindow", u"Poziom 8", None))
        self.comboBox_3.setItemText(9, QCoreApplication.translate("MainWindow", u"Poziom 9", None))
        self.comboBox_3.setItemText(10, QCoreApplication.translate("MainWindow", u"Poziom 10", None))

#if QT_CONFIG(tooltip)
        self.frame_97.setToolTip(QCoreApplication.translate("MainWindow", u"Predykcje", None))
#endif // QT_CONFIG(tooltip)
        self.label_242.setText(QCoreApplication.translate("MainWindow", u"Pami\u0119taj, \u017ce to nic straconego!", None))
        self.label_243.setText(QCoreApplication.translate("MainWindow", u"Je\u017celi od zawsze marzy\u0142e\u015b o byciu operatorem BSP, to mo\u017cesz: ", None))
        self.label_246.setText("")
        self.rada.setText(QCoreApplication.translate("MainWindow", u"Komputer oceni\u0142, \u017ce nie kontrolujesz emocji i nie radzisz sobie z presj\u0105 wynikaj\u0105c\u0105 z postawionych bada\u0144, poniewa\u017c twoje t\u0119tno wykaza\u0142o bardzo du\u017c\u0105 zmienno\u015b\u0107", None))
        self.label_248.setText("")
        self.mysl.setText(QCoreApplication.translate("MainWindow", u"Komputer oceni\u0142, \u017ce nie kontrolujesz emocji i nie radzisz sobie z presj\u0105 wynikaj\u0105c\u0105 z postawionych bada\u0144, poniewa\u017c twoje t\u0119tno wykaza\u0142o bardzo du\u017c\u0105 zmienno\u015b\u0107", None))
        self.Autor.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"O projekcie", None))
        self.label_15.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Projekt powsta\u0142 w ramach pracy magisterskiej, ma on za zadanie okre\u015bli\u0107 predyspozycje badanego do pracy w roli pilotuj\u0105cego bezza\u0142ogowy statek powietrzny. Do tego celu zosta\u0142 u\u017cyty projekt firmy Microsoft - AIRSIM. Zdecydowano si\u0119 na ten wyb\u00f3r, poniewa\u017c symulator oferuje szerokie mo\u017cliwo\u015bci rozwoju aplikacji autorskich wykorzystuj\u0105cych ten projekt poprzez u\u017cyczenie u\u017cytkownikom interfejs\u00f3w programowania aplikacji. Ponadto, aplikacja zosta\u0142a udost\u0119pniona na portalu Github i istnieje mo\u017cliwo\u015b\u0107 samodzielnego zmieniania kodu \u017ar\u00f3d\u0142owego na potrzeby wykonywanego zadania. ", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"O dyplomancie", None))
        self.label_16.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"sier\u017c. pchor. Rafa\u0142 Wysocki, s\u0142uchacz V roku WML, autor projektu.", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"O promotorze", None))
        self.label_17.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"pp\u0142k dr in\u017c. Konrad Wojtowicz, prodziekan ds. studenckich i wsp\u00f3\u0142pracy mi\u0119dzynarodowej WML", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"Linki", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"Wska\u017anika autorstwa Khamisi Kibeta", None))
        self.label_191.setText("")
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"https://www.spinncode.com", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"https://www.youtube.com/@SpinnTV", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"https://github.com/KhamisiKibet", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"Ikony ", None))
        self.label_196.setText("")
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"https://icons8.com/icons", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"Wojskowa Akademia Techniczna", None))
        self.label_199.setText("")
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"https://www.wojsko-polskie.pl/wat/", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"Wydzia\u0142 Mechatroniki, Uzbrojenia i Lotnictwa", None))
        self.label_203.setText("")
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"https://wml.wat.edu.pl", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"GitHub", None))
        self.label_205.setText("")
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"https://github.com/Mevaco2000", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Drone Controller Test - Rafa\u0142 Wysocki, wersja 1.0.0 /2023", None))
    # retranslateUi

