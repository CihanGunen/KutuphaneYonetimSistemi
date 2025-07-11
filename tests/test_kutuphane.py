import pytest
from src.app.models.kitap import Kitap
from src.app.models.uye import Uye
from src.app.models.kutuphane import Kutuphane

def test_kitap_ekle_ve_bul():
    kutuphane = Kutuphane()
    kitap = Kitap("Test Kitap", "Test Yazar", "12345")
    kutuphane.kitap_ekle(kitap)
    bulunan = kutuphane.kitap_bul("12345")
    assert bulunan is not None
    assert bulunan.isim == "Test Kitap"
    print("✅ test_kitap_ekle_ve_bul: Kitap başarıyla eklendi ve bulundu.")

def test_uye_ekle_ve_bul():
    kutuphane = Kutuphane()
    uye = Uye("Ali", "Veli", "u1")
    kutuphane.uye_ekle(uye)
    bulunan = kutuphane.uye_bul("u1")
    assert bulunan is not None
    assert bulunan.ad == "Ali"
    print("✅ test_uye_ekle_ve_bul: Üye başarıyla eklendi ve bulundu.")

def test_odunc_verme_ve_iade():
    kutuphane = Kutuphane()
    kitap = Kitap("Kitap1", "Yazar1", "isbn1")
    uye = Uye("Ayşe", "Kara", "uye1")
    kutuphane.kitap_ekle(kitap)
    kutuphane.uye_ekle(uye)

    # Ödünç ver
    verildi = uye.kitap_odunc_al(kitap)
    assert verildi is True
    assert kitap.mevcut_mu() is False

    # Aynı kitap tekrar verilemez
    verildi_ikinci = uye.kitap_odunc_al(kitap)
    assert verildi_ikinci is False

    # İade et
    iade = uye.kitap_iade_et(kitap)
    assert iade is True
    assert kitap.mevcut_mu() is True

    # Aynı kitap tekrar iade edilemez
    iade_ikinci = uye.kitap_iade_et(kitap)
    assert iade_ikinci is False

    print("✅ test_odunc_verme_ve_iade: Ödünç alma ve iade işlemleri başarılı.")
