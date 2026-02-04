from django.db import models

# Model untuk tabel Kategori
class Kategori(models.Model):
    # kolom kunci utama kategori (ID)
    id_kategori = models.AutoField(primary_key=True)
    # menyimpan teks (nama kategori)
    nama_kategori = models.CharField(max_length=100)

    class Meta:
        # Menghubungkan model ini ke nama tabel asli di database MySQL
        db_table = 'kategori'
        managed = False

    # Menampilkan nama kategori di dropdown form (bukan tulisan "object")
    def __str__(self):
        return self.nama_kategori

# Model untuk tabel Status
class Status(models.Model):
    # Menandakan id_status sebagai Auto Increment dan Primary Key
    id_status = models.AutoField(primary_key=True)
    # Menyimpan status produk (misal: bisa dijual / tidak bisa dijual)
    nama_status = models.CharField(max_length=50)

    class Meta:
        db_table = 'status'
        managed = False

    def __str__(self):
        return self.nama_status

# Model untuk tabel Produk (Tabel Utama)
class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=150)
    harga = models.IntegerField()
    
    # ForeignKey digunakan untuk menghubungkan (relasi) ke tabel Kategori dan status
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, db_column='kategori_id')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, db_column='status_id')

    class Meta:
        db_table = 'produk'
        managed = False
    
    def __str__(self):
        return self.nama_produk