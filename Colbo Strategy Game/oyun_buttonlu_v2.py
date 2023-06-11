import numpy as np
import time
from tahta_gorsellestirme import TahtaGorsellestirme
from log_tutucu import log_tut

class oyun():
    class oyuncu():
        def __init__(self):
            self.doruk=0
            self.bloklar = []
            self.duvarlar = []
    
    def __init__(self):
        self.tanimla_tahta()
        self.tanimla_oyuncular()
        
        
        
        """  #TEST BLOKLARI
        for x in range(5):
            for y in range(5):
                self.ekle_blok_direkt([x+1,y+1], self.oyuncu1)
                self.tahta[x+1,y+1] = self.oyuncu1.__name__

        """
        
        #ekran
        
        TahtaGorsellestirme(self.tahta)

        
    def tanimla_tahta(self):
        self.tahta = np.zeros(shape=(12,12),dtype='int32')
        self.tahta_name = 0
        
    def tanimla_oyuncular(self):
        self.oyuncu1 = self.oyuncu()
        self.oyuncu2 = self.oyuncu()
        self.oyuncu3 = self.oyuncu()
        self.oyuncu4 = self.oyuncu()
        self.oyuncu1.__name__ = 1
        self.oyuncu2.__name__ = 3
        self.oyuncu3.__name__ = 5
        self.oyuncu4.__name__ = 7 
        self.root_locations_oyuncu1 = [[1,1],[2,2],[1,2],[2,1]]
        self.root_locations_oyuncu2 = [[1,10],[2,9],[2,10],[1,9]]
        self.root_locations_oyuncu3 = [[10,1],[9,2],[10,2],[9,1]]
        self.root_locations_oyuncu4 = [[10,10],[9,9],[10,9],[9,10]]
        self.doruk_locations_oyuncu1 = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[2,0],[3,0],[4,0],[5,0]]
        self.doruk_locations_oyuncu2 = [[0,11],[0,10],[0,9],[0,8],[0,7],[0,6],[1,11],[2,11],[3,11],[4,11],[5,11]]
        self.doruk_locations_oyuncu3 = [[11,0],[10,0],[9,0],[8,0],[7,0],[6,0],[11,1],[11,2],[11,3],[11,4],[11,5]]
        self.doruk_locations_oyuncu4 = [[11,11],[11,10],[11,9],[11,8],[11,7],[11,6],[10,11],[9,11],[8,11],[7,11],[6,11]]
        self.yasaklar = np.concatenate((self.doruk_locations_oyuncu1,self.doruk_locations_oyuncu2,self.doruk_locations_oyuncu3,self.doruk_locations_oyuncu4)).tolist()
        
        def ekle_tahta_root_lokasyonlari(root_lokasyonlari,oyuncu):
            for lok in root_lokasyonlari:
                self.ekle_duvar_direkt(lok, oyuncu)
                [t1,t2] = lok
                self.tahta[t1,t2] = oyuncu.__name__ + 1
        
        ekle_tahta_root_lokasyonlari(self.root_locations_oyuncu1, self.oyuncu1)
        ekle_tahta_root_lokasyonlari(self.root_locations_oyuncu2, self.oyuncu2)                    
        ekle_tahta_root_lokasyonlari(self.root_locations_oyuncu3, self.oyuncu3)
        ekle_tahta_root_lokasyonlari(self.root_locations_oyuncu4, self.oyuncu4)
        
        def ekle_tahta_doruk_lokasyonlari(doruk_lokasyonlari,sayi=9):
            for [t1,t2] in doruk_lokasyonlari:
                self.tahta[t1,t2] = sayi
        
        ekle_tahta_doruk_lokasyonlari(self.doruk_locations_oyuncu1)
        ekle_tahta_doruk_lokasyonlari(self.doruk_locations_oyuncu2)
        ekle_tahta_doruk_lokasyonlari(self.doruk_locations_oyuncu3)
        ekle_tahta_doruk_lokasyonlari(self.doruk_locations_oyuncu4)
        
        
        
       
            
    def ekle_blok_direkt(self,blok,oyuncu):
        oyuncu.bloklar.append(blok)
        
    def ekle_duvar_direkt(self,duvar,oyuncu):
        oyuncu.duvarlar.append(duvar)
        
    #%% HAMLELER BUTONLU
    def blok_cevre_kontrol(self,a,b,oyuncu):        #blok çevresinde oyuncuya ait duvar ya da blok var mı?
        if [a,b+1] in oyuncu.bloklar or [a,b+1] in oyuncu.duvarlar:
            return True
        elif [a,b-1] in oyuncu.bloklar or [a,b-1] in oyuncu.duvarlar:
            return True        
        elif [a+1,b] in oyuncu.bloklar or [a+1,b] in oyuncu.duvarlar:
            return True
        elif [a-1,b] in oyuncu.bloklar or [a-1,b] in oyuncu.duvarlar:
            return True
        else:
            print("HEDEF LOKASYONUN ÇEVRESİNDE OYUNCUYA AİT BLOK BULUNMUYOR")
            return False
        
    def ekle_blok(self,a,b,oyuncu):
        
        if [a,b] in self.yasaklar:              #HEDEF YASAK BLOK MU?
            print("HEDEFTE YASAK BLOK VAR")
            return (False , 0)
        
        elif [a,b] in oyuncu.bloklar or [a,b] in oyuncu.duvarlar: #HEDEF ZATEN OYUNCUYA AİT Mİ?
            print("HEDEFTE ZATEN BLOK YA DA DUVARIN BULUNUYOR")
            return (False , 0)
        
        elif self.tahta[a,b] == 0:                      #HEDEF BOŞ MU?
            isitable = self.blok_cevre_kontrol(a, b, oyuncu)
            if isitable == True:
                self.ekle_blok_direkt([a,b], oyuncu) #blok ekle
                self.tahta[a,b] = oyuncu.__name__    #tahtaya işle
                print("HEDEF BOŞ -> BLOKLA DOLDURULDU")
                log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu blok {a},{b} ye blok ekledi")
                TahtaGorsellestirme(self.tahta)
                return (True,1)
            else:
                return (False,0)
        
        elif self.tahta[a,b] in [1,3,5,7]:              #HEDEF BAŞKA OYUNCUYA AİT BLOK MU?
            isitable = self.blok_cevre_kontrol(a, b, oyuncu)
            if isitable == True:
                if self.tahta[a,b] == 1:
                    self.oyuncu1.bloklar.remove([a,b])
                    print("HEDEF BLOK 1.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 3:
                    self.oyuncu2.bloklar.remove([a,b])
                    print("HEDEF BLOK 2.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 5:
                    self.oyuncu3.bloklar.remove([a,b])
                    print("HEDEF BLOK 3.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 7:
                    self.oyuncu4.bloklar.remove([a,b])
                    print("HEDEF BLOK 4.OYUNCUDAN SİLİNDİ")
                
                self.ekle_blok_direkt([a,b], oyuncu) #blok ekle
                self.tahta[a,b] = oyuncu.__name__    #tahtaya işle
                TahtaGorsellestirme(self.tahta)
                log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu  {a},{b} ye blok ekledi")
                return (True,1)
                
            elif isitable == False:
                return (False,0)
        
        elif self.tahta[a,b] in [2,4,6,8]:              #HEDEF BAŞKA OYUNCUYA AİT DUVAR MI?
            isitable = self.blok_cevre_kontrol(a, b, oyuncu)
            if isitable == True:
                if self.tahta[a,b] == 2:
                    self.oyuncu1.duvarlar.remove([a,b])
                    print("HEDEF BLOKTAKİ DUVAR 1.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 4:
                    self.oyuncu2.duvarlar.remove([a,b])
                    print("HEDEF BLOKTAKİ DUVAR 2.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 6:
                    self.oyuncu3.duvarlar.remove([a,b])
                    print("HEDEF BLOKTAKİ DUVAR 3.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 8:
                    self.oyuncu4.duvarlar.remove([a,b])
                    print("HEDEF BLOKTAKİ DUVAR 4.OYUNCUDAN SİLİNDİ")
                
                
                self.ekle_blok_direkt([a,b], oyuncu) #blok ekle
                self.tahta[a,b] = oyuncu.__name__    #tahtaya işle

                TahtaGorsellestirme(self.tahta)
                log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu {a},{b} ye blok ekledi")
                return (True,2)
                    
            elif isitable == False:
                return (False,0)
            
    def ekle_duvar(self,a,b,oyuncu):
        if [a,b] in self.yasaklar: #YASAK BLOK MU?
            print("HEDEF BLOK YASAKLI")
            return (False,0)
        
        elif [a,b] in oyuncu.bloklar or [a,b] in oyuncu.duvarlar: #OYUNCU ZATEN SAHİP Mİ?
            print("HEDEFTE ZATEN DUVAR YA DA BLOKUN BULUNUYOR")
            return (False,0)
        
        elif self.tahta[a,b] == 0: #HEDEF BOŞ MU?
            isitable = self.blok_cevre_kontrol(a, b, oyuncu)
            if isitable ==True:
                print("DUVAR EKLENİYOR")
                #oyuncuya duvar ekle
                self.ekle_duvar_direkt([a,b], oyuncu)
                self.tahta[a,b] = oyuncu.__name__ +1
                TahtaGorsellestirme(self.tahta)
                log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu {a},{b} ye duvar ekledi")
                return (True,1)
            elif isitable ==False:
                return (False,0)
        
        elif self.tahta[a,b] in [1,3,5,7]: #HEDEFTE BAŞKA BLOK MU VAR?
            isitable = self.blok_cevre_kontrol(a, b, oyuncu)
            if isitable == True:
                #hedef oyuncudan blok sil
                if self.tahta[a,b] == 1:
                    self.oyuncu1.bloklar.remove([a,b])
                    print("HEDEF BLOK 1.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 3:
                    self.oyuncu2.bloklar.remove([a,b])
                    print("HEDEF BLOK 2.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 5:
                    self.oyuncu3.bloklar.remove([a,b])
                    print("HEDEF BLOK 3.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 7:
                    self.oyuncu4.bloklar.remove([a,b])
                    print("HEDEF BLOK 4.OYUNCUDAN SİLİNDİ")
                
                #oyuncuya duvar ekle
                self.ekle_duvar_direkt([a,b], oyuncu)
                self.tahta[a,b] = oyuncu.__name__ +1
                TahtaGorsellestirme(self.tahta)
                log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu blok {a},{b} ye duvar ekledi")
                return (True,1)
            elif isitable == False:
                return (False,0)
            
        elif self.tahta[a,b] in [2,4,6,8]: #HEDEFTE BAŞKA DUVAR MI VAR?
            isitable = self.blok_cevre_kontrol(a,b,oyuncu)
            if isitable == True:
                if self.tahta[a,b] == 2:
                    self.oyuncu1.duvarlar.remove([a,b])
                    print("HEDEF BLOKTAKİ DUVAR 1.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 4:
                    self.oyuncu2.duvarlar.remove([a,b])
                    print("HEDEF BLOKTAKİ DUVAR 2.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 6:
                    self.oyuncu3.duvarlar.remove([a,b])
                    print("HEDEF BLOKTAKİ DUVAR 3.OYUNCUDAN SİLİNDİ")
                elif self.tahta[a,b] == 8:
                    self.oyuncu4.duvarlar.remove([a,b])
                    print("HEDEF BLOKTAKİ DUVAR 4.OYUNCUDAN SİLİNDİ")
                #ekle duvar
                self.ekle_duvar_direkt([a,b], oyuncu)
                self.tahta[a,b] = oyuncu.__name__ +1
                TahtaGorsellestirme(self.tahta)
                log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu blok {a},{b} ye duvar ekledi")
                return (True,2)
                
            
            elif isitable == False:
                return (False,0)
                
            
    def ekle_sicrama(self,a,b,oyuncu):
        if [a,b] in self.yasaklar:
            print("YASAKLI BLOK")
            return (False,0)
        
        elif [a,b] in oyuncu.bloklar or [a,b] in oyuncu.duvarlar:
            print("ZATEN BU BLOKTA DUVAR YA DA BLOĞUN VAR")
            return (False,0)
        
        elif self.tahta[a,b] == 0:
            print("BLOK BOŞ -> BLOK EKLE")
            self.ekle_blok_direkt([a,b], oyuncu)
            self.tahta[a,b] = oyuncu.__name__
            TahtaGorsellestirme(self.tahta)
            log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu blok {a},{b} ye sicradi")
            return (True,1)
        
        elif self.tahta[a,b] in [1,3,5,7]:
            print("HEDEFTE BAŞKA BİR OYUNCUNUN BLOĞU VAR")
            
            if self.tahta[a,b] == 1:
                self.oyuncu1.bloklar.remove([a,b])
            
            elif self.tahta[a,b] == 3:
                self.oyuncu2.bloklar.remove([a,b])
                
            elif self.tahta[a,b] == 5:
                self.oyuncu3.bloklar.remove([a,b])
            
            elif self.tahta[a,b] == 7:
                self.oyuncu4.bloklar.remove([a,b])
            
            self.ekle_blok_direkt([a,b], oyuncu)
            self.tahta[a,b] = oyuncu.__name__
            TahtaGorsellestirme(self.tahta)
            log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu blok {a},{b} ye sicradi")
            return (True,1)
        
        elif self.tahta[a,b] in [2,4,6,8]:
            print("RAKİP DUVARIN ÜSTÜNE SIÇRAMA YAPILAMAZ")
            
            return (False,1)
        
    def sil_blok_rakip(self,a,b,oyuncu):
        if [a,b] in self.yasaklar:
            print("SİLMEK İÇİN YASAKLI BLOK")
            return (False,0)
        
        elif [a,b] in oyuncu.bloklar or [a,b] in oyuncu.duvarlar:
            print("BU BLOĞA SAHİPSİN SİLİNEMEZ")
            return (False,0)
        
        elif self.tahta[a,b] == 0:
            print("BU BLOK BOŞ SİLİNEMEZ")
            return (False,0)
        
        elif self.tahta[a,b] in [1,3,5,7]:
            if self.tahta[a,b] == 1:
                self.oyuncu1.bloklar.remove([a,b])
                print("1.OYUNCUDAN BLOK SİLİNDİ")    
            elif self.tahta[a,b] == 3:
                self.oyuncu2.bloklar.remove([a,b])
                print("2.OYUNCUDAN BLOK SİLİNDİ")                
            elif self.tahta[a,b] == 5:
                self.oyuncu3.bloklar.remove([a,b])
                print("3.OYUNCUDAN BLOK SİLİNDİ")    
            elif self.tahta[a,b] == 7:
                self.oyuncu4.bloklar.remove([a,b])
                print("4.OYUNCUDAN BLOK SİLİNDİ")    
            self.tahta[a,b] = 0
            TahtaGorsellestirme(self.tahta)
            log_tut().log_ekle(f"{oyuncu.__name__} kodlu Oyuncu blok {a},{b}den blok sildi")
            return (True,1)
            
        elif self.tahta[a,b] in [2,4,6,8]:
            print("RAKİP OYUNUCUNUN DUVARI SILINEMEZ")
            return (False , 0)
    #%% HAMLELER OTO
    def ekle_blok_oto(self,oyuncu):
        while True:
            a=np.random.randint(0,12)
            b=np.random.randint(0,12)
            
            success,maliyet = self.ekle_blok(a, b, oyuncu)
            if success == True:             
                TahtaGorsellestirme(self.tahta)
                break
        return (success,maliyet)      
    
    def ekle_duvar_oto(self,oyuncu):
        while True:
            a=np.random.randint(0,12)
            b=np.random.randint(0,12)
            
            success,maliyet = self.ekle_duvar(a, b, oyuncu)
            if success == True:
                TahtaGorsellestirme(self.tahta)
                break
        return (success,maliyet)
   

    def ekle_sicrama_oto(self,oyuncu):
        while True:
            a=np.random.randint(0,12)
            b=np.random.randint(0,12)
            success , maliyet = self.ekle_sicrama(a, b, oyuncu)
            if success == True:
                TahtaGorsellestirme(self.tahta)
                break           
        return (success,maliyet)

    
    def sil_blok_rakip_oto(self,oyuncu):
        while True:
            a=np.random.randint(0,12)
            b=np.random.randint(0,12)
            success , maliyet = self.sil_blok_rakip(a, b, oyuncu)
            if success == True:
                TahtaGorsellestirme(self.tahta)
                break
        return (success,maliyet)

    #%% DORUK
    def oyuncu_doruk_aktif(self,oyuncu,a,b):
        self.hangi_bolge_doruk = None
        
        if   a <= 5 and b <= 5:
            self.hangi_bolge_doruk = self.doruk_locations_oyuncu1
            
        elif a <= 5 and b >=6:
            self.hangi_bolge_doruk = self.doruk_locations_oyuncu3 
        elif a >= 6 and b <= 5:
            self.hangi_bolge_doruk = self.doruk_locations_oyuncu2
        elif a >= 6 and b >= 6:
            self.hangi_bolge_doruk = self.doruk_locations_oyuncu4
        
        for i in self.hangi_bolge_doruk:
            if i in self.yasaklar:
                pass
            else:
                return False
        
        print(oyuncu.bloklar)

        if   oyuncu.__name__ == 1:
            self.oyuncu1.doruk = 1
            
            #oyuncu rootu azalt
            blok1 = [1,2]
            blok2 = [2,1]
            self.oyuncu1.duvarlar.remove(blok1)
            self.oyuncu1.duvarlar.remove(blok2)
            self.ekle_blok_direkt(blok1, oyuncu)  
            self.ekle_blok_direkt(blok2, oyuncu)
            self.tahta[1,2] = oyuncu.__name__
            self.tahta[2,1] = oyuncu.__name__             
            
            
            for i in self.hangi_bolge_doruk :
                self.yasaklar.remove(i)
                self.oyuncu1.bloklar.append(i)
                [a,b] = i
                self.tahta[a,b] = oyuncu.__name__
              
            TahtaGorsellestirme(self.tahta)    
        elif oyuncu.__name__ == 3:
            self.oyuncu2.doruk = 1
            blok1 = [2,10]
            blok2 = [1,9]
            self.oyuncu2.duvarlar.remove(blok1)
            self.oyuncu2.duvarlar.remove(blok2)
            self.ekle_blok_direkt(blok1, oyuncu)  
            self.ekle_blok_direkt(blok2, oyuncu)  
            self.tahta[2,10] = oyuncu.__name__
            self.tahta[1,9] = oyuncu.__name__
            for i in self.hangi_bolge_doruk:
                self.yasaklar.remove(i)
                self.oyuncu2.bloklar.append(i)
                [a,b] = i
                self.tahta[a,b] = oyuncu.__name__   
            
        elif oyuncu.__name__ == 5:
            self.oyuncu3.doruk = 1
            blok1 = [9,10]
            blok2 = [10,9]
            self.oyuncu3.duvarlar.remove(blok1)
            self.oyuncu3.duvarlar.remove(blok2)
            self.ekle_blok_direkt(blok1, oyuncu)  
            self.ekle_blok_direkt(blok2, oyuncu)
            self.tahta[10,9] = oyuncu.__name__
            self.tahta[9,10] = oyuncu.__name__
            for i in self.hangi_bolge_doruk :
                self.yasaklar.remove(i)
                self.oyuncu3.bloklar.append(i)
                [a,b] = i
                self.tahta[a,b] = oyuncu.__name__  
                
        elif oyuncu.__name__ == 7:
            self.oyuncu4.doruk = 1
            blok1 = [10,2]
            blok2 = [9,1]
            self.oyuncu4.duvarlar.remove(blok1)
            self.oyuncu4.duvarlar.remove(blok2)
            self.ekle_blok_direkt(blok1, oyuncu)  
            self.ekle_blok_direkt(blok2, oyuncu)
            self.tahta[10,1] = oyuncu.__name__
            self.tahta[9,2] = oyuncu.__name__
            for i in self.hangi_bolge_doruk:
                self.yasaklar.remove(i)
                self.oyuncu4.bloklar.append(i)
                [a,b] = i
                self.tahta[a,b] = oyuncu.__name__  
        TahtaGorsellestirme(self.tahta)
        
    #%% SÜREÇ ###BURASINI DÜZELTTT #DORUK AKTİF ETME DUVAR KKIRMA GİBİ...
    def oyuncu_karar_ver_oto(self,oyuncu):
        while True:
            if len(oyuncu.bloklar) + len(oyuncu.duvarlar) > 20 and oyuncu.doruk == 0 and len(oyuncu.duvarlar ) <12:
                c = np.random.randint(0,2)
                if c == 0:
                    a = np.random.randint(0,11)
                    b = np.random.randint(0,11)
                    success = self.oyuncu_doruk_aktif(oyuncu,a,b)
                    if success == True:
                        print(f"|{oyuncu.__name__} doruk aktif etti")   
                        break
                    else:
                        print("O DORUK NOKTASI ZATEN DOLDURULDU")
                elif c ==1:
                    print(f"|{oyuncu.__name__} doruk aktif etmedi")
                    self.oyuncu_hamleler_oto(oyuncu)
                    break
            else:
                self.oyuncu_hamleler_oto(oyuncu)
                break
        TahtaGorsellestirme(self.tahta)
        
    def oyuncu_hamleler_oto(self,oyuncu):
        sayac_blokekle = 5
        sayac_duvarekle = 4
        sayac_sicramaekle = 1
        sayac_rakiptensil = 2
        
        random_list_secim_1 = [0,0,0,0,0,1,1,1,1,1,1]
        random_list_secim_2 = [0,0,0,0,0,1,1,1,1,1,1]
        c = np.random.randint(0,10)
        c = random_list_secim_1[c]
        if c == 0:
            while True:
                print(sayac_blokekle," ",sayac_duvarekle," ",sayac_rakiptensil," ",sayac_sicramaekle)
                if sayac_blokekle <= 0 :
                    break
                success , maliyet = self.ekle_blok_oto(oyuncu)
                if success == True:
                    sayac_blokekle -= maliyet
        elif c==1:
            while True:
                print(sayac_blokekle," ",sayac_duvarekle," ",sayac_rakiptensil," ",sayac_sicramaekle)
                if sayac_duvarekle <= 0:
                    break
                success , maliyet = self.ekle_duvar_oto(oyuncu)
                if success == True:
                    sayac_duvarekle -= maliyet    
                    
        c = np.random.randint(0,10)
        c = random_list_secim_2[c]
        if c == 0:
            while True:
                print(sayac_blokekle," ",sayac_duvarekle," ",sayac_rakiptensil," ",sayac_sicramaekle)
                if sayac_sicramaekle <= 0 :
                    break
                success , maliyet = self.ekle_sicrama_oto(oyuncu)
                if success == True:
                    sayac_sicramaekle -= maliyet
        elif c==1:
            hata_sayac = 0 #Silinecek bi blok bulunamadığında , 50 kez deneyip sıçrama seçmesi için
            while True:
                print(sayac_blokekle," ",sayac_duvarekle," ",sayac_rakiptensil," ",sayac_sicramaekle)
                if sayac_rakiptensil <= 0 :
                    break
                success , maliyet = self.sil_blok_rakip_oto(oyuncu)
                if success == True:
                    sayac_rakiptensil -= maliyet    
                hata_sayac +=1
                
                if hata_sayac == 50:
                    self.ekle_sicrama_oto(oyuncu)
                    break
                        
        self.goster_tahta()
        TahtaGorsellestirme(self.tahta)

    def goster_tahta(self):
        print("\n")
        print("0 1 2 3 4 5 6 7 8 9 10 11\n")
        for i,row in enumerate(self.tahta):
            if i >= 10:
                print(row," ",i)
            else : 
                
                print(row," ",i) 
        print("\n")
        
        
        
        
        
        
        
        
        
        
        
        
  
                
                
                
                
                
                
                
                
                
                