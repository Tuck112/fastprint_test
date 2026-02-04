# Fastprint Inventory Management System

Fastprint Inventory Management System adalah aplikasi web untuk mengelola data inventaris produk secara terstruktur dan efisien.  
Aplikasi ini dikembangkan menggunakan **Django** dan **MySQL** sebagai bagian dari **tes seleksi Junior Programmer di Fastprint Indonesia**.

Proyek ini menitikberatkan pada:
- Struktur kode yang rapi dan mudah dipahami
- Penggunaan relasi database yang benar
- Implementasi CRUD yang jelas
- Integrasi dengan legacy database MySQL

---

## 🎯 Tujuan Aplikasi

Aplikasi ini dibuat untuk membantu admin dalam:
- Mengelola data produk
- Mengelompokkan produk berdasarkan kategori dan status
- Memisahkan produk yang masih bisa dijual dan yang sudah tidak aktif
- Menyajikan data dalam tampilan yang sederhana dan mudah digunakan

---

## 🚀 Fitur Utama

- **Manajemen Produk (CRUD)**  
  Menambah, melihat, mengubah, dan menghapus data produk.

- **Filter Status Otomatis**  
  Produk otomatis dikelompokkan menjadi:
  - Bisa Dijual
  - Tidak Bisa Dijual (Arsip)

- **Relasi Data Dinamis**  
  Dropdown Kategori dan Status menggunakan relasi Foreign Key.

- **UI Responsif**  
  Menggunakan Bootstrap 5 untuk tampilan yang bersih dan user friendly.

- **Legacy Database Support**  
  Terintegrasi dengan database MySQL yang sudah ada menggunakan `managed = False`.

---

## 🧭 Alur Bisnis Aplikasi

1. Admin membuka aplikasi
2. Sistem menampilkan daftar produk
3. Produk ditampilkan berdasarkan status (aktif / arsip)
4. Admin dapat:
   - Menambahkan produk baru
   - Mengedit produk
   - Menghapus produk
5. Saat menambah atau mengedit produk:
   - Kategori dan status dipilih melalui dropdown
6. Data tersimpan langsung ke database MySQL

## 🛠️ Teknologi yang Digunakan & Cara Menjalankan Proyek

### Teknologi yang Digunakan

- **Backend**: Python 3.x, Django
- **Database**: MySQL (XAMPP / Laragon)
- **Frontend**: Bootstrap 5, Django Template Language
- **Library Tambahan**:
  - `mysqlclient` (koneksi database MySQL)
  - `requests` (integrasi API eksternal)

---

### ⚙️ Cara Instalasi & Menjalankan Proyek

#### Clone Repository
```bash
git clone https://github.com/Tuck112/fastprint_test.git
cd fastprint_test
Buat & Aktifkan Virtual Environment
python -m venv venv
.\venv\Scripts\activate
Install Dependensi
pip install -r requirements.txt
Konfigurasi Database
Aktifkan MySQL (XAMPP / Laragon)

Buat database:

db_fastprint
Sesuaikan konfigurasi database di:

fastprint/settings.py
Jalankan Server
python manage.py runserver
Akses aplikasi di browser:

http://127.0.0.1:8000/
📂 Struktur Proyek
Struktur Saat Ini
fastprint_test/
├── fastprint/
├── produk_app/
├── templates/
├── manage.py
└── requirements.txt
