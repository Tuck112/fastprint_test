# Fastprint Inventory Management System

Proyek ini adalah aplikasi manajemen inventaris produk yang dikembangkan menggunakan **Django** dan **MySQL** sebagai bagian dari tes seleksi Junior Programmer di Fastprint Indonesia.

## 🚀 Fitur Utama
* **CRUD Produk**: Create, Read, Update, dan Delete data produk secara dinamis.
* **Filter Status Otomatis**: Memisahkan tampilan produk yang "Bisa Dijual" dan produk yang masuk kategori "Tidak Bisa Dijual" (Arsip).
* **Dropdown Dinamis**: Menggunakan relasi tabel (Foreign Key) untuk Kategori dan Status produk.
* **UI Responsif**: Menggunakan Bootstrap 5 untuk tampilan yang bersih dan profesional.
* **Integrasi Database**: Menggunakan database MySQL yang sudah ada (*legacy database support*) dengan konfigurasi `managed = False`.

---

## 🛠️ Teknologi yang Digunakan
* **Backend**: Python 3.x & Django Framework.
* **Database**: MySQL (XAMPP/Laragon).
* **Frontend**: Bootstrap 5 & Django Template Language (DTL).
* **Library**: `mysqlclient` (koneksi database) & `requests` (integrasi API).

---

## ⚙️ Cara Instalasi & Menjalankan Proyek

1. **Clone Repositori**
   ```bash
   git clone [https://github.com/Tuck112/fastprint_test.git](https://github.com/Tuck112/fastprint_test.git)
   cd fastprint_test

Setup Virtual Environment

Bash
python -m venv venv
# Aktivasi di Windows:
.\venv\Scripts\activate
Install Dependensi Pastikan Anda sudah berada di dalam folder proyek sebelum menjalankan perintah ini:

Bash
pip install -r requirements.txt
Konfigurasi Database

Aktifkan MySQL (XAMPP/Laragon).

Buat database dengan nama db_fastprint.

Sesuaikan DATABASES di file fastprint/settings.py jika username/password MySQL Anda berbeda.

Jalankan Server

Bash
python manage.py runserver
Akses aplikasi di: http://127.0.0.1:8000/

fastprint_test/
├── fastprint/          # Konfigurasi utama proyek Django
├── produk_app/         # Aplikasi inti (Models, Views, Forms)
│   ├── models.py       # Definisi tabel & relasi database
│   ├── views.py        # Logika bisnis & pengelolaan data
│   └── forms.py        # Validasi & styling form Bootstrap
├── templates/          # File HTML (UI/Antarmuka)
├── .gitignore          # Pengaturan pengecualian file (seperti venv)
├── requirements.txt    # Daftar library yang diperlukan
└── README.md           # Dokumentasi proyek
