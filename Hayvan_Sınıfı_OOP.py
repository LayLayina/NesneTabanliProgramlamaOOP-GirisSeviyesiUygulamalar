#Bu projede ise 4 tane sınıfı oluşturun.
#Hayvan Sınıfı ------> Bütün hayvanların ortak özelliklerinin toplandığı sınıf olacak.
#Köpek Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa köpeklere ait ek özellikler ve metodlar ekleyin.
#Kuş Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa kuşlara ait ek özellikler ve metodlar ekleyin.
#At Sınıfı ------> Bu sınıf, hayvan sınıfından miras alan bir sınıf olacak. Ayrıca bu sınıfa atlara ait ek özellikler ve metodlar ekleyin.

import time

class Hayvan():
    
    def __init__(self, ayak_sayısı = 0, yas = 0, renk = "Belirtilmedi"):
        self.ayak_sayısı = ayak_sayısı
        self.yas = yas
        self.renk = renk

    def bilgileri_goster(self):
        print("Hayvan Bilgileri.....")
        print("Ayak Sayısı: {} \nYaş: {} \nRenk: {}".format(self.ayak_sayısı,self.yas,self.renk))

    def ayak_sayısı_artır_azalt(self):
        
        while True:
            
            islem = input("Arttırmak İçin '+' Azaltmak İçin '-' Çıkmak İçin 'q' tuşuna basınız")

            if islem == "+":
                if self.ayak_sayısı == 4:
                    print("Ayak Sayısı 4 üzerinde olamaz...")
                    

                else:
                    self.ayak_sayısı += 1
                    print("Ayak Sayısı: {}".format(self.ayak_sayısı))
            elif islem == "-":
                if self.ayak_sayısı == 0:
                    print("Ayak Sayısı 0 altında olamaz...")
                    
                
                else:
                    self.ayak_sayısı -= 1
                    print("Ayak Sayısı: {}".format(self.ayak_sayısı))
                    
                
            elif islem == "q":
                print("Ayak Sayısı Arttır Azalt Fonksiyonundan Çıkılıyor...")
                time.sleep(1)
                break


    def yas_artır_azalt(self):

        while True:

            islem_yas = input("Arttırmak İçin '+' Azaltmak İçin '-' Çıkmak İçin 'q' tuşuna basınız")

            if islem_yas == "+":
                self.yas +=1
                print("Yaş: {}".format(self.yas))


            elif islem_yas == "-":
                if self.yas == 0:
                    print("Yaş 0 altında olamaz...")
                    

                else:
                    self.yas -= 1
                    print("Yaş: {}".format(self.yas))

            elif islem_yas == "q":
                print("Güncel Yaş: {}".format(self.yas))
                print("Yaş Arttır Azalt Fonksiyonundan Çıkılıyor...")
                time.sleep(1)
                break

    def renk_ekle(self):

        while True:

            renkler = ["Siyah" , "Beyaz"]

            islem_renk = input("Renk Eklemek İçin '+' Renk Silmek İçin '-' Çıkmak  İçin 'q' tuşuna basınız")

            if islem_renk == "+":

                renk_giris = input("Renk Giriniz:")
                renkler.append(renk_giris)
                print("Renkler: {}".format(renkler))

            elif islem_renk == "-":

                renk_giris_1 = input("Silmek İstediğiniz Rengi Giriniz:")
                renkler.remove(renk_giris_1)
                print("Renkler: {}".format(renkler))

            elif islem_renk == "q":
                print("Renkler: {}".format(renkler))
                print("Renk Ayar Fonksiyonundan Çıkılıyor...")
                time.sleep(1)
                break



class Köpek(Hayvan):
    def __init__(self, ayak_sayısı = 0, yas = 0 , renk = "Belirtilmedi" , dis_sayısı = 0):
        super().__init__(ayak_sayısı=0,yas=0,renk="Belirtilmedi")
        self.dis_sayısı = dis_sayısı
        
    def bilgileri_goster(self):
        print("Ayak Sayısı: {} \nYaş: {} \nRenk: {} \nDiş Sayısı: {}".format(self.ayak_sayısı,self.yas,self.renk,self.dis_sayısı))    
        
    def dis_sayısı_artır(self):
        while True:
            artır = input("Diş Sayısı Artırmak İçin '+' Azaltmak İçin '-' Çıkmak İçin 'q' Tuşuna Basınız")

            if artır == "+":
                if self.dis_sayısı == 32:
                    print("Diş Sayısı 32 Üzerinde Olamaz...")
                    print("Diş Sayısı: {}".format(self.dis_sayısı))
                    
                else:
                    self.dis_sayısı += 1
                    print("Diş Sayısı: {}".format(self.dis_sayısı))

            elif artır == "-":
                if self.dis_sayısı == 0:
                    print("Diş Sayısı: {}".format(self.dis_sayısı))

                else:
                    self.dis_sayısı -= 1
                    print("Diş Sayısı: {}".format(self.dis_sayısı))

            elif artır == "q":
                print("Diş Sayısı Arttır Azalt Fonksiyonundan Çıkılıyor...")
                time.sleep(1)
                break
                

