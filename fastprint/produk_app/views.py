from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm

# Fungsi untuk menampilkan daftar produk yang statusnya 'bisa dijual'
def produk_list(request):
    # Mengambil data dari database dengan filter status 
    data = Produk.objects.filter(status__nama_status='bisa dijual')
    return render(request, 'produk_app/list_produk.html', {'produk': data})

# Fungsi untuk menampilkan produk yang TIDAK bisa dijual (Arsip)
def produk_tidak_bisa_dijual(request):
    # Menggunakan exclude untuk mengambil semua data kecuali yang statusnya 'bisa dijual'
    data = Produk.objects.exclude(status__nama_status='bisa dijual')
    return render(request, 'produk_app/list_produk.html', {
        'produk': data,
        'title_page': 'Daftar Produk (Tidak Bisa Dijual)',
        'is_archive': True
    })

# Fungsi untuk menambah produk baru
def produk_add(request):
    # Cek jika user mengirimkan data melalui tombol simpan (POST)
    if request.method == "POST":
        form = ProdukForm(request.POST)
        # Validasi data yang diinput sudah benar
        if form.is_valid():
            form.save() # Menyimpan data baru ke database
            return redirect('produk_list') 
    else:
        # Jika hanya membuka halaman, tampilkan form kosong
        form = ProdukForm()
    return render(request, 'produk_app/form_produk.html', {'form': form, 'title': 'Tambah Produk'})

# Fungsi untuk mengubah/edit data produk yang sudah ada
def produk_edit(request, id):
    # Mencari data produk berdasarkan ID, jika tidak ada tampilkan
    obj = get_object_or_404(Produk, id_produk=id)
    if request.method == "POST":
        # Mengisi form dengan data lama (obj) ditambah data baru dari user
        form = ProdukForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        # Menampilkan form dengan isi data produk yang dipilih
        form = ProdukForm(instance=obj)
    return render(request, 'produk_app/form_produk.html', {'form': form, 'title': 'Edit Produk'})

# Fungsi untuk menghapus produk
def produk_delete(request, id):
    # Mencari data produk berdasarkan ID
    obj = get_object_or_404(Produk, id_produk=id)
    # Menghapus data dari database
    obj.delete()
    # Kembali ke halaman daftar produk
    return redirect('produk_list')