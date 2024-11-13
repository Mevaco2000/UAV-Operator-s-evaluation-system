import sys
import os 
from ui_VR_levels import *
import airsim
import time
from PySide2 import QtCore,QtGui
from PySide2.QtCore import QThread, Signal
import math
import pandas as pd
import statistics

class LandingThread(QThread):
   def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       client.moveToPositionAsync(0,0,-3,10).join()
       client.moveToPositionAsync(0,0,-1,10).join()
       client.landAsync(5).join()
       client.reset()
       client.enableApiControl(False)
       client.armDisarm(False)
##########Level 1######################
class WorkerThread_7(QThread):
   #Definicja sygnału pokazującego badającemu postęp poziomu#
   update_progress=Signal(int)
   #Metoda obliczająca drogę, którą przebywa BSP#
   def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
   #Metoda wykonująca ruch BSP do zadanej pozycji#
   def move3(self,x2,y2,z2,v):
        #Połączenie z symulatorem AIRSim#
        client=airsim.MultirotorClient()
        #Pobranie informacji nt. aktualnej pozycji BSP#
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        #Polecenie ruchu#
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
   ###########Scenariusz##########################
   def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       self.update_progress.emit(0)
       client.moveByAngleRatesZAsync(0,0,-3.14,-10,2).join()
       self.move3(0,0,-50,5)
       self.update_progress.emit(25)
       self.move3(10,0,-50,5)
       self.update_progress.emit(50)
       self.move3(20,0,-50,5)
       self.update_progress.emit(75)
       self.move3(30,0,-50,5)
       self.update_progress.emit(100)         
##########Level 2######################
class WorkerThread_8(QThread):
   #Definicja sygnału pokazującego badającemu postęp poziomu#
   update_progress=Signal(int)
   #Metoda obliczająca drogę, którą przebywa BSP#
   def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
   #Metoda wykonująca obrót BSP aby kamera była ustawiona równolegle do osi łączącej zadaną pozycję z obecną#
   def rotate_drone(self,x2,y2):
       client=airsim.MultirotorClient()
       orientation=client.simGetVehiclePose().orientation
       state=client.getMultirotorState()
       position2=state.kinematics_estimated.position
       pitch,roll,yaw=airsim.to_eularian_angles(orientation)
       x1=position2.x_val
       y1=position2.y_val
       tangens=math.atan((y2-y1)/(x2-x1))
       print("************************************************")
       print("Tangens1")
       print(tangens*180/3.14)
       #Wynik obrotu w przypadku braku odchylen
       if yaw<=0.05:
          wynik=yaw-tangens
       else:
          wynik=-(yaw-tangens)
       print("Wynik obliczen")
       print(wynik*180/3.14)
       client.moveByAngleRatesZAsync(0,0,wynik/2,position2.z_val,2).join()
   #Metoda wykonująca ruch BSP do zadanej pozycji#
   def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
   ###########Scenariusz##########################
   def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       self.update_progress.emit(0)
       self.rotate_drone(45,-15)
       self.update_progress.emit(12.5)
       client.moveToPositionAsync(45,-15,-50,5).join()
       self.update_progress.emit(25)
       self.rotate_drone(60,0)
       self.update_progress.emit(37.5)
       client.moveToPositionAsync(60,0,-50,5).join()
       self.update_progress.emit(50)
       self.rotate_drone(45,15)
       self.update_progress.emit(62.5)
       client.moveToPositionAsync(45,15,-50,5).join()
       self.update_progress.emit(75)
       self.rotate_drone(30,0)
       self.update_progress.emit(87.5)
       client.moveToPositionAsync(30,0,-50,5).join()
       self.update_progress.emit(100)       
##########Level 3######################
class WorkerThread_9(QThread):
   #Definicja sygnału pokazującego badającemu postęp poziomu#
   update_progress=Signal(int)
   #Metoda wykonująca obrót BSP aby kamera była ustawiona równolegle do osi łączącej zadaną pozycję z obecną#
   def rotate_drone(self,x2,y2):
       client=airsim.MultirotorClient()
       orientation=client.simGetVehiclePose().orientation
       state=client.getMultirotorState()
       position2=state.kinematics_estimated.position
       pitch,roll,yaw=airsim.to_eularian_angles(orientation)
       x1=position2.x_val
       y1=position2.y_val
       tangens=math.atan((y2-y1)/(x2-x1))
       print("************************************************")
       print("Tangens1")
       print(tangens*180/3.14)
       #Wynik obrotu w przypadku braku odchylen
       if yaw<=0:
          wynik=yaw-tangens
       else:
          wynik=-(yaw-tangens)
      
       print("Wynik obliczen")
       print(wynik*180/3.14)
       client.moveByAngleRatesZAsync(0,0,wynik/2,position2.z_val,2).join()
   #Metoda obliczająca drogę, którą przebywa BSP#
   def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
   #Metoda wykonująca ruch BSP do zadanej pozycji#
   def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
   ###########Scenariusz##########################
   def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       self.update_progress.emit(0)
       v=10
       self.move3(45,-15,-50,v)
       self.update_progress.emit(25)
       self.move3(60,0,-50,v)
       self.update_progress.emit(50)
       self.move3(45,15,-50,v)
       self.update_progress.emit(75)

       self.move3(30,0,-50,v)
       self.update_progress.emit(100)   
