import math


def baslik(yazi):
    print("=" * 40)
    print(yazi.center(40))
    print("=" * 40)



def kontrol(mesaj="Bir sayı girin: "):
    while True:  # doğru girene kadar sor
        girdi = input(mesaj).strip()

        if girdi == "":
            print("Boş bırakılamaz!")
            continue  # tekrar sor

        try:
            return float(girdi)  # sayıysa geri döndür ve fonksiyondan çık
        except ValueError:
            print("Lütfen sadece sayı girin!")

def kontrol_int(mesaj="Bir sayı girin: "):
    while True:
        girdi = input(mesaj).strip()
        if girdi == "":
            print("Boş bırakılamaz!")
            continue
        if girdi.isdigit():
            return int(girdi)
        else:
            print("Lütfen sadece tam sayı girin!")


# 2D fonksiyonlar

def kare() :
    while True:
        seçim = input("Alan (A) | Çevre (Ç) | Köşegen (K) : ").strip().upper()
        if seçim in ["A", "Ç", "K"]:
            break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")

    kare_kenar_uzunluk = kontrol("Kenar uzunluğunu girin : ")

    if seçim == "A" :
        print(f"Karenin alanı {pow(kare_kenar_uzunluk , 2)} . ")
    elif seçim == "Ç" :
        print(f"Karenin çevresi {kare_kenar_uzunluk * 4} . ")
    elif seçim == "K" :
        print(f"Karenin köşegeni {kare_kenar_uzunluk * math.sqrt(2)} . ")

def dikdortgen() :
    while True:
        seçim = input("Alan (A) | Çevre (Ç) | Köşegen (K) : ").strip().upper()
        if seçim in ["A", "Ç", "K"]:
            break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    dikdörtgen_kenar_uzunluk1 = kontrol("Birinci kenarı girin : ")
    dikdörtgen_kenar_uzunluk2 = kontrol("İkinci kenarı girin : ")

    if seçim == "A" :
        print(f"Dikdörtgenin alanı {dikdörtgen_kenar_uzunluk1 * dikdörtgen_kenar_uzunluk2} . ")
    elif seçim == "Ç" :
        print(f"Dikdörtgenin çevresi {(dikdörtgen_kenar_uzunluk1 + dikdörtgen_kenar_uzunluk2)*2} . ")
    elif seçim == "K" :
        print(f"Dikdörtgenin köşegeni {math.sqrt(dikdörtgen_kenar_uzunluk2**2 + dikdörtgen_kenar_uzunluk1**2)} . ")

def daire() :
    while True:
        seçim = input("Alan (A) | Çevre (Ç) : ").strip().upper()
        if seçim in ["A", "Ç"]:
            break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    yarıçap = kontrol("Yarıçap uzunluğunu girin : ")

    if seçim == "A" :
        print(f"Çemberin alanı {math.pi * yarıçap**2} . ")
    elif seçim == "Ç" :
        print(f"Çemberin çevresi {2 * math.pi * yarıçap} . ")

def paralelkenar() :
    while True:
        seçim = input("Alan (A) | Çevre (Ç) : ").strip().upper()
        if seçim in ["A", "Ç"]:
            break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    paralel_kenar1 = kontrol("Taban kenarını girin : ")
    paralel_kenar2 = kontrol("Yan kenarı girin : ")

    if seçim == "A" :
        yükseklik = kontrol("Yüksekliği girin : ")
        print(f"Paralelkenarın alanı {paralel_kenar1 * yükseklik} . ")
    elif seçim == "Ç" :
        print(f"Paralelkenarın çevresi {(paralel_kenar1 + paralel_kenar2) * 2 } . ")

def yamuk() :
    while True:
        seçim = input("Alan (A) | Çevre (Ç) : ").strip().upper()
        if seçim in ["A", "Ç"]:
            break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    yamuk_kenar1 = kontrol("Alt tabanı girin : ")
    yamuk_kenar2 = kontrol("Üst tabanı girin : ")
    
    if seçim == "A" :
        yükseklik = kontrol("Yüksekliği girin : ")
        print(f"Yamuğun alanı {yükseklik * ((yamuk_kenar1 + yamuk_kenar2)/2)} . ")
    elif seçim == "Ç" :
        yamuk_kenar3 = kontrol("Birinci yan kenarı girin : ")
        yamuk_kenar4 = kontrol("İkinci yan kenarı girin : ")
        print(f"Yamuğun çevresi {yamuk_kenar1+yamuk_kenar2+yamuk_kenar3+yamuk_kenar4} . ")

