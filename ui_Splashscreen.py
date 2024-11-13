# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SplashscreenrygMSL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import splash_rc

class Ui_MainWindow1(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(584, 349)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border-image: url(:/nowyPrzedrostek/Zdjecia/Splash.png);")
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(20, 170, 541, 41))
        self.progressBar.setStyleSheet(u"\n"
"QProgressBar {\n"
"	border-image:transparent;\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(93, 0, 255);\n"
"    width: 20px;\n"
"}")
        self.progressBar.setValue(24)
        self.progressBar.setTextVisible(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 120, 271, 41))
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border-image: transparent;\n"
"color:rgb(250, 230, 255);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(330, 230, 224, 84))
        self.frame.setStyleSheet(u"border-image:transparent;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border-image:transparent;")
        self.label_2.setPixmap(QPixmap(u":/nowyPrzedrostek/Icons/Magisterka_python(1)/icons8-drone-64-splash.png"))

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border-image:transparent;")
        self.label_3.setPixmap(QPixmap(u":/nowyPrzedrostek/Icons/Magisterka_python(1)/icons8-drone-64-splash.png"))

        self.horizontalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"border-image:transparent;")
        self.label_4.setPixmap(QPixmap(u":/nowyPrzedrostek/Icons/Magisterka_python(1)/icons8-drone-64-splash.png"))

        self.horizontalLayout.addWidget(self.label_4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trwa wczytywanie...", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
    # retranslateUi

