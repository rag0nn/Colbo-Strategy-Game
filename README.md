# Colbo-Strategy-Game
Colbo_v1 , "masa oyunu" türünde 4 kişi ile oynanan bir strateji oyunudur, amaç kendi bloklarını artırığ rakiplerinkini azaltarak kazanan olmaktır.
Python dilinde ve Pyqt5 gui'si ile yapılmıştır.

## OYUNUN BAŞLANGICI
12x12'lik bir tahtanın dört köşesine 2x2 olarak her oyuncunun base'i vardır.Ve bunlar oyundaki duvar bloklarından oluşmaktadır.
![baase_start](https://github.com/rag0nn/Colbo-Strategy-Game/blob/main/Colbo%20Strategy%20Game/aciklama-gorselleri/oyun_v1_base_start.jpg)

(Görseller sol üstteki kırmızı oyuncuyu temsil ediyor)
## OYUN SÜRECİ
Her turda her oyuncuya önce 2 seçenek sunulur:"5 Adım bloğu ekle" veya "4 duvar ekle" , tercihin ardından tekrar 2 seçenek sunulur:"1 sıçrama ekle" veya "2 kere  rakipten sil"
oyuncular her turda seçimlerini belirleyerek oyunu sürdürürler.Ayrıca şartlar sağlanıyorsa "doruk aktif" hamlesini istediklerinde yapabilirler
Duvar sayısı 0'a inen oyuncu oyundan elenir ve son kişi kalana kadar oyun devam eder.

## HAMLELER
- ### ADIM BLOĞU EKLEMEK 
Sahip olunan bir duvarın ya da bloğun devamı olarak koyulması gereken,rakibin "sıçrama" veya "silme" hameleleri ile ele geçirilebilen bloklardır.
![blok_ekleme](https://github.com/rag0nn/Colbo-Strategy-Game/blob/main/Colbo%20Strategy%20Game/aciklama-gorselleri/oyun_v1_blok.jpg)

- ### DUVAR EKLEMEK
Sahip olunan bir blok ya da duvarın devamı olarak koyulması gereken,rakibin "sıçrama " veya "silme" hamleleri ile ele geçirilemeyen bloklardır.
![duvar ekleme](https://github.com/rag0nn/Colbo-Strategy-Game/blob/main/Colbo%20Strategy%20Game/aciklama-gorselleri/oyun_v1_duvar.jpg)

- ### SIÇRAMA EKLEMEK
Tahtanın "doruk" ve duvar noktaları hariç herhangi bir noktasına koyulabilen adım bloklardır
![sicrama](https://github.com/rag0nn/Colbo-Strategy-Game/blob/main/Colbo%20Strategy%20Game/aciklama-gorselleri/oyun_v1_sicrama.jpg)

- ### RAKİPTEN SİLMEK

![sil](https://github.com/rag0nn/Colbo-Strategy-Game/blob/main/Colbo%20Strategy%20Game/aciklama-gorselleri/oyun_v1_sil_1.jpg)
![sil2](https://github.com/rag0nn/Colbo-Strategy-Game/blob/main/Colbo%20Strategy%20Game/aciklama-gorselleri/oyun_v1_sil_2.jpg)
Rakibin duvar harici bir adım bloğunu silmeye yarar

- ### DORUK AKTİF ETMEK
Seçilen bloğun hangi oyuncunun rootuna yakınsa o taraftaki kenar blokları tarar ve aktif eden oyuncunun başlangıçtaki root bloklarını yarıya düşürür,Ani bir adım bloğu genişlemesi sağlar
Doruk aktif için oyuncuya ait duvar + adım blokları sayısı 20 veya daha fazla olmalı ve duvar sayısı 12'yi geçmemelidir.
![doruk](https://github.com/rag0nn/Colbo-Strategy-Game/blob/main/Colbo%20Strategy%20Game/aciklama-gorselleri/oyun_v1_doruk.jpg)

## KOD İÇERİĞİ
4 python dosyasından oluşmaktardır  bunlar : log_tutucu ,oyun, oyun_gui ve tahta_gorsellestirme'dir.log_tutucu yapılan hamlelerin logunu tutar , oyun dosyayısı oyunun işleyişi hakkındaki kodları içerir,oyun_gui oyunun arayüzü ve tetiklenmeleri içerir ana dosyamız budur , tahta_gorselleştirme dosyası oyun dosyasının gönderdiği ve oyuncuların taglarini içeren matrisi alarak renkli ve büyütülmüş bir hale getirir.Bunlar dışında tahta.png , tahta_cizildi.png ve log.txt bulunur,tahta.png güncel tahta görselidir,tahta_cizildi ise tahta ekranı üzerinde işaretlemeye yarayan çizgileri , bu işleve ait butonlarla tetiklendikçe değişitirilmesi ile sürekli güncellenir.
