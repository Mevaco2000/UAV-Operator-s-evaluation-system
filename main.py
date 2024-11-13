import sys
import os
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets
from PySide2.QtWidgets import QMessageBox
import PySide2.QtGui as QtGui
from ui_magisterka_gui import *
import subprocess
import airsim
from PySide2.QtCore import QTimer
import time
import math
from PySide2.QtGui import QTransform
import cv2
import numpy as np
import tensorflow as tf
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model
from keras.preprocessing import image
import serial 
import pandas as pd
from PySide2.QtCharts import QtCharts
import statistics
from Splashscreen1 import *
from VR_levels_2 import *
import winsound
import random

##############Watek dla pobierania wartosci tetna z czujnika MAX30102#############################################################################
##################################################################################################################################################

class Worker1(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker1, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
    @Slot()
    def run(self):
        self.fn(*self.args,**self.kwargs)
class TetnoThread(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(TetnoThread, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
    @Slot()
    def run(self):
        self.fn(*self.args,**self.kwargs)
#############Aplikacja############################################################################################################################
#################################################################################################################################################
class MainWindow(QMainWindow):
    def __init__(self):
        #####Ustawianie UI########################################################################
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        
        ####Usuwanie window border#################################################################
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ###Ustawienie tła jako przezroczyste########################################################
        self.setGeometry(1920,0,1600,1000)
        #self.setGeometry(0,0,1600,1000)
        #Ukrywanie elementow sidebar#################################################################
        self.ui.Settings.hide()
        self.ui.Home.hide()
        self.ui.Analiza.hide()
        self.ui.Informacje.hide()
        self.ui.Misje.hide()
        self.ui.Parametry.hide()
        self.ui.Przewodnik.hide()
        self.ui.VR.hide()
        ############################################################################################
        self.przejdzdoVR=0
        #Ukrywanie elementów instrukcji############################################################
        self.ui.frame_81.setVisible(False)
        self.ui.frame_82.setVisible(False)
        self.ui.frame_83.setVisible(False)
        self.ui.frame_84.setVisible(False)
        self.ui.frame_85.setVisible(False)
        self.ui.frame_86.setVisible(False)
        self.ui.frame_87.setVisible(False)
        self.ui.frame_88.setVisible(False)
        self.ui.frame_89.setVisible(False)
        self.ui.frame_90.setVisible(False)
        self.ui.frame_91.setVisible(False)
        self.ui.frame_92.setVisible(False)
        self.ui.frame_93.setVisible(False)
        #Tablice z cytatami i autorami cytatow pocieszajacych########################################
        self.cytaty=[]
        self.autor=[]
        self.cytaty.append("Gdy przyjmiesz, że negatywne wieści nie są czymś złym, lecz dowodem na potrzebę zmiany, nie mogą cie już one pokonać. Są dla ciebie nauką")
        self.autor.append("Bill Gates")
        self.cytaty.append("Geniusz to 1 procent inspiracji i 99 procentów potu")
        self.autor.append("Thomas Edison")
        self.cytaty.append("Prawdziwy akt odkrycia nie polega na odnajdywaniu nowych lądów, lecz na patrzeniu na stare w nowy sposób")
        self.autor.append("Marcel Proust")
        self.cytaty.append("Marzenie jest formą planowania")
        self.autor.append("Gloria Steinem")
        self.cytaty.append("Jeśli potrafisz o tym marzyć, to potrafisz także tego dokonać.")
        self.autor.append("Walt Disney")
        self.cytaty.append("Najtrudniejsze jest zdecydowanie się na działanie. Reszta to już tylko kwestia wytrwałości")
        self.autor.append("Amelia Earhart")
        self.cytaty.append("Nie obawiaj się porażki - to nie porażka, ale mało ambitny cel jest błędem. W wielkiej próbie honorowo jest nawet polec")
        self.autor.append("Bruce Lee")
        self.cytaty.append("Nie dokonuje odkrycia, kto nie bada niemożliwości")
        self.autor.append("Albert Einstein")
        self.cytaty.append("Trzeba się nauczyć ponosić porażki. Nie można stworzyć nic nowego, jeżeli nie potrafi się akceptować pomyłek")
        self.autor.append("Charles Knight")
        self.cytaty.append("Mądry człowiek nie opłakuje przegranej, lecz szuka sposobu, aby wyleczyć odniesione rany")
        self.autor.append("William Shakespeare")
        self.cytaty.append("Małe szanse są często początkiem wielkich przedsięwzięć")
        self.autor.append("Demostenes")
        self.ui.mysl.setText(self.cytaty[1])
        self.ui.Autor.setText(self.autor[1])

        #Definicja poczatkowych komunikatow##########################################################
        self.napis_tetno=""
        self.napis_twarz=""
        self.napis_misje=""
        self.napis_tetno2=""
        self.napis_tetnoVR2=""
        self.napis_twarz2=""
        self.napis_misje2=""
        #Ukrywanie zdjec ozdobnych w tutorial page###################################################
        self.ui.frame_94.setVisible(False)
        #definicja zmiennej warunkujacej ktora ramka ma sie pojawic##################################
        self.instruction_count=0
        ###Efekt cienia##############################################################################
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(30)
        #Efekt cienia na centralwidget###############################################################
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        #Ustawienie sciezki do folderu###############################################################
        self.path=os.path.dirname(__file__)
        #ikona i tytuł###############################################################################
        self.setWindowIcon(QtGui.QIcon(self.path+r"\Icons\Magisterka_python(1)\icons8-drone-60.png"))
        self.setWindowTitle("Drone Controller Test")
        #Size grip okna#############################################################################
        QtWidgets.QSizeGrip(self.ui.frame_8)
        #########Przyciski funkcyjne min,max,off####################################################
        self.ui.Min.clicked.connect(lambda:self.showMinimized())
        self.ui.Min.clicked.connect(lambda:self.VR_levels.showMinimized())
        self.ui.Max.clicked.connect(lambda:self.restore_or_maximize_window())
        self.ui.Close.clicked.connect(lambda:self.close_window())
        #########Ruszanie oknem##########################################################################
        def moveWindow(e):
          if self.isMaximized()== False:
            if e.buttons() == Qt.LeftButton:
                self.move(self.pos()+e.globalPos()-self.clickPosition)
                self.clickPosition=e.globalPos()
                e.accept() 
        #########Przyblizanie/Oddalanie mapy#############################################################
        def handle_wheel_event(event):
           delta = event.angleDelta().y()
           zoom_factor = 1.2 if delta > 0 else 1 / 1.2
           self.ui.AirSimNH_GV.scale(zoom_factor, zoom_factor)
           event.accept()
        ######Style######################################################################################
        self.stylesheet_default=str(
            "QFrame{background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));}"
            "QFrame::hover{background-color:rgb(50, 48, 52);}"
            "QLabel{background-color:transparent;}")         
        self.stylesheet_clicked=str(
            "QFrame{background-color: qlineargradient(spread:reflect, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(1, 5, 44, 255), stop:1 rgba(16, 14, 27, 255));}"
            "QFrame::hover{background-color:rgb(50, 48, 52);}"
            "QLabel{background-color:transparent;}"            
        )
        self.stylesheet_corners=str(
            "QFrame#side_menu_container{border-top-left-radius:30px; border-bottom-left-radius:40px}"
        )
        #########Definicje dodatkowych elementów#############################################################
        ###Definicja sciezki do symulatora###########################################################
        self.script_path=(self.path+r"\Srodowiska Symulatora\AirSimNH (1)\AirSimNH\WindowsNoEditor\AirSimNH.exe")
        ###Definicja nazwy symulatora################################################################
        self.script_name="AirSimNH.exe"
        ###Ustawienie podstawowej mapy na AirSimNH###################################################
        self.ui.Actualmap.setText("AirSimNH") 
        ###Definicja sciezki do VR###################################################################
        self.script_path_VR=(self.path+r"\Srodowiska Symulatora\AirSimNH (1)\AirSimNH\WindowsNoEditor\AirSimNH.exe")
        ###Definicja nazwy VR########################################################################
        self.script_name_VR="AirSimNH.exe"
        ###Schowanie przycisku do generacji wykresow#################################################
        self.ui.Wykresy.setVisible(False)
        ###Ustawianie tooltipow poczatkowych dla przyciskow zmieniajacych ikony#####################
        self.ui.Menu_button.setToolTip("Rozwiń menu")
        self.ui.Max.setToolTip("Zmaksymalizuj")
        ###Przycisk ukazujacy sie w wypadku pozostania w badaniu 1, umozliwiajacy przejscie do 2####
        self.ui.VR_wspolne.setVisible(False)
        ###Ustawienie przyciskow od wyboru mapy i rozdzielczosci jako AirSim i x1920#################
        self.ui.Btn_AirSimNH.click()
        self.ui.x1920_btn.click()
        ###Schowanie ramki od wyniku misji - nieuzywana##############################################
        self.ui.WynikMisji_frame.setVisible(False)
        ###Standardowe wymiary okna symulatora#######################################################
        self.windowSizeX=1920
        self.windowSizeY=1080
        ###Deklaracja zegarów do odliczania taktów przy przesyle parametrów do aplikacji#############
        self.timer=QTimer(self)
        self.timer_VR=QTimer(self)
        ###Zmiennna do zmiany stanu połączenia#######################################################
        self.connection=0
        ###Zmienna do zmiany stanu włączenia okna VR_levels##########################################
        self.secondwindow=0
        ###Numer uruchomienia#######################################################################
        self.camera_changed=0
        ###Czasy wyswietlane na ekranie podczas badan###############################################
        self.time=0
        self.time_VR=0
        ###Zmienna do zmiany stanu włączenia symulatora#############################################
        self.isAirSimOpened=0
        ###Zmienna do zmiany poziomów - -1 bo 0 gdy zaczyna sie wywolanie funkcji###################
        self.levelpassed=-1
        ############Czas Misje######################################################################
        self.czas_l1=0
        self.czas_l2=0
        self.czas_l3=0
        self.czas_l4=0
        self.czas_l5=0
        self.czas_l6=0
        self.czas_l7=0
        self.czas_l8=0
        self.czas_l9=0
        self.czas_l10=0
        ##########Zmienne do tabeli#############################################################################################################################################
        ########################################################################################################################################################################
        #Level 1###################################################################################
        self.l1_w=0#wynik misji
        self.l1_c=0#czas wykonania misji
        self.l1_t=0#srednie tetno   
        self.l1_f=0#srednia z twarzy
        #Level 2###################################################################################
        self.l2_w=0
        self.l2_c=0
        self.l2_t=0
        self.l2_f=0
        #Level 3###################################################################################
        self.l3_w=0
        self.l3_c=0
        self.l3_t=0
        self.l3_f=0
        #Level 4###################################################################################
        self.l4_w=0
        self.l4_c=0
        self.l4_t=0
        self.l4_f=0
        #Level 5#####################################################################################
        self.l5_w=0
        self.l5_c=0
        self.l5_t=0
        self.l5_f=0
        #Level 6#######################################################################################
        self.l6_w=0
        self.l6_c=0
        self.l6_t=0
        self.l6_f=0
        #Level 7#####################################################################################
        self.l7_w=0
        self.l7_c=0
        self.l7_t=0
        self.l7_f=0
        #Level 8##################################################################################
        self.l8_w=0
        self.l8_c=0
        self.l8_t=0
        self.l8_f=0
        #Level 9#################################################################################
        self.l9_w=0
        self.l9_c=0
        self.l9_t=0
        self.l9_f=0
        #Level 10######################################################################################
        self.l10_w=0
        self.l10_c=0
        self.l10_t=0
        self.l10_f=0
        #Tetna i emocje - tablice##########################################################################
        self.tetno1=[]
        self.tetno2=[]
        self.tetno3=[]
        self.tetno4=[]
        self.tetno5=[]
        self.tetno6=[]
        self.tetno7=[]
        self.tetno8=[]
        self.tetno9=[]
        self.tetno10=[]
        #Tablice zapisujace czas poszczegolnych pomiarow tetna################################################
        self.time_samples1=[]
        self.time_samples2=[]
        self.time_samples3=[]
        self.time_samples4=[]
        self.time_samples5=[]
        self.time_samples6=[]
        self.time_samples7=[]
        self.time_samples8=[]
        self.time_samples9=[]
        self.time_samples10=[]
        #Tablice zapisujace wszystkie emocje w trakcie badania###############################################
        self.emocje1=[]
        self.emocje2=[]
        self.emocje3=[]
        self.emocje4=[]
        self.emocje5=[]
        self.emocje6=[]
        self.emocje7=[]
        self.emocje8=[]
        self.emocje9=[]
        self.emocje10=[]
        #Zmienne pomiedzy ekstremami##########################################################################
        self.czas_ekst1=0
        self.czas_ekst2=0
        self.czas_ekst3=0
        self.czas_ekst4=0
        self.czas_ekst5=0
        self.czas_ekst6=0
        self.czas_ekst7=0
        self.czas_ekst8=0
        self.czas_ekst9=0
        self.czas_ekst10=0
        #Deklaracja zmiennych pomiedzy ekstremami w badaniu VR###############################################
        self.czas_ekst1_vr=0
        self.czas_ekst2_vr=0
        self.czas_ekst3_vr=0
        self.czas_ekst4_vr=0
        self.czas_ekst5_vr=0
        self.czas_ekst6_vr=0
        self.czas_ekst7_vr=0
        self.czas_ekst8_vr=0
        self.czas_ekst9_vr=0
        self.czas_ekst10_vr=0
        ##Zmienna warunkujaca czy zostal zastosowany tryb automatycznego przekierowywania
        self.auto=0
        ############Mapa AirSim#######################
        self.scene=QtWidgets.QGraphicsScene()
        self.ui.AirSimNH_GV.setScene(self.scene)
        self.ui.AirSimNH_GV.setInteractive(True)
        self.ui.AirSimNH_GV.wheelEvent=handle_wheel_event
        self.ui.AirSimNH_GV.scale(2,2)
        GV_Background=QImage(":/Zdjecia/Zdjecia/AirSimNH.png")
        self.scene.setBackgroundBrush(GV_Background)
        self.scene.setSceneRect(600,100,GV_Background.width(),GV_Background.height())
        #Rozmiar obrazka drona przesuwającego się po mapie#
        x=12
        Drone_Background=QImage(":/icons/Icons/Magisterka_python(1)/icons8-drone-12.png").scaled(x,x,Qt.KeepAspectRatio,Qt.FastTransformation)
        self.rect=QtWidgets.QGraphicsRectItem(0,0,x,x)
        self.rect.setPen(Qt.NoPen)
        self.rect.setPos(2038,1548)
        self.rect.setBrush(Drone_Background)
        self.scene.addItem(self.rect) 
        self.ui.AirSimNH_GV.centerOn(self.rect)
        ########Tabela z tresciami misji####################
        self.ui.Misje_male.setColumnWidth(0,400)
        self.ui.Misje_male.setColumnWidth(1,100)
        self.ui.Misje_male.setColumnWidth(2,100)
        self.ui.Misje_male.setColumnWidth(3,100)
        self.ui.Misje_male.setVisible(False)
        self.ui.label_66.setVisible(False)
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page0)
        self.ui.stackedWidget_3.setCurrentWidget(self.ui.page0_2)
        #Definicja początkowych tooltipów dla diód sygnalizacyjnych#
        self.ui.emocje_LED.setToolTip("Emocje nie są jeszcze rozpoznawane")
        self.ui.tetno_LED.setToolTip("Brak połączenia z czujnikiem tętna")
        #Definicja liczników wystąpienia poszczególnych emocji#
        self.angry1=0
        self.disgusted1=0
        self.fear1=0
        self.happy1=0
        self.sad1=0
        self.surprised1=0
        self.neutral1=0
        #Definicja domyślnego numeru kamerki#
        self.camera_number=0
        #Wywołanie metody zmieniającej kamerki#
        self.CameraChanged()
        #Definicja początkowych numerów pól określających PORT#
        self.ui.comboBox_4.setCurrentIndex(7)
        self.ui.comboBox_5.setCurrentIndex(16)
        index=self.ui.comboBox_4.currentIndex()
        self.COM_nr="COM{}".format(index)
        self.baudrate=115200
        #######Zmienna do zmiany obrazka tetna###############
        self.kolorobrazka=0
        #########Dostosowywanie wskaznikow####################################################################   
        ###########################################################################################
        #Wskaznik predkosci
        ##########################################################################################
        self.ui.widget.units="m/s"
        self.ui.widget.minValue=0
        self.ui.widget.maxValue=40
        self.ui.widget.scalaCount=10
        self.ui.widget.enableBarGraph=False
        self.ui.widget.setCustomGaugeTheme(
            color1="#0a0a22",
            color2="#1b1b20"
        )
        self.ui.widget.setEnableNeedlePolygon(True)
        self.ui.widget.setNeedleCenterColor(color1="#0a0a22")
        self.ui.widget.setScalePolygonColor(
            color1="red",
            color2="yellow",
            color3="green"
        )
        self.ui.widget.setScaleValueColor(255,255,255,255)
        self.ui.widget.setDisplayValueColor(255,255,255,255)
        self.ui.widget.setFineScaleColor("white")
        self.ui.widget.setBigScaleColor("white")
        self.ui.widget.setNeedleColor(255,255,255,255)
        ###########################################################################
        #Wskaznik wysokosci
        ##########################################################################
        self.ui.widget_2.units=""
        self.ui.widget_2.minValue=0
        self.ui.widget_2.scalaCount=10
        self.ui.widget_2.maxValue=100
        self.ui.widget_2.enableBarGraph=False
        self.ui.widget_2.setCustomGaugeTheme(
            color1="#0a0a22",
        )
        self.ui.widget_2.setEnableNeedlePolygon(False)
        self.ui.widget_2.setNeedleCenterColor(color1="#0a0a22")
        self.ui.widget_2.setScalePolygonColor(
            color1="red",
            color2="yellow",
            color3="green"
        )
        self.ui.widget_2.setScaleValueColor(255,255,255,255)
        self.ui.widget_2.setDisplayValueColor(255,255,255,255)
        self.ui.widget_2.setFineScaleColor("white")
        self.ui.widget_2.setBigScaleColor("white")
        #######################################################
        #Wskaznik czasu
        #######################################################
        self.ui.widget_3.units="s"
        self.ui.widget_3.minValue=0
        self.ui.widget_3.maxValue=45
        self.ui.widget_3.enableBarGraph=False
        self.ui.widget_3.setCustomGaugeTheme(
            color1="#ffffff"
        )
        ##########Kamerka#################################################################################
        os.environ["OPENCV_VIDEOIO_DEBUG"]="1"
        os.environ["OPENCV_VIDEOIO_PRIORITY_MSMF"]="0"
        cv2.destroyAllWindows()
        #####Klasyfikator kaskadowy dla znajdywania twarzy################################################
        path = os.path.dirname(cv2.__file__)
        self.clf =cv2.CascadeClassifier(path+r"\data\haarcascade_frontalface_default.xml")
        #####Rozmiar twarzy (w pikselach) ktora bedzie interpretowana przez model#######################################
        self.img_size=128
        #####Wczytanie modelu sieci do rozpoznawania emocji###############################################
        self.model=load_model(self.path+r"\model_rozpoznawanie_emocji_moj_2.h5")
        ####Wczytanie modeli do oceny predyspozycji######################################################
        self.model_misje=load_model(self.path+r"\model_misje.h5")
        self.model_tetno=load_model(self.path+r"\model_tetno.h5")
        self.model_twarz=load_model(self.path+r"\model_twarze.h5")
        self.model_tetnoVR=load_model(self.path+r"\model_tetno_vr.h5")
        ####Flaga determinujaca czy zamknac rozpoznanie emocji############################################
        self.flaga=0
        #########Zapisywanie#############################################################################
        self.ui.Save.setVisible(False)
        self.ui.Save_2.setVisible(False)
        #########Wczytanie pliku#########################################################################
        self.data2=pd.read_csv(self.path+r"\Dane_z_lotu.csv")
        ###Poruszanie oknem###############################################################################  
        self.ui.header_frame.mouseMoveEvent = moveWindow
        ###########AirSim-exeute########################################################################
        self.ui.Run_AirSim.clicked.connect(lambda:self.AirSimGo())
        ##########AirSim-polaczenie z aplikacja#########################################################
        self.ui.Run_AirSim.clicked.connect(lambda:self.Connect())
        ###########Wybor Mapy - powiazanie ze zmiana przycisku##########################################
        self.ui.Btn_Aband.clicked.connect(lambda:self.AbandonedPark())
        self.ui.Btn_Africa.clicked.connect(lambda:self.Africa())
        self.ui.Btn_AirSimNH.clicked.connect(lambda:self.AirSimNH())
        self.ui.Btn_Blocks.clicked.connect(lambda:self.Blocks())
        self.ui.Btn_Land.clicked.connect(lambda:self.LandscapeMountains())
        self.ui.btn_MSBuild.clicked.connect(lambda:self.MSBuild())
        self.ui.btn_ZJ.clicked.connect(lambda:self.ZJ())
        ###########Wybor Mapy - VR #####################################################################
        self.ui.VR_AirSimNH.clicked.connect(lambda:self.VR_AirSimNH())
        self.ui.VR_africa.clicked.connect(lambda:self.VR_Africa())
        self.ui.VR_abandoned.clicked.connect(lambda:self.VR_Abandoned())
        self.ui.VR_blocks.clicked.connect(lambda:self.VR_Blocks())
        self.ui.VR_landscape.clicked.connect(lambda:self.VR_Landscape())
        self.ui.VR_MSBuild.clicked.connect(lambda:self.VR_MSBuild2018())
        ###########Wybor rozdzielczosci - powiazanie ze zmiana przycisku################################
        self.ui.x1920_btn.clicked.connect(lambda:self.x1920x1080())
        self.ui.x1024x720_btn.clicked.connect(lambda:self.x1024x720())
        self.ui.x1200x800_btn.clicked.connect(lambda:self.x1200x800())
        self.ui.x1366x768_btn.clicked.connect(lambda:self.x1366x768())
        self.ui.x1440x900_btn.clicked.connect(lambda:self.x1440x900())
        self.ui.x1600x900_btn.clicked.connect(lambda:self.x1600x900())
        self.ui.x1680x1050_btn.clicked.connect(lambda:self.x1680x1050())
        ####Przyciski menu i powiązanie ich ze zdarzeniami##############################################
        self.ui.Menu_button.clicked.connect(lambda:self.slideLeftMenu())
        self.ui.Home_button.clicked.connect(lambda:self.Home())
        self.ui.Informacje_button.clicked.connect(lambda:self.Informacje())
        self.ui.Misje_button.clicked.connect(lambda:self.Misje())
        self.ui.Parametry_button.clicked.connect(lambda:self.Parametry())
        self.ui.Przewodnik_button.clicked.connect(lambda:self.Przewodnik())
        self.ui.Settings_button.clicked.connect(lambda:self.Settings())
        self.ui.Analiza_button.clicked.connect(lambda:self.Analiza())
        ####Zmienna warunkująca zmiane koloru przycisku po zakonczeniu badania w VR#####################
        self.zmiana_przycisk=0
        #####VR#########################################################################################
        self.ui.VR_Button.clicked.connect(lambda:self.VR())
        self.ui.VR_start.clicked.connect(lambda:self.VR_start())
        self.ui.VR_start.clicked.connect(lambda:self.Connect_VR())
        #self.ui.landing_button.clicked.connect(lambda:MainWindow.VR_landing(self))
        self.ui.Clear_button.clicked.connect(lambda:self.clean_all_processes())
        #########Przycisk misji i powiązanie go ze zdarzeniem###########################################
        self.ui.Misje_Button.clicked.connect(lambda:self.Misje_badawcze())
        ##########Strona startowa#######################################################################
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page)
        ##########Mapa AirSimNH na start################################################################
        self.ui.stackedWidget_mapy.setCurrentWidget(self.ui.AirSimNH_mapa)
        ##########Powiazanie zmiany strony ze zmiana stylu frame od przyciskow sidebar##################
        self.ui.stackedWidget.currentChanged.connect(lambda:self.Changing_Frame())
        ##########Powiazanie zegara z aktualizacja parametrow###########################################
        self.timer.timeout.connect(lambda:self.Parametry_send())
        ##########Powiazanie zegara z aktualizacja parametrow VR #######################################
        self.timer_VR.timeout.connect(lambda:self.Parametry_send_VR())
        #########Podglad kamerki#######################################################################
        self.ui.Camera_button.clicked.connect(lambda:self.Camera_showing())
        #########Zapisywanie do pliku danych############################################################
        self.ui.Save.clicked.connect(lambda:self.Save_data())
        self.ui.Save_2.clicked.connect(lambda:self.Save_data2())
        ########Generowanie wykresów###################################################################
        self.ui.Wykresy.clicked.connect(lambda:self.Generacja_wykresow())
        ##########Zaokraglone narożniki#################################################################
        self.ui.centralwidget.setStyleSheet(self.stylesheet_corners)
        #######Przełączanie między wykresami###########################################################
        self.ui.comboBox.currentIndexChanged.connect(lambda:self.tetno_wykresy())
        self.ui.comboBox_2.currentIndexChanged.connect(lambda:self.tetno_wykresy2())
        self.ui.comboBox_3.currentIndexChanged.connect(lambda:self.tetno_wykresy3())
        #######Przełączanie numeru portu################################################################
        self.ui.comboBox_4.currentIndexChanged.connect(lambda:self.COM())
        #######Przęłączanie baudrate###################################################################
        self.ui.comboBox_5.currentIndexChanged.connect(lambda:self.Baudrate())
        #######Zmiana indeksu kamerki##################################################################
        self.ui.comboBox_6.currentIndexChanged.connect(lambda:self.CameraChanged())
        ######Generowanie wykresow#####################################################################
        self.ui.Wykresy_2.setVisible(False)
        self.ui.Wykresy_2.clicked.connect(lambda:self.Generacja_wykresowVR())
        #####Przejscie do VR po pierwszym badaniu#####################################################
        self.ui.VR_wspolne.clicked.connect(lambda:self.VR_wspolne())
        ####Ramki instrukcji##########################################################################
        self.ui.pushButton.clicked.connect(lambda:self.instrukcja())
        self.timer_cytat=QTimer()
        self.timer_cytat.start(20000)
        self.timer_cytat.timeout.connect(lambda:self.zmien_cytaty())
        #########Wątek z tętnem########################################################################
        self.pool=QThreadPool()
        #Definicja zmiennej określającej czy udało się otworzyć PORT do przesyłania tętna y=1 tak, y=0 nie#
        self.y=1
        #Definicja zmiennej określającej czy mają zostać pokazane uwagi dotyczące PORTu i symulatora###
        self.uwaga_port=0
        self.uwaga_symulator=0
        ###############Pokaż okno######################################################################
        self.show()
        ######Pokazanie msgboxa na poczatku - czy chcesz do instrukcji?##############################
        self.timer_auto_box=QTimer()
        self.timer_auto_box.start(2000)
        self.timer_auto_box.timeout.connect(lambda:self.Auto_box())    
###############FUNKCJE/ZDARZENIA############################################################################
#########################################################################################################
#########################################################################################################
    ######Funkcja do przesyłu tętna ####################################################################
    def tetno_thread(self):
        self.ser=serial.Serial(self.COM_nr,baudrate=self.baudrate)
        if self.ser.is_open == False:
                self.y=0
        while self.y==1:
            data=self.ser.readline().decode('utf-8')
            data=float(data)
            data/=1000.0
            self.tetno_update(data)
    ######Funkcja zmieniajaca numer portu################################################################
    def COM(self):
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Porównaj wybrany numer portu z tym, który został przydzielony w menedżerze urządzeń!")
        #msgbox.setWindowTitle("Istotna uwaga")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
        index=self.ui.comboBox_4.currentIndex()
        self.COM_nr="COM{}".format(index)
    ######Funkcja zmieniająca baudrate portu############################################################
    def Baudrate(self):
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Czujnik działa prawidłowo przy wartości 115200 baud/s! Sprawdź czy w menedżerze urządzń również jest ustawiona ta wartość.")
        #msgbox.setWindowTitle("Istotna uwaga")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
        index=self.ui.comboBox_5.currentIndex()
        match index:
            case 0:
                self.baudrate=75
            case 1:
               self.baudrate=110
            case 2:
                self.baudrate=134
            case 3:
               self.baudrate=150
            case 4:
                self.baudrate=300
            case 5:
                self.baudrate=600
            case 6:
                self.baudrate=1200
            case 7:
               self.baudrate=1800
            case 8:
                self.baudrate=2400
            case 9:
                self.baudrate=4800
            case 10:
                self.baudrate=7200
            case 11:
                self.baudrate=9600
            case 12:
                self.baudrate=14400
            case 13:
                self.baudrate=19200
            case 14:
                self.baudrate=38400
            case 15:
                self.baudrate=57600
            case 16:
                self.baudrate=115200    
            case 17:
                self.baudrate=128000           
    ######Funkcja zmieniajaca indeks kamerki############################################################
    def CameraChanged(self):
        self.x=1
        self.cam=cv2.VideoCapture(self.camera_number)
        if self.camera_changed !=0:
            msgbox=QMessageBox()
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText("Upewnij się, że indeks kamerki został wybrany prawidłowo")
            #msgbox.setWindowTitle("Istotna uwaga")
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
            msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            x=msgbox.exec_()
        index=self.ui.comboBox_6.currentIndex()
        self.camera_number=index
        self.camera_changed+=1
    ######Funkcja zmieniajca cytaty w oknie z predykcjam###############################################
    def zmien_cytaty(self):
        x=random.randrange(0,10)
        self.ui.mysl.setText(self.cytaty[x])
        self.ui.Autor.setText(self.autor[x])
    #####Funkcja przewijania instrukcji################################################################
    def instrukcja(self):
        match self.instruction_count:
            case 0:
                self.ui.frame_93.setVisible(True)
            case 1:
                self.ui.frame_92.setVisible(True)
            case 2:
                self.ui.frame_91.setVisible(True)
            case 3:
                self.ui.frame_90.setVisible(True)
            case 4:
                self.ui.frame_89.setVisible(True)
            case 5:
                self.ui.frame_88.setVisible(True)
            case 6:
                self.ui.frame_87.setVisible(True)
            case 7:
                self.ui.frame_86.setVisible(True)
            case 8:
                self.ui.frame_85.setVisible(True)
            case 9:
                self.ui.frame_84.setVisible(True)
            case 10:
                self.ui.frame_83.setVisible(True)
            case 11:
                self.ui.frame_82.setVisible(True)
            case 12:
                self.ui.frame_81.setVisible(True)
        self.instruction_count+=1
        ###Ozdoba w tutorial page####################################################
        self.ui.frame_94.setVisible(True)
    ####Przelaczanie miedzy badaniami#####################################################
    def VR_wspolne(self):
        os.system(f"TASKKILL /F /IM {self.script_name}")
        self.VR()
    ####Message box czy chcemy instrukcje####################################################
    def Auto_box(self):
        #Efekty tła#
        self.timer_auto_box.stop()
        self.efect=QGraphicsBlurEffect()
        self.setGraphicsEffect(self.efect)
        self.setWindowOpacity(0.9)
        #MessageBox
        msgbox=QMessageBox()
        msgbox.setIconPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-automatic-64.png"))
        msgbox.setGeometry(2520,300,300,300)
        #msgbox.setGeometry(620,300,300,300)
        msgbox.setText("W pierwszej kolejności powinieneś zobaczyć instrukcję obsługi, czy chcesz?")
        msgbox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY=msgbox.button(QMessageBox.Yes)
        buttonY.setText('Tak!')
        buttonX=msgbox.button(QMessageBox.No)
        buttonX.setText('Nie, znam aplikację')
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
        #Cofniecie efektow tla#
        self.setWindowOpacity(1)
        self.efect.setEnabled(False)
        if msgbox.clickedButton() ==buttonY:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Tutorial_page)
    ####Message box czy chcemy przejsc do badania w VR####################################################     
    def Auto_box1(self): 
        #Efekty tła#
        self.timer_auto_box1.stop()
        self.efect10=QGraphicsBlurEffect()
        self.setGraphicsEffect(self.efect10)
        self.setWindowOpacity(0.9)
        #MessageBox
        msgbox1=QMessageBox()
        msgbox1.setIconPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-automatic-64.png"))
        msgbox1.setGeometry(2520,300,300,300)
        msgbox1.setText("Czy chcesz przejsc teraz do badania w VR?")
        msgbox1.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        buttonY1=msgbox1.button(QMessageBox.Yes)
        buttonY1.setText('Tak!')
        buttonX1=msgbox1.button(QMessageBox.No)
        buttonX1.setText('Nie, zostanę przy tym badaniu')
        msgbox1.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox1.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x1=msgbox1.exec_()
        #Cofniecie efektow tla#
        self.setWindowOpacity(1)
        self.efect10.setEnabled(False)
        if msgbox1.clickedButton() == buttonY1:
            self.timer.stop()
            self.isAirSimOpened=0
            os.system(f"TASKKILL /F /IM {self.script_name}")
            self.VR()
            self.przejdzdoVR=1
    ###etoda do znajdywania czasu pomiedzy ekstremami#########################################################
    def znajdz_czas_miedzy_ekstremami(self,tablica=[],czas=[]): 
        maksymalna=max(tablica)
        indeks_maksa=tablica.index(maksymalna)
        minimalna=min(tablica)
        amplituda=maksymalna-minimalna
        indeks_minimum=tablica.index(minimalna)
        czas_miedzy=abs(czas[indeks_maksa]-czas[indeks_minimum])
        if czas_miedzy == 0:
            ratio=0
        else:
            ratio=amplituda/czas_miedzy
        return ratio
     ###Metoda do aktualizacji zmian tętna######################################################################
    def tetno_update(self,val):
        self.ui.tetno_LED.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-green-circle-48.png"))
        self.ui.tetno_LED.setToolTip("Jest połączenie z czujnikiem tętna")
        self.ui.label_141.setText(str(val)) 
        self.ui.Heart_rate.display(val)
        if self.secondwindow == 1:
            self.VR_levels.ui2.tetno.setText(str(val))
            match self.VR_levels.level:
                case 1:
                    self.VR_levels.tetno1.append(val)
                    self.VR_levels.time_samples1.append(time.time())
                case 2:
                    self.VR_levels.tetno2.append(val)
                    self.VR_levels.time_samples2.append(time.time())
                case 3:
                    self.VR_levels.tetno3.append(val)
                    self.VR_levels.time_samples3.append(time.time())
                case 4:
                    self.VR_levels.tetno4.append(val)
                    self.VR_levels.time_samples4.append(time.time())
                case 5:
                    self.VR_levels.tetno5.append(val)
                    self.VR_levels.time_samples5.append(time.time())
                case 6:
                    self.VR_levels.tetno6.append(val)
                    self.VR_levels.time_samples6.append(time.time())
                case 7:
                    self.VR_levels.tetno7.append(val)
                    self.VR_levels.time_samples7.append(time.time())
                case 8:
                    self.VR_levels.tetno8.append(val)
                    self.VR_levels.time_samples8.append(time.time())
                case 9: 
                    self.VR_levels.tetno9.append(val)
                    self.VR_levels.time_samples9.append(time.time())
                case 10:
                    self.VR_levels.tetno10.append(val)
                    self.VR_levels.time_samples10.append(time.time())
        match self.levelpassed:    
            case 0:
                self.tetno1.append(val)
                self.time_samples1.append(time.time())
            case 1:
                self.tetno2.append(val)
                self.time_samples2.append(time.time())
            case 2:
                self.tetno3.append(val)
                self.time_samples3.append(time.time())
            case 3:
                self.tetno4.append(val)
                self.time_samples4.append(time.time())
            case 4:
                self.tetno5.append(val)
                self.time_samples5.append(time.time())
            case 5:
                self.tetno6.append(val)
                self.time_samples6.append(time.time())
            case 6:
                self.tetno7.append(val)
                self.time_samples7.append(time.time())
            case 7:
                self.tetno8.append(val)
                self.time_samples8.append(time.time())
            case 8:
                self.tetno9.append(val)
                self.time_samples9.append(time.time())
            case 9:
                self.tetno10.append(val)
                self.time_samples10.append(time.time())
    def most_frequent(self,List):
        counter = 0
        num = List[0]
        for i in List:
            curr_frequency = List.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                num = i
        return num
     
#Przesyl parametrow w trakcie badania w pierwszym etapie#####################################################
    def Parametry_send(self):
      if self.isAirSimOpened==1:
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        self.time=self.time+1
        ###############Wysyłanie parametrow do LCD Number#################################################
        position=state.kinematics_estimated.position
        orientation=client.simGetVehiclePose().orientation
        pitch,roll,yaw=airsim.to_eularian_angles(orientation)
        velocity=state.kinematics_estimated.linear_velocity
        radianstodegree=180/3.14
        pitch=pitch*radianstodegree
        roll=roll*radianstodegree
        yaw=yaw*radianstodegree
        self.ui.Odchylenie.display(f"{yaw:.2f}")
        self.ui.Przechylenie.display(f"{roll:.2f}")
        self.ui.Pochylenie.display(f"{pitch:.2f}")
        height=position.z_val*(-1)
        self.ui.Wysokosc.display(f"{height:.2f}")
        self.ui.Pozycja_X.display(f"{position.x_val:.2f}")
        self.ui.pozycja_Y.display(f"{position.y_val:.2f}")
        self.ui.Predkosc_X.display(f"{velocity.x_val:.2f}")
        self.ui.Predkosc_Y.display(f"{velocity.y_val:.2f}")
        self.ui.Predkosc_Z.display(f"{velocity.z_val:.2f}")
        self.ui.Czas.display(f"{self.time:.2f}")
        vel=math.sqrt(math.pow(velocity.x_val,2)+math.pow(velocity.y_val,2)+math.pow(velocity.z_val,2))
        self.ui.Predkosc.display(f"{vel:.2f}")
        #################Liczniki#############################################
        self.ui.widget.updateValue(vel,False)
        self.ui.widget_2.updateValue(height,False)
        ################Rozpoznawanie emocji##################################
        #self.Camera_show()
        ################Dane z serialporta (Tętno)############################
        if self.kolorobrazka==0:
         self.ui.label_143.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-heart-rate-50-1.png"))
         if self.secondwindow==1:
            self.VR_levels.ui2.label_2.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-heart-rate-50-1.png"))
         self.kolorobrazka=1
        else: 
         self.ui.label_143.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-heart-rate-50.png"))
         if self.secondwindow==1:
            self.VR_levels.ui2.label_2.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-heart-rate-50.png"))
         self.kolorobrazka=0  
        ##################Mapa################################################
        transform=QTransform()
        transform.translate(position.y_val*4,position.x_val*-4)
        self.rect.setTransform(transform)
        self.ui.AirSimNH_GV.centerOn(self.rect)
