# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VR_levelsDsIDor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_VR_Levels(object):
    def setupUi(self, VR_Levels):
        if not VR_Levels.objectName():
            VR_Levels.setObjectName(u"VR_Levels")
        VR_Levels.resize(481, 914)
        VR_Levels.setCursor(QCursor(Qt.ArrowCursor))
        VR_Levels.setStyleSheet(u"QMainWindow\n"
"{\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 35);\n"
"}\n"
"QToolTip {\n"
"	border: 3px solid rgb(0, 0, 127)i;\n"
"    padding: 5px;\n"
"    border-radius: 10px;\n"
"    opacity: 200;\n"
"	background-color: rgb(15, 14, 28);\n"
"	color: rgb(255, 255, 255);\n"
"}")
        self.centralwidget = QWidget(VR_Levels)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 35);")
        self.frame_35 = QFrame(self.centralwidget)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setGeometry(QRect(43, 60, 402, 841))
        self.frame_35.setStyleSheet(u"QPushButton\n"
"{\n"
" border-radius:20px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"}\n"
"")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_35)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.dzialanie = QLabel(self.frame_35)
        self.dzialanie.setObjectName(u"dzialanie")
        font = QFont()
        font.setFamily(u"Arial Narrow")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.dzialanie.setFont(font)

        self.verticalLayout.addWidget(self.dzialanie, 0, Qt.AlignHCenter)

        self.VR_poziom1 = QPushButton(self.frame_35)
        self.VR_poziom1.setObjectName(u"VR_poziom1")
        self.VR_poziom1.setMinimumSize(QSize(400, 30))
        self.VR_poziom1.setMaximumSize(QSize(290, 30))
        font1 = QFont()
        font1.setFamily(u"MS Gothic")
        self.VR_poziom1.setFont(font1)
        self.VR_poziom1.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-level-1-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom1.setIcon(icon)
        self.VR_poziom1.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.VR_poziom1, 0, Qt.AlignHCenter)

        self.label_72 = QLabel(self.frame_35)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout.addWidget(self.label_72)

        self.progressBar = QProgressBar(self.frame_35)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"")
        self.progressBar.setValue(0)

        self.verticalLayout.addWidget(self.progressBar)

        self.VR_poziom2 = QPushButton(self.frame_35)
        self.VR_poziom2.setObjectName(u"VR_poziom2")
        self.VR_poziom2.setMinimumSize(QSize(400, 30))
        self.VR_poziom2.setMaximumSize(QSize(290, 30))
        self.VR_poziom2.setFont(font1)
        self.VR_poziom2.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-2-circled-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom2.setIcon(icon1)
        self.VR_poziom2.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.VR_poziom2, 0, Qt.AlignHCenter)

        self.label_73 = QLabel(self.frame_35)
        self.label_73.setObjectName(u"label_73")

        self.verticalLayout.addWidget(self.label_73)

        self.progressBar_2 = QProgressBar(self.frame_35)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"")
        self.progressBar_2.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_2)

        self.VR_poziom3 = QPushButton(self.frame_35)
        self.VR_poziom3.setObjectName(u"VR_poziom3")
        self.VR_poziom3.setMinimumSize(QSize(400, 30))
        self.VR_poziom3.setMaximumSize(QSize(290, 30))
        self.VR_poziom3.setFont(font1)
        self.VR_poziom3.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-circled-3-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom3.setIcon(icon2)
        self.VR_poziom3.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.VR_poziom3, 0, Qt.AlignHCenter)

        self.label_74 = QLabel(self.frame_35)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout.addWidget(self.label_74)

        self.progressBar_3 = QProgressBar(self.frame_35)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setStyleSheet(u"")
        self.progressBar_3.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_3)

        self.VR_poziom4 = QPushButton(self.frame_35)
        self.VR_poziom4.setObjectName(u"VR_poziom4")
        self.VR_poziom4.setMinimumSize(QSize(400, 30))
        self.VR_poziom4.setMaximumSize(QSize(290, 30))
        self.VR_poziom4.setFont(font1)
        self.VR_poziom4.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-4-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom4.setIcon(icon3)
        self.VR_poziom4.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.VR_poziom4, 0, Qt.AlignHCenter)

        self.label_75 = QLabel(self.frame_35)
        self.label_75.setObjectName(u"label_75")

        self.verticalLayout.addWidget(self.label_75)

        self.progressBar_4 = QProgressBar(self.frame_35)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setStyleSheet(u"")
        self.progressBar_4.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_4)

        self.VR_poziom5 = QPushButton(self.frame_35)
        self.VR_poziom5.setObjectName(u"VR_poziom5")
        self.VR_poziom5.setMinimumSize(QSize(400, 30))
        self.VR_poziom5.setMaximumSize(QSize(290, 30))
        self.VR_poziom5.setFont(font1)
        self.VR_poziom5.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-circled-5-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom5.setIcon(icon4)
        self.VR_poziom5.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.VR_poziom5, 0, Qt.AlignHCenter)

        self.label_66 = QLabel(self.frame_35)
        self.label_66.setObjectName(u"label_66")

        self.verticalLayout.addWidget(self.label_66)

        self.progressBar_5 = QProgressBar(self.frame_35)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setStyleSheet(u"")
        self.progressBar_5.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_5)

        self.VR_poziom6 = QPushButton(self.frame_35)
        self.VR_poziom6.setObjectName(u"VR_poziom6")
        self.VR_poziom6.setMinimumSize(QSize(400, 30))
        self.VR_poziom6.setMaximumSize(QSize(290, 30))
        self.VR_poziom6.setFont(font1)
        self.VR_poziom6.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-circled-6-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom6.setIcon(icon5)
        self.VR_poziom6.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.VR_poziom6, 0, Qt.AlignHCenter)

        self.label_67 = QLabel(self.frame_35)
        self.label_67.setObjectName(u"label_67")

        self.verticalLayout.addWidget(self.label_67)

        self.progressBar_6 = QProgressBar(self.frame_35)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_6)

        self.VR_poziom7 = QPushButton(self.frame_35)
        self.VR_poziom7.setObjectName(u"VR_poziom7")
        self.VR_poziom7.setMinimumSize(QSize(400, 30))
        self.VR_poziom7.setMaximumSize(QSize(290, 30))
        self.VR_poziom7.setFont(font1)
        self.VR_poziom7.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-7-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom7.setIcon(icon6)
        self.VR_poziom7.setIconSize(QSize(32, 32))

        self.verticalLayout.addWidget(self.VR_poziom7, 0, Qt.AlignHCenter)

        self.label_70 = QLabel(self.frame_35)
        self.label_70.setObjectName(u"label_70")

        self.verticalLayout.addWidget(self.label_70)

        self.progressBar_7 = QProgressBar(self.frame_35)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_7)

        self.VR_poziom8 = QPushButton(self.frame_35)
        self.VR_poziom8.setObjectName(u"VR_poziom8")
        self.VR_poziom8.setMinimumSize(QSize(400, 30))
        self.VR_poziom8.setMaximumSize(QSize(290, 30))
        self.VR_poziom8.setFont(font1)
        self.VR_poziom8.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-8-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom8.setIcon(icon7)
        self.VR_poziom8.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.VR_poziom8, 0, Qt.AlignHCenter)

        self.label_68 = QLabel(self.frame_35)
        self.label_68.setObjectName(u"label_68")

        self.verticalLayout.addWidget(self.label_68)

        self.progressBar_8 = QProgressBar(self.frame_35)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_8)

        self.VR_poziom9 = QPushButton(self.frame_35)
        self.VR_poziom9.setObjectName(u"VR_poziom9")
        self.VR_poziom9.setMinimumSize(QSize(400, 30))
        self.VR_poziom9.setMaximumSize(QSize(290, 30))
        self.VR_poziom9.setFont(font1)
        self.VR_poziom9.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-9-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom9.setIcon(icon8)
        self.VR_poziom9.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.VR_poziom9, 0, Qt.AlignHCenter)

        self.label_69 = QLabel(self.frame_35)
        self.label_69.setObjectName(u"label_69")

        self.verticalLayout.addWidget(self.label_69)

        self.progressBar_9 = QProgressBar(self.frame_35)
        self.progressBar_9.setObjectName(u"progressBar_9")
        self.progressBar_9.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_9)

        self.VR_poziom10 = QPushButton(self.frame_35)
        self.VR_poziom10.setObjectName(u"VR_poziom10")
        self.VR_poziom10.setMinimumSize(QSize(400, 30))
        self.VR_poziom10.setMaximumSize(QSize(290, 30))
        self.VR_poziom10.setFont(font1)
        self.VR_poziom10.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-10mph-speed-sign-50 (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.VR_poziom10.setIcon(icon9)
        self.VR_poziom10.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.VR_poziom10, 0, Qt.AlignHCenter)

        self.label_71 = QLabel(self.frame_35)
        self.label_71.setObjectName(u"label_71")

        self.verticalLayout.addWidget(self.label_71)

        self.progressBar_10 = QProgressBar(self.frame_35)
        self.progressBar_10.setObjectName(u"progressBar_10")
        self.progressBar_10.setValue(0)

        self.verticalLayout.addWidget(self.progressBar_10)

        self.frame_2 = QFrame(self.frame_35)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.landing_button = QPushButton(self.frame_2)
        self.landing_button.setObjectName(u"landing_button")
        icon10 = QIcon()
        icon10.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-landing-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.landing_button.setIcon(icon10)
        self.landing_button.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.landing_button)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/Icons/Magisterka_python(1)/icons8-heart-rate-50.png"))

        self.verticalLayout_2.addWidget(self.label_2, 0, Qt.AlignHCenter)

        self.tetno = QLabel(self.frame_3)
        self.tetno.setObjectName(u"tetno")
        font2 = QFont()
        font2.setFamily(u"Poor Richard")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.tetno.setFont(font2)
        self.tetno.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.tetno)


        self.horizontalLayout_2.addWidget(self.frame_3)

        self.Repeat = QPushButton(self.frame_2)
        self.Repeat.setObjectName(u"Repeat")
        icon11 = QIcon()
        icon11.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-undo-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Repeat.setIcon(icon11)
        self.Repeat.setIconSize(QSize(64, 64))

        self.horizontalLayout_2.addWidget(self.Repeat)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 461, 52))
        self.frame.setStyleSheet(u"QPushButton\n"
"{\n"
" border-radius:20px;\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	background-color: rgb(0, 0, 127);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.label.setFont(font3)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.Save_2 = QPushButton(self.frame)
        self.Save_2.setObjectName(u"Save_2")
        icon12 = QIcon()
        icon12.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-automatic-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save_2.setIcon(icon12)
        self.Save_2.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.Save_2)

        self.Save = QPushButton(self.frame)
        self.Save.setObjectName(u"Save")
        icon13 = QIcon()
        icon13.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-save-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Save.setIcon(icon13)
        self.Save.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.Save)

        self.Min = QPushButton(self.frame)
        self.Min.setObjectName(u"Min")
        icon14 = QIcon()
        icon14.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-minimize-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Min.setIcon(icon14)
        self.Min.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.Min)

        self.Close = QPushButton(self.frame)
        self.Close.setObjectName(u"Close")
        icon15 = QIcon()
        icon15.addFile(u":/icons/Icons/Magisterka_python(1)/icons8-close-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Close.setIcon(icon15)
        self.Close.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.Close)

        VR_Levels.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(VR_Levels)
        self.statusbar.setObjectName(u"statusbar")
        VR_Levels.setStatusBar(self.statusbar)

        self.retranslateUi(VR_Levels)

        QMetaObject.connectSlotsByName(VR_Levels)
    # setupUi

    def retranslateUi(self, VR_Levels):
        VR_Levels.setWindowTitle(QCoreApplication.translate("VR_Levels", u"MainWindow", None))
        self.dzialanie.setText(QCoreApplication.translate("VR_Levels", u"TextLabel", None))
        self.VR_poziom1.setText(QCoreApplication.translate("VR_Levels", u" Poziom 1", None))
        self.label_72.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania...", None))
        self.VR_poziom2.setText(QCoreApplication.translate("VR_Levels", u"Poziom 2 ", None))
        self.label_73.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania...", None))
        self.VR_poziom3.setText(QCoreApplication.translate("VR_Levels", u"Poziom 3", None))
        self.label_74.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania...", None))
        self.VR_poziom4.setText(QCoreApplication.translate("VR_Levels", u"Poziom 4", None))
        self.label_75.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania", None))
        self.VR_poziom5.setText(QCoreApplication.translate("VR_Levels", u"Poziom 5", None))
        self.label_66.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania", None))
        self.VR_poziom6.setText(QCoreApplication.translate("VR_Levels", u"Poziom 6", None))
        self.label_67.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania", None))
        self.VR_poziom7.setText(QCoreApplication.translate("VR_Levels", u"Poziom 7", None))
        self.label_70.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania", None))
        self.VR_poziom8.setText(QCoreApplication.translate("VR_Levels", u"Poziom 8 ", None))
        self.label_68.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania", None))
        self.VR_poziom9.setText(QCoreApplication.translate("VR_Levels", u"Poziom 9", None))
        self.label_69.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania", None))
        self.VR_poziom10.setText(QCoreApplication.translate("VR_Levels", u"Poziom 10", None))
        self.label_71.setText(QCoreApplication.translate("VR_Levels", u"Post\u0119p zadania", None))
