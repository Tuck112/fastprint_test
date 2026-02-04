from django.urls import path
from . import views

urlpatterns = [
    path('', views.produk_list, name='produk_list'),
    path('arsip/', views.produk_tidak_bisa_dijual, name='produk_tidak_dijual'),
    path('tambah/', views.produk_add, name='produk_add'),
    path('edit/<int:id>/', views.produk_edit, name='produk_edit'),
    path('hapus/<int:id>/', views.produk_delete, name='produk_delete'),
]