##########Level 4######################
class WorkerThread_10(QThread):
   #Definicja sygnału pokazującego badającemu postęp poziomu#
   update_progress=Signal(int)
   #Metoda obliczająca drogę, którą przebywa BSP#
   def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
   #Metoda wykonująca ruch BSP do zadanej pozycji#
   def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
   ###########Scenariusz##########################
   def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       self.update_progress.emit(0)
       v=10
       
       self.move3(40,-10,-60,v)
       self.update_progress.emit(12)
       self.move3(50,-20,-40,v)
       self.update_progress.emit(20)

       self.move3(60,-30,-40,v)
       self.update_progress.emit(28)
       self.move3(70,-20,-60,v)
       self.update_progress.emit(36)
       self.move3(80,-10,-40,v)
       self.update_progress.emit(44)
       
       self.move3(90,0,-60,v)
       self.update_progress.emit(52)
       self.move3(80,10,-40,v)
       self.update_progress.emit(60)
       self.move3(70,20,-60,v)
       self.update_progress.emit(68)
       
       self.move3(60,30,-40,v)
       self.update_progress.emit(76)
       self.move3(50,20,-60,v)
       self.update_progress.emit(84)
       self.move3(40,10,-40,v)
       self.update_progress.emit(92)
       
       
       self.move3(30,0,-60,v)
       self.update_progress.emit(100)     
##########Level 5######################
class WorkerThread(QThread):#######Level 5
    #Definicja sygnału pokazującego badającemu postęp poziomu#
    update_progress=Signal(int)
    if_land=Signal(int)
    #Metoda obliczająca drogę, którą przebywa BSP#
    def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=2*math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
    #Metoda wykonująca ruch BSP do zadanej pozycji#
    def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
    #Metoda wykonująca obrót BSP aby kamera była ustawiona równolegle do osi łączącej zadaną pozycję z obecną#
    def rotate_drone(self,x2,y2):
       client=airsim.MultirotorClient()
       orientation=client.simGetVehiclePose().orientation
       state=client.getMultirotorState()
       position2=state.kinematics_estimated.position
       pitch,roll,yaw=airsim.to_eularian_angles(orientation)
       x1=position2.x_val
       y1=position2.y_val
       wynik=math.atan((y2-y1)/(x2-x1))
       if wynik>0 and yaw>0:
          wynik=-abs(wynik)-abs(yaw)
       elif wynik>0 and yaw<0:
          wynik=abs(wynik)-abs(yaw)
       elif wynik<0 and yaw>0:
          wynik=3.14-abs(wynik)-abs(yaw)
       else:
          wynik=3.14+abs(wynik)-abs(yaw)
       print("Kat przyszlego obrotu")
       print(wynik*180/3.14)
       print("Obecne odchylenie")
       print(yaw*180/3.14)
       client.moveByAngleRatesZAsync(0,0,wynik,position2.z_val,1).join()
    ###########Scenariusz##########################
    def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       self.update_progress.emit(0)
       v=10
       
       self.move3(40,0,-50,v)
       self.update_progress.emit(12)
       self.move3(50,-30,-50,v)
       self.update_progress.emit(20)

       self.move3(60,-30,-50,v)
       self.update_progress.emit(28)
       self.move3(70,-30,-50,v)
       self.update_progress.emit(36)
       self.move3(90,-10,-50,v)
       self.update_progress.emit(44)
       
       self.move3(90,0,-50,v)
       self.update_progress.emit(52)
       self.move3(90,10,-50,v)
       self.update_progress.emit(60)
       self.move3(70,30,-50,v)
       self.update_progress.emit(68)
       
       self.move3(60,30,-50,v)
       self.update_progress.emit(76)
       self.move3(50,30,-50,v)
       self.update_progress.emit(84)
       self.move3(40,0,-50,v)
       self.update_progress.emit(92)
       
       
       self.move3(30,0,-50,v)
       self.update_progress.emit(100)    
#######Level 6########################
class WorkerThread_2(QThread):#########Level 6
    #Definicja sygnału pokazującego badającemu postęp poziomu#
    update_progress=Signal(int)
    #Metoda obliczająca drogę, którą przebywa BSP#
    def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=2*math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
    #Metoda wykonująca ruch BSP do zadanej pozycji#
    def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
    #Metoda wykonująca obrót BSP aby kamera była ustawiona równolegle do osi łączącej zadaną pozycję z obecną#
    def rotate_drone(self,x2,y2):
       client=airsim.MultirotorClient()
       orientation=client.simGetVehiclePose().orientation
       state=client.getMultirotorState()
       position2=state.kinematics_estimated.position
       pitch,roll,yaw=airsim.to_eularian_angles(orientation)
       x1=position2.x_val
       y1=position2.y_val
       wynik=math.atan((y2-y1)/(x2-x1))
       if wynik>0 and yaw>0:
          wynik=-abs(wynik)-abs(yaw)
       elif wynik>0 and yaw<0:
          wynik=abs(wynik)-abs(yaw)
       elif wynik<0 and yaw>0:
          wynik=3.14-abs(wynik)-abs(yaw)
       else:
          wynik=3.14+abs(wynik)-abs(yaw)
       print("Kat przyszlego obrotu")
       print(wynik*180/3.14)
       print("Obecne odchylenie")
       print(yaw*180/3.14)
       client.moveByAngleRatesZAsync(0,0,wynik,position2.z_val,1).join()
    ###########Scenariusz##########################
    def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       self.update_progress.emit(0)
       v=15
       
       self.move3(40,0,-30,v)
       self.update_progress.emit(12)
       self.move3(50,-30,-70,v)
       self.update_progress.emit(20)

       self.move3(60,-30,-30,v)
       self.update_progress.emit(28)
       self.move3(70,-30,-70,v)
       self.update_progress.emit(36)
       self.move3(90,-10,-30,v)
       self.update_progress.emit(44)
       
       self.move3(90,0,-70,v)
       self.update_progress.emit(52)
       self.move3(90,10,-30,v)
       self.update_progress.emit(60)
       self.move3(70,30,-70,v)
       self.update_progress.emit(68)
       
       self.move3(60,30,-30,v)
       self.update_progress.emit(76)
       self.move3(50,30,-70,v)
       self.update_progress.emit(84)
       self.move3(40,0,-30,v)
       self.update_progress.emit(92)
       
       
       self.move3(30,0,-50,v)
       self.update_progress.emit(100)       