def ucgen() :
    while True:
        şkl_seçim = input("Eşkenar (E) | İkizkenar (İ) | Çeşitkenar (Ç) : ").strip().upper()
        if şkl_seçim in ["İ", "E","Ç"]:
            break
        print(f"{şkl_seçim} doğru değil. Lütfen tekrar deneyin.")

    while True:
        seçim = input("Alan (A) | Çevre (Ç) : ").strip().upper()
        if seçim in ["A", "Ç"]:
            break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")

    üçgen_kenar_eş = kontrol("Üçgenin (1.) kenarı girin : ")

    if şkl_seçim == "E" :
        if seçim == "A" :
            print(f"Üçgenin alanı {(üçgen_kenar_eş ** 2 * math.sqrt(3)) / 4 } . ")
        elif seçim == "Ç" :
            print(f"Üçgenin çevresi {üçgen_kenar_eş*3} . ")
    elif şkl_seçim == "İ" :
        üçgen_kenar_ikiz = kontrol("Üçgenin (2.) kenarı girin : ")
        if seçim == "A" :
            print(f"Üçgenin alanı {(üçgen_kenar_ikiz / 4) * math.sqrt(4*üçgen_kenar_eş**2 - üçgen_kenar_ikiz**2)} . ")
        elif seçim == "Ç" :
            print(f"Üçgenin çevresi {üçgen_kenar_ikiz*2 + üçgen_kenar_eş} . ")
    elif şkl_seçim == "Ç" :
        üçgen_kenar_ikiz = kontrol("Üçgenin (2.) kenarı girin : ")
        üçgen_kenar_çeşit = kontrol("Üçgenin (3.) kenarı girin : ")
        if seçim == "A" :
            ort = (üçgen_kenar_eş + üçgen_kenar_ikiz + üçgen_kenar_çeşit) / 2 
            print(f"Üçgenin alanı {math.sqrt(ort*(ort-üçgen_kenar_ikiz)*(ort-üçgen_kenar_eş)*(ort-üçgen_kenar_çeşit))} . ")
        elif seçim == "Ç" :
            print(f"Üçgenin çevresi {üçgen_kenar_çeşit+üçgen_kenar_eş+üçgen_kenar_ikiz} . ")

def cokgenler() :
    while True:
        seçim = input("Alan (A) | Çevre (Ç) : ").strip().upper()
        if seçim in ["A", "Ç"]:
            break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")

    kenar_sayısı = kontrol("Kenar sayısını girin : ")
    kenar_uzunluk = kontrol("Kenar uzunluğunu girin : ")

    if seçim == "A" :
        print(f"{kenar_sayısı}genin alanı {(kenar_sayısı*(kenar_uzunluk**2)) / (4 * math.tan(math.pi / kenar_sayısı)) } . ")
    elif seçim == "Ç" :
        print(f"{kenar_sayısı}genin çevresi {kenar_sayısı * kenar_uzunluk} . ")

# 3D fonksiyonlar

def küp() :
    while True:
        seçim = input("Yüzey alanı (A) | Hacim (H) | Çevre (Ç) : ").strip().upper()
        if seçim in ["A","Ç","H"]:
           break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    kenar_uzunluğu = kontrol("Kenar uzunluğunu girin : ")

    if seçim == "A" :
        print(f"Küpün yüzey alanı {(kenar_uzunluğu**2) * 6} . ")
    elif seçim == "Ç" :
        print(f"Küpün çevresi {kenar_uzunluğu * 12} . ")
    elif seçim == "H" :
        print(f"Küpün hacmi {kenar_uzunluğu ** 3} . ")

def dikdörtgenler_prizması() :
    while True:
        seçim = input("Yüzey alanı (A) | Hacim (H) | Çevre (Ç) : ").strip().upper()
        if seçim in ["A","Ç","H"]:
           break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    kenar1 = kontrol("1. kenarı girin : ")
    kenar2 = kontrol("2. kenarı girin : ")
    kenar3 = kontrol("3. kenarı girin : ")

    if seçim == "A" :
        print(f"Dikdörtgenler prizmasının yüzey alanı {2 * ((kenar1 * kenar2) + (kenar1 * kenar3) + (kenar2 * kenar3))} . ")
    elif seçim == "Ç" :
        print(f"Dikdörtgenler prizmasının çevresi {kenar1 * 4 + kenar2 * 4 + kenar3 * 4} . ")
    elif seçim == "H" :
        print(f"Dikdörtgenler prizmasının hacmi {kenar3 * kenar2 * kenar1} . ")

def küre() :
    while True:
        seçim = input("Yüzey alanı (A) | Hacim (H) : ").strip().upper()
        if seçim in ["A","H"]:
           break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    yaricap = kontrol("Yarıçapı girin : ")

    if seçim == "A" :
        print(f"Kürenin yüzey alanı {(yaricap**2) * 4 * math.pi} . ")
    elif seçim == "H" :
        print(f"Kürenin hacmi {(4/3)* math.pi * (yaricap ** 3)} . ")