#if QT_CONFIG(tooltip)
        self.landing_button.setToolTip(QCoreApplication.translate("VR_Levels", u"Wyl\u0105duj i zako\u0144cz badanie", None))
#endif // QT_CONFIG(tooltip)
        self.landing_button.setText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("VR_Levels", u"Twoje aktualne t\u0119tno", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText("")
        self.tetno.setText(QCoreApplication.translate("VR_Levels", u"0", None))
#if QT_CONFIG(tooltip)
        self.Repeat.setToolTip(QCoreApplication.translate("VR_Levels", u"Wykonaj badanie ponownie", None))
#endif // QT_CONFIG(tooltip)
        self.Repeat.setText("")
        self.label.setText(QCoreApplication.translate("VR_Levels", u"Poziomy - Wirtualna rzeczywistosc", None))
#if QT_CONFIG(tooltip)
        self.Save_2.setToolTip(QCoreApplication.translate("VR_Levels", u"Automatyczne prze\u0142\u0105czanie poziom\u00f3w", None))
#endif // QT_CONFIG(tooltip)
        self.Save_2.setText("")
        self.Save.setText("")
#if QT_CONFIG(tooltip)
        self.Min.setToolTip(QCoreApplication.translate("VR_Levels", u"Minimalizuj", None))
#endif // QT_CONFIG(tooltip)
        self.Min.setText("")
#if QT_CONFIG(tooltip)
        self.Close.setToolTip(QCoreApplication.translate("VR_Levels", u"Zamknij", None))
#endif // QT_CONFIG(tooltip)
        self.Close.setText("")
    # retranslateUi

