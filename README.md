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

## 🖼️ Tampilan Antarmuka

### 1. Homepage (Daftar Produk)
![Homepage](https://github.com/user-attachments/assets/22ac9799-eb3e-4340-8451-830843236e76)
* **Daftar Produk**: Menampilkan data dalam bentuk tabel dengan label warna untuk kategori.
* **Filter Status**: Memisahkan produk layak jual dan produk arsip secara otomatis melalui tab navigasi.

### 2. Tambah & Edit Produk
![Tambah Produk](https://github.com/user-attachments/assets/5625ebb2-ca82-4c6e-8848-038753236e76)
* **Form Dinamis**: Antarmuka menggunakan `ModelForm` untuk validasi otomatis.
* **Dropdown Terintegrasi**: Kolom Kategori dan Status mengambil data relasi (*Foreign Key*) langsung dari database.

### 3. Keamanan Data (Pop-up Konfirmasi)
![Konfirmasi Hapus](https://github.com/user-attachments/assets/5625ebb2-ca82-4c6e-8848-038753236e76)
* **Pop-up Konfirmasi**: Muncul peringatan browser sebelum pengguna menghapus data untuk mencegah kesalahan fatal.

## ⚙️ Cara Instalasi & Menjalankan Proyek

1. **Clone Repositori**
   1. git clone [https://github.com/Tuck112/fastprint_test.git](https://github.com/Tuck112/fastprint_test.git)
   2. cd fastprint_test
   
2. **Setup Virtual Environment**
   1. python -m venv venv
   2. .\venv\Scripts\activate
      
3. **Install Dependensi**
   1. pip install -r requirements.txt

4. **Konfigurasi Database**
   1. Aktifkan MySQL (XAMPP).
   2. Buat database dengan nama db_fastprint (bisa juga langsung di download pada repository).
   3. Import file .sql database ke phpMyAdmin.
   4. Sesuaikan pengaturan di fastprint/settings.py jika username/password MySQL Anda berbeda.

5. **Jalankan Server**
   1. python manage.py runserver
   2. Akses aplikasi di: http://127.0.0.1:8000/

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