#######Level 7########################
class WorkerThread_3(QThread):########Level 7
    #Definicja sygnału pokazującego badającemu postęp poziomu#
    update_progress=Signal(int)
    #Metoda obliczająca drogę, którą przebywa BSP#
    def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=2*math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
    #Metoda wykonująca ruch BSP do zadanej pozycji#
    def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
    #Metoda wykonująca obrót BSP aby kamera była ustawiona równolegle do osi łączącej zadaną pozycję z obecną#
    def rotate_drone(self,x2,y2):
       client=airsim.MultirotorClient()
       orientation=client.simGetVehiclePose().orientation
       state=client.getMultirotorState()
       position2=state.kinematics_estimated.position
       pitch,roll,yaw=airsim.to_eularian_angles(orientation)
       x1=position2.x_val
       y1=position2.y_val
       wynik=math.atan((y2-y1)/(x2-x1))
       if wynik>0 and yaw>0:
          wynik=-abs(wynik)-abs(yaw)
       elif wynik>0 and yaw<0:
          wynik=abs(wynik)-abs(yaw)
       elif wynik<0 and yaw>0:
          wynik=3.14-abs(wynik)-abs(yaw)
       else:
          wynik=3.14+abs(wynik)-abs(yaw)
       client.moveByAngleRatesZAsync(0,0,wynik,position2.z_val,1).join()
    ###########Scenariusz##########################
    def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       

       v=17
       self.move3(40,0,-30,v)
       self.update_progress.emit(12)
       self.move3(50,-30,-70,v)
       self.update_progress.emit(20)
       client.moveByAngleRatesZAsync(0.0,-0.5,0,-60,2).join()

       self.move3(60,-30,-30,v)
       self.update_progress.emit(28)
       self.move3(70,-30,-70,v)
       self.update_progress.emit(36)
       self.move3(90,-10,-30,v)
       self.update_progress.emit(44)
       client.moveByAngleRatesZAsync(0.0,-0.5,0,-60,4).join()
       self.move3(90,0,-70,v)
       self.update_progress.emit(52)
       self.move3(90,10,-30,v)
       self.update_progress.emit(60)
       self.move3(70,30,-70,v)
       self.update_progress.emit(68)
       client.moveByAngleRatesZAsync(0.0,-0.5,0,-60,2).join()
       self.move3(60,30,-30,v)
       self.update_progress.emit(76)
       self.move3(50,30,-70,v)
       self.update_progress.emit(84)
       self.move3(40,0,-30,v)
       self.update_progress.emit(92)
       client.moveByAngleRatesZAsync(0.0,-0.5,0,-60,2).join()
       
       self.move3(30,0,-50,v)
       self.update_progress.emit(100)     
#######Level 8########################
class WorkerThread_4(QThread):#######Level 8
    #Definicja sygnału pokazującego badającemu postęp poziomu#
    update_progress=Signal(int)
    #Metoda obliczająca drogę, którą przebywa BSP#
    def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=2*math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
    #Metoda wykonująca ruch BSP do zadanej pozycji#
    def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
    #Metoda wykonująca obrót BSP aby kamera była ustawiona równolegle do osi łączącej zadaną pozycję z obecną#
    def rotate_drone(self,x2,y2):
       client=airsim.MultirotorClient()
       orientation=client.simGetVehiclePose().orientation
       state=client.getMultirotorState()
       position2=state.kinematics_estimated.position
       pitch,roll,yaw=airsim.to_eularian_angles(orientation)
       x1=position2.x_val
       y1=position2.y_val
       wynik=math.atan((y2-y1)/(x2-x1))
       if wynik>0 and yaw>0:
          wynik=-abs(wynik)-abs(yaw)
       elif wynik>0 and yaw<0:
          wynik=abs(wynik)-abs(yaw)
       elif wynik<0 and yaw>0:
          wynik=3.14-abs(wynik)-abs(yaw)
       else:
          wynik=3.14+abs(wynik)-abs(yaw)
       print("Kat przyszlego obrotu")
       print(wynik*180/3.14)
       print("Obecne odchylenie")
       print(yaw*180/3.14)
       client.moveByAngleRatesZAsync(0,0,wynik,position2.z_val,1).join()
    ###########Scenariusz##########################
    def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       v=17
       self.move3(40,0,-30,v)
       self.update_progress.emit(12)
       self.move3(50,-30,-70,v)
       self.update_progress.emit(20)
       client.moveByAngleRatesZAsync(-0.5,0,0,-60,2).join()

       self.move3(60,-30,-30,v)
       self.update_progress.emit(28)
       self.move3(70,-30,-70,v)
       self.update_progress.emit(36)
       self.move3(90,-10,-30,v)
       self.update_progress.emit(44)
       client.moveByAngleRatesZAsync(-0.5,0,0,-60,2).join()
       self.move3(90,0,-70,v)
       self.update_progress.emit(52)
       self.move3(90,10,-30,v)
       self.update_progress.emit(60)
       self.move3(70,30,-70,v)
       self.update_progress.emit(68)
       client.moveByAngleRatesZAsync(-0.5,0,0,-60,2).join()
       self.move3(60,30,-30,v)
       self.update_progress.emit(76)
       self.move3(50,30,-70,v)
       self.update_progress.emit(84)
       self.move3(40,0,-30,v)
       self.update_progress.emit(92)
       client.moveByAngleRatesZAsync(-0.5,0,0,-60,2).join()
       
       self.move3(30,0,-50,v)
       self.update_progress.emit(100)    