def silindir() :
    while True:
        seçim = input("Yüzey alanı (A) | Hacim (H) | Yan alan (Y) | Taban alan (T) : ").strip().upper()
        if seçim in ["A","Y","H","T"]:
           break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    yaricap = kontrol("Tabanın yarıçapını girin : ")

    if seçim == "A" :
        yukseklik = kontrol("Silindirin yüksekliğini girin : ")
        print(f"Silindirin yüzey alanı {2 * math.pi * yaricap * (yaricap + yukseklik)} . ")
    elif seçim == "H" :
        yukseklik = kontrol("Silindirin yüksekliğini girin : ")
        print(f"Silindirin hacmi {math.pi * (yaricap**2) * yukseklik} . ")
    elif seçim == "Y" :
        yukseklik = kontrol("Silindirin yüksekliğini girin : ")
        print(f"Silindirin yanal alanı {2 * math.pi * yaricap * yukseklik} . ")
    elif seçim == "T" :
        print(f"Silindirin taban alanı {math.pi * yaricap**2} . ")

def koni() :
    while True:
        seçim = input("Yüzey alanı (A) | Hacim (H) | Yan alan (Y) | Taban alan (T) : ").strip().upper()
        if seçim in ["A","Y","H","T"]:
           break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    yukseklik = kontrol("Yükseklği girin : ")
    yaricap = kontrol("Yarıçapı girin : ")
    ana_dogru = float(math.sqrt(yaricap**2 + yukseklik**2))

    if seçim == "T" :
        print(f"Koninin taban alanı {math.pi * (yaricap **2)} . ")
    elif seçim == "Y" :
        print(f"Koninin yanal alanı {math.pi * yaricap * ana_dogru} . ")
    elif seçim == "A" :
        print(f"Koninin yüzey alanı {(math.pi * yaricap * ana_dogru)+(math.pi * (yaricap **2))} . ")
    elif seçim == "H" :
        print(f"Koninin hacmi {(math.pi * (yaricap**2) * yukseklik)/3} . ")

def kare_prizma() :
    while True:
        seçim = input("Yüzey alanı (A) | Hacim (H) | Yan alan (Y) | Taban alan (T) : ").strip().upper()
        if seçim in ["A","Y","H","T"]:
           break
        print(f"{seçim} doğru değil. Lütfen tekrar deneyin.")
    yukseklik = kontrol("Yükseklği girin : ")
    kenar = kontrol("Taban kenarını girin : ")

    if seçim == "T" :
        print(f"Kare prizmanın taban alanı {kenar**2} . ")
    elif seçim == "Y" :
        print(f"Kare prizmanın yanal alanı {4 * yukseklik * kenar} . ")
    elif seçim == "A" :
        print(f"Kare prizmanın yüzey alanı {2*(kenar**2)+(4 * yukseklik * kenar)} . ")
    elif seçim == "H" :
        print(f"Kare prizmanın hacmi {kenar**2 * yukseklik} . ")


print(" ")
baslik("CATOWIC GEOMETRİK HESAPLAYICI")
print(" ")
print("Merhaba ben Catowic geometrik hesaplayıcıma hoşgeldin . ")
print("Bu hesap makinesi geometrik şekillerin alan , çevre ve benzeri hesaplarını yapmak içindir . ")
print("Github : https://github.com/catowic")
print("Youtube : https://www.youtube.com/@Catowic")
print("Hataları bildirmek için : https://x.com/catowic . ") 


#işlemler

basla = True

while basla == True :
    basla = False
    print(" ")
    howD = input("3D or 2D : ").upper().strip()
    print(" ")


    if howD == "3D" :
        print("Küp için (1) . ")
        print("Dikdörtgenler prizması için (2) . ")
        print("Küre için (3) . ")
        print("Silindir için (4) . ")
        print("Koni için (5) . ")
        print("Kare prizma için (6) . ")

        while True:
            shape = kontrol_int("Numara girin : ")
            if shape in [1,2,3,4,5,6]:
                break
            print("Yanlış seçim , tekrar deneyin . ")

        if shape == 1 :
            küp()
        elif shape == 2 :
            dikdörtgenler_prizması()
        elif shape == 3 :
            küre()
        elif shape == 4 :
            silindir()
        elif shape == 5 :
            koni()
        elif shape == 6 :
            kare_prizma()
        else :
            print(f"{shape} yanlış . Tekrar deneyin . ")  
    elif howD == "2D" :
        print("Kare için (1) .")
        print("Dikdörtgen için (2) .")
        print("Daire için (3) .")
        print("Paralelkenar için (4) .")
        print("Yamuk için (5) .")
        print("Üçgen için (6) .")
        print("Çokgenler için (7) . ")
        
        while True:
            shape = kontrol_int("Numara girin : ")
            if shape in [1,2,3,4,5,6,7]:
                break
            print("Yanlış seçim , tekrar deneyin . ")

        if shape == 1 :
            kare()
        elif shape == 2 :
            dikdortgen()
        elif shape == 3 :
            daire()
        elif shape == 4 :
            paralelkenar()
        elif shape == 5 :
            yamuk()
        elif shape == 6 :
            ucgen()
        elif shape == 7 :
            cokgenler()
        else :
            print(f"{shape} yanlış . Tekrar deneyin . ")
    else :
        print(f"{howD} yanlış . Tekrar deneyin . ")

    basla = True
    print(" ")







