from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import QPixmap
import numpy as np
import cv2
import time
from threading import Thread
from oyun_buttonlu_v2 import oyun
from log_tutucu import log_tut

class oyun_gui(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        
        log_tut().log_temizle()
        self.oyun = oyun()

        #ekran
        self.ekran = QLabel(self)  
        self.pixmap1 = QPixmap("tahta.png")
        self.ekran.setPixmap(self.pixmap1)
        self.ekran.resize(self.pixmap1.width(),self.pixmap1.height())
       
        
      
        #buttonlar
        btnAsagi = QPushButton("Aşağı")
        btnAsagi.setMinimumHeight(40)
        btnAsagi.setStyleSheet("font-weight: bold; font-size: 16pt")
        btnAsagi.clicked.connect(self.asagi_btn_action)
                                 
        btnYukari = QPushButton("Yukarı")
        btnYukari.setMinimumHeight(40)     
        btnYukari.setStyleSheet("font-weight: bold; font-size: 16pt")
        btnYukari.clicked.connect(self.yukari_btn_action)
        
        btnSol = QPushButton("Sol")
        btnSol.setMinimumHeight(40)
        btnSol.setStyleSheet("font-weight: bold; font-size: 16pt")
        btnSol.clicked.connect(self.sol_btn_action)        
        
        btnSag = QPushButton("Sağ")
        btnSag.setMinimumHeight(40)
        btnSag.setStyleSheet("font-weight: bold; font-size: 16pt") 
        btnSag.clicked.connect(self.sag_btn_action)
        
        btnSec = QPushButton("Seç")
        btnSec.setMinimumHeight(40)
        btnSec.setStyleSheet("font-weight: bold; font-size: 16pt") 
        btnSec.clicked.connect(self.sec_btn_action)

        #btnDoruk = QPushButton("Doruk")
        #btnDoruk.setMinimumHeight(40)
        #btnDoruk.setStyleSheet("font-weight: bold; font-size: 16pt")         
        #btnDoruk.clicked.connect(self.doruk_btn_action)



        #radioboxlar ve terminal labeller
        self.lbl_oyuncu1 = QLabel("OYUNCU1")
        self.lbl_bloklar1 = QLabel("bloklar")
        self.lbl_duvarlar1 = QLabel("duvarlar")
        
        self.lbl_oyuncu2 = QLabel("OYUNCU2")
        self.lbl_bloklar2 = QLabel("bloklar")
        self.lbl_duvarlar2 = QLabel("duvarlar")
        
        self.lbl_oyuncu3 = QLabel("OYUNCU3")
        self.lbl_bloklar3 = QLabel("bloklar")
        self.lbl_duvarlar3 = QLabel("duvarlar")
        
        self.lbl_oyuncu4 = QLabel("OYUNCU4")
        self.lbl_bloklar4 = QLabel("bloklar")
        self.lbl_duvarlar4 = QLabel("duvarlar")
        
        self.textbox_terminal = QLineEdit("terminal-text---")
        self.textbox_terminal.resize(200, 200)
        self.textbox_terminal.setReadOnly(True)
        self.textbox_terminal.setStyleSheet("font-weight: italic; font-size: 16pt") 
        
        
        self.radiobox_blokekle = QRadioButton("Blok ekle")
        self.radiobox_duvarekle  = QRadioButton("Duvar ekle")
        self.radiobox_sicrama = QRadioButton("Sicrama Yap") 
        self.radiobox_sil = QRadioButton("Rakipten Sil")
        self.radiobox_doruk = QRadioButton("Doruk Aktif Et")
    
        self.radiobox_blokekle.toggled.connect(self.onClickedBlokEkle)
        self.radiobox_duvarekle.toggled.connect(self.onClickedDuvarEkle)
        self.radiobox_sicrama.toggled.connect(self.onClickedSicramaEkle)
        self.radiobox_sil.toggled.connect(self.onClickedRakiptenSil)
        

        
        tuslar_layout = QGridLayout()
        tuslar_layout.addWidget(btnYukari,0,1)
        tuslar_layout.addWidget(btnAsagi,2,1)
        tuslar_layout.addWidget(btnSol,1,0)
        tuslar_layout.addWidget(btnSag,1,2)
        tuslar_layout.addWidget(btnSec,4,1)
        #tuslar_layout.addWidget(btnDoruk,5,1)
        

        
        info_layout = QGridLayout()
        info_layout.addWidget(self.lbl_oyuncu1,0,1)
        info_layout.addWidget(self.lbl_bloklar1,0,2)
        info_layout.addWidget(self.lbl_duvarlar1,0,3)
        
        info_layout.addWidget(self.lbl_oyuncu2,1,1)
        info_layout.addWidget(self.lbl_bloklar2,1,2)
        info_layout.addWidget(self.lbl_duvarlar2,1,3)
        
        info_layout.addWidget(self.lbl_oyuncu3,2,1)
        info_layout.addWidget(self.lbl_bloklar3,2,2)
        info_layout.addWidget(self.lbl_duvarlar3,2,3)
        
        info_layout.addWidget(self.lbl_oyuncu4,3,1)
        info_layout.addWidget(self.lbl_bloklar4,3,2)
        info_layout.addWidget(self.lbl_duvarlar4,3,3)

        
        info_layout.setAlignment(Qt.AlignCenter)
        
        self.radiobox_layout = QGridLayout()
        self.radiobox_layout.addWidget(self.radiobox_blokekle,0,0)
        self.radiobox_layout.addWidget(self.radiobox_duvarekle,0,1)
        self.radiobox_layout.addWidget(self.radiobox_sicrama,1,0)
        self.radiobox_layout.addWidget(self.radiobox_sil,1,1)
        self.radiobox_layout.addWidget(self.radiobox_doruk, 2,1)
        self.radiobox_layout.setAlignment(Qt.AlignCenter)
        
        vertical_layout = QVBoxLayout()
        vertical_layout.addLayout(info_layout)
        vertical_layout.addWidget(self.textbox_terminal)
        vertical_layout.addLayout(self.radiobox_layout)
        vertical_layout.addLayout(tuslar_layout)
        #vertical_layout.setAlignment(Qt.AlignBaseline)
        
        horizontal_layout_wide = QHBoxLayout()
        horizontal_layout_wide.addWidget(self.ekran)
        horizontal_layout_wide.addLayout(vertical_layout)
        
        self.setLayout(horizontal_layout_wide)
        self.setWindowTitle("Oyun Gui")
        self.resize(1200,700)
        
        self.secili_x = 0
        self.secili_y = 0
        
        self.dizi_elenen_oyuncular = [0,0,0,0]
        
        self.sayac_blokekle = 0
        self.sayac_duvarekle = 0
        self.sayac_sicramaekle = 0
        self.sayac_sil = 0
        self.sayac_doruk = 0


    def doruk_btn_action(self):
        if self.sayac_doruk == 0:
            if (len(self.oyun.oyuncu1.bloklar) +len(self.oyun.oyuncu1.duvarlar)) >= 12:
                if len(self.oyun.oyuncu1.duvarlar) < 12:
                
                    self.oyun.oyuncu_doruk_aktif(self.oyun.oyuncu1)
                    self.sayac_doruk = 1
            
                    self.ekran_yenile()
                else:
                    print("12 DEN FAZLA DUVARIN VARKEN DORUK AKTİF EDİLEMEZ")
            else:
                print("YETERİ KADAR BLOĞUN YOK")
        else:
             print("DORUK ZATEN KULLANILDI")
        
    def asagi_btn_action(self):
        self.secili_y +=1
        self.gorsel_ciz(self.secili_x,self.secili_y)
        self.ekran_degistir()

    def yukari_btn_action(self):
        self.secili_y -=1
        self.gorsel_ciz(self.secili_x,self.secili_y)
        self.ekran_degistir()
        
    def sol_btn_action(self):
        self.secili_x -=1
        self.gorsel_ciz(self.secili_x,self.secili_y)
        self.ekran_degistir()
        
    def sag_btn_action(self):
        self.secili_x +=1
        self.gorsel_ciz(self.secili_x,self.secili_y)
        self.ekran_degistir()

    def sec_btn_action(self):
        self.lbl_bloklar1.setText(f"BLOKLAR : {len(self.oyun.oyuncu1.bloklar)}")
        self.lbl_duvarlar1.setText(f"DUVARLAR : {len(self.oyun.oyuncu1.duvarlar)}")

            
        if self.radiobox_blokekle.isChecked():
            if self.sayac_blokekle < 5:
                
                print("blok ekleme hakkı var!")
                success,maliyet = self.oyun.ekle_blok(self.secili_y,self.secili_x, self.oyun.oyuncu1)

                if success == True:
                    self.ekran_yenile()
                    self.sayac_blokekle += maliyet
                    self.sayac_duvarekle = 4
            else:
                print("blok ekleme hakkı bitti!")
                
                
        elif self.radiobox_duvarekle.isChecked():
            if self.sayac_duvarekle < 4:
                
                print("duvar ekleme hakkı var!")
                success ,maliyet = self.oyun.ekle_duvar(self.secili_y, self.secili_x, self.oyun.oyuncu1)

                if success == True:
                    self.ekran_yenile()
                    self.sayac_duvarekle +=maliyet
                    self.sayac_blokekle = 5
            
            else:
                print("Duvar ekleme hakkı bitti!")
          
        elif  self.radiobox_sicrama.isChecked():
            if self.sayac_sicramaekle < 1:
                print("Sicrama Ekleme hakkı var!")
                
                success,maliyet = self.oyun.ekle_sicrama(self.secili_y, self.secili_x,self.oyun.oyuncu1)

                if success == True:
                    self.ekran_yenile()
                    self.sayac_sicramaekle +=maliyet
                    self.sayac_sil = 2
            else:
                print("Sicrama ekleme hakkı bitti!")
        
        elif self.radiobox_sil.isChecked():
            if self.sayac_sil  < 2:
                print("Silme hakkı var!")
                success ,maliyet= self.oyun.sil_blok_rakip(self.secili_y, self.secili_x, self.oyun.oyuncu1)

                if success == True:
                    self.ekran_yenile()
                    self.sayac_sil +=maliyet
                    self.sayac_sicramaekle = 1
            else:
                print("Silme hakkı bitti!")
                
        elif self.radiobox_doruk.isChecked():

                
            if self.sayac_doruk == 0:
                if (len(self.oyun.oyuncu1.bloklar) +len(self.oyun.oyuncu1.duvarlar)) >= 12:
                    if len(self.oyun.oyuncu1.duvarlar) < 12:
                    
                        self.oyun.oyuncu_doruk_aktif(self.oyun.oyuncu1,self.secili_x,self.secili_y)
                        self.sayac_doruk = 1
                
                        self.ekran_yenile()
                    else:
                        print("12 DEN FAZLA DUVARIN VARKEN DORUK AKTİF EDİLEMEZ")
                else:
                    print("YETERİ KADAR BLOĞUN YOK")
            else:
                 print("DORUK ZATEN KULLANILDI")
            if self.sayac_doruk == 1:
                self.sayac_blokekle = 5
                self.sayac_duvarekle = 4
                self.sayac_sicramaekle = 1
                self.sayac_sil = 2
                self.sayac_doruk +=1
                self.radiobox_doruk.setCheckable(False)
        print(self.sayac_blokekle," ",self.sayac_duvarekle," ",self.sayac_sicramaekle," ",self.sayac_sil," ")           
        
        
        if self.sayac_blokekle > 4 and self.sayac_duvarekle > 3 and self.sayac_sicramaekle > 0 and self.sayac_sil > 1:
            time.sleep(1)
            self.hamleler_devam_thread()
            self.sayac_blokekle = 0 
            self.sayac_duvarekle = 0
            self.sayac_sicramaekle = 0
            self.sayac_sil = 0
            
        
        
            
        
    def onClickedBlokEkle(self):
        print("BLOK EKLE BUTONUNA BASILDI")
                
    def onClickedDuvarEkle(self):
        print("DUVAR EKLE BUTONUNA BASILDI")

    def onClickedSicramaEkle(self):
        print("SİCRAMA EKLE BUTONUN BASILDI")
        
    def onClickedRakiptenSil(self):
        print("SİL BUTONUNA BASILDI")

    
    def ekran_degistir(self):
        self.pixmap2 = QPixmap("tahta_cizildi.png")
        self.ekran.setPixmap(self.pixmap2)
        self.ekran.resize(self.pixmap2.width(),self.pixmap2.height())
        
    def gorsel_ciz(self,x,y):
        im = cv2.imread("tahta.png")
        #yatay

        im[50*y:50*y + 4,:] = [50,50,50]
        im[50*y+50:50*y + 50 + 4,:] = [50,50,50]        
        #dikey
   
        im[:,50 *x:50 * x + 4] = [50,50,50]
        im[:,50 *x + 50:50 * x + 50 + 4] = [50,50,50]        
        cv2.imwrite("tahta_cizildi.png",im)
     
    def ekran_yenile(self):
        self.pixmap2 = QPixmap("tahta.png")
        self.ekran.setPixmap(self.pixmap2)
        self.ekran.resize(self.pixmap2.width(),self.pixmap2.height())
        
    def hamleler_devam_thread(self):
        t1 = Thread(target=self.hamleler_devam)
        t1.start()
    
    def hamleler_devam(self):
        if len(self.oyun.oyuncu2.duvarlar) != 0:
            self.oyun.oyuncu_karar_ver_oto(self.oyun.oyuncu2)
            self.ekran_yenile()
            self.lbl_bloklar2.setText(f"bloklar :{len(self.oyun.oyuncu2.bloklar) }")
            self.lbl_duvarlar2.setText(f"duvarlar : {len(self.oyun.oyuncu2.duvarlar)}")
            
            self.textbox_terminal.setText(log_tut().log_oku())
            time.sleep(2)
            
        else:
            print("OYUNCU 1 YENİLDİ")
            self.dizi_elenen_oyuncular[1] = 1
        
        if len(self.oyun.oyuncu3.duvarlar) != 0:
            self.oyun.oyuncu_karar_ver_oto(self.oyun.oyuncu3)
            self.ekran_yenile()
            self.lbl_bloklar3.setText(f"bloklar :{len(self.oyun.oyuncu3.bloklar) }")
            self.lbl_duvarlar3.setText(f"duvarlar : {len(self.oyun.oyuncu3.duvarlar)}")
            self.textbox_terminal.setText(log_tut().log_oku())
            time.sleep(2)
        else:
            print("OYUNCU 2 YENİLDİ")
            self.dizi_elenen_oyuncular[2] = 1
            
        if len(self.oyun.oyuncu4.duvarlar) != 0:
            self.oyun.oyuncu_karar_ver_oto(self.oyun.oyuncu4)
            self.ekran_yenile()
            self.lbl_bloklar4.setText(f"bloklar :{len(self.oyun.oyuncu4.bloklar) }")
            self.lbl_duvarlar4.setText(f"duvarlar : {len(self.oyun.oyuncu4.duvarlar)}")
            self.textbox_terminal.setText(log_tut().log_oku())
            time.sleep(2)
        else:
            print("OYUNCU 3 YENİLDİ")
            self.dizi_elenen_oyuncular[3] = 1
        
        if len(self.oyun.oyuncu1.duvarlar)==0:
            print("\n \n \n \nOYUNU KAYBETTİNİZ")
            self.close()
            
        if self.dizi_elenen_oyuncular[1] ==1 and self.dizi_elenen_oyuncular[2] ==1 and self.dizi_elenen_oyuncular[3] ==1:
            print("\n \n \n \n TEBRİKLER OYUNU KAZANDINIZ!")
            self.textbox_terminal.setText("TEBRİKLER! OYUNU KAZANDINIZ !")
            
            time.sleep(10)
            self.close()
        
        self.lbl_bloklar1.setText(f"bloklar :{len(self.oyun.oyuncu1.bloklar) }")
        self.lbl_duvarlar1.setText(f"duvarlar : {len(self.oyun.oyuncu1.duvarlar)}")
            
       

        
        
app = QApplication([])
widget = oyun_gui()
widget.show()
app.exec_()
        