#######Level 9#######################
class WorkerThread_5(QThread):######Level 9 
    #Definicja sygnału pokazującego badającemu postęp poziomu#
    update_progress=Signal(int)
    #Metoda obliczająca drogę, którą przebywa BSP#
    def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=2*math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
    #Metoda wykonująca ruch BSP do zadanej pozycji#
    def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
    #Metoda wykonująca obrót BSP aby kamera była ustawiona równolegle do osi łączącej zadaną pozycję z obecną#
    def rotate_drone(self,x2,y2):
       client=airsim.MultirotorClient()
       orientation=client.simGetVehiclePose().orientation
       state=client.getMultirotorState()
       position2=state.kinematics_estimated.position
       pitch,roll,yaw=airsim.to_eularian_angles(orientation)
       x1=position2.x_val
       y1=position2.y_val
       wynik=math.atan((y2-y1)/(x2-x1))
       if wynik>0 and yaw>0:
          wynik=-abs(wynik)-abs(yaw)
       elif wynik>0 and yaw<0:
          wynik=abs(wynik)-abs(yaw)
       elif wynik<0 and yaw>0:
          wynik=3.14-abs(wynik)-abs(yaw)
       else:
          wynik=3.14+abs(wynik)-abs(yaw)
       print("Kat przyszlego obrotu")
       print(wynik*180/3.14)
       print("Obecne odchylenie")
       print(yaw*180/3.14)
       client.moveByAngleRatesZAsync(0,0,wynik,position2.z_val,1).join()
    ###########Scenariusz##########################
    def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       v=25
       self.move3(40,0,-70,v)
       client.moveByAngleRatesZAsync(0,-0.5,0,-60,2).join()
       self.update_progress.emit(12)
       self.move3(50,-30,-10,v)
       self.update_progress.emit(20)
       

       self.move3(60,-30,-30,v)
       self.update_progress.emit(28)
       self.move3(70,-30,-70,v)
       self.update_progress.emit(36)
       client.moveByAngleRatesZAsync(0,-0.5,0,-60,2).join()
       self.move3(90,-10,-5,v)
       self.update_progress.emit(44)
       
       self.move3(90,0,-70,v)
       self.update_progress.emit(52)
       self.move3(90,10,-10,v)
       self.update_progress.emit(60)
       self.move3(70,30,-70,v)
       self.update_progress.emit(68)
       client.moveByAngleRatesZAsync(0,-0.5,0,-60,2).join()
       self.move3(60,30,-5,v)
       self.update_progress.emit(76)
       self.move3(50,30,-70,v)
       self.update_progress.emit(84)
       self.move3(40,0,-10,v)
       self.update_progress.emit(92)
       client.moveByAngleRatesZAsync(0,-0.5,0,-60,2).join()
       
       self.move3(30,0,-50,v)
       self.update_progress.emit(100)  
#######Level 10#######################
class WorkerThread_6(QThread):######Level 10
    #Definicja sygnału pokazującego badającemu postęp poziomu#
    update_progress=Signal(int)
    #Metoda obliczająca drogę, którą przebywa BSP#
    def droga3(self,x1,x2,y1,y2,z1,z2):
        droga=2*math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2)+math.pow((z2-z1),2))
        return droga
    #Metoda wykonująca ruch BSP do zadanej pozycji#
    def move3(self,x2,y2,z2,v):
        client=airsim.MultirotorClient()
        state=client.getMultirotorState()
        o=state.kinematics_estimated.position
        client.moveOnPathAsync([o,airsim.Vector3r(x2,y2,z2)],v,(self.droga3(o.x_val,x2,o.y_val,y2,o.z_val,z2)/v),airsim.DrivetrainType.ForwardOnly,airsim.YawMode(False,0),v*1.5,
                              1).join()
    #Metoda wykonująca obrót BSP aby kamera była ustawiona równolegle do osi łączącej zadaną pozycję z obecną#
    def rotate_drone(self,x2,y2):
       client=airsim.MultirotorClient()
       orientation=client.simGetVehiclePose().orientation
       state=client.getMultirotorState()
       position2=state.kinematics_estimated.position
       pitch,roll,yaw=airsim.to_eularian_angles(orientation)
       x1=position2.x_val
       y1=position2.y_val
       wynik=math.atan((y2-y1)/(x2-x1))
       if wynik>0 and yaw>0:
          wynik=-abs(wynik)-abs(yaw)
       elif wynik>0 and yaw<0:
          wynik=abs(wynik)-abs(yaw)
       elif wynik<0 and yaw>0:
          wynik=3.14-abs(wynik)-abs(yaw)
       else:
          wynik=3.14+abs(wynik)-abs(yaw)
       print("Kat przyszlego obrotu")
       print(wynik*180/3.14)
       print("Obecne odchylenie")
       print(yaw*180/3.14)
       client.moveByAngleRatesZAsync(0,0,wynik,position2.z_val,1).join()
    ###########Scenariusz##########################
    def run(self):
       client=airsim.MultirotorClient()
       client.enableApiControl(True)
       client.armDisarm(True)
       v=25
       self.move3(40,0,-70,v)
       client.moveByAngleRatesZAsync(0,-0.5,0,-60,2).join()
       self.update_progress.emit(12)
       self.move3(50,-30,-20,v)
       self.update_progress.emit(20)
       

       self.move3(60,-30,-30,v)
       self.update_progress.emit(28)
       self.move3(70,-30,-70,v)
       self.update_progress.emit(36)
       client.moveByAngleRatesZAsync(0,-0.5,0,-60,2).join()
       self.move3(90,-10,-10,v)
       self.update_progress.emit(44)
       
       self.move3(90,0,-70,v)
       client.moveByAngleRatesZAsync(1.0,0,0,-60,1).join()
       self.update_progress.emit(52)
       self.move3(90,10,-10,v)
       self.update_progress.emit(60)
       self.move3(70,30,-70,v)
       client.moveByAngleRatesZAsync(-1.0,0,0,-60,1).join()
       self.update_progress.emit(68)
       client.moveByAngleRatesZAsync(0,-0.5,0,-60,2).join()
       self.move3(60,30,-10,v)
       self.update_progress.emit(76)
       self.move3(50,30,-70,v)
       client.moveByAngleRatesZAsync(0,-0.5,5,-60,2).join()
       self.update_progress.emit(84)
       self.move3(40,0,-10,v)
       self.update_progress.emit(92)
       client.moveByAngleRatesZAsync(0,-0.5,0,-60,2).join()
       
       self.move3(30,0,-50,v)
       self.update_progress.emit(100)
       client.landAsync(3).join()
       client.reset()
       client.enableApiControl(False)
       client.armDisarm(False)
