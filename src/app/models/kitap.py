class Kitap:
    def __init__(self, isim, yazar, isbn):
        self.isim = isim
        self.yazar = yazar
        self.isbn = isbn
        self.__mevcut = True  # Kitabın ödünçte olup olmadığını tutar (encapsulation)

    def odunc_ver(self):
        if self.__mevcut:
            self.__mevcut = False
            return True
        return False

    def iade_et(self):
        self.__mevcut = True

    def mevcut_mu(self):
        return self.__mevcut

    def __str__(self):
        durum = "Mevcut" if self.__mevcut else "Ödünçte"
        return f"{self.isim} - {self.yazar} ({durum})"
