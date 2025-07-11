from src.app.models.kitap import Kitap
from src.app.models.uye import Uye
from src.app.models.kutuphane import Kutuphane
import uuid  # UUID üretmek için

kutuphane = Kutuphane()

def kitap_ekle():
    isim = input("Kitap ismi: ")
    yazar = input("Yazar ismi: ")
    isbn = input("ISBN: ")

    if kutuphane.kitap_bul(isbn):
        print("Bu ISBN ile kayıtlı bir kitap zaten var.")
        return
    yeni_kitap = Kitap(isim, yazar, isbn)
    kutuphane.kitap_ekle(yeni_kitap)
    print(f"Kitap '{isim}' başarıyla eklendi.")

def uye_ekle():
    ad = input("Üye adı: ")
    soyad = input("Üye soyadı: ")
    uye_id = str(uuid.uuid4())[:8]
    yeni_uye = Uye(ad, soyad, uye_id)
    kutuphane.uye_ekle(yeni_uye)
    print(f"Üye '{ad} {soyad}' başarıyla eklendi. ID: {uye_id}")

def kitaplari_listele():
    kutuphane.kitaplari_listele()

def uyeleri_listele():
    kutuphane.uyeleri_listele()

def kitap_odunc_ver():
    uye_id = input("Üye ID'si: ")
    isbn = input("Kitap ISBN'si: ")

    uye = kutuphane.uye_bul(uye_id)
    if not uye:
        print("Üye bulunamadı.")
        return

    kitap = kutuphane.kitap_bul(isbn)
    if not kitap:
        print("Kitap bulunamadı.")
        return

    if uye.kitap_odunc_al(kitap):
        print(f"Kitap '{kitap.isim}' başarıyla ödünç verildi.")
    else:
        print("Kitap şu anda ödünçte.")

def kitap_iade_al():
    uye_id = input("Üye ID'si: ")
    isbn = input("Kitap ISBN'si: ")

    uye = kutuphane.uye_bul(uye_id)
    if not uye:
        print("Üye bulunamadı.")
        return

    kitap = kutuphane.kitap_bul(isbn)
    if not kitap:
        print("Kitap bulunamadı.")
        return

    if uye.kitap_iade_et(kitap):
        print(f"Kitap '{kitap.isim}' başarıyla iade alındı.")
    else:
        print("Bu üyenin böyle bir ödünç kitabı yok.")

def baslat():
    while True:
        print("\n📚 KÜTÜPHANE YÖNETİM SİSTEMİ 📚")
        print("1. Kitap Ekle")
        print("2. Üye Ekle")
        print("3. Kitapları Listele")
        print("4. Üyeleri Listele")
        print("5. Kitap Ödünç Ver")
        print("6. Kitap İade Al")
        print("0. Çıkış")

        secim = input("Seçiminizi yapın: ")

        if secim == "1":
            kitap_ekle()
        elif secim == "2":
            uye_ekle()
        elif secim == "3":
            kitaplari_listele()
        elif secim == "4":
            uyeleri_listele()
        elif secim == "5":
            kitap_odunc_ver()
        elif secim == "6":
            kitap_iade_al()
        elif secim == "0":
            print("Çıkılıyor... İyi günler!")
            break
        else:
            print("❌ Geçersiz seçim. Lütfen tekrar deneyin.")
