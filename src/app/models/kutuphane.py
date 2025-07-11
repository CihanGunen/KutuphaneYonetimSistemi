from .kitap import Kitap
from .uye import Uye
from src.app.services.json_storage import JsonStorage

class Kutuphane:
    def __init__(self):
        self.storage = JsonStorage()
        self.kitaplar = []
        self.uyeler = []
        self.verileri_yukle()

    def verileri_yukle(self):
        kitap_data = self.storage.kitaplari_yukle()
        for kd in kitap_data:
            kitap = Kitap(kd["isim"], kd["yazar"], kd["isbn"])
            if not kd.get("mevcut", True):
                kitap.odunc_ver()  # ödünçte ise durumunu ayarla
            self.kitaplar.append(kitap)

        uye_data = self.storage.uyeleri_yukle()
        for ud in uye_data:
            uye = Uye(ud["ad"], ud["soyad"], ud["uye_id"])
            # Ödünç alınan kitaplar JSON'da tutulmuyorsa boş bırakıyoruz
            self.uyeler.append(uye)

    def verileri_kaydet(self):
        kitaplar_json = []
        for kitap in self.kitaplar:
            kitaplar_json.append({
                "isim": kitap.isim,
                "yazar": kitap.yazar,
                "isbn": kitap.isbn,
                "mevcut": kitap.mevcut_mu()
            })

        uyeler_json = []
        for uye in self.uyeler:
            uyeler_json.append({
                "ad": uye.ad,
                "soyad": uye.soyad,
                "uye_id": uye.uye_id
            })

        self.storage.kitaplari_kaydet(kitaplar_json)
        self.storage.uyeleri_kaydet(uyeler_json)

    # Diğer fonksiyonlarda verileri değiştirdikten sonra bu metodu çağır
    def kitap_ekle(self, kitap: Kitap):
        self.kitaplar.append(kitap)
        self.verileri_kaydet()

    def uye_ekle(self, uye: Uye):
        self.uyeler.append(uye)
        self.verileri_kaydet()

    def kitap_bul(self, isbn: str):
        for kitap in self.kitaplar:
            if kitap.isbn == isbn:
                return kitap
        return None

    def uye_bul(self, uye_id: str):
        for uye in self.uyeler:
            if uye.uye_id == uye_id:
                return uye
        return None

    def kitaplari_listele(self):
        if not self.kitaplar:
            print("Kütüphanede kitap yok.")
            return
        for kitap in self.kitaplar:
            print(kitap)

    def uyeleri_listele(self):
        if not self.uyeler:
            print("Kütüphanede üye yok.")
            return
        for uye in self.uyeler:
            print(uye)