class VR_Levels(QMainWindow):
    VR_repeat=0
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui2 = Ui_VR_Levels()
        self.ui2.setupUi(self)
        #######Ustawienie aby okno aplikacji było bez widocznych granic#########
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        ######Ustawienia aby okno zawsze pokazywało się "na górze"#############
        self.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
        ######Rozmiar okna#############
        self.setGeometry(2800,50,480,910)
        #####Ścieżka do pliku###########
        self.path=os.path.dirname(__file__)
        #####Ikona###########
        self.setWindowIcon(QtGui.QIcon(self.path+r"\Icons\Magisterka_python(1)\icons8-vr-glasses-64.png"))
        #####Tytuł okna######
        self.setWindowTitle("VR_poziomy")
        ####Wczytywanie danych z pliku##########
        self.data=pd.read_csv(self.path+r"\Tabela1_vr.csv")
        self.data0=pd.DataFrame()
        ####Definicja poczatkowego napisu w oknie########
        self.ui2.dzialanie.setText("Witamy! Rozpocznij od poziomu 1")
        ####Uniemozliwienie zapisania danych na poczatku###########
        self.ui2.Save.setEnabled(False)
        #*********************************************************############***************************#######################
        ################################################Powiązanie metod z sygnałami############################################
        #Zapisywanie danych do pliku#
        self.ui2.Save.clicked.connect(lambda:self.SaveData())
        #################Poziomy poszczególnych scenariuszy##########################
        self.ui2.VR_poziom1.clicked.connect(lambda:self.VR_poziom1())
        self.ui2.VR_poziom2.clicked.connect(lambda:self.VR_poziom2())
        self.ui2.VR_poziom3.clicked.connect(lambda:self.VR_poziom3())
        self.ui2.VR_poziom4.clicked.connect(lambda:self.VR_poziom4())
        self.ui2.VR_poziom5.clicked.connect(lambda:self.VR_poziom5())
        self.ui2.VR_poziom6.clicked.connect(lambda:self.VR_poziom6())
        self.ui2.VR_poziom7.clicked.connect(lambda:self.VR_poziom7())
        self.ui2.VR_poziom8.clicked.connect(lambda:self.VR_poziom8())
        self.ui2.VR_poziom9.clicked.connect(lambda:self.VR_poziom9())
        self.ui2.VR_poziom10.clicked.connect(lambda:self.VR_poziom10())
        ###############Lądowanie awaryjne############################################
        self.ui2.landing_button.clicked.connect(lambda:self.landing())
        ##############Zamknięcie okna###############################################
        self.ui2.Close.clicked.connect(lambda:self.close())
        ##############Minimalizowanie okna###########################################
        self.ui2.Min.clicked.connect(lambda:self.showMinimized())
        ##############Powtórzenie pomiarów###########################################
        self.ui2.Repeat.clicked.connect(lambda:self.repeat())
        ##############Automatyczne przełączanie scenariuszy##########################
        self.ui2.Save_2.clicked.connect(lambda:self.automat())
        ##Definicja zmiennej warunkującej automatyczne przełączanie między poziomami#
        self.automatyczneprzelaczanie=0
        ##Definicja zegara zmieniającego ikonę tętna########
        self.timer=QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(lambda:self.tetno_zmiana_obrazka())
        ##Zmienna warunkujaca zmiane ikony tetna############
        self.kolorobrazka=0
        ##Definicja zmiennej okreslajacej ilosc wykonanych poziomow##########
        self.levels=0
        ##Definicja zmiennej warunkujacej zapis danych odpowiednich dla danego poziomu#
        self.level=0
        ##Definicja list zawierajacych dane rejestrowane w trakcie każdego z poziomów####
        #Tętno#
        self.tetno0=[]
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
        #Czas#
        self.time0=0
        self.time1=0
        self.time2=0
        self.time3=0
        self.time4=0
        self.time5=0
        self.time6=0
        self.time7=0
        self.time8=0
        self.time9=0
        self.time10=0
        #Czas między poszczególnych ekstremami#
        self.czas_ekst_1=0
        self.czas_ekst_2=0
        self.czas_ekst_3=0
        self.czas_ekst_4=0
        self.czas_ekst_5=0
        self.czas_ekst_6=0
        self.czas_ekst_7=0
        self.czas_ekst_8=0
        self.czas_ekst_9=0
        self.czas_ekst_10=0
        #Odstepy czasowe pomiedzy poszczegolnymi pomiarami tętna#
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
        ###Definicja zmiennej warunkującej koniec danego poziomu#
        self.koniec=0
        ###Definicja zmiennej warunkującej koniec badania####
        self.koniec_koncow=0
        ###Definicja zmiennej umożliwiającej powtórzenie danego poziomu po wylądowaniu#
        self.landingbacklevel=0
        ##############Pokazanie okna aplikacji##################
        self.show()
    #####Metoda umożliwiająca automatyczne przełączanie między poziomami######
    def automat(self): 
       self.automatyczneprzelaczanie=1
       self.ui2.Save_2.setEnabled(False)
       self.ui2.Save_2.setStyleSheet("background-color:red")
       self.ui2.VR_poziom1.click()
       self.ui2.VR_poziom1.setEnabled(False)
       self.ui2.VR_poziom2.setEnabled(False)
       self.ui2.VR_poziom3.setEnabled(False)
       self.ui2.VR_poziom4.setEnabled(False)
       self.ui2.VR_poziom5.setEnabled(False)
       self.ui2.VR_poziom6.setEnabled(False)
       self.ui2.VR_poziom7.setEnabled(False)
       self.ui2.VR_poziom8.setEnabled(False)
       self.ui2.VR_poziom9.setEnabled(False)
       self.ui2.VR_poziom10.setEnabled(False)
       self.ui2.Repeat.setEnabled(False)
    #####Metoda służąca do obliczania czasu pomiędzy maksymalną i minimalną wartością tętna######
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
    #####Metoda zmieniająca ikonę tętna (miganie)#####
    def tetno_zmiana_obrazka(self):
       if self.kolorobrazka==0:
         self.ui2.label_2.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-heart-rate-50-1.png"))
         self.kolorobrazka=1
       else: 
         self.ui2.label_2.setPixmap(QPixmap(self.path+r"\Icons\Magisterka_python(1)\icons8-heart-rate-50.png"))
         self.kolorobrazka=0
       self.time0 +=1  
       match self.level:
          case 1:
             self.time1 +=1
          case 2:
             self.time2 +=1
          case 3:
            self.time3 +=1
          case 4:
             self.time4 +=1
          case 5:
             self.time5 +=1
          case 6:
             self.time6 +=1
          case 7:
             self.time7 +=1
          case 8: 
             self.time8 +=1
          case 9: 
             self.time9 +=1
          case 10:
             self.time10 +=1
    #####Metoda umożliwiająca powtórzenie całego badania####
    def repeat(self):
       self.ui2.dzialanie.setText("Badanie zaczęło się od nowa, zacznij od poziomu 1...")
       self.ui2.VR_poziom1.setEnabled(True)
       self.ui2.VR_poziom2.setEnabled(False)
       self.ui2.VR_poziom3.setEnabled(False)
       self.ui2.VR_poziom4.setEnabled(False)
       self.ui2.VR_poziom5.setEnabled(False)
       self.ui2.VR_poziom6.setEnabled(False)
       self.ui2.VR_poziom7.setEnabled(False)
       self.ui2.VR_poziom8.setEnabled(False)
       self.ui2.VR_poziom9.setEnabled(False)
       self.ui2.VR_poziom10.setEnabled(False)
       self.ui2.progressBar.setValue(0)
       self.ui2.progressBar_2.setValue(0)
       self.ui2.progressBar_3.setValue(0)
       self.ui2.progressBar_4.setValue(0)
       self.ui2.progressBar_5.setValue(0)
       self.ui2.progressBar_6.setValue(0)
       self.ui2.progressBar_7.setValue(0)
       self.ui2.progressBar_8.setValue(0)
       self.ui2.progressBar_9.setValue(0)
       self.ui2.progressBar_10.setValue(0)
       VR_Levels.VR_repeat=1
    #####Metoda służąca do wykonania lądowania awaryjnego i przerwania badania#######
    def landing(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       match self.worker:
          case WorkerThread():
              self.levels=1
          case WorkerThread_2():
              self.levels=2
          case WorkerThread_3():
              self.levels=3
          case WorkerThread_4():
              self.levels=4
          case WorkerThread_5():
              self.levels=5
          case WorkerThread_6():
              self.levels=6
          case WorkerThread_7():
              self.levels=7
          case WorkerThread_8():
              self.levels=8
          case WorkerThread_9():
              self.levels=9
          case WorkerThread_10():
              self.levels=10
       self.worker.terminate()
       self.worker=LandingThread()
       self.worker.start()
       self.level=0
       self.ui2.dzialanie.setText("Trwa lądowanie...")
       self.worker.finished.connect(self.pokazprzyciski)
       self.worker.quit()
    ####Metoda 
    def pokazprzyciski(self):
       self.worker.terminate()
       print(self.landingbacklevel)
       match self.levels:
          case 0:
             self.schowaj_przyciski()
          case 1:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_5.setValue(0)
             self.ui2.VR_poziom5.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 5...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom6.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 6...")            
          case 2:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_6.setValue(0)
             self.ui2.VR_poziom6.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 6...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom7.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 7...")    
          case 3:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_7.setValue(0)
             self.ui2.VR_poziom7.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 7...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom8.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 8...")    
          case 4:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_8.setValue(0)
             self.ui2.VR_poziom8.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 8...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom9.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 9...")    
          case 5:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_9.setValue(0)
             self.ui2.VR_poziom9.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 9...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom10.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 10...")    
          case 6:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_10.setValue(0)
             self.ui2.VR_poziom10.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 10...")
            else:
             self.schowaj_przyciski()
             self.ui2.dzialanie.setText("Gratulacje! Ukonczyles badanie")
             self.ui2.Repeat.setEnabled(True)
          case 7:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar.setValue(0)
             self.ui2.VR_poziom1.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 1...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom2.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 2...") 
          case 8:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_2.setValue(0)
             self.ui2.VR_poziom2.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 2...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom3.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 3...")   
          case 9:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_3.setValue(0)
             self.ui2.VR_poziom3.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 3...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom4.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 4...") 
          case 10:
            if self.landingbacklevel==0:
             self.schowaj_przyciski()
             self.ui2.progressBar_4.setValue(0)
             self.ui2.VR_poziom4.setEnabled(True)
             self.ui2.dzialanie.setText("Powróć do poziomu 4...")
            else:
             self.schowaj_przyciski()
             self.ui2.VR_poziom5.setEnabled(True)
             self.ui2.dzialanie.setText("Przejdz do poziomu 5...") 
    ####Metoda
    def schowaj_przyciski(self):
       self.ui2.VR_poziom1.setEnabled(False)
       self.ui2.VR_poziom2.setEnabled(False)
       self.ui2.VR_poziom3.setEnabled(False)
       self.ui2.VR_poziom4.setEnabled(False)
       self.ui2.VR_poziom5.setEnabled(False)
       self.ui2.VR_poziom6.setEnabled(False)
       self.ui2.VR_poziom7.setEnabled(False)
       self.ui2.VR_poziom8.setEnabled(False)
       self.ui2.VR_poziom9.setEnabled(False)
       self.ui2.VR_poziom10.setEnabled(False)
       self.ui2.Repeat.setEnabled(False)
    ####Metoda
    def evt_progress(self,val):
       self.ui2.progressBar_5.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 5...")
       elif val==100:
          self.landingbacklevel=1
    def evt_finished(self):
       self.ui2.dzialanie.setText("Przejdz do poziomu 6...")
       self.ui2.VR_poziom6.setEnabled(True)
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       self.level=0
       if self.automatyczneprzelaczanie==1:
          self.ui2.VR_poziom6.click()
    def evt_progress_2(self,val):
       self.ui2.progressBar_6.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 6...")
       elif val==100:
          self.landingbacklevel=1
    def evt_finished_2(self):
          self.ui2.VR_poziom7.setEnabled(True)
          self.ui2.dzialanie.setText("Przejdz do poziomu 7...")
          self.ui2.Save.setEnabled(True)
          self.koniec=1
          self.level=0
          if self.automatyczneprzelaczanie==1:
            self.ui2.VR_poziom7.click()
    def evt_progress_3(self,val):
       self.ui2.progressBar_7.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 7...")
       elif val==100:
          self.landingbacklevel=1      
    def evt_finished_3(self):
       self.ui2.VR_poziom8.setEnabled(True)
       self.ui2.dzialanie.setText("Przejdz do poziomu 8...")
       self.level=0
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       if self.automatyczneprzelaczanie==1:
          self.ui2.VR_poziom8.click()
    def evt_progress_4(self,val):
       self.ui2.progressBar_8.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 8...")
       elif val==100:
          self.landingbacklevel=1         
    def evt_finished_4(self):
       self.ui2.VR_poziom9.setEnabled(True)
       self.ui2.dzialanie.setText("Przejdz do poziomu 9...")
       self.level=0
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       if self.automatyczneprzelaczanie==1:
          self.ui2.VR_poziom9.click()
    def evt_progress_5(self,val):
       self.ui2.progressBar_9.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 9...")
       elif val==100:
          self.landingbacklevel=1
    def evt_finished_5(self):
       self.ui2.VR_poziom10.setEnabled(True)
       self.ui2.dzialanie.setText("Przejdz do poziomu 10")
       self.level=0
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       if self.automatyczneprzelaczanie==1:
          self.ui2.VR_poziom10.click()
    def evt_progress_6(self,val):
       self.ui2.progressBar_10.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 10...")
       elif val==100:
          self.landingbacklevel=1
    def evt_finished_6(self):
       self.ui2.dzialanie.setText("Gratulacje zakonczyles badanie!")
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       self.koniec_koncow=1
       self.level=0 
       self.SaveData() 
       if self.automatyczneprzelaczanie==1:
          self.ui2.landing_button.click()
          self.ui2.Save_2.setStyleSheet("background-color:none")    
    def evt_progress_7(self,val):
       self.ui2.progressBar.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 1...")
       elif val==100:
          self.landingbacklevel=1
    def evt_finished_7(self):
       self.ui2.VR_poziom2.setEnabled(True)
       self.ui2.dzialanie.setText("Przejdz do poziomu 2")
       self.level=0
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       if self.automatyczneprzelaczanie==1:
          self.ui2.VR_poziom2.click()
    def evt_progress_8(self,val):
       self.ui2.progressBar_2.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 2...")
       elif val==100:
          self.landingbacklevel=1
    def evt_finished_8(self):
       self.ui2.VR_poziom3.setEnabled(True)
       self.ui2.dzialanie.setText("Przejdz do poziomu 3") 
       self.level=0
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       if self.automatyczneprzelaczanie==1:
          self.ui2.VR_poziom3.click()
    def evt_progress_9(self,val):
       self.ui2.progressBar_3.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 3...")
       elif val==100:
          self.landingbacklevel=1
    def evt_finished_9(self):
       self.ui2.VR_poziom4.setEnabled(True)
       self.ui2.dzialanie.setText("Przejdz do poziomu 4")    
       self.level=0
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       if self.automatyczneprzelaczanie==1:
          self.ui2.VR_poziom4.click()
    def evt_progress_10(self,val):
       self.ui2.progressBar_4.setValue(val)
       if val<100: 
          self.ui2.dzialanie.setText("Trwa poziom 4...")
       elif val==100:
          self.landingbacklevel=1
          self.koniec=1
    def evt_finished_10(self):
       self.ui2.VR_poziom5.setEnabled(True)
       self.ui2.dzialanie.setText("Przejdz do poziomu 5")
       self.level=0   
       self.ui2.Save.setEnabled(True)
       self.koniec=1
       if self.automatyczneprzelaczanie==1:
          self.ui2.VR_poziom5.click()
    
    def VR_poziom1(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_7()
       self.worker.start()
       self.level=1
       self.worker.update_progress.connect(self.evt_progress_7)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_7)
       self.worker.quit()
    def VR_poziom2(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_8()
       self.worker.start()
       self.level=2

       self.worker.update_progress.connect(self.evt_progress_8)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_8)
       self.worker.quit()
    def VR_poziom3(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_9()
       self.worker.start()
       self.level=3

       self.worker.update_progress.connect(self.evt_progress_9)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_9)
       self.worker.quit()
    def VR_poziom4(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_10()
       self.worker.start()
       self.level=4

       self.worker.update_progress.connect(self.evt_progress_10)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_10)
       self.worker.quit()
    def VR_poziom5(self):
       VR_Levels.VR_repeat=0
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread()
       self.worker.start()
       self.level=5
       
       self.worker.update_progress.connect(self.evt_progress)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished)
       self.worker.quit()   
    def VR_poziom6(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_2()
       self.worker.start()
       self.level=6
       self.worker.update_progress.connect(self.evt_progress_2)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_2)
       self.worker.quit()
    def VR_poziom7(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_3()
       self.worker.start()
       self.level=7

       self.worker.update_progress.connect(self.evt_progress_3)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_3)
       self.worker.quit()
    def VR_poziom8(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_4()
       self.worker.start()
       self.level=8

       self.worker.update_progress.connect(self.evt_progress_4)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_4)
       self.worker.quit()
    def VR_poziom9(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_5()
       self.worker.start()
       self.level=9

       self.worker.update_progress.connect(self.evt_progress_5)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_5)
       self.worker.quit()
    def VR_poziom10(self):
       client=airsim.MultirotorClient()
       client.confirmConnection()
       self.worker=WorkerThread_6()
       self.worker.start()
       self.level=10

       self.worker.update_progress.connect(self.evt_progress_6)
       self.schowaj_przyciski()
       self.worker.finished.connect(self.evt_finished_6)
       self.worker.quit()
    def SaveData(self):
      if len(self.tetno1)!=0:
         print(len(self.tetno1))
         print(len(self.time_samples1))
         self.czas_ekst_1=self.znajdz_czas_miedzy_ekstremami(self.tetno1,self.time_samples1)
      else: 
         self.tetno1=[0, 0]
      if len(self.tetno2)!=0:
       self.czas_ekst_2=self.znajdz_czas_miedzy_ekstremami(self.tetno2,self.time_samples2)
      else: 
         self.tetno2=[0, 0]
      if len(self.tetno3)!=0:
       self.czas_ekst_3=self.znajdz_czas_miedzy_ekstremami(self.tetno3,self.time_samples3)
      else: 
         self.tetno3=[0, 0]
      if len(self.tetno4)!=0:
       self.czas_ekst_4=self.znajdz_czas_miedzy_ekstremami(self.tetno4,self.time_samples4)
      else: 
         self.tetno4=[0,0]
      if len(self.tetno5)!=0:
       self.czas_ekst_5=self.znajdz_czas_miedzy_ekstremami(self.tetno5,self.time_samples5)
      else: 
         self.tetno5=[0,0]
      if len(self.tetno6)!=0:
       self.czas_ekst_6=self.znajdz_czas_miedzy_ekstremami(self.tetno6,self.time_samples6)
      else: 
         self.tetno6=[0,0]
      if len(self.tetno7)!=0:
       self.czas_ekst_7=self.znajdz_czas_miedzy_ekstremami(self.tetno7,self.time_samples7)
      else: 
         self.tetno7=[0,0]
      if len(self.tetno8)!=0:
       self.czas_ekst_8=self.znajdz_czas_miedzy_ekstremami(self.tetno8,self.time_samples8)
      else: 
         self.tetno8=[0,0]
      if len(self.tetno9)!=0:
       self.czas_ekst_9=self.znajdz_czas_miedzy_ekstremami(self.tetno9,self.time_samples9)
      else: 
         self.tetno9=[0,0]
      if len(self.tetno10)!=0:
       self.czas_ekst_10=self.znajdz_czas_miedzy_ekstremami(self.tetno10,self.time_samples10)
      else: 
         self.tetno10=[0,0]

      self.data_t1=sum(self.tetno1)/len(self.tetno1) 
      self.data_t2=sum(self.tetno2)/len(self.tetno2) 
      self.data_t3=sum(self.tetno3)/len(self.tetno3) 
      self.data_t4=sum(self.tetno4)/len(self.tetno4) 
      self.data_t5=sum(self.tetno5)/len(self.tetno5) 
      self.data_t6=sum(self.tetno6)/len(self.tetno6) 
      self.data_t7=sum(self.tetno7)/len(self.tetno7) 
      self.data_t8=sum(self.tetno8)/len(self.tetno8) 
      self.data_t9=sum(self.tetno9)/len(self.tetno9)
      self.data_t10=sum(self.tetno10)/len(self.tetno10)
      self.data.loc[len(self.data.index)]=[self.data_t1,
                                          self.time1,
                                          statistics.variance(self.tetno1),
                                          self.czas_ekst_1,
                                          self.data_t2,
                                          self.time2,
                                          statistics.variance(self.tetno2),
                                          self.czas_ekst_2,
                                          self.data_t3,
                                          self.time3,
                                          statistics.variance(self.tetno3),
                                          self.czas_ekst_3,
                                          self.data_t4,
                                          self.time4,
                                          statistics.variance(self.tetno4),
                                          self.czas_ekst_4,
                                          self.data_t5,
                                          self.time5,
                                          statistics.variance(self.tetno5),
                                          self.czas_ekst_5,
                                          self.data_t6,
                                          self.time6,
                                          statistics.variance(self.tetno6),
                                          self.czas_ekst_6,
                                          self.data_t7,
                                          self.time7,
                                          statistics.variance(self.tetno7),
                                          self.czas_ekst_7,
                                          self.data_t8,
                                          self.time8,
                                          statistics.variance(self.tetno8),
                                          self.czas_ekst_8,
                                          self.data_t9,
                                          self.time9,
                                          statistics.variance(self.tetno9),
                                          self.czas_ekst_9,
                                          self.data_t10,
                                          self.time10,
                                          statistics.variance(self.tetno10),
                                          self.czas_ekst_10,
      ]
      self.data.to_csv(self.path+r"\Tabela1_vr.csv",index=False)
    def timer1_event(self):
       self.time1=self.time1+1
     

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window2 = VR_Levels()
    sys.exit(app.exec_())