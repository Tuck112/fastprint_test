from django.db import models

class Kategori(models.Model):
    id_kategori = models.AutoField(primary_key=True)
    nama_kategori = models.CharField(max_length=100)

    class Meta:
        db_table = 'kategori'
        managed = False

    # Fungsi ini supaya di dropdown muncul nama kategorinya (bukan "object")
    def __str__(self):
        return self.nama_kategori

class Status(models.Model):
    id_status = models.AutoField(primary_key=True)
    nama_status = models.CharField(max_length=50)

    class Meta:
        db_table = 'status'
        managed = False

   
    def __str__(self):
        return self.nama_status

class Produk(models.Model):
    id_produk = models.AutoField(primary_key=True)
    nama_produk = models.CharField(max_length=150)
    harga = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, db_column='kategori_id')
    status = models.ForeignKey(Status, on_delete=models.CASCADE, db_column='status_id')

    class Meta:
        db_table = 'produk'
        managed = False
    
    def __str__(self):
        return self.nama_produk