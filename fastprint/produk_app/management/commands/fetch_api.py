from django.core.management.base import BaseCommand
from datetime import datetime
import requests, hashlib
from produk_app.models import Produk, Kategori, Status

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
        now = datetime.now()
        
        username = f"tesprogrammer{now.strftime('%d%m%y')}C{now.strftime('%H')}"
        password_raw = f"bisacoding-{now.strftime('%d-%m-%y')}"
        password = hashlib.md5(password_raw.encode()).hexdigest()

        try:
            response = requests.post(url, data={'username': username, 'password': password})
            result = response.json()

            if result.get('error') == 0:
                for item in result['data']:
                   
                    nama_kat = item.get('kategori') or "Lainnya"
                    nama_stat = item.get('status') or "tidak bisa dijual"

                  
                    kat_obj, _ = Kategori.objects.get_or_create(nama_kategori=nama_kat)
                    stat_obj, _ = Status.objects.get_or_create(nama_status=nama_stat)
                    
                  
                    Produk.objects.update_or_create(
                        id_produk=item['id_produk'],
                        defaults={
                            'nama_produk': item['nama_produk'],
                            'harga': int(item['harga']),
                            'kategori': kat_obj, 
                            'status': stat_obj  
                        }
                    )
                self.stdout.write(self.style.SUCCESS("Data berhasil ditarik dan ID terisi otomatis!"))
            else:
                self.stdout.write(self.style.ERROR(f"Auth Gagal: {result.get('ket')}"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error: {str(e)}"))