# Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.
#Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.


class Bilgisiyar_sınıfı():
    def __init__(self,pc_durum = "Kapalı",pc_sayı = 0,ögrenci_sayı = 0,pc_ses = 0):
        self.pc_durum = pc_durum
        self.pc_sayı = pc_sayı
        self.ögrenci_sayı = ögrenci_sayı
        self.pc_ses = pc_ses

    def pc_ac(self):
        print("Bilgisiyarlar Açılıyor....")
        self.pc_durum = "Açık"

    def pc_kapat(self):
        print("Bilgisiyarlar Kapanıyor....")
        self.pc_durum = "Kapalı"

    def pc_sayı_arttır_azalt(self):

        while True:

            sayı = input("Pc Sayısı Artırmak için '+' Azaltmak için '-' Çıkmak için 'q' ya basınız.")
            if sayı == "q":
                print("Bilgisiyar Sayı Ayarlarından Çıkılıyor....")
                break

            if sayı == "+":
                self.pc_sayı += 1
                print("Pc Sayı: {}".format(self.pc_sayı))

            elif sayı == "-":
                if self.pc_sayı == 0:
                    print("0'ın altında Bilgisiyar Sayısı Olamaz....")
                else:
                    self.pc_sayı -= 1
                    
                print("Pc Sayı: {}".format(self.pc_sayı))
            
        
    
    def ögrenci_sayı_artır_azalt(self):

        while True:
            ö_sayı = input("Ögrenci Sayısını Artırmak İçin '+' Azaltmak İçin '-' Çıkmak İçin 'q' ya basınız.")
            if ö_sayı == "+":
                self.ögrenci_sayı += 1
                print("Pc Sayı: {}".format(self.ögrenci_sayı))

            elif ö_sayı == "-":
                if self.ögrenci_sayı == 0:
                    print("0'ın altında Ögrenci Sayısı Olamaz....")

                else:
                    self.ögrenci_sayı -= 1
                print("Pc Sayı: {}".format(self.ögrenci_sayı))

            elif ö_sayı == "q":
                print("Öğrenci Sayı Ayarlarından Çıkılıyor....")
                break
            
    
    def pc_ses_artır_azalt(self):
        
        while True:
            p_ses = input("Bilgisiyar Ses Seviyesini Artırmak İçin '+' Azaltmak İçin '-' Çıkmak İçin 'q' ya basınız.")

            if p_ses == "q":
                print("Programdan Çıkılıyor....")
                break

            elif p_ses == "+":
                self.pc_ses += 1

            elif p_ses == "-":
                if self.pc_ses == 0:
                    print("0'ın altında Ses Seviyesi Olamaz....")
                
                else:
                    self.pc_ses -= 1
            

            print("Ses Seviyesi: {}".format(self.pc_ses))

    def __str__(self):
        return "Pc Durum: {} \nPc Sayı: {} \nÖgrenci Sayı: {} \nPc Ses: {}".format(self.pc_durum , self.pc_sayı , self.ögrenci_sayı , self.pc_ses)

                

bilgisiyar_sınıfı = Bilgisiyar_sınıfı()

print("""
----------------------------------------
Bilgisiyar Sınıfı

1.Bilgisiyarları Aç

2.Bilgisiyarları Kapat

3.Bilgisiyar Sayısını Arttır - Azalt

4.Öğrenci Sayısını Arttır - Azalt

5.Bilgisiyar Ses Seviyesi Arttır - Azalt 

6.Bilgisiyar Bilgileri

Çıkmak İçin q ya basınız.
----------------------------------------
""")


while True:
    islem = input("Lütfen İşlem Griniz:")

    if islem  == "q":
        print("Programdan Çıkılıyor....")
        break

    elif islem == "1":
        bilgisiyar_sınıfı.pc_ac()

    elif islem == "2":
        bilgisiyar_sınıfı.pc_kapat()

    elif islem == "3":
        bilgisiyar_sınıfı.pc_sayı_arttır_azalt()

    elif islem == "4":
        bilgisiyar_sınıfı.ögrenci_sayı_artır_azalt()

    elif islem == "5":
        bilgisiyar_sınıfı.pc_ses_artır_azalt()

    elif islem == "6":
        print(bilgisiyar_sınıfı45454-)

    
    
    