from PySide2 import *
import cv2 
from ui_weryfikacja import *
import sys
from keras.preprocessing import image
import numpy as np
import os
class Weryfikacja(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.nr_kamerki=0
        self.img_size=128
        self.clf =cv2.CascadeClassifier(r"C:\Users\Admin\AppData\Local\Programs\Python\Python310\lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")
        self.nr_folderu=0
        self.warunki=0
        self.nr_zdjecia_ds=0
        self.nr_zdjecia_ss=0
        self.nr_zdjecia_sk=0
        self.ui.pushButton_11.clicked.connect(lambda:self.kamerka())
        self.ui.pushButton_3.clicked.connect(lambda:self.slaba_kamerka())
        self.ui.pushButton_12.clicked.connect(lambda:self.dobra_kamerka())
        self.ui.pushButton_13.clicked.connect(lambda:self.slaba_kamerka_1())
        self.ui.pushButton.clicked.connect(lambda:self.dobre_swiatlo())
        self.ui.pushButton_2.clicked.connect(lambda:self.slabe_swiatlo())
        self.ui.pushButton_4.clicked.connect(lambda:self.angry())
        self.ui.pushButton_5.clicked.connect(lambda:self.disgust())
        self.ui.pushButton_6.clicked.connect(lambda:self.fear())
        self.ui.pushButton_7.clicked.connect(lambda:self.happy())
        self.ui.pushButton_8.clicked.connect(lambda:self.sad())
        self.ui.pushButton_9.clicked.connect(lambda:self.surprise())
        self.ui.pushButton_10.clicked.connect(lambda:self.neutral())
        self.ui.label_8.setText(str(self.nr_kamerki))


        dir_path = r"C:\Do Linuxa\Magisterka\{}".format(self.nr_folderu)
        for path in os.listdir(dir_path):
                                        if os.path.isfile(os.path.join(dir_path, path)):
                                            self.nr_zdjecia_ds += 1

        dir_path = r"C:\Do Linuxa\Magisterka\slabe_swiatlo\{}".format(self.nr_folderu)
        for path in os.listdir(dir_path):
                                        if os.path.isfile(os.path.join(dir_path, path)):
                                            self.nr_zdjecia_ss += 1
        dir_path = r"C:\Do Linuxa\Magisterka\{}".format(self.nr_folderu)
        for path in os.listdir(dir_path):
                                        if os.path.isfile(os.path.join(dir_path, path)):
                                            self.nr_zdjecia_sk += 1
        self.timer_update=QTimer()   
        self.timer_update.start(1000) 
        self.timer_update.timeout.connect(lambda:self.update())                                        
        self.show()



    def update(self):
       match self.warunki:
               case 0:
                x=0
                dir_path = r"C:\Do Linuxa\Magisterka\slabe_swiatlo\{}".format(self.nr_folderu)
                for path in os.listdir(dir_path):
                    if os.path.isfile(os.path.join(dir_path, path)):   
                        x+=1
                self.ui.label_6.setText(str(x))
               case 1:
                x=0
                dir_path = r"C:\Do Linuxa\Magisterka\{}".format(self.nr_folderu)
                for path in os.listdir(dir_path):
                    if os.path.isfile(os.path.join(dir_path, path)):   
                        x+=1
                self.ui.label_6.setText(str(x))
               case 2:
                x=0
                dir_path = r"C:\Do Linuxa\Magisterka\slaba_kamerka\{}".format(self.nr_folderu)
                for path in os.listdir(dir_path):
                    if os.path.isfile(os.path.join(dir_path, path)):   
                        x+=1
                self.ui.label_6.setText(str(x))
    def angry(self):
         self.nr_folderu=0
         self.ui.label_4.setText("angry")
    def disgust(self):
         self.nr_folderu=1
         self.ui.label_4.setText("disgust")
    def fear(self):
         self.nr_folderu=2
         self.ui.label_4.setText("fear")
    def happy(self):
         self.nr_folderu=3
         self.ui.label_4.setText("happy")
    def sad(self):
         self.nr_folderu=4
         self.ui.label_4.setText("sad")
    def surprise(self):
         self.nr_folderu=5
         self.ui.label_4.setText("surprise")
    def neutral(self):
         self.nr_folderu=6
         self.ui.label_4.setText("neutral")

    def dobre_swiatlo(self):
         self.warunki=1
         self.ui.label_6.setText(str(self.nr_zdjecia_ds))
         self.ui.label_2.setText("Dobre światło")
    def slabe_swiatlo(self):
        self.warunki=0
        self.ui.label_6.setText(str(self.nr_zdjecia_ss))
        self.ui.label_2.setText("Słabe światło")
    def dobra_kamerka(self):
         self.nr_kamerki=1
         self.ui.label_8.setText(str(self.nr_kamerki))
         self.ui.label_8.setText(str(self.nr_kamerki))
    def slaba_kamerka_1(self):
         self.nr_kamerki=0   
    def slaba_kamerka(self):
        
        self.ui.label_2.setText("Slaba kamerka")
        self.warunki=2
        
        self.ui.label_6.setText(str(self.nr_zdjecia_sk))
        
    def kamerka(self):
        cam=cv2.VideoCapture(self.nr_kamerki)
        while True:
            ret, frame = cam.read()
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
                    cv2.imshow("test",frame)
                    k=cv2.waitKey(1)
                    if k%256==27: #Esc#
                                print("Close the app")
                                cam.release()
                                break
                    elif k%256==32: #spacja#
                           match self.warunki:
                                case 0: #slabe swiatlo
                                     
                                     self.ui.label_2.setText("Słabe światło")
                                     nazwa_pliku=r"C:\Do Linuxa\Magisterka\slabe_swiatlo\{}\zdjecie_nr_{}.png".format(self.nr_folderu,self.nr_zdjecia_ss)
                                     cv2.imwrite(nazwa_pliku,roi_gray)
                                     self.nr_zdjecia_ss+=1
                                     self.ui.label_6.setText(str(self.nr_zdjecia_ss))
                                case 1: #dobre swiatlo
                                     
                                     self.ui.label_2.setText("Dobre światło")
                                     nazwa_pliku=r"C:\Do Linuxa\Magisterka\{}\zdjecie_nr_{}.png".format(self.nr_folderu,self.nr_zdjecia_ds)
                                     cv2.imwrite(nazwa_pliku,roi_gray)  
                                     self.nr_zdjecia_ds+=1
                                     self.ui.label_6.setText(str(self.nr_zdjecia_ds))
                                case 2: #slaba kamerka
                                     
                                     self.ui.label_2.setText("Slaba kamerka")
                                     nazwa_pliku=r"C:\Do Linuxa\Magisterka\slaba_kamerka\{}\zdjecie_nr_{}.png".format(self.nr_folderu,self.nr_zdjecia_sk)
                                     cv2.imwrite(nazwa_pliku,roi_gray)  
                                     self.nr_zdjecia_sk+=1
                                     self.ui.label_6.setText(str(self.nr_zdjecia_sk))
                           


if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Weryfikacja()
    sys.exit(app.exec_())