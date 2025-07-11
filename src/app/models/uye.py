class Uye:
    def __init__(self, ad, soyad, uye_id):
        self.ad = ad
        self.soyad = soyad
        self.uye_id = uye_id
        self.odunc_kitaplar = []

    def kitap_odunc_al(self, kitap):
        if kitap.odunc_ver():
            self.odunc_kitaplar.append(kitap)
            return True
        return False

    def kitap_iade_et(self, kitap):
        if kitap in self.odunc_kitaplar:
            kitap.iade_et()
            self.odunc_kitaplar.remove(kitap)
            return True
        return False

    def __str__(self):
        return f"{self.ad} {self.soyad} (ID: {self.uye_id})"