class Kus(Hayvan):
    def __init__(self, ayak_sayısı = 0,yas = 0,renk = "Belirtilmedi",gram = 0):
        super().__init__(ayak_sayısı = 0,yas = 0,renk = "Belirtilmedi")
        self.gram = gram

    def bilgileri_goster(self):
        print("Ayak Sayısı: {} \nYaş: {} \nRenk: {} \nGram: {}".format(self.ayak_sayısı,self.yas,self.renk,self.gram))

    def gram_artır(self):

        while True:
            gram_art = input("Gram Arttırmak İçin '+' Azaltmak İçin '-' Çıkmak İçin 'q' Tuşuna Basınız '+10'")
        
            if gram_art == "+":
                self.gram += 10
                print("Gram: {}".format(self.gram))

            elif gram_art == "-":
                if self.gram <= 10:
                    print("10 Gram Altı Olamaz...")
                    print("Gram: {}".format(self.gram))

                else:
                    self.gram -= 10
                    print("Gram: {}".format(self.gram))

            elif gram_art == "q":
                print("Gram Artırma Azaltma Fonksiyonundan Çıkılıyor...")
                time.sleep(1)
                break




hayvan = Hayvan()
köpek = Köpek()
kus = Kus()
print("""
 İşlemler;

 1-Hayvanların Genel Özellikleri

 2-Köpeklerin Genel Özellikleri

 3-Kuşların Genel Özellikleri
 
 Çıkmak İçin q ya basınız...
 """)


while True:
    islem1 = input("İşlem Seçiniz:")

    if islem1 == "1":
        hayvan.bilgileri_goster()

    elif islem1 == "2":
        

        while True:
            print("""
            Köpekler İle İlgili Özellikler;

            1-Köpeklerin Özellikleri

            2-Ayak Sayısı Artır Azalt

            3-Yaş Arttır Azalt

            4-Renk Ekle Çıkar

            5-Diş Sayısı Artır Azalt
            
            Çıkmak İçin q Ya basınız...
            """)


            islem_kopek = input("İşlem Seçiniz...")

            if islem_kopek == "1":
                köpek.bilgileri_goster()

            elif islem_kopek == "2":
                köpek.ayak_sayısı_artır_azalt()

            elif islem_kopek == "3":
                köpek.yas_artır_azalt()

            elif islem_kopek == "4":
                köpek.renk_ekle()

            elif islem_kopek == "5":
                köpek.dis_sayısı_artır()

            elif islem_kopek == "q":
                print("Köpek Fonksiyonlarından Çıkılıyor...")
                time.sleep(1)
                break    

    elif islem1 == "3":
        
        while True:
            print("""
            Kuşlar İle İlgili Özellikler;

            1-Kuşların Özellikleri

            2-Ayak Sayısı Artır Azalt

            3-Yaş Artır Azalt

            4-Renk Ekle Çıkar

            5-Gram Artır Azalt
            
            Çıkmak İçin q ya basınız...
            """)

            islem_kus = input("İşlem Seçiniz...")

            if islem_kus == "1":
                kus.bilgileri_goster()

            elif islem_kus == "2":
                kus.ayak_sayısı_artır_azalt()

            elif islem_kus == "3":
                kus.yas_artır_azalt()
            
            elif islem_kus == "4":
                kus.renk_ekle()

            elif islem_kus == "5":
                kus.gram_artır()

            elif islem_kus == "q":
                print("Kuş Fonksiyonlarından Çıkılıyor...")
                time.sleep(1)
                break
    elif islem1 == "q":
        print("Hayvvanların Genel Özelliklerinden Çıkılıyor...")
        time.sleep(1)
        break

