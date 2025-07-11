# Kütüphane Yönetim Sistemi (Python OOP Projesi)
yeni

Bu proje, Python OOP kullanılarak geliştirilmiş basit bir kütüphane yönetim sistemidir.  
Kitap ekleme, üye ekleme, kitap ödünç verme ve iade alma işlemlerini destekler.  
Veriler JSON dosyalarında kalıcı olarak saklanır.

---

## Özellikler

- Kitap ve üye yönetimi  
- Kitapların ödünç verilmesi ve iade alınması  
- JSON tabanlı veri kalıcılığı (dosyalarda saklama)  
- Modüler, OOP tabanlı kod yapısı  
- Komut satırı arayüzü (CLI) ile kullanıcı dostu kullanım  

---

## Ön Koşullar

- Python 3.8 veya üzeri  
- `python-dotenv` (gerekirse)  
- Diğer bağımlılıklar için `requirements.txt`  

---

## Kurulum

1. Projeyi klonlayın veya dosyaları indirin:

   ```bash
   git clone https://github.com/CihanGunen/KutuphaneYonetimSistemi
   cd KutuphaneYonetimSistemi
   ```

2. Sanal ortam oluşturun ve aktive edin:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate     # Windows
   ```

3. Gerekli bağımlılıkları yükleyin:

   ```bash
   pip install -r requirements.txt
   ```

---

## Proje Yapısı
---
kutuphane-yonetim-sistemi/
├── data/                  # JSON veri dosyaları (kitaplar, uyeler)
├── src/
│   └── app/
│       ├── cli/
│       │   └── [main_menu.py](src/app/cli/main_menu.py)
│       ├── models/
│       │   ├── [kitap.py](src/app/models/kitap.py)
│       │   ├── [uye.py](src/app/models/uye.py)
│       │   └── [kutuphane.py](src/app/models/kutuphane.py)
│       └── services/
│           └── [json_storage.py](src/app/services/json_storage.py)
├── tests/
│   └── [test_kutuphane.py](tests/test_kutuphane.py)
├── [README.md](README.md)
├── [requirements.txt](requirements.txt)
└── [run.py](run.py)                 # Ana giriş noktası
---

---

## Kullanım

```bash
python run.py
```

---

## Testler

Testleri çalıştırmak için:

```bash
pytest -s
```

---

