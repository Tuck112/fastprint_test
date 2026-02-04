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

## 📂 Struktur Repositori

```text
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

## HOMEPAGE
<img width="1907" height="1087" alt="image" src="https://github.com/user-attachments/assets/2d04447e-6002-4a16-bf8a-586148190bdb" />
Aplikasi ini memiliki antarmuka yang bersih dan fungsional:
1. **Daftar Produk**: Menampilkan data dalam bentuk tabel dengan label warna untuk kategori.
2. **Filter Status**: Memisahkan produk layak jual dan produk arsip secara otomatis.
3. **Form Dinamis**: Memudahkan pengelolaan data (Tambah/Edit) dengan validasi input.

## TAMBAH PRODAK
<img width="1917" height="1093" alt="image" src="https://github.com/user-attachments/assets/22ac9799-eb3c-41e3-8a44-a31b521968fc" />
1. **Form Dinamis**: Antarmuka tambah produk menggunakan ModelForm untuk validasi otomatis.
2. **Dropdown Terintegrasi**: Kolom Kategori dan Status mengambil data relasi (Foreign Key) langsung dari database.
3. **Clean Design**: Tampilan form menggunakan card.

## POP UP KONFIRMASI
<img width="1911" height="1092" alt="image" src="https://github.com/user-attachments/assets/5625ebb2-ca0b-4f8b-a2d9-8afbd232d72f" />
1.Pop up konfirmasi yang muncul apabila user menekan buttom hapus
