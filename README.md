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
<a href="kutuphane-yonetim-sistemi/">kutuphane-yonetim-sistemi/</a>
├── <a href="data/">data/</a>                  
├── <a href="src/">src/</a>
│   └── <a href="src/app/">app/</a>
│       ├── <a href="src/app/cli/">cli/</a>
│       │   └── <a href="src/app/cli/main_menu.py">main_menu.py</a>
│       ├── <a href="src/app/models/">models/</a>
│       │   ├── <a href="src/app/models/kitap.py">kitap.py</a>
│       │   ├── <a href="src/app/models/uye.py">uye.py</a>
│       │   └── <a href="src/app/models/kutuphane.py">kutuphane.py</a>
│       └── <a href="src/app/services/">services/</a>
│           └── <a href="src/app/services/json_storage.py">json_storage.py</a>
├── <a href="tests/">tests/</a>
│   └── <a href="tests/test_kutuphane.py">test_kutuphane.py</a>
├── <a href="README.md">README.md</a>
├── <a href="requirements.txt">requirements.txt</a>
└── <a href="run.py">run.py</a>
</pre>

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
