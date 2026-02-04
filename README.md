🚀 Fitur Utama
Manajemen Produk (CRUD): Tambah, Lihat, Edit, dan Hapus produk secara real-time.

Filter Status Otomatis: Memisahkan produk yang "Bisa Dijual" dan produk yang harus diarsip ("Tidak Bisa Dijual").

Dropdown Dinamis: Menggunakan relasi tabel untuk Kategori dan Status produk.

UI Responsif: Dibangun dengan Bootstrap 5 agar nyaman diakses dari perangkat apapun.

Integrasi Database: Menggunakan database MySQL yang sudah ada (legacy database support).

🛠️ Struktur Kode Teknis
Proyek ini mengikuti pola desain MVT (Model-View-Template):

Models: Menggunakan managed = False untuk menghubungkan aplikasi dengan tabel MySQL yang dibuat secara manual. Fungsi __str__ diterapkan untuk memastikan keterbacaan data pada antarmuka admin dan form.

Views: Berisi logika bisnis, termasuk penggunaan filter() dan exclude() untuk pemisahan status barang.

Forms: Menggunakan ModelForm dengan widgets Bootstrap untuk memvalidasi input dan mempercepat pembuatan UI.

Templates: Menggunakan sintaks Django Template Language (DTL) untuk menampilkan data secara dinamis dan aman.

📋 Prasyarat Sistem
Python 3.x

MySQL (XAMPP/Laragon)

Library: django, mysqlclient

⚙️ Cara Instalasi & Menjalankan Proyek
Clone Repositori

Bash
git clone https://github.com/Tuck112/fastprint_test.git
cd fastprint_test
Setup Virtual Environment

Bash
python -m venv venv
# Aktivasi di Windows:
.\venv\Scripts\activate
Install Dependensi

Bash
pip install -r requirements.txt
Konfigurasi Database Pastikan MySQL Anda aktif dan buat database bernama db_fastprint (atau sesuai setelan di settings.py). Import tabel produk, kategori, dan status.

Jalankan Server

Bash
python manage.py runserver
Buka browser dan akses http://127.0.0.1:8000/.

📂 Struktur Repositori
Plaintext
fastprint_test/
├── fastprint/          # Konfigurasi utama Django
├── produk_app/         # Aplikasi inti (Models, Views, Forms)
├── templates/          # File HTML (UI)
├── .gitignore          # File untuk mengecualikan folder venv
├── requirements.txt    # Daftar library yang diperlukan
└── README.md           # Dokumentasi ini
