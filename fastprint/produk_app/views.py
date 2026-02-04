from django.shortcuts import render, redirect, get_object_or_404
from .models import Produk
from .forms import ProdukForm


def produk_list(request):
    
    data = Produk.objects.filter(status__nama_status='bisa dijual')
    return render(request, 'produk_app/list_produk.html', {'produk': data})

def produk_tidak_bisa_dijual(request):
   
    data = Produk.objects.exclude(status__nama_status='bisa dijual')
    return render(request, 'produk_app/list_produk.html', {
        'produk': data,
        'title_page': 'Daftar Produk (Tidak Bisa Dijual)',
        'is_archive': True
    })

def produk_add(request):
    if request.method == "POST":
        form = ProdukForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm()
    return render(request, 'produk_app/form_produk.html', {'form': form, 'title': 'Tambah Produk'})

def produk_edit(request, id):
    obj = get_object_or_404(Produk, id_produk=id)
    if request.method == "POST":
        form = ProdukForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('produk_list')
    else:
        form = ProdukForm(instance=obj)
    return render(request, 'produk_app/form_produk.html', {'form': form, 'title': 'Edit Produk'})

def produk_delete(request, id):
    obj = get_object_or_404(Produk, id_produk=id)
    obj.delete()
    return redirect('produk_list')