##### Przesył parametrów do VRa ##########################################################################
    def Parametry_send_VR(self):
        if self.connection_VR==1:
            client=airsim.MultirotorClient()
            state=client.getMultirotorState()
            self.time_VR=self.time_VR+1
            if(VR_Levels.VR_repeat==1):
               self.time_VR=0
            ###############Wysyłanie parametrow do LCD Number#################################################
            position2=state.kinematics_estimated.position
            orientation2=client.simGetVehiclePose().orientation
            pitch2,roll2,yaw2=airsim.to_eularian_angles(orientation2)
            velocity2=state.kinematics_estimated.linear_velocity
            radianstodegree=180/3.14
            pitch2=pitch2*radianstodegree
            roll2=roll2*radianstodegree
            yaw2=yaw2*radianstodegree
            self.ui.Odchylenie_2.display(f"{yaw2:.2f}")
            self.ui.Przechylenie_2.display(f"{roll2:.2f}")
            self.ui.Pochylenie_2.display(f"{pitch2:.2f}")
            height=position2.z_val*(-1)
            self.ui.Wysokosc_2.display(f"{height:.2f}")
            self.ui.Pozycja_X_2.display(f"{position2.x_val:.2f}")
            self.ui.pozycja_Y_2.display(f"{position2.y_val:.2f}")
            self.ui.Predkosc_X_2.display(f"{velocity2.x_val:.2f}")
            self.ui.Predkosc_Y_2.display(f"{velocity2.y_val:.2f}")
            self.ui.Predkosc_Z_2.display(f"{velocity2.z_val:.2f}")
            self.ui.Czas_2.display(f"{self.time_VR:.2f}")
            vel2=math.sqrt(math.pow(velocity2.x_val,2)+math.pow(velocity2.y_val,2)+math.pow(velocity2.z_val,2))
            self.ui.Predkosc_2.display(f"{vel2:.2f}")
            ####Jeżeli dotrze sygnał z VR_levels o koncu badania to przycisk do zapisu wyników sie pojawia####
            if self.VR_levels.koniec==1 and self.przejdzdoVR==1:
                self.ui.Save_2.setVisible(True)
            if self.VR_levels.koniec_koncow==1:
                if self.zmiana_przycisk==0:
                    self.ui.Save_2.setStyleSheet("QPushButton:hover{background-color: rgb(30, 32, 34);}QPushButton{background-color: rgb(0, 0, 127);border-radius:20px;border: 3px;}")
                    self.zmiana_przycisk=1
                else:
                    self.ui.Save_2.setStyleSheet("QPushButton:hover{background-color: rgb(30, 32, 34);}QPushButton{background-color: qlineargradient(spread:pad, x1:0.005, y1:0, x2:1, y2:1, stop:0 rgba(52, 43, 52, 255), stop:1 rgba(0, 8, 36, 255));border-radius:20px;border: 3px;}")  
                    self.zmiana_przycisk=0  
            #DODAWANIE PARAMETROW DO TABELI 
            #sql="INSERT INTO "+self.nazwatabeli+"""(wysokosc, pozycja_X, pozycja_Y, Predkosc_X, Predkosc_Y, Predkosc_Z) VALUES (%s,%s,%s,%s,%s,%s)""" 
            #val=height,position2.x_val,position2.y_val,velocity2.x_val,velocity2.y_val,velocity2.z_val
            #self.mycursor.execute(sql,val)
            #self.mydb.commit()
    ####Metoda do rozpoczecia badania pierwszego etapu##############################################
    def Misje_badawcze(self):
        if self.isAirSimOpened==1:
            self.levelpassed=0
            self.ui.label_70.setVisible(False)
            self.ui.Misje_Button.setVisible(False)
            self.ui.Misje_male.setVisible(True)
            self.ui.label_66.setVisible(True)
            self.ui.VR_Button.setEnabled(False)
            self.ui.Camera_button.setEnabled(False)
            self.ui.Run_AirSim.setEnabled(False)
            client=airsim.MultirotorClient()
            
            self.misja_time=QTimer(self)
            self.misja_time.start(1000)
            self.emocje_reading=1
            self.worker1=Worker1(self.Camera_show)
            self.pool.start(self.worker1)
            self.tetno=TetnoThread(self.tetno_thread)
            self.pool.start(self.tetno)
            self.misja_time.timeout.connect(lambda:self.Poziomy())      
    ####Metoda do zmiany poziomow###################################################################
    def Poziomy(self):
        if self.isAirSimOpened==1 and self.y==1:
            client=airsim.MultirotorClient()
            state=client.getMultirotorState()
            position=state.kinematics_estimated.position
            match self.levelpassed:
                case 0:
                    self.level1()
                    ####Odgrywanie dzwieku z trescia misji#####################
                    if self.czas_l1==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level1.wav",winsound.SND_FILENAME)
                        
                        
                    self.czas_l1=self.czas_l1+1
                    self.ui.label_66.setText("Poleć na współrzędne (30,-30)")
                    self.ui.Misje_male.item(0,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(0,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(0,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(0,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l1,False)
                case 1:
                    self.level2()
                    if self.czas_l2==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level2.wav",winsound.SND_FILENAME)
                    self.czas_l2=self.czas_l2+1
                    self.ui.label_66.setText("Będąc w pułapie wysokości (20,25) poleć na współrzędne (-15,15)")
                    self.ui.Misje_male.item(0,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(0,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(0,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(0,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(1,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(1,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(1,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(1,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l2,False)
                    self.czas_ekst1=self.znajdz_czas_miedzy_ekstremami(self.tetno1,self.time_samples1)
                case 2:
                    if self.czas_l3==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level3.wav",winsound.SND_FILENAME)
                        
                    self.czas_l3=self.czas_l3+1
                    self.level3()
                    self.ui.label_66.setText("Wyląduj we współrzędnych (10,10) ")
                    self.ui.Misje_male.item(1,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(1,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(1,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(1,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(2,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(2,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(2,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(2,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l3,False)
                    self.czas_ekst2=self.znajdz_czas_miedzy_ekstremami(self.tetno2,self.time_samples2)
                case 3:
                    if self.czas_l4==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level4.wav",winsound.SND_FILENAME)
                        
                    self.czas_l4=self.czas_l4+1
                    self.level4()
                    self.ui.label_66.setText("Poleć na współrzędne (30,30) i osiągnij wysokość 50 metrów")
                    self.ui.Misje_male.item(2,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(2,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(2,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(2,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(3,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(3,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(3,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(3,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l4,False)
                    self.czas_ekst3=self.znajdz_czas_miedzy_ekstremami(self.tetno3,self.time_samples3)
                case 4:
                    if self.czas_l5==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level5.wav",winsound.SND_FILENAME)
                    self.czas_l5=self.czas_l5+1
                    self.level5()
                    self.ui.label_66.setText("Poleć na współrzędne (-20,-20) osiągając prędkość 20 wezlow/s")
                    self.ui.Misje_male.item(3,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(3,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(3,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(3,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(4,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(4,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(4,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(4,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l5,False)
                    self.czas_ekst4=self.znajdz_czas_miedzy_ekstremami(self.tetno4,self.time_samples4)
                case 5:
                    if self.czas_l6==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level6.wav",winsound.SND_FILENAME)
                    self.czas_l6=self.czas_l6+1
                    self.level6()
                    self.ui.label_66.setText("Wyląduj we współrzędnych (0,0)")
                    self.ui.Misje_male.item(4,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(4,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(4,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(4,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(5,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(5,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(5,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(5,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l6,False)
                    self.czas_ekst5=self.znajdz_czas_miedzy_ekstremami(self.tetno5,self.time_samples5)
                case 6:
                    if self.czas_l7==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level7.wav",winsound.SND_FILENAME)
                    self.czas_l7=self.czas_l7+1
                    self.level7()
                    self.ui.label_66.setText("Poleć na współrzędne (15,15) {wiatr 2wezly/s)")
                    self.ui.Misje_male.item(5,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(5,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(5,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(5,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(6,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(6,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(6,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(6,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l7,False)
                    self.czas_ekst6=self.znajdz_czas_miedzy_ekstremami(self.tetno6,self.time_samples6)
                case 7:
                    if self.czas_l8==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level8.wav",winsound.SND_FILENAME)
                    self.czas_l8=self.czas_l8+1
                    self.level8()
                    self.ui.label_66.setText("Poleć na współrzędne (-10,-10) i zawiśnij w pułapie (15,20) {wiatr 2wezly/s)")
                    self.ui.Misje_male.item(6,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(6,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(6,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(6,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(7,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(7,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(7,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(7,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l8,False)
                    self.czas_ekst7=self.znajdz_czas_miedzy_ekstremami(self.tetno7,self.time_samples7)
                case 8:
                    if self.czas_l9==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level9.wav",winsound.SND_FILENAME)
                    self.czas_l9=self.czas_l9+1
                    self.level9()
                    self.ui.label_66.setText("Poleć na współrzędne (-45,-20) nie przekraczając wysokości 20 {wiatr 5 wezlow/s)")
                    self.ui.Misje_male.item(7,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(7,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(7,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(7,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(8,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(8,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(8,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(8,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l9,False)
                    self.czas_ekst8=self.znajdz_czas_miedzy_ekstremami(self.tetno8,self.time_samples8)
                case 9:
                    if self.czas_l10==0:
                        winsound.PlaySound(self.path+r"\Nagrania_dzwiek\Level10.wav",winsound.SND_FILENAME)
                    self.czas_l10=self.czas_l10+1
                    self.level10()
                    self.ui.label_66.setText("Wyląduj we współrzędnych (0,0) {wiatr 7.5 wezlow/s}")
                    self.ui.Misje_male.item(8,0).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(8,1).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(8,2).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(8,3).setBackground(QColor(24,24,48))
                    self.ui.Misje_male.item(9,0).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(9,1).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(9,2).setBackground(QColor(13,48,186))
                    self.ui.Misje_male.item(9,3).setBackground(QColor(13,48,186))
                    self.ui.widget_3.updateValue(30.0-self.czas_l10,False)
                    self.czas_ekst9=self.znajdz_czas_miedzy_ekstremami(self.tetno9,self.time_samples9)
                case 10: 
                    self.misja_time.stop()
                    ####Obliczanie parametrow ktore zostana zapisane do pliku################
                    self.l1_t=sum(self.tetno1)/len(self.tetno1)
                    self.l2_t=sum(self.tetno2)/len(self.tetno2)
                    self.l3_t=sum(self.tetno3)/len(self.tetno3)
                    self.l4_t=sum(self.tetno4)/len(self.tetno4)
                    self.l5_t=sum(self.tetno5)/len(self.tetno5)
                    self.l6_t=sum(self.tetno6)/len(self.tetno6)
                    self.l7_t=sum(self.tetno7)/len(self.tetno7)
                    self.l8_t=sum(self.tetno8)/len(self.tetno8)
                    self.l9_t=sum(self.tetno9)/len(self.tetno9)
                    self.l10_t=sum(self.tetno10)/len(self.tetno10)
                    self.l1_f=self.most_frequent(self.emocje1)
                    self.l1_f=np.round(self.l1_f)
                    self.l2_f=self.most_frequent(self.emocje2)
                    self.l2_f=np.round(self.l2_f)
                    self.l3_f=self.most_frequent(self.emocje3)
                    self.l3_f=np.round(self.l3_f)
                    self.l4_f=self.most_frequent(self.emocje4)
                    self.l4_f=np.round(self.l4_f)
                    self.l5_f=self.most_frequent(self.emocje5)
                    self.l5_f=np.round(self.l5_f)
                    self.l6_f=self.most_frequent(self.emocje6)
                    self.l6_f=np.round(self.l6_f)
                    self.l7_f=self.most_frequent(self.emocje7)
                    self.l7_f=np.round(self.l7_f)
                    self.l8_f=self.most_frequent(self.emocje8)
                    self.l8_f=np.round(self.l8_f)
                    self.l9_f=self.most_frequent(self.emocje9)
                    self.l9_f=np.round(self.l9_f)
                    self.l10_f=self.most_frequent(self.emocje10)
                    self.l10_f=np.round(self.l10_f)
                    self.twarze=[self.l1_f,
                                self.l2_f,
                                self.l3_f,
                                self.l4_f,
                                self.l5_f,
                                self.l6_f,
                                self.l7_f,
                                self.l8_f,
                                self.l9_f,
                                self.l10_f]
                    self.czas_ekst10=self.znajdz_czas_miedzy_ekstremami(self.tetno10,self.time_samples10)
                    self.ui.Save.setVisible(True)
                    self.ui.Wykresy.setVisible(True)
                    #self.ui.VR_wspolne.setVisible(True)
                    self.timer_auto_box1=QTimer()
                    self.timer_auto_box1.start(2000)
                    self.timer_auto_box1.timeout.connect(lambda:self.Auto_box1())
                    self.ui.Run_AirSim.setEnabled(False)
                    self.emocje_reading=0
        elif self.y==0 and self.uwaga_port==0:
            self.message("PORT NIE JEST OTWARTY!")
            self.uwaga_port=1
        elif self.isAirSimOpened==0 and self.uwaga_symulator==0:
            self.message("Symulator nie jest włączony")
            self.uwaga_symulator=1      
##############POZIOMY PIERWSZEGO BADANIA#########################################################################################
                    
#####################################################################################################
    #### Poziom 1 #####
    def level1(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)           
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity
           client.simPrintLogMessage("Polec na wspolrzedne (30,-30)",severity=2)       
           client.simPlotArrows([position],[airsim.Vector3r(30,-30,0)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)
           if (position.x_val>20) and (position.x_val<40) and (position.y_val>-40) and (position.y_val<-20) and self.czas_l1<30:
            client.simPrintLogMessage("Poziom 1"," Zaliczony")
            self.ui.Misje_male.item(0,3).setText("Zaliczony")
            self.levelpassed=1
            self.l1_w=1
           elif self.czas_l1>=30: 
            client.simPrintLogMessage("Poziom 1"," Niezaliczony") 
            self.ui.Misje_male.item(0,3).setText("Niezaliczony")
            self.levelpassed=1
            self.l1_w=0
           self.l1_c=self.czas_l1
    #### Poziom 2 #####
    def level2(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)           
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity           
           client.simPrintLogMessage("Bedac w pulapie wysokosci (20,25) polec na wspolrzedne (-15,15)",severity=2)
           client.simPlotArrows([position],[airsim.Vector3r(-15,15,20)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)       
           if (position.x_val>-20) and (position.x_val<-10) and (position.y_val>10) and (position.y_val<25) and (position.z_val<-17.5) and (position.z_val>-27.5) and self.czas_l2<30:
            client.simPrintLogMessage("Poziom 2"," Zaliczony")
            self.ui.Misje_male.item(1,3).setText("Zaliczony")
            self.l2_w=1
            self.levelpassed=2
           elif self.czas_l2>=30: 
            client.simPrintLogMessage("Poziom 2"," Niezaliczony") 
            self.ui.Misje_male.item(1,3).setText("Niezaliczony")
            self.levelpassed=2
            self.l2_w=0
           self.l2_c=self.czas_l2
    #### Poziom 3 #####
    def level3(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)           
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity 
           client.simPrintLogMessage("Wyladuj we wspolrzednych (10,10) ",severity=2) 
           client.simPlotArrows([position],[airsim.Vector3r(10,10,0)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)          
           if (position.x_val>5) and (position.x_val<15) and (position.y_val>5) and (position.y_val<15) and self.czas_l3<30 and velocity.z_val<0.05:
            client.simPrintLogMessage("Poziom 3"," Zaliczony")
            self.ui.Misje_male.item(2,3).setText("Zaliczony")
            self.l3_w=1
            self.levelpassed=3
           elif self.czas_l3>=30: 
            client.simPrintLogMessage("Poziom 3"," Niezaliczony") 
            self.ui.Misje_male.item(2,3).setText("Niezaliczony")
            self.levelpassed=3
            self.l3_w=0
           self.l3_c=self.czas_l3
    #### Poziom 4 #####                           
    def level4(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)          
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity
           client.simPrintLogMessage("Polec na wspolrzedne (30,30) i osiagnij wysokosc 50 metrow",severity=2) 
           client.simPlotArrows([position],[airsim.Vector3r(30,30,-50)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)
           if (position.x_val>25) and (position.x_val<35 ) and (position.y_val>25) and (position.y_val<35) and (position.z_val<-47.5)  and self.czas_l4<30:
            client.simPrintLogMessage("Poziom 4"," Zaliczony")
            self.ui.Misje_male.item(3,3).setText("Zaliczony")
            self.levelpassed=4
            self.l4_w=1
           elif self.czas_l4>=30: 
            client.simPrintLogMessage("Poziom 4"," Niezaliczony") 
            self.ui.Misje_male.item(3,3).setText("Niezaliczony")
            self.levelpassed=4
            self.l4_w=0
           self.l4_c=self.czas_l4   
    #### Poziom 5 #####           
    def level5(self):
           #########Polaczenie z symulatorem AirSim#############
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           #Pobranie informacji dotyczącej położenia kątowego BSP#
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation) 
           #Pobranie informacji dotyczącej pozycji BSP#         
           position=state.kinematics_estimated.position
           #Pobranie informacji dotyczącej prędkości liniowej BSP#  
           velocity=state.kinematics_estimated.linear_velocity 
           #Pokazanie napisu w oknie symulatora z treśćią misji#
           client.simPrintLogMessage("Polec na wspolrzedne (-20,-20) osiagajac predkosc 20 m/s",severity=2)  
           #Sprawdzanie wykonania misji#
           if (position.x_val>-30) and (position.x_val<-10) and (position.y_val>-30) and (position.y_val<-10)  and self.czas_l5<30:
            client.simPrintLogMessage("Poziom 5"," Zaliczony")
            self.ui.Misje_male.item(4,3).setText("Zaliczony")
            #Zmienna warunkujaca przejscie do kolejnego poziomu#
            self.levelpassed=5
            #Oznaczenie wyniku wykonania misji jako zaliczone#
            self.l5_w=1
           elif self.czas_l5>=30: 
            client.simPrintLogMessage("Poziom 5"," Niezaliczony") 
            self.ui.Misje_male.item(4,3).setText("Niezaliczony")
            #Zmienna warunkujaca przejscie do kolejnego poziomu#
            self.levelpassed=5
            #Oznaczenie wyniku wykonania misji jako niezaliczone#
            self.l5_w=0
           #Oznaczenie czasu wykonania misji#
           self.l5_c=self.czas_l5 
    #### Poziom 6 #####  
    def level6(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)
           radianstodegree=180/3.14
           pitch=pitch*radianstodegree
           roll=roll*radianstodegree
           yaw=yaw*radianstodegree          
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity   
           client.simPrintLogMessage("Wyladuj we wspolrzednych (0,0)",severity=2)  
           client.simPlotArrows([position],[airsim.Vector3r(0,0,0)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)       
           if (position.x_val>-2.5) and (position.x_val<2.5) and (position.y_val>-2.5) and (position.y_val<2.5) and velocity.z_val<0.05 and self.czas_l6<20:
            client.simPrintLogMessage("Poziom 6"," Zaliczony")
            self.ui.Misje_male.item(5,3).setText("Zaliczony")
            self.levelpassed=6
            self.l6_w=1
           elif self.czas_l6>=30: 
            client.simPrintLogMessage("Poziom 6"," Niezaliczony") 
            self.ui.Misje_male.item(5,3).setText("Niezaliczony")
            self.levelpassed=6
            self.l6_w=0
           self.l6_c=self.czas_l6
    #### Poziom 7 #####                            
    def level7(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)
           radianstodegree=180/3.14
           pitch=pitch*radianstodegree
           roll=roll*radianstodegree
           yaw=yaw*radianstodegree          
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity
           client.simSetWind(airsim.Vector3r(1,1,1.5))
           client.simPrintLogMessage("Polec na wspolrzedne (15,15) {wiatr 2wezly/s)",severity=2)
           client.simPlotArrows([position],[airsim.Vector3r(15,15,10)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)            
           if (position.x_val>5) and (position.x_val<25) and (position.y_val>5) and (position.y_val<25) and self.czas_l7<30:
            client.simPrintLogMessage("Poziom 7"," Zaliczony")
            self.ui.Misje_male.item(6,3).setText("Zaliczony")
            self.levelpassed=7
            self.l7_w=1
           elif self.czas_l7>=30: 
            client.simPrintLogMessage("Poziom 7"," Niezaliczony") 
            self.ui.Misje_male.item(6,3).setText("Niezaliczony")
            self.levelpassed=7
            self.l7_w=0
           self.l7_c=self.czas_l7
    #### Poziom 8 #####                         
    def level8(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)
           radianstodegree=180/3.14
           pitch=pitch*radianstodegree
           roll=roll*radianstodegree
           yaw=yaw*radianstodegree          
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity 
           client.simPrintLogMessage("Polec na wspolrzedne (-10,-10) i zawisnij w pulapie (15,20) {wiatr 2wezly/s)",severity=2) 
           client.simPlotArrows([position],[airsim.Vector3r(-10,-10,17.5)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)
           client.simSetWind(airsim.Vector3r(1,1.5,1))          
           if (position.x_val>-15) and (position.x_val<-5) and (position.y_val>-15) and (position.y_val<-5) and (position.z_val<-10) and (position.z_val>-25) and self.czas_l8<30:
            client.simPrintLogMessage("Poziom 8"," Zaliczony")
            self.ui.Misje_male.item(7,3).setText("Zaliczony")
            self.levelpassed=8
            self.l8_w=1
           elif self.czas_l8>=30: 
            client.simPrintLogMessage("Poziom 8"," Niezaliczony") 
            self.ui.Misje_male.item(7,3).setText("Niezaliczony")
            self.levelpassed=8
            self.l8_w=0
           self.l8_c=self.czas_l8   
    #### Poziom 9 #####                     
    def level9(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)
           radianstodegree=180/3.14
           pitch=pitch*radianstodegree
           roll=roll*radianstodegree
           yaw=yaw*radianstodegree          
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity  
           client.simPrintLogMessage("Polec na wspolrzedne (-45,-20) nie przekraczajac wysokosci 20 {wiatr 5 wezlow/s)",severity=2) 
           client.simPlotArrows([position],[airsim.Vector3r(-45,-20,10)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)
           client.simSetWind(airsim.Vector3r(8,8,8))         
           if (position.x_val>-50) and (position.x_val<-40) and (position.y_val>-25) and (position.y_val<-15) and (position.z_val>-22.5) and self.czas_l9<30:
            client.simPrintLogMessage("Poziom 9"," Zaliczony")
            self.ui.Misje_male.item(8,3).setText("Zaliczony")
            self.levelpassed=9
            self.l9_w=1
           elif self.czas_l9>=30: 
            client.simPrintLogMessage("Poziom 9"," Niezaliczony") 
            self.ui.Misje_male.item(8,3).setText("Niezaliczony")
            self.levelpassed=9
            self.l9_w=0
           self.l9_c=self.czas_l9    
    #### Poziom 10 #####                       
    def level10(self):
           client=airsim.MultirotorClient()
           state=client.getMultirotorState()
           orientation=client.simGetVehiclePose().orientation
           pitch,roll,yaw=airsim.to_eularian_angles(orientation)          
           position=state.kinematics_estimated.position
           velocity=state.kinematics_estimated.linear_velocity  
           client.simPrintLogMessage("Wyląduj we współrzędnych (0,0) {wiatr 7.5 wezlow/s}",severity=2) 
           client.simPlotArrows([position],[airsim.Vector3r(0,0,0)],color_rgba=[1,0,0,1],thickness=5,arrow_size=2,duration=1)
           client.simSetWind(airsim.Vector3r(15,15,15))         
           if (position.x_val>-4) and (position.x_val<4) and (position.y_val>-4) and (position.y_val<4) and (velocity.z_val<0.05) and self.czas_l10<30:
            client.simPrintLogMessage("Poziom 10"," Zaliczony")
            self.ui.Misje_male.item(9,3).setText("Zaliczony")
            self.levelpassed=10
            self.l10_w=1
           elif self.czas_l10>=30: 
            client.simPrintLogMessage("Poziom 10"," Niezaliczony") 
            self.ui.Misje_male.item(9,3).setText("Niezaliczony")
            self.levelpassed=10
            self.l10_w=0
           self.l10_c=self.czas_l10                
    #####Metoda wywoływania okna w momencie wczytywania symulatora###############################
    def splash1(self):
        self.timersplash1.stop()
        self.timer.start(1000)
        self.efect.setEnabled(False)
        client=airsim.MultirotorClient()
        client.confirmConnection()
        self.connection=1
#Polaczenie z AirSim w trakcie pierwszego z badan###############################################
    def Connect(self):
        if self.isAirSimOpened==1:
            self.splash=SplashScreen1()
            self.efect=QGraphicsBlurEffect()
            self.setGraphicsEffect(self.efect)
            
            self.timersplash1=QTimer()
            self.timersplash1.start(4000)
            self.timersplash1.timeout.connect(lambda:self.splash1())
#Polaczenie z AirSim w trakcie drugiego z badan#################################################
    def Connect_VR(self):
            if self.secondwindow==1: 
                client=airsim.MultirotorClient()
                client.confirmConnection()
                self.connection_VR=1
                self.timer_VR.start(1000)     
                             
#Rozdzielczosc okna############################################################################ 
    def x1920x1080(self):
        self.windowSizeX=1920
        self.windowSizeY=1080
    def x1680x1050(self):
        self.windowSizeX=1680
        self.windowSizeY=1050        
    def x1200x800(self):
        self.windowSizeX=1200
        self.windowSizeY=800        
    def x1600x900(self):
        self.windowSizeX=1600
        self.windowSizeY=900        
    def x1366x768(self):
        self.windowSizeX=1366
        self.windowSizeY=768       
    def x1440x900(self):
        self.windowSizeX=1440
        self.windowSizeY=900        
    def x1024x720(self):
        self.windowSizeX=1024
        self.windowSizeY=720
#Uruchamianie AirSIM do pierwszego z badan#####################################################################################
    def AirSimGo(self):
        if self.isAirSimOpened==0:
         self.p=subprocess.Popen([self.script_path,f"-windowed", f"-resx={self.windowSizeX}" ,f"-resy={self.windowSizeY}"])
         client=airsim.MultirotorClient()
         self.ui.Misje_Button.setVisible(True)
         self.ui.stackedWidget.setCurrentWidget(self.ui.Parameters_page)
         self.isAirSimOpened=1
         self.pid=self.p.pid
         
         ##Jezeli jest odpalony to zamknij poprzednia instancje################################################################
        else:
           os.system(f"TASKKILL /F /IM {self.script_name}")
           self.isAirSimOpened=0

#Wybor Mapy###################################################################################################################
    def AbandonedPark(self):
        self.script_path=(self.path+r"\Srodowiska Symulatora\AbandonedPark\AbandonedPark\WindowsNoEditor\AbandonedPark.exe")
        self.script_name="AbandonedPark.exe"
        self.ui.stackedWidget_mapy.setCurrentWidget(self.ui.Aband_mapa)
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
    def Africa(self):
        self.script_path=(self.path+r"\Srodowiska Symulatora\Africa\Africa\WindowsNoEditor\Africa_001.exe")
        self.script_name="Africa_001.exe"
        self.ui.stackedWidget_mapy.setCurrentWidget(self.ui.Africa_Mapa)
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        #msgbox.setWindowTitle("Istotna uwaga")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
    def AirSimNH(self):
        self.script_path=(self.path+r"\Srodowiska Symulatora\AirSimNH (1)\AirSimNH\WindowsNoEditor\AirSimNH.exe")
        self.script_name="AirSimNH.exe"
        self.ui.stackedWidget_mapy.setCurrentWidget(self.ui.AirSimNH_mapa)
    def Blocks(self):
        self.script_path=(self.path+r"\Srodowiska Symulatora\Blocks\Blocks\WindowsNoEditor\Blocks.exe")
        self.script_name="Blocks.exe"
        self.ui.stackedWidget_mapy.setCurrentWidget(self.ui.Blocks_mapa)
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
    def LandscapeMountains(self):
        self.script_path=(self.path+r"\Srodowiska Symulatora\LandscapeMountains\LandscapeMountains\WindowsNoEditor\LandscapeMountains.exe")
        self.script_name="LandscapeMountains.exe"
        self.ui.stackedWidget_mapy.setCurrentWidget(self.ui.Lands_mapa)
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
    def MSBuild(self):
        self.script_path=(self.path+r"\Srodowiska Symulatora\MSBuild2018\MSBuild2018\WindowsNoEditor\MSBuild2018.exe")
        self.script_name="MSBuild2018.exe"
        self.ui.stackedWidget_mapy.setCurrentWidget(self.ui.MSBuild_mapa)
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
    def ZJ(self):
        self.script_path=(self.path+r"\Srodowiska Symulatora\Coastline\Coastline\WindowsNoEditor\Coastline.exe")
        self.script_name="Coastline.exe"
        self.ui.stackedWidget_mapy.setCurrentWidget(self.ui.ZJ_mapa)
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
#Funkcja zmieniajaca style##############################################################################################################
    def Changing_Frame(self):
       
        if self.ui.stackedWidget.currentWidget()==self.ui.Home_page:
         self.ui.Home_frame.setStyleSheet(self.stylesheet_clicked)
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Settings_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Przewodnik_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Parametry_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Misje_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Informacje_frame.setStyleSheet(self.stylesheet_default)
        elif self.ui.stackedWidget.currentWidget()==self.ui.Analyze_page:
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Home_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_clicked)
         self.ui.Settings_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Przewodnik_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Parametry_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Misje_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Informacje_frame.setStyleSheet(self.stylesheet_default)          
        elif self.ui.stackedWidget.currentWidget()==self.ui.Settings_page:
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Home_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Settings_frame.setStyleSheet(self.stylesheet_clicked)
         self.ui.Przewodnik_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Parametry_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Misje_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Informacje_frame.setStyleSheet(self.stylesheet_default) 
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
        elif self.ui.stackedWidget.currentWidget()==self.ui.Tutorial_page:
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Home_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Settings_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Przewodnik_frame.setStyleSheet(self.stylesheet_clicked)
         self.ui.Parametry_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Misje_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Informacje_frame.setStyleSheet(self.stylesheet_default) 
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
        elif self.ui.stackedWidget.currentWidget()==self.ui.Parameters_page:
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Home_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Settings_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Przewodnik_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Parametry_frame.setStyleSheet(self.stylesheet_clicked)
         self.ui.Misje_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Informacje_frame.setStyleSheet(self.stylesheet_default) 
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
        elif self.ui.stackedWidget.currentWidget()==self.ui.Mission_page:
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Home_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Settings_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Przewodnik_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Parametry_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Misje_frame.setStyleSheet(self.stylesheet_clicked)
         self.ui.Informacje_frame.setStyleSheet(self.stylesheet_default) 
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
        elif self.ui.stackedWidget.currentWidget()==self.ui.Info_page:
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Home_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Settings_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Przewodnik_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Parametry_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Misje_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Informacje_frame.setStyleSheet(self.stylesheet_clicked) 
         self.ui.VR_frame.setStyleSheet(self.stylesheet_default)
        elif self.ui.stackedWidget.currentWidget()==self.ui.VR_page:
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Home_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Analiza_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Settings_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Przewodnik_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Parametry_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Misje_frame.setStyleSheet(self.stylesheet_default)
         self.ui.Informacje_frame.setStyleSheet(self.stylesheet_default) 
         self.ui.VR_frame.setStyleSheet(self.stylesheet_clicked)

##########Metoda zmieniajace strony################################################################################################
    def Home(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home_page)
        if self.secondwindow==1:
            self.VR_levels.showMinimized()
    def Informacje(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Info_page)
        if self.secondwindow==1:
            self.VR_levels.showMinimized() 
    def Misje(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Mission_page)  
        if self.secondwindow==1:
            self.VR_levels.showMinimized()
    def Parametry(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Parameters_page)
        if self.secondwindow==1:
            self.VR_levels.showMinimized()
    def Przewodnik(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Tutorial_page) 
        if self.secondwindow==1:
            self.VR_levels.showMinimized() 
    def Settings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Settings_page)
        if self.secondwindow==1:
            self.VR_levels.showMinimized()
    def Analiza(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Analyze_page)
        if self.secondwindow==1:
            self.VR_levels.showMinimized()
    def VR(self):
       self.ui.stackedWidget.setCurrentWidget(self.ui.VR_page)
       if self.secondwindow==1:
        self.VR_levels.show()
    #Funkcja zwijania/rozwijania sidebar menu#######################################################################################
    def slideLeftMenu(self):
        width=self.ui.side_menu_container.width()
        if width==142:
            newWidth=68
            self.ui.Menu_button.setIcon(QIcon(self.path+r"\Icons\Magisterka_python(1)\icons8-menu-50.png"))
            self.ui.Menu_button.setToolTip("Rozwiń menu")
            self.ui.Settings.hide()
            self.ui.Home.hide()
            self.ui.Analiza.hide()
            self.ui.Informacje.hide()
            self.ui.Misje.hide()
            self.ui.Parametry.hide()
            self.ui.Przewodnik.hide()
            self.ui.VR.hide()
            print(width)
        else:
            newWidth=142
            self.ui.Menu_button.setIcon(QIcon(self.path+r"\Icons\Magisterka_python(1)\icons8-back-50.png"))
            self.ui.Menu_button.setToolTip("Zwiń menu")
            self.ui.Settings.show()
            self.ui.Home.show()
            self.ui.Analiza.show()
            self.ui.Informacje.show()
            self.ui.Misje.show()
            self.ui.Parametry.show()
            self.ui.Przewodnik.show()
            self.ui.VR.show()
        self.animation=QtCore.QPropertyAnimation(self.ui.side_menu_container,b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InCurve)
        self.animation.start()
    #Funkcja naciśnięcia myszki niezbędna do ruszania oknem ###########################################################################   
    def mousePressEvent(self, event):
          self.clickPosition=event.globalPos()
    #Funkcja warunkująca zmniejszanie lub zwiększanie okna ############################################################################
    def close_window(self): 
       self.close()
       os.system(f"TASKKILL /F /IM {self.script_name}")
       os.system(f"TASKKILL /F /IM {self.script_name_VR}") 
       os.system(f"TASKKILL /F /IM Python.exe")  
       self.tetno.terminate()
       self.VR_levels.close()
       self.cam.release()
       cv2.destroyAllWindows()
    ##########Metoda umozliwiajaca maksymalizowanie okna##########################################################################
    def restore_or_maximize_window(self):
         if self.isMaximized():
           self.showNormal()
           self.ui.Max.setIcon(QtGui.QIcon(self.path+r"\Icons\Magisterka_python(1)\icons8-resize-50.png"))
           self.ui.Max.setToolTip("Zmaksymalizuj")
           self.ui.AirSimNH_GV.centerOn(self.rect)
         else: 
          self.showMaximized()
          self.ui.Max.setIcon(QtGui.QIcon(self.path+r"\Icons\Magisterka_python(1)\icons8-minimize-50-1.png"))
          self.ui.Max.setToolTip("Zmniejsz okno")
          self.ui.AirSimNH_GV.centerOn(self.rect)
    ##########Mapy do badania w wirtualnej rzeczywistosci########################################################################
    #######################################################################################################################
    def VR_AirSimNH(self):
        self.script_path_VR=(self.path+r"\Srodowiska Symulatora\AirSimNH (1)\AirSimNH\WindowsNoEditor\AirSimNH.exe")
        self.script_name_VR="AirSimNH.exe" 
        self.ui.Actualmap.setText("AirSimNH")      
    def VR_Africa(self):
        self.script_path_VR=(self.path+r"\Srodowiska Symulatora\Africa\Africa\WindowsNoEditor\Africa_001.exe")
        self.script_name_VR="Africa_001.exe"
        self.ui.Actualmap.setText("Africa")
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
    def VR_Abandoned(self):
        self.script_path_VR=(self.path+r"\Srodowiska Symulatora\AbandonedPark\AbandonedPark\WindowsNoEditor\AbandonedPark.exe")
        self.script_name_VR="AbandonedPark.exe" 
        self.ui.Actualmap.setText("Abandoned Park")  
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()  
    def VR_Blocks(self):
        self.script_path_VR=(self.path+r"\Srodowiska Symulatora\Blocks\Blocks\WindowsNoEditor\Blocks.exe")
        self.script_name_VR="Blocks.exe"
        self.ui.Actualmap.setText("Blocks") 
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()    
    def VR_Landscape(self):
        self.script_path_VR=(self.path+r"\Srodowiska Symulatora\LandscapeMountains\LandscapeMountains\WindowsNoEditor\LandscapeMountains.exe")
        self.script_name_VR="LandscapeMountains.exe" 
        self.ui.Actualmap.setText("Landscape Mountains")      
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
    def VR_MSBuild2018(self):
        self.script_path_VR=(self.path+r"\Srodowiska Symulatora\MSBuild2018\MSBuild2018\WindowsNoEditor\MSBuild2018.exe")
        self.script_name_VR="MSBuild2018.exe"
        self.ui.Actualmap.setText("MSBuild2018")
        msgbox=QMessageBox()
        msgbox.setIcon(QMessageBox.Warning)
        msgbox.setText("Badanie w VR jest zooptymalizowane pod kątem mapy AirSimNH, uruchomienie programu w innym środowisku jest moźliwe, ale niezalecane.")
        msgbox.setStandardButtons(QMessageBox.Ok)
        msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
        msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        x=msgbox.exec_()
    ######Metoda umozliwiajaca wlaczenie symulatora do badania w wirtualnej rzeczywistosci######################################
    def VR_start(self):
       self.p=subprocess.Popen([f"{self.script_path_VR}"])
       self.VR_levels = VR_Levels()
       #self.VR_levels=VR_wojtowicz()
       
       
       self.VR_levels.show()
       self.secondwindow=1
       self.ui.Run_AirSim.setEnabled(False)
       self.ui.Parametry_button.setEnabled(False)
       self.ui.VR_blocks.setEnabled(False)
       self.ui.VR_landscape.setEnabled(False)
       self.ui.VR_abandoned.setEnabled(False)
       self.ui.VR_MSBuild.setEnabled(False)
       self.ui.VR_africa.setEnabled(False)
    #####Metoda do sprawdzania emocji z twarzy w trakcie poboru parametrow######################################################
    def Camera_show(self):
        #Sprawdzenie czy kamerka jest otwarta#
        if not self.cam.isOpened():
            #Wyslanie wiadomosci uzytkownikowi#
            self.message("Włączenie kamerki nie powiodło się, upewnij się że jej indeks został wybrany prawidłowo")
            #Zatrzymanie dzialania algorytmu rozpoznajacego emocje#
            self.x=0
            #Rozpoznawanie emocji#
        while self.x==1 and self.emocje_reading==1:
            max_index=6
            ret, frame = self.cam.read()
            #Odwrocenie obrazu kamerki#
            frame=cv2.flip(frame,1)
            #Pokazanie użytkownikowi poprawności działania#
            self.ui.emocje_LED.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-green-circle-48.png"))
            self.ui.emocje_LED.setToolTip("Emocje są rozpoznawane")
            if frame is not None and ret==True: 
                #Odwrócenie kolorów na skalę szarości#
                gray1=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
                #Utworzenie tablicy trójwymiarowej zawierającej odcienie szarości#
                gray=cv2.merge((gray1,gray1,gray1))
                #Wykrycie twarzy#
                faces=self.clf.detectMultiScale(gray1,scaleFactor=1.1,minNeighbors=1,minSize=(224,224))
                #Jeżeli nie wykryto twarzy, ustawia domyślnie neutralną emocję#
                if not len(faces)>0:
                    max_index=6
                    self.ui.Emotion.display(max_index)
                    self.emocja(max_index)
                #Jeżeli wykryto twarz, rozpoczyna rozpoznanie#
                for (x,y, width,height) in faces: 
                    cv2.rectangle(frame,(x,y),(x+width,y+height),(255,255,0),2)
                    roi_gray=gray[y:y+height,x:x+width]
                    if roi_gray is not None:
                        roi_gray=cv2.resize(roi_gray,(self.img_size,self.img_size))
                        img_pixels=image.img_to_array(roi_gray)
                        img_pixels = np.expand_dims(img_pixels,axis=0)
                        #Normalizacja danych przed rozpoznaniem#
                        img_pixels /= 255
                        #Rozpoznanie twarzy przy pomocy modelu sztucznej inteligencji#
                        predictions=self.model.predict(img_pixels,verbose=1)
                        max_index=np.argmax(predictions[0])
                        #Pokazanie użytkownikowi indeksu wykrytej emocji#
                        self.ui.Emotion.display(max_index)
                        #Zapis wykrytej emocji#
                        self.emocja(max_index)
                        
                      
                
                match self.levelpassed:    
                    case 0:
                        self.emocje1.append(max_index)
                    case 1:
                        self.emocje2.append(max_index)
                    case 2:
                        self.emocje3.append(max_index)
                    case 3:
                        self.emocje4.append(max_index)
                    case 4:
                        self.emocje5.append(max_index)
                    case 5:
                        self.emocje6.append(max_index)
                    case 6:
                        self.emocje7.append(max_index)
                    case 7:
                        self.emocje8.append(max_index)
                    case 8:
                        self.emocje9.append(max_index)
                    case 9:
                        self.emocje10.append(max_index)
    ##########Metoda umozliwiajaca sprawdzenie dzialania algorytmu sprawdzajacego emocje _ PRACA PRZEJSCIOWA###################################################
    ###########################################################################################################################################################
    ###########################################################################################################################################################
    def Camera_showing(self):
        if not self.cam.isOpened():
                self.message("Włączenie kamerki nie powiodło się, upewnij się że jej indeks został wybrany prawidłowo")
                self.x=0
        while self.x==1:
            ret, frame = self.cam.read()
            frame=cv2.flip(frame,1)
            if frame is not None and ret==True: 
                    gray1=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
                    gray=cv2.merge((gray1,gray1,gray1))
                    faces=self.clf.detectMultiScale(gray1,scaleFactor=1.1,minNeighbors=1,minSize=(224,224))
                    for (x,y, width,height) in faces: 
                        cv2.rectangle(frame,(x,y),(x+width,y+height),(255,255,0),2)
                        roi_gray=gray[y:y+height,x:x+width]
                        if roi_gray is not None:
                            roi_gray=cv2.resize(roi_gray,(self.img_size,self.img_size))
                            img_pixels=image.img_to_array(roi_gray)
                            img_pixels = np.expand_dims(img_pixels,axis=0)
                            img_pixels /= 255
                            predictions=self.model.predict(img_pixels,verbose=0)
                            max_index=np.argmax(predictions[0])
                            emotions=('angry','disgust','fear','happy','sad','surprise','neutral')
                            text=emotions[max_index]
                            cv2.putText(frame,text,(x-10,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,0))
                    cv2.imshow("test",frame)
                    k=cv2.waitKey(1)
                    if k%256==27:
                                print("Close the app")
                                break 
    
    def Save_data2(self):
            self.data2.loc[len(self.data2.index)]=[self.l1_w,
                                             self.l1_c,
                                             self.l1_t,
                                             self.l1_f,
                                             statistics.variance(self.tetno1),
                                             self.czas_ekst1,
                                             self.VR_levels.data_t1,
                                             statistics.variance(self.VR_levels.tetno1),
                                             self.VR_levels.czas_ekst_1,
                                             ################################
                                             self.l2_w,
                                             self.l2_c,
                                             self.l2_t,
                                             self.l2_f,
                                             statistics.variance(self.tetno2),
                                             self.czas_ekst2,
                                             self.VR_levels.data_t2,
                                             statistics.variance(self.VR_levels.tetno2),
                                             self.VR_levels.czas_ekst_2,
                                             ################################
                                             self.l3_w,
                                             self.l3_c,
                                             self.l3_t,
                                             self.l3_f,
                                             statistics.variance(self.tetno3),
                                             self.czas_ekst3,
                                             self.VR_levels.data_t3,
                                             statistics.variance(self.VR_levels.tetno3),
                                             self.VR_levels.czas_ekst_3,
                                             ################################
                                             self.l4_w,
                                             self.l4_c,
                                             self.l4_t,
                                             self.l4_f,
                                             statistics.variance(self.tetno4),
                                             self.czas_ekst4,
                                             self.VR_levels.data_t4,
                                             statistics.variance(self.VR_levels.tetno4),
                                             self.VR_levels.czas_ekst_4,
                                             ################################
                                             self.l5_w,
                                             self.l5_c,
                                             self.l5_t,
                                             self.l5_f,
                                             statistics.variance(self.tetno5),
                                             self.czas_ekst5,
                                             self.VR_levels.data_t5,
                                             statistics.variance(self.VR_levels.tetno5),
                                             self.VR_levels.czas_ekst_5,
                                             ################################
                                             self.l6_w,
                                             self.l6_c,
                                             self.l6_t,
                                             self.l6_f,
                                             statistics.variance(self.tetno6),
                                             self.czas_ekst6,
                                             self.VR_levels.data_t6,
                                             statistics.variance(self.VR_levels.tetno6),
                                             self.VR_levels.czas_ekst_6,
                                             ################################
                                             self.l7_w,
                                             self.l7_c,
                                             self.l7_t,
                                             self.l7_f,
                                             statistics.variance(self.tetno7),
                                             self.czas_ekst7,
                                             self.VR_levels.data_t7,
                                             statistics.variance(self.VR_levels.tetno7),
                                             self.VR_levels.czas_ekst_7,
                                             ################################
                                             self.l8_w,
                                             self.l8_c,
                                             self.l8_t,
                                             self.l8_f,
                                             statistics.variance(self.tetno8),
                                             self.czas_ekst8,
                                             self.VR_levels.data_t8,
                                             statistics.variance(self.VR_levels.tetno8),
                                             self.VR_levels.czas_ekst_8,
                                             ################################
                                             self.l9_w,
                                             self.l9_c,
                                             self.l9_t,
                                             self.l9_f,
                                             statistics.variance(self.tetno9),
                                             self.czas_ekst9,
                                             self.VR_levels.data_t9,
                                             statistics.variance(self.VR_levels.tetno9),
                                             self.VR_levels.czas_ekst_9,
                                             ################################
                                             self.l10_w,
                                             self.l10_c,
                                             self.l10_t,
                                             self.l10_f,
                                             statistics.variance(self.tetno10),
                                             self.czas_ekst10,
                                             self.VR_levels.data_t10,
                                             statistics.variance(self.VR_levels.tetno10),
                                             self.VR_levels.czas_ekst_10]
            self.data2.to_csv(r"C:\Do Linuxa\Magisterka\Dane_z_lotu.csv",index=False)
            print(self.data2)
            print("**********************Predyspozycje**************************")
            self.predyspozycje()
            self.Generacja_wykresow()
            self.Generacja_wykresowVR()
    #################################GENERACJA WYKRESOW Z DANYMI Z BADANIA W PIERWSZYM ETAPIE###########################################################
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
    def Generacja_wykresow(self):   
        #######Lewy górny#########
        self.chart00=QtCharts.QChart()
        series00=QtCharts.QLineSeries()
        self.chart01=QtCharts.QChart()
        series01=QtCharts.QLineSeries()
        self.chart02=QtCharts.QChart()
        series02=QtCharts.QLineSeries()
        self.chart03=QtCharts.QChart()
        series03=QtCharts.QLineSeries()
        self.chart04=QtCharts.QChart()
        series04=QtCharts.QLineSeries()
        self.chart05=QtCharts.QChart()
        series05=QtCharts.QLineSeries()
        self.chart06=QtCharts.QChart()
        series06=QtCharts.QLineSeries()
        self.chart07=QtCharts.QChart()
        series07=QtCharts.QLineSeries()
        self.chart08=QtCharts.QChart()
        series08=QtCharts.QLineSeries()
        self.chart09=QtCharts.QChart()
        series09=QtCharts.QLineSeries()
        self.chart10=QtCharts.QChart()
        series10=QtCharts.QLineSeries()  
        ##########Wykres ze wszystkimi#########################
        i=0
        wszystkietabele=[]
        wszystkietabele.extend(self.tetno1)
        wszystkietabele.extend(self.tetno2)
        wszystkietabele.extend(self.tetno3)
        wszystkietabele.extend(self.tetno4)
        wszystkietabele.extend(self.tetno5)
        wszystkietabele.extend(self.tetno6)
        wszystkietabele.extend(self.tetno7)
        wszystkietabele.extend(self.tetno8)
        wszystkietabele.extend(self.tetno9)
        wszystkietabele.extend(self.tetno10)
        #Wartosci charakterystyczne#########
        average=sum(wszystkietabele)/len(wszystkietabele)
        maks=max(wszystkietabele)
        mini=min(wszystkietabele)
        self.ui.label_148.setText(str(maks))
        self.ui.label_151.setText(str(mini))
        self.ui.label_154.setText(str(average))
        ##
        calyczas=[]
        calyczas.append(self.l1_c)
        calyczas.append(self.l2_c)
        calyczas.append(self.l3_c)
        calyczas.append(self.l4_c)
        calyczas.append(self.l5_c)
        calyczas.append(self.l6_c)
        calyczas.append(self.l7_c)
        calyczas.append(self.l8_c)
        calyczas.append(self.l9_c)
        calyczas.append(self.l10_c)
        x=sum(calyczas)/len(wszystkietabele)
        while i<len(wszystkietabele): 
            series00.append(x*i,wszystkietabele[i])
            i+=1
        self.chart00.addSeries(series00)
        self.chart00.setTitle('Przebieg tetna w czasie')
        self.chart00.createDefaultAxes()
        self.ui.chart0.setChart(self.chart00)
        #####Level1########
        i01=0
        x01=self.l1_c/len(self.tetno1)
        while i01<len(self.tetno1): 
            series01.append(x01*i01,self.tetno1[i01])
            i01+=1
        self.chart01.addSeries(series01)
        self.chart01.setTitle('Przebieg tetna w czasie')
        self.chart01.createDefaultAxes()
        self.ui.chart1.setChart(self.chart01)
        ####Level 2###########
        i02=0
        x02=self.l2_c/len(self.tetno2)
        while i02<len(self.tetno2): 
            series02.append(x02*i02,self.tetno2[i02])
            i02+=1
        self.chart02.addSeries(series02)
        self.chart02.setTitle('Przebieg tetna w czasie')
        self.chart02.createDefaultAxes()
        self.ui.chart2.setChart(self.chart02)
        ####Level 3#########
        i03=0
        x03=self.l3_c/len(self.tetno3)
        while i03<len(self.tetno3): 
            series03.append(x03*i03,self.tetno3[i03])
            i03+=1
        self.chart03.addSeries(series03)
        self.chart03.setTitle('Przebieg tetna w czasie')
        self.chart03.createDefaultAxes()
        self.ui.chart3.setChart(self.chart03)

        #######Level 4#########
        i04=0
        x04=self.l4_c/len(self.tetno4)
        while i04<len(self.tetno4): 
            series04.append(x04*i04,self.tetno4[i04])
            i04+=1
        self.chart04.addSeries(series04)
        self.chart04.setTitle('Przebieg tetna w czasie')
        self.chart04.createDefaultAxes()
        self.ui.chart4.setChart(self.chart04)

        #Level 5########
        i05=0
        x05=self.l5_c/len(self.tetno5)
        while i05<len(self.tetno5): 
            series05.append(x05*i05,self.tetno5[i05])
            i05+=1
        self.chart05.addSeries(series05)
        self.chart05.setTitle('Przebieg tetna w czasie')
        self.chart05.createDefaultAxes()
        self.ui.chart5.setChart(self.chart05)

        #Level 6######
        i06=0
        x06=self.l6_c/len(self.tetno6)
        while i06<len(self.tetno6): 
            series06.append(x06*i06,self.tetno6[i06])
            i06+=1
        self.chart06.addSeries(series06)
        self.chart06.setTitle('Przebieg tetna w czasie')
        self.chart06.createDefaultAxes()
        self.ui.chart6.setChart(self.chart06)

        #Level 7######
        i07=0
        x07=self.l7_c/len(self.tetno7)
        while i07<len(self.tetno7): 
            series07.append(x07*i07,self.tetno7[i07])
            i07+=1
        self.chart07.addSeries(series07)
        self.chart07.setTitle('Przebieg tetna w czasie')
        self.chart07.createDefaultAxes()
        self.ui.chart7.setChart(self.chart07)

        #Level 8#######
        i08=0
        x08=self.l8_c/len(self.tetno8)
        while i08<len(self.tetno8): 
            series08.append(x08*i08,self.tetno8[i08])
            i08+=1
        self.chart08.addSeries(series08)
        self.chart08.setTitle('Przebieg tetna w czasie')
        self.chart08.createDefaultAxes()
        self.ui.chart8.setChart(self.chart08)

        #Level 9#########
        i09=0
        x09=self.l9_c/len(self.tetno9)
        while i09<len(self.tetno9): 
            series09.append(x09*i09,self.tetno9[i09])
            i09+=1
        self.chart09.addSeries(series09)
        self.chart09.setTitle('Przebieg tetna w czasie')
        self.chart09.createDefaultAxes()
        self.ui.chart9.setChart(self.chart09)

        #Level 10########
        i10=0
        x10=self.l10_c/len(self.tetno10)
        while i10<len(self.tetno10): 
            series10.append(x10*i10,self.tetno10[i10])
            i10+=1
        self.chart10.addSeries(series10)
        self.chart10.setTitle('Przebieg tetna w czasie')
        self.chart10.createDefaultAxes()
        self.ui.chart10.setChart(self.chart10)

        #####Lewy dolny########
        chart2=QtCharts.QChart()
        series2=QtCharts.QBarSeries()
        data1=QtCharts.QBarSet('level1')
        data1.append(self.l1_t)
        data2=QtCharts.QBarSet('level2')
        data2.append(self.l2_t)
        data3=QtCharts.QBarSet('level3')
        data3.append(self.l3_t)
        data4=QtCharts.QBarSet('level4')
        data4.append(self.l4_t)
        data5=QtCharts.QBarSet('level5')
        data5.append(self.l5_t)
        data6=QtCharts.QBarSet('level6')
        data6.append(self.l6_t)
        data7=QtCharts.QBarSet('level7')
        data7.append(self.l7_t)
        data8=QtCharts.QBarSet('level8')
        data8.append(self.l8_t)
        data9=QtCharts.QBarSet('level9')
        data9.append(self.l9_t)
        data10=QtCharts.QBarSet('level10')
        data10.append(self.l10_t)
        series2.append(data1)
        series2.append(data2)
        series2.append(data3)
        series2.append(data4)
        series2.append(data5)
        series2.append(data6)
        series2.append(data7)
        series2.append(data8)
        series2.append(data9)
        series2.append(data10)
        chart2.addSeries(series2)
        chart2.setTitle('Srednia wartosc tetno w zaleznosci od poziomu')
        chart2.createDefaultAxes()
        self.ui.widget_5.setChart(chart2)
        #####Prawy gorny########
        self.angry=0
        self.disgusted=0
        self.fear=0
        self.happy=0
        self.sad=0
        self.surprised=0
        self.neutral=0
        for twarze in self.twarze:
            match twarze:
                case 0:
                    self.angry+=1
                case 1:
                    self.disgusted+=1
                case 2:
                    self.fear+=1
                case 3:
                    self.happy+=1
                case 4:
                    self.sad+=1
                case 5:
                    self.surprised+=1
                case 6:
                    self.neutral+=1
        self.ui.label_158.setText(str(self.angry1))
        self.ui.label_161.setText(str(self.disgusted1))
        self.ui.label_164.setText(str(self.fear1))
        self.ui.label_167.setText(str(self.happy1))
        self.ui.label_178.setText(str(self.sad1))
        self.ui.label_170.setText(str(self.surprised1))
        self.ui.label_173.setText(str(self.neutral1))
        self.angry/=10
        self.disgusted/=10
        self.fear/=10
        self.happy/=10
        self.sad/=10
        self.surprised/=10
        self.neutral/=10
        chart3=QtCharts.QChart()
        chart3.setTitle("Procentowy udzial emocji")
        self.pie_series=QtCharts.QPieSeries()
        self.pie_series.append('zdenerwowany',self.angry)
        self.pie_series.append('zdegustowany',self.disgusted)
        self.pie_series.append('przestraszony',self.fear)
        self.pie_series.append('szczesliwy',self.happy)
        self.pie_series.append('smutny',self.sad)
        self.pie_series.append('zaskoczony',self.surprised)
        self.pie_series.append('neutralny',self.neutral)
        self.pie_series.setLabelsPosition(QtCharts.QPieSlice.LabelInsideHorizontal)
        self.pie_series.setLabelsVisible(True)
        self.pie_series.slices()[0].pressed.connect(self.exploded0)
        self.pie_series.slices()[1].pressed.connect(self.exploded1)
        self.pie_series.slices()[2].pressed.connect(self.exploded2)
        self.pie_series.slices()[3].pressed.connect(self.exploded3)
        self.pie_series.slices()[4].pressed.connect(self.exploded4)
        self.pie_series.slices()[5].pressed.connect(self.exploded5)
        self.pie_series.slices()[6].pressed.connect(self.exploded6)
        self.pie_series.slices()[0].released.connect(self.restore0)
        self.pie_series.slices()[1].released.connect(self.restore1)
        self.pie_series.slices()[2].released.connect(self.restore2)
        self.pie_series.slices()[3].released.connect(self.restore3)
        self.pie_series.slices()[4].released.connect(self.restore4)
        self.pie_series.slices()[5].released.connect(self.restore5)
        self.pie_series.slices()[6].released.connect(self.restore6)
        chart3.addSeries(self.pie_series)
        chart3.createDefaultAxes()
        chart3.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart3.legend().setVisible(True)
        chart3.legend().setAlignment(Qt.AlignBottom)
        self.ui.widget_6.setChart(chart3)

        #######Prawy dolny############################
        self.chart000=QtCharts.QChart()
        series000=QtCharts.QLineSeries()
        self.chart010=QtCharts.QChart()
        series010=QtCharts.QLineSeries()
        self.chart020=QtCharts.QChart()
        series020=QtCharts.QLineSeries()
        self.chart030=QtCharts.QChart()
        series030=QtCharts.QLineSeries()
        self.chart040=QtCharts.QChart()
        series040=QtCharts.QLineSeries()
        self.chart050=QtCharts.QChart()
        series050=QtCharts.QLineSeries()
        self.chart060=QtCharts.QChart()
        series060=QtCharts.QLineSeries()
        self.chart070=QtCharts.QChart()
        series070=QtCharts.QLineSeries()
        self.chart080=QtCharts.QChart()
        series080=QtCharts.QLineSeries()
        self.chart090=QtCharts.QChart()
        series090=QtCharts.QLineSeries()
        self.chart100=QtCharts.QChart()
        series100=QtCharts.QLineSeries()
        ########################Tworzenie 11 wykresow
        
        ##########Wykres ze wszystkimi#########################
        i00=0
        wszystkietabele1=[]
        wszystkietabele1.extend(self.emocje1)
        wszystkietabele1.extend(self.emocje2)
        wszystkietabele1.extend(self.emocje3)
        wszystkietabele1.extend(self.emocje4)
        wszystkietabele1.extend(self.emocje5)
        wszystkietabele1.extend(self.emocje6)
        wszystkietabele1.extend(self.emocje7)
        wszystkietabele1.extend(self.emocje8)
        wszystkietabele1.extend(self.emocje9)
        wszystkietabele1.extend(self.emocje10)
        calyczas1=[]
        calyczas1.append(self.l1_c)
        calyczas1.append(self.l2_c)
        calyczas1.append(self.l3_c)
        calyczas1.append(self.l4_c)
        calyczas1.append(self.l5_c)
        calyczas1.append(self.l6_c)
        calyczas1.append(self.l7_c)
        calyczas1.append(self.l8_c)
        calyczas1.append(self.l9_c)
        calyczas1.append(self.l10_c)
        x00=sum(calyczas1)/len(wszystkietabele1)
        while i00<len(wszystkietabele1): 
            series000.append(x00*i00,wszystkietabele1[i00])
            i00+=1
        self.chart000.addSeries(series000)
        self.chart000.setTitle('Przebieg emocji w czasie')
        self.chart000.createDefaultAxes()
        self.ui.chart0_2.setChart(self.chart000)
        #####Level1########
        i010=0
        x010=self.l1_c/len(self.emocje1)
        while i010<len(self.emocje1): 
            series010.append(x010*i010,self.emocje1[i010])
            i010+=1
        self.chart010.addSeries(series010)
        self.chart010.setTitle('Przebieg emocji w czasie')
        self.chart010.createDefaultAxes()
        self.ui.chart1_2.setChart(self.chart010)
        ####Level 2###########
        i020=0
        x020=self.l2_c/len(self.emocje2)
        while i020<len(self.emocje2): 
            series020.append(x020*i020,self.emocje2[i020])
            i020+=1
        self.chart020.addSeries(series020)
        self.chart020.setTitle('Przebieg emocji w czasie')
        self.chart020.createDefaultAxes()
        self.ui.chart2_2.setChart(self.chart020)
        ####Level 3#########
        i030=0
        x030=self.l3_c/len(self.emocje3)
        while i030<len(self.emocje3): 
            series030.append(x030*i030,self.emocje3[i030])
            i030+=1
        self.chart030.addSeries(series030)
        self.chart030.setTitle('Przebieg emocji w czasie')
        self.chart030.createDefaultAxes()
        self.ui.chart3_2.setChart(self.chart030)

        #######Level 4#########
        i040=0
        x040=self.l4_c/len(self.emocje4)
        while i040<len(self.emocje4): 
            series040.append(x040*i040,self.emocje4[i040])
            i040+=1
        self.chart040.addSeries(series040)
        self.chart040.setTitle('Przebieg emocji w czasie')
        self.chart040.createDefaultAxes()
        self.ui.chart4_2.setChart(self.chart040)

        #Level 5########
        i050=0
        x050=self.l5_c/len(self.emocje5)
        while i050<len(self.emocje5): 
            series050.append(x050*i050,self.emocje5[i050])
            i050+=1
        self.chart050.addSeries(series050)
        self.chart050.setTitle('Przebieg emocji w czasie')
        self.chart050.createDefaultAxes()
        self.ui.chart5_2.setChart(self.chart050)

        #Level 6######
        i060=0
        x060=self.l6_c/len(self.emocje6)
        while i060<len(self.emocje6): 
            series060.append(x060*i060,self.emocje6[i060])
            i060+=1
        self.chart060.addSeries(series060)
        self.chart060.setTitle('Przebieg emocji w czasie')
        self.chart060.createDefaultAxes()
        self.ui.chart6_2.setChart(self.chart060)

        #Level 7######
        i070=0
        x070=self.l7_c/len(self.emocje7)
        while i070<len(self.emocje7): 
            series070.append(x070*i070,self.emocje7[i070])
            i070+=1
        self.chart070.addSeries(series070)
        self.chart070.setTitle('Przebieg emocji w czasie')
        self.chart070.createDefaultAxes()
        self.ui.chart7_2.setChart(self.chart070)

        #Level 8#######
        i080=0
        x080=self.l8_c/len(self.emocje8)
        while i080<len(self.emocje8): 
            series080.append(x080*i080,self.emocje8[i080])
            i080+=1
        self.chart080.addSeries(series080)
        self.chart080.setTitle('Przebieg emocji w czasie')
        self.chart080.createDefaultAxes()
        self.ui.chart8_2.setChart(self.chart080)

        #Level 9#########
        i090=0
        x090=self.l9_c/len(self.emocje9)
        while i090<len(self.emocje9): 
            series090.append(x090*i090,self.emocje9[i090])
            i090+=1
        self.chart090.addSeries(series090)
        self.chart090.setTitle('Przebieg emocji w czasie')
        self.chart090.createDefaultAxes()
        self.ui.chart9_2.setChart(self.chart090)

        #Level 10########
        i100=0
        x100=self.l10_c/len(self.emocje10)
        while i100<len(self.emocje10): 
            series100.append(x100*i100,self.emocje10[i100])
            i100+=1
        self.chart100.addSeries(series100)
        self.chart100.setTitle('Przebieg emocji w czasie')
        self.chart100.createDefaultAxes()
        self.ui.chart10_2.setChart(self.chart100)
        if self.auto==0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.Mission_page)
    ########Metoda do wyrzucania messageboxow######################################################################################################
    def message(self,str):
            msgbox=QMessageBox()
            msgbox.setIcon(QMessageBox.Warning)
            msgbox.setText(str)
            #msgbox.setWindowTitle("Istotna uwaga")
            msgbox.setStandardButtons(QMessageBox.Ok)
            msgbox.setStyleSheet("QMessageBox {background-color: rgb(35, 32, 47);color: rgb(255, 255, 255);border: none;}"
                             'QMessageBox QLabel {color:rgb(255,255,255); font: bold 11pt "Cantarell";}')
            msgbox.setWindowFlags(QtCore.Qt.FramelessWindowHint)
            x=msgbox.exec_()
    ##############Metody umozliwiajace interakcje z wykresem kolowym################################################################################
    #**********************************************************************************************************************************************#
    def exploded0(self):
        self.pie_series.slices()[0].setExploded(True)
        self.pie_series.slices()[0].setExplodedDistanceFactor(0.4)
        self.pie_series.slices()[0].setLabelVisible(True)
    def exploded1(self):
        self.pie_series.slices()[1].setExploded(True)
        self.pie_series.slices()[1].setExplodedDistanceFactor(0.4)
        self.pie_series.slices()[1].setLabelVisible(True)
    def exploded2(self):
        self.pie_series.slices()[2].setExploded(True)
        self.pie_series.slices()[2].setExplodedDistanceFactor(0.4)
        self.pie_series.slices()[2].setLabelVisible(True)
    def exploded3(self):
        self.pie_series.slices()[3].setExploded(True)
        self.pie_series.slices()[3].setExplodedDistanceFactor(0.4)
        self.pie_series.slices()[3].setLabelVisible(True)
    def exploded4(self):
        self.pie_series.slices()[4].setExploded(True)
        self.pie_series.slices()[4].setExplodedDistanceFactor(0.4)
        self.pie_series.slices()[4].setLabelVisible(True)
    def exploded5(self):
        self.pie_series.slices()[5].setExploded(True)
        self.pie_series.slices()[5].setExplodedDistanceFactor(0.4)
        self.pie_series.slices()[5].setLabelVisible(True)
    def exploded6(self):
        self.pie_series.slices()[6].setExploded(True)
        self.pie_series.slices()[6].setExplodedDistanceFactor(0.4)
        self.pie_series.slices()[6].setLabelVisible(True)
    def restore0(self):
        self.pie_series.slices()[0].setExploded(False)
        self.pie_series.slices()[0].setLabelVisible(True)
    def restore1(self):
        self.pie_series.slices()[1].setExploded(False)
        self.pie_series.slices()[1].setLabelVisible(True)
    def restore2(self):
        self.pie_series.slices()[2].setExploded(False)
        self.pie_series.slices()[2].setLabelVisible(True)
    def restore3(self):
        self.pie_series.slices()[3].setExploded(False)
        self.pie_series.slices()[3].setLabelVisible(True)
    def restore4(self):
        self.pie_series.slices()[4].setExploded(False)
        self.pie_series.slices()[4].setLabelVisible(True)
    def restore5(self):
        self.pie_series.slices()[5].setExploded(False)
        self.pie_series.slices()[5].setLabelVisible(True)
    def restore6(self):
        self.pie_series.slices()[6].setExploded(False)
        self.pie_series.slices()[6].setLabelVisible(True)
    ###########Metoda umozlwiajaca przelaczanie wykresu lewego gornego##########################################
    def tetno_wykresy(self):
        index=self.ui.comboBox.currentIndex()
        match index:
            case 0:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page0)
            case 1:
               self.ui.stackedWidget_2.setCurrentWidget(self.ui.page1)
            case 2:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page2)
            case 3:
               self.ui.stackedWidget_2.setCurrentWidget(self.ui.page3)
            case 4:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page4)
            case 5:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page5)
            case 6:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page6)
            case 7:
               self.ui.stackedWidget_2.setCurrentWidget(self.ui.page7)
            case 8:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page8)
            case 9:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page9)
            case 10:
                self.ui.stackedWidget_2.setCurrentWidget(self.ui.page10)
    ####Metoda umozliwiaja przelaczanie wykresow prawych dolnych###################################################
    def tetno_wykresy2(self):
        index=self.ui.comboBox_2.currentIndex()
        match index:
            case 0:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.page0_2)
            case 1:
               self.ui.stackedWidget_3.setCurrentWidget(self.ui.page1_2)
            case 2:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.page2_2)
            case 3:
               self.ui.stackedWidget_3.setCurrentWidget(self.ui.page3_2)
            case 4:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.page4_2)
            case 5:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.page5_2)
            case 6:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.page6_2)
            case 7:
               self.ui.stackedWidget_3.setCurrentWidget(self.ui.page7_2)
            case 8:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.page8_2)
            case 9:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.page9_2)
            case 10:
                self.ui.stackedWidget_3.setCurrentWidget(self.ui.page10_2)  
    ########## Metoda generujaca wykresy z danymi z badania w VR #############################################################################   
    def Generacja_wykresowVR(self):
        if self.przejdzdoVR==1:
            self.Generacja_wykresow()
        if self.VR_levels.koniec ==1:
            self.chartVR0=QtCharts.QChart()
            seriesVR0=QtCharts.QLineSeries()
            self.chartVR1=QtCharts.QChart()
            seriesVR1=QtCharts.QLineSeries()
            self.chartVR2=QtCharts.QChart()
            seriesVR2=QtCharts.QLineSeries()
            self.chartVR3=QtCharts.QChart()
            seriesVR3=QtCharts.QLineSeries()
            self.chartVR4=QtCharts.QChart()
            seriesVR4=QtCharts.QLineSeries()
            self.chartVR5=QtCharts.QChart()
            seriesVR5=QtCharts.QLineSeries()
            self.chartVR6=QtCharts.QChart()
            seriesVR6=QtCharts.QLineSeries()
            self.chartVR7=QtCharts.QChart()
            seriesVR7=QtCharts.QLineSeries()
            self.chartVR8=QtCharts.QChart()
            seriesVR8=QtCharts.QLineSeries()
            self.chartVR9=QtCharts.QChart()
            seriesVR9=QtCharts.QLineSeries()
            self.chartVR10=QtCharts.QChart()
            seriesVR10=QtCharts.QLineSeries()
            
            ##########Wykres ze wszystkimi#########################
            iVR=0
            wszystkietabeleVR=[]
            wszystkietabeleVR.extend(self.VR_levels.tetno1)
            wszystkietabeleVR.extend(self.VR_levels.tetno2)
            wszystkietabeleVR.extend(self.VR_levels.tetno3)
            wszystkietabeleVR.extend(self.VR_levels.tetno4)
            wszystkietabeleVR.extend(self.VR_levels.tetno5)
            wszystkietabeleVR.extend(self.VR_levels.tetno6)
            wszystkietabeleVR.extend(self.VR_levels.tetno7)
            wszystkietabeleVR.extend(self.VR_levels.tetno8)
            wszystkietabeleVR.extend(self.VR_levels.tetno9)
            wszystkietabeleVR.extend(self.VR_levels.tetno10)
            averageVR=sum(wszystkietabeleVR)/len(wszystkietabeleVR)
            minVR=min(wszystkietabeleVR)
            maxVR=max(wszystkietabeleVR)
            self.ui.label_187.setText(str(averageVR))
            self.ui.label_184.setText(str(minVR))
            self.ui.label_181.setText(str(maxVR))
            
            calyczasVR=[]
            calyczasVR.append(self.VR_levels.time1)
            calyczasVR.append(self.VR_levels.time2)
            calyczasVR.append(self.VR_levels.time3)
            calyczasVR.append(self.VR_levels.time4)
            calyczasVR.append(self.VR_levels.time5)
            calyczasVR.append(self.VR_levels.time6)
            calyczasVR.append(self.VR_levels.time7)
            calyczasVR.append(self.VR_levels.time8)
            calyczasVR.append(self.VR_levels.time9)
            calyczasVR.append(self.VR_levels.time10)
            xVR=sum(calyczasVR)/len(wszystkietabeleVR)
            while iVR<len(wszystkietabeleVR): 
                seriesVR0.append(xVR*iVR,wszystkietabeleVR[iVR])
                iVR+=1
            self.chartVR0.addSeries(seriesVR0)
            self.chartVR0.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR0.createDefaultAxes()
            self.ui.chart0_3.setChart(self.chartVR0)
            #####Level1########
            iVR01=0
            xVR01=self.VR_levels.time1/len(self.VR_levels.tetno1)
            while iVR01<len(self.VR_levels.tetno1): 
                seriesVR1.append(xVR01*iVR01,self.VR_levels.tetno1[iVR01])
                iVR01+=1
            self.chartVR1.addSeries(seriesVR1)
            self.chartVR1.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR1.createDefaultAxes()
            self.ui.chart1_3.setChart(self.chartVR1)
            ####Level 2###########
            iVR02=0
            xVR02=self.VR_levels.time2/len(self.VR_levels.tetno2)
            while iVR02<len(self.VR_levels.tetno2): 
                seriesVR2.append(xVR02*iVR02,self.VR_levels.tetno2[iVR02])
                iVR02+=1
            self.chartVR2.addSeries(seriesVR2)
            self.chartVR2.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR2.createDefaultAxes()
            self.ui.chart2_3.setChart(self.chartVR2)
            ####Level 3#########
            iVR03=0
            xVR03=self.VR_levels.time3/len(self.VR_levels.tetno3)
            while iVR03<len(self.VR_levels.tetno3): 
                seriesVR3.append(xVR03*iVR03,self.VR_levels.tetno3[iVR03])
                iVR03+=1
            self.chartVR3.addSeries(seriesVR3)
            self.chartVR3.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR3.createDefaultAxes()
            self.ui.chart3_3.setChart(self.chartVR3)

            #######Level 4#########
            iVR04=0
            xVR04=self.VR_levels.time4/len(self.VR_levels.tetno4)
            while iVR04<len(self.VR_levels.tetno4): 
                seriesVR4.append(xVR04*iVR04,self.VR_levels.tetno4[iVR04])
                iVR04+=1
            self.chartVR4.addSeries(seriesVR4)
            self.chartVR4.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR4.createDefaultAxes()
            self.ui.chart4_3.setChart(self.chartVR4)

            #Level 5########
            iVR05=0
            xVR05=self.VR_levels.time5/len(self.VR_levels.tetno5)
            while iVR05<len(self.VR_levels.tetno5): 
                seriesVR5.append(xVR05*iVR05,self.VR_levels.tetno5[iVR05])
                iVR05+=1
            self.chartVR5.addSeries(seriesVR5)
            self.chartVR5.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR5.createDefaultAxes()
            self.ui.chart5_3.setChart(self.chartVR5)

            #Level 6######
            iVR06=0
            xVR06=self.VR_levels.time6/len(self.VR_levels.tetno6)
            while iVR06<len(self.VR_levels.tetno6): 
                seriesVR6.append(xVR06*iVR06,self.VR_levels.tetno6[iVR06])
                iVR06+=1
            self.chartVR6.addSeries(seriesVR6)
            self.chartVR6.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR6.createDefaultAxes()
            self.ui.chart6_3.setChart(self.chartVR6)

            #Level 7######
            iVR07=0
            xVR07=self.VR_levels.time7/len(self.VR_levels.tetno7)
            while iVR07<len(self.VR_levels.tetno7): 
                seriesVR7.append(xVR07*iVR07,self.VR_levels.tetno7[iVR07])
                iVR07+=1
            self.chartVR7.addSeries(seriesVR7)
            self.chartVR7.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR7.createDefaultAxes()
            self.ui.chart7_3.setChart(self.chartVR7)

            #Level 8#######
            iVR08=0
            xVR08=self.VR_levels.time8/len(self.VR_levels.tetno8)
            while iVR08<len(self.VR_levels.tetno8): 
                seriesVR8.append(xVR08*iVR08,self.VR_levels.tetno8[iVR08])
                iVR08+=1
            self.chartVR8.addSeries(seriesVR8)
            self.chartVR8.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR8.createDefaultAxes()
            self.ui.chart8_3.setChart(self.chartVR8)

            #Level 9#########
            iVR09=0
            xVR09=self.VR_levels.time9/len(self.VR_levels.tetno9)
            while iVR09<len(self.VR_levels.tetno9): 
                seriesVR9.append(xVR09*iVR09,self.VR_levels.tetno9[iVR09])
                iVR09+=1
            self.chartVR9.addSeries(seriesVR9)
            self.chartVR9.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR9.createDefaultAxes()
            self.ui.chart9_3.setChart(self.chartVR9)

            #Level 10########
            iVR10=0
            xVR10=self.VR_levels.time10/len(self.VR_levels.tetno10)
            while iVR10<len(self.VR_levels.tetno10): 
                seriesVR10.append(xVR10*iVR10,self.VR_levels.tetno10[iVR10])
                iVR10+=1
            self.chartVR10.addSeries(seriesVR10)
            self.chartVR10.setTitle('Przebieg tetna w czasie badania w VR')
            self.chartVR10.createDefaultAxes()
            self.ui.chart10_3.setChart(self.chartVR10)
            self.ui.stackedWidget.setCurrentWidget(self.ui.Analyze_page)
    #####Metoda umozliwiajaca przelaczanie miedzy wykresami lewy gorny VR####################################################
    def tetno_wykresy3(self):
        index=self.ui.comboBox_3.currentIndex()
        match index:
            case 0:
                self.ui.stackedWidget_4.setCurrentWidget(self.ui.page0_3)
            case 1:
               self.ui.stackedWidget_4.setCurrentWidget(self.ui.page1_3)
            case 2:
                self.ui.stackedWidget_4.setCurrentWidget(self.ui.page2_3)
            case 3:
               self.ui.stackedWidget_4.setCurrentWidget(self.ui.page3_3)
            case 4:
                self.ui.stackedWidget_4.setCurrentWidget(self.ui.page4_3)
            case 5:
                self.ui.stackedWidget_4.setCurrentWidget(self.ui.page5_3)
            case 6:
                self.ui.stackedWidget_4.setCurrentWidget(self.ui.page6_3)
            case 7:
               self.ui.stackedWidget_4.setCurrentWidget(self.ui.page7_3)
            case 8:
                self.ui.stackedWidget_4.setCurrentWidget(self.ui.page8_3)
            case 9:
                self.ui.stackedWidget_4.setCurrentWidget(self.ui.page9_3)
            case 10:
                self.ui.stackedWidget_4.setCurrentWidget(self.ui.page10_3)       
    ######Pokazywanie aktualnej emocji na ekranie########################################################################
    def emocja(self,max_index):
        match max_index:
                    case 0:
                        self.ui.label_142.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-angry-50.png"))
                        self.ui.label_140.setText("zdenerwowany")
                        self.angry1 +=1
                    case 1:
                        self.ui.label_142.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-disgusting-50.png"))
                        self.ui.label_140.setText("zdegustowany")
                        self.disgusted1+=1
                    case 2:
                        self.ui.label_142.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-shocked-50.png"))
                        self.ui.label_140.setText("przestraszony")
                        self.fear1+=1
                    case 3:
                        self.ui.label_142.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-happy-50.png"))
                        self.ui.label_140.setText("szczesliwy")
                        self.happy1+=1
                    case 4:
                        self.ui.label_142.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-sad-50.png"))
                        self.ui.label_140.setText("smutny")
                        self.sad1+=1
                    case 5:
                        self.ui.label_142.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-surprised-50 (1).png"))
                        self.ui.label_140.setText("zaskoczony")
                        self.surprised1+=1
                    case 6:
                        self.ui.label_142.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-neutral-50.png"))
                        self.ui.label_140.setText("neutralny")
                        self.neutral1+=1
    #####Metoda umożliwiająca zamknięcie wszystkich możliwych poprzednich instancji########################################
    def clean_all_processes(self): 
       self.isAirSimOpened=0
       os.system(f"TASKKILL /F /IM {self.script_name_VR}") 
       os.system(f"TASKKILL /F /IM {self.script_name}")
       os.system(f"TASKKILL /F /IM Python")
       self.cam.release()
       self.tetno.terminate()
       cv2.destroyAllWindows()   
    ######Implementacja modelu oceniajacego predyspozycje##################################################################
    def predyspozycje(self):
        #########Predykcje na dzielonych sieciach##############################################
        dane_do_misji=pd.DataFrame([         self.l1_w,
                                             self.l1_c,
                                             ################################
                                             self.l2_w,
                                             self.l2_c,
                                             ################################
                                             self.l3_w,
                                             self.l3_c,
                                             ################################
                                             self.l4_w,
                                             self.l4_c,
                                             ################################
                                             self.l5_w,
                                             self.l5_c,
                                             ################################
                                             self.l6_w,
                                             self.l6_c,
                                             ################################
                                             self.l7_w,
                                             self.l7_c,
                                             ################################
                                             self.l8_w,
                                             self.l8_c,
                                             ################################
                                             self.l9_w,
                                             self.l9_c,
                                             ################################
                                             self.l10_w,
                                             self.l10_c,
                                             ])
        dane_do_misji=dane_do_misji.to_numpy()
        dane_do_misji=np.array(dane_do_misji).reshape(-1,20)
        print("Model podzielony**********************************")
        
        ######################################################################
        
        dane_do_tetna=pd.DataFrame([         self.l1_t,
                                             statistics.variance(self.tetno1),
                                             self.czas_ekst1,
                                             self.l2_t,
                                             
                                             statistics.variance(self.tetno2),
                                             self.czas_ekst2,
                                             self.l3_t,
                                             
                                             statistics.variance(self.tetno3),
                                             self.czas_ekst3,
                                             self.l4_t,
                                             
                                             statistics.variance(self.tetno4),
                                             self.czas_ekst4,
                                             self.l5_t,
                                             
                                             statistics.variance(self.tetno5),
                                             self.czas_ekst5,
                                             self.l6_t,
                                             
                                             statistics.variance(self.tetno6),
                                             self.czas_ekst6,
                                             self.l7_t,
                                             
                                             statistics.variance(self.tetno7),
                                             self.czas_ekst7,
                                             self.l8_t,
                                            
                                             statistics.variance(self.tetno8),
                                             self.czas_ekst8,
                                             self.l9_t,
                                             
                                             statistics.variance(self.tetno9),
                                             self.czas_ekst9,
                                             self.l10_t,
                                             
                                             statistics.variance(self.tetno10),
                                             self.czas_ekst10,

        ])
        dane_do_tetna=dane_do_tetna.to_numpy()
        dane_do_tetna=np.array(dane_do_tetna).reshape(-1,30)
        dane_do_twarzy=pd.DataFrame([self.l1_f,
                        self.l2_f,
                        self.l3_f,
                        self.l4_f,
                        self.l5_f,
                        self.l6_f,
                        self.l7_f,
                        self.l8_f,
                        self.l9_f,
                        self.l10_f,

        ])
        dane_do_twarzy=dane_do_twarzy.to_numpy()
        dane_do_twarzy=np.array(dane_do_twarzy).reshape(-1,10)
        dane_do_tetna_VR=pd.DataFrame([  
                                            self.VR_levels.data_t1,
                                             statistics.variance(self.VR_levels.tetno1),
                                             self.VR_levels.czas_ekst_1,
                                                self.VR_levels.data_t2,
                                             statistics.variance(self.VR_levels.tetno2),
                                             self.VR_levels.czas_ekst_2,
                                            self.VR_levels.data_t3,
                                             statistics.variance(self.VR_levels.tetno3),
                                             self.VR_levels.czas_ekst_3,
                                                self.VR_levels.data_t4,
                                             statistics.variance(self.VR_levels.tetno4),
                                             self.VR_levels.czas_ekst_4,
                                            self.VR_levels.data_t5,
                                             statistics.variance(self.VR_levels.tetno5),
                                             self.VR_levels.czas_ekst_5,
                                            self.VR_levels.data_t6,
                                             statistics.variance(self.VR_levels.tetno6),
                                             self.VR_levels.czas_ekst_6,
                                            self.VR_levels.data_t7,
                                             statistics.variance(self.VR_levels.tetno7),
                                             self.VR_levels.czas_ekst_7,
                                                self.VR_levels.data_t8,
                                             statistics.variance(self.VR_levels.tetno8),
                                             self.VR_levels.czas_ekst_8,
                                                self.VR_levels.data_t9,
                                             statistics.variance(self.VR_levels.tetno9),
                                             self.VR_levels.czas_ekst_9,
                                            self.VR_levels.data_t10,
                                             statistics.variance(self.VR_levels.tetno10),
                                             self.VR_levels.czas_ekst_10
        ])
        dane_do_tetna_VR=dane_do_tetna_VR.to_numpy()
        dane_do_tetna_VR=np.array(dane_do_tetna_VR).reshape(-1,30)

        self.misje=np.argmax(self.model_misje.predict(dane_do_misji)[0])
        
        self.tetno=np.argmax(self.model_tetno.predict(dane_do_tetna)[0])
        
        self.twarz=np.argmax(self.model_twarz.predict(dane_do_twarzy)[0])
        
        self.tetnoVR=np.argmax(self.model_tetnoVR.predict(dane_do_tetna_VR)[0])
        
        if self.tetnoVR==0 or self.tetno==0:
            self.napis_tetno="Postaraj się popracować nad swoim układem krążenia, takie działania jak aktywność fizyczna i zbilansowana dieta mogą pomóc. "
        if self.twarz==0: 
            self.napis_twarz="Spróbuj popracować nad emocjami lub ekspresją swojej twarzy. "
        if self.misje==0:
            self.napis_misje="Poświęć więcej czasu na trening przy wykorzystaniu symulatorów BSP. "
        suma_napisow=self.napis_tetno+self.napis_twarz+self.napis_misje
        x=(pow(2,3)*self.misje)+(pow(2,2)*self.tetno)+(pow(2,1)*self.twarz)+self.tetnoVR
        print(x)
        procenty=x*100/15.0
        self.napis_procent="Komputer ocenił, że nadajesz się na operatora BSP w {} procentach".format(procenty)
        if self.misje==0 and self.tetno==0 and self.twarz==0 and self.tetnoVR==0:
            self.napis_misje2="Niestety, wykonałeś zbyt mało misji lub zajęło ci to zbyt dużo czasu. "
            self.napis_tetno2="Twoje tętno osiągało zbyt duże wartości lub charakteryzowało się dużą zmiennością. "
            self.napis_twarz2="Twoja twarz przedstawiała inne emocje niż szczęście i neutralność. "
            self.napis_tetnoVR2="W trakcie badania w wirtualnej rzeczywistości twoje tętno zmieniało się zbyt często. "
        if self.misje==0 and self.tetno==0 and self.twarz==0 and self.tetnoVR==1:
            self.napis_misje2="Niestety, wykonałeś zbyt mało misji lub zajęło ci to zbyt dużo czasu. "
            self.napis_tetno2="Twoje tętno osiągało zbyt duże wartości lub charakteryzowało się dużą zmiennością. "
            self.napis_twarz2="Twoja twarz przedstawiała inne emocje niż szczęście i neutralność. "
        if self.misje==0 and self.tetno==0 and self.twarz==1 and self.tetnoVR==0:
            self.napis_misje2="Niestety, wykonałeś zbyt mało misji lub zajęło ci to zbyt dużo czasu. "
            self.napis_tetno2="Twoje tętno osiągało zbyt duże wartości lub charakteryzowało się dużą zmiennością. "
            self.napis_tetnoVR2="W trakcie badania w wirtualnej rzeczywistości twoje tętno zmieniało się zbyt często. "
        if self.misje==0 and self.tetno==0 and self.twarz==1 and self.tetnoVR==1:
            self.napis_misje2="Niestety, wykonałeś zbyt mało misji lub zajęło ci to zbyt dużo czasu. "
            self.napis_tetno2="Twoje tętno osiągało zbyt duże wartości lub charakteryzowało się dużą zmiennością. "

        if self.misje==0 and self.tetno==1 and self.twarz==0 and self.tetnoVR==0:
            self.napis_misje2="Niestety, wykonałeś zbyt mało misji lub zajęło ci to zbyt dużo czasu. "
            self.napis_twarz2="Twoja twarz przedstawiała inne emocje niż szczęście i neutralność. "
            self.napis_tetnoVR2="W trakcie badania w wirtualnej rzeczywistości twoje tętno zmieniało się zbyt często. "
        if self.misje==0 and self.tetno==1 and self.twarz==0 and self.tetnoVR==1:
            self.napis_misje2="Niestety, wykonałeś zbyt mało misji lub zajęło ci to zbyt dużo czasu. "
            self.napis_twarz2="Twoja twarz przedstawiała inne emocje niż szczęście i neutralność. "
        if self.misje==0 and self.tetno==1 and self.twarz==1 and self.tetnoVR==0:
            self.napis_misje2="Niestety, wykonałeś zbyt mało misji lub zajęło ci to zbyt dużo czasu. "
            self.napis_tetnoVR2="W trakcie badania w wirtualnej rzeczywistości twoje tętno zmieniało się zbyt często. "
        if self.misje==0 and self.tetno==1 and self.twarz==1 and self.tetnoVR==1:
            self.napis_misje2="Niestety, wykonałeś zbyt mało misji lub zajęło ci to zbyt dużo czasu. "
        if self.misje==1 and self.tetno==0 and self.twarz==0 and self.tetnoVR==0:
            self.napis_tetno2="Twoje tętno osiągało zbyt duże wartości lub charakteryzowało się dużą zmiennością. "
            self.napis_twarz2="Twoja twarz przedstawiała inne emocje niż szczęście i neutralność. "
            self.napis_tetnoVR2="W trakcie badania w wirtualnej rzeczywistości twoje tętno zmieniało się zbyt często. "
        if self.misje==1 and self.tetno==0 and self.twarz==0 and self.tetnoVR==1:
            self.napis_tetno2="Twoje tętno osiągało zbyt duże wartości lub charakteryzowało się dużą zmiennością. "
            self.napis_twarz2="Twoja twarz przedstawiała inne emocje niż szczęście i neutralność. "
        if self.misje==1 and self.tetno==0 and self.twarz==1 and self.tetnoVR==0:
            self.napis_tetno2="Twoje tętno osiągało zbyt duże wartości lub charakteryzowało się dużą zmiennością. "
            self.napis_tetnoVR2="W trakcie badania w wirtualnej rzeczywistości twoje tętno zmieniało się zbyt często. "
        if self.misje==1 and self.tetno==0 and self.twarz==1 and self.tetnoVR==1:
            self.napis_tetno2="Twoje tętno osiągało zbyt duże wartości lub charakteryzowało się dużą zmiennością. "
        if self.misje==1 and self.tetno==1 and self.twarz==0 and self.tetnoVR==0:
            self.napis_twarz2="Twoja twarz przedstawiała inne emocje niż szczęście i neutralność. "
            self.napis_tetnoVR2="W trakcie badania w wirtualnej rzeczywistości twoje tętno zmieniało się zbyt często. "
        if self.misje==1 and self.tetno==1 and self.twarz==0 and self.tetnoVR==1:
            self.napis_twarz2="Twoja twarz przedstawiała inne emocje niż szczęście i neutralność. "
        if self.misje==1 and self.tetno==1 and self.twarz==1 and self.tetnoVR==0:
            self.napis_tetnoVR2="W trakcie badania w wirtualnej rzeczywistości twoje tętno zmieniało się zbyt często. "
        if self.misje==1 and self.tetno==1 and self.twarz==1 and self.tetnoVR==1:
            self.napis_misje2="Gratulacje! Wszystko poszło idealnie! Masz wszystkie cechy aby być świetnym operatorem BSP!. "
            suma_napisow="Tak trzymaj!"
        self.ui.procenty.setText(self.napis_procent)
        self.ui.rada.setText(suma_napisow) 
        suma=self.napis_misje2+self.napis_tetno2+self.napis_twarz2+self.napis_tetnoVR2
        self.ui.komunikat.setText(suma)
         


############EXECUTE#####################        
if __name__=="__main__":
    app=QApplication(sys.argv)
    path=os.path.dirname(__file__)
    pixmap = QPixmap(path+r"\splash.png")
    splash = QSplashScreen(pixmap)
    splash.setGeometry(2400,300,800,450)
    splash.show()
    app.processEvents()
    window=MainWindow()
    splash.finish(window)

    sys.exit(app.exec_())