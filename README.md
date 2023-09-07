Link adaptable:
https://homeworkreminderz.adaptable.app/main/

# Panduan Implementasi

## Persiapan
Pertama-tama, saya memastikan bahwa saya memiliki semua yang dibutuhkan untuk mengimplementasikan proyek ini. Berikut adalah langkah-langkah yang perlu saya lakukan:

### 1. Setup Library yang Dibutuhkan
Langkah pertama adalah membuat file `requirements.txt` yang berisi daftar library yang diperlukan untuk proyek ini. Saya dapat membuatnya dengan menambahkan library berikut ke dalam file tersebut:

```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```

Setelah itu, saya dapat menginstal semua library ini dengan menjalankan perintah berikut di terminal:

#### Tanpa Virtual Environment
```sh
pip install -r requirements.txt
```

#### Menggunakan Virtual Environment
```sh
python -m venv venv # Buat virtual env
./venv/Scripts/activate # pada Windows atau
source venv/Scripts/activate # pada Mac
pip install -r requirements.txt
```

## 2. Membuat Proyek Django Baru
Selanjutnya, saya perlu membuat proyek Django baru. Saya dapat melakukannya dengan menggunakan perintah `django-admin createproject NAMA_PROYEK`. Ini akan membuat direktori baru dengan nama `NAMA_PROYEK`, yang akan berisi file `manage.py` dan folder `NAMA_PROYEK` yang berisi pengaturan dan routing proyek.

Saya dapat menjalankan proyek dengan perintah `python manage.py runserver`. Pastikan untuk menjalankannya sebelum mengakses `http://localhost:8000/hello`, yang merupakan URL web Django saya.

## 3. Membuat Aplikasi "main"
Selanjutnya, saya perlu membuat aplikasi dengan nama "main" di dalam proyek saya. Saya dapat melakukannya dengan perintah `python manage.py createapp NAMA_APLIKASI`. Setelah membuat aplikasi, saya perlu mendaftarkannya di dalam file `settings.py` yang berada di dalam folder proyek. Saya tambahkan nama aplikasi tersebut ke dalam `INSTALLED_APPS` seperti ini:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'NAMA_APLIKASI'
]
```

## 4. Konfigurasi Routing Proyek
Untuk menjalankan aplikasi yang telah saya buat, saya perlu mengkonfigurasi routing proyek saya. Saya menambahkan path yang mengarah ke aplikasi tersebut di dalam file `urls.py` yang berada di dalam direktori proyek. Contohnya, jika saya ingin menggunakan path `/iniapp` untuk aplikasi "main", saya tambahkan ini ke dalam `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('iniapp/', include('main.urls'))
]
```

Selanjutnya, saya buat file `urls.py` di dalam folder "main" dengan kode berikut:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello),
]
```

Dengan konfigurasi ini, ketika saya mengakses `http://localhost:8000/iniapp/hello` di browser, saya akan melihat apa yang dikembalikan oleh fungsi `hello` yang ada di dalam file `views.py`.

Jika saya ingin aplikasi saya berada langsung di path utama, seperti `http://localhost:8000/hello`, saya bisa mengatur `urlpatterns` di dalam file `urls.py` proyek dengan cara ini:

```python
path('', include('main.urls'))
```

## 5. Membuat Fungsi Render pada views.py
Untuk mengatur tampilan yang akan dilihat oleh pengguna ketika mengakses `http://localhost:8000/hello`, saya perlu membuat halaman HTML. Saya buat direktori `templates` di dalam folder "main" dan tambahkan file HTML yang akan saya tampilkan, misalnya `hello.html`. Isi file `hello.html` dengan kode berikut:

```html
<head>
    <title>Trading Inventory</title>
</head>
<body>
    <h1>Nama : Eryawan Presma Yulianrifat</h1>
    <h1>Kelas : PBP D</h1>
</body>
```

Kemudian, di dalam file `views.py`, saya dapat mengembalikan halaman HTML tersebut dengan menggunakan fungsi `render` seperti ini:

```python
from django.shortcuts import render

def hello(request):
    return render(request, 'hello.html')
```

Perubahan ini akan langsung terlihat ketika saya mengakses `http://localhost:8000/hello`.

## 6. Membuat Model Sebagai Database
Jika saya ingin menggunakan database, saya perlu membuat model yang akan menjadi penghubung antara Python dan database saya. Model ini akan berada di dalam file `models.py` di dalam aplikasi "main". Sebagai contoh, jika saya ingin membuat database yang berisi informasi tentang barang dengan atribut nama, jumlah, dan deskripsi, saya dapat membuat model seperti ini:

```python
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    description = models.TextField()
```

Namun, untuk menghubungkan model ini dengan tampilan, saya perlu melakukan lebih banyak konfigurasi yang akan dibahas dalam tutorial PBP selanjutnya.

## 7. Melakukan Deploy ke Adaptable
Terakhir, jika saya ingin mendeploy proyek saya ke Adaptable, pastikan repositori proyek saya sudah berada di GitHub dan bersifat public. Selanjutnya, di Adaptable, pilih opsi "deploy a new app" dan pilih repositori yang sesuai dengan proyek yang akan saya deploy. Pilih template "Python App Template" dan tentukan jenis database yang saya inginkan, misalnya "PostgreSQL".

Pastikan untuk sesuaikan versi Python dengan versi yang digunakan di lingkungan lokal saya dengan menjalankan `python --version` di terminal lokal. Selanjutnya, masukkan perintah `python manage.py migrate && gunicorn NAMA_PROYEK.wsgi` ke dalam kolom "Start Command". Akhirnya, tentukan nama aplikasi saya dan centang opsi "HTTP Listener on PORT".

![alt text](images/tugas2pbp.png)

Ketika ada permintaan dari luar, Django akan mencoba mencari pola URL yang ada dalam file urls.py. Setelah menemukan pola URL yang sesuai dengan yang telah kita tulis, Django akan mengakses fungsi yang sesuai dalam file views.py sesuai dengan pola URL yang dituju. Di dalam fungsi yang dipanggil, kita memiliki kemampuan untuk menulis, membaca, menghapus, dan memperbarui basis data. Setelah itu, kita dapat mengirimkan halaman HTML yang akan dirender oleh browser pengguna.

Virtual environment digunakan untuk mengisolasi dependensi proyek, mencegah konflik, menjaga kebersihan sistem, dan memungkinkan portabilitas. Meskipun mungkin bisa membuat aplikasi web Django tanpa virtual environment, secara umum virutal environment digunakan untuk mencegah masalah dependensi dan konflik.


MVC (Model-View-Controller): Memisahkan data (Model), tampilan (View), dan logika pengendalian (Controller).
MVT (Model-View-Template): Sama seperti MVC, dengan Template yang memisahkan tampilan.
MVVM (Model-View-ViewModel): Memisahkan Model, tampilan (View), dan ViewModel yang menghubungkan keduanya, umumnya digunakan dalam aplikasi UI dinamis seperti aplikasi mobile.