from django import forms
from .models import Produk

# Form ini digunakan untuk memproses input data produk
class ProdukForm(forms.ModelForm):
    class Meta:
        # Menghubungkan form ini secara otomatis dengan model Produk
        model = Produk
        
        # Menentukan field (kolom) apa saja yang akan ditampilkan di dalam form
        fields = ['nama_produk', 'harga', 'kategori', 'status']
        
        # Widgets digunakan untuk mengatur tampilan elemen HTML
        widgets = {
            # Menambahkan class Bootstrap 'form-control'
            'nama_produk': forms.TextInput(attrs={'class': 'form-control'}),
            'harga': forms.NumberInput(attrs={'class': 'form-control'}),
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }