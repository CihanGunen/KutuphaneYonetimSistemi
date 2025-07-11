import json
import os

class JsonStorage:
    def __init__(self, data_dir="data", kitap_file="kitaplar.json", uye_file="uyeler.json"):
        self.data_dir = data_dir
        self.kitap_file = os.path.join(data_dir, kitap_file)
        self.uye_file = os.path.join(data_dir, uye_file)

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

    def kitaplari_yukle(self):
        if not os.path.isfile(self.kitap_file):
            return []
        with open(self.kitap_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def uyeleri_yukle(self):
        if not os.path.isfile(self.uye_file):
            return []
        with open(self.uye_file, "r", encoding="utf-8") as f:
            return json.load(f)

    def kitaplari_kaydet(self, kitaplar):
        with open(self.kitap_file, "w", encoding="utf-8") as f:
            json.dump(kitaplar, f, ensure_ascii=False, indent=4)

    def uyeleri_kaydet(self, uyeler):
        with open(self.uye_file, "w", encoding="utf-8") as f:
            json.dump(uyeler, f, ensure_ascii=False, indent=4)
