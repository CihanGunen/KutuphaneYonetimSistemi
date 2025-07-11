# Kütüphane Yönetim Sistemi (Python OOP Projesi)

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

<pre>
kutuphane-yonetim-sistemi/
├── data/                  
├── src/
│   └── app/
│       ├── cli/
│       │   └── <a href="src/app/cli/main_menu.py">main_menu.py</a>
│       ├── models/
│       │   ├── <a href="src/app/models/kitap.py">kitap.py</a>
│       │   ├── <a href="src/app/models/uye.py">uye.py</a>
│       │   └── <a href="src/app/models/kutuphane.py">kutuphane.py</a>
│       └── services/
│           └── <a href="src/app/services/json_storage.py">json_storage.py</a>
├── tests/
│   └── <a href="tests/test_kutuphane.py">test_kutuphane.py</a>
├── <a href="README.md">README.md</a>
├── <a href="requirements.txt">requirements.txt</a>
└── <a href="run.py">run.py</a>
</pre>


---

## Proje Yapısı

```
kutuphane-yonetim-sistemi/
├── data/                  # JSON veri dosyaları (kitaplar, uyeler)
├── src/
│   └── app/
│       ├── cli/
│       │   └── main_menu.py
│       ├── models/
│       │   ├── kitap.py
│       │   ├── uye.py
│       │   └── kutuphane.py
│       └── services/
│           └── json_storage.py
├── tests/
│   └── test_kutuphane.py
├── README.md
├── requirements.txt
└── run.py                 # Ana giriş noktası
```

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

