# UAS - Laporan Analisis Sistem Todo-List Django

| Nama         | : Fajar Bayu Timur |
|--------------|---------------|
| NIM          | : 32231003  |
| Program Studi| : Teknik Informatika |
| Semester     | : 3 (Tiga) |

## 1. Pendahuluan

### 1.1 Latar Belakang
Sistem ini merupakan implementasi todo-list menggunakan framework Django. Django dipilih karena merupakan framework Python yang powerful untuk pengembangan web dengan arsitektur MVT (Model-View-Template).

### 1.2 Tujuan
Tujuan dari sistem ini adalah untuk menyediakan manajemen task yang efektif dengan fitur kategorisasi dan komentar.

## 2. Arsitektur Sistem

### 2.1 Teknologi yang Digunakan
- Framework: Django 5.1.5
- Database: SQLite3
- Frontend: Bootstrap 4
- Template Engine: Django Template Language (DTL)
- Package: django-widget-tweaks

### 2.2 Struktur Database
1. Model Category
   - Fungsi: Mengelompokkan task
   - Fields: name, description, created_at
   - Relasi: One-to-Many dengan Task

2. Model Task
   - Fungsi: Menyimpan data tugas
   - Fields: title, description, status, category, created_at, updated_at
   - Relasi: Many-to-One dengan Category, One-to-Many dengan Comment

3. Model Comment
   - Fungsi: Menyimpan komentar task
   - Fields: task, content, created_at
   - Relasi: Many-to-One dengan Task

## 3. Alur Program

### 3.1 Alur Task
1. Melihat Daftar Task
   - URL: `/`
   - View: `index_view()`
   - Template: `index.html`

2. Membuat Task Baru
   - URL: `/create`
   - View: `create_view()`
   - Template: `form.html`

3. Melihat Detail Task
   - URL: `/<task_id>`
   - View: `detail_view()`
   - Template: `detail.html`

4. Mengubah Task
   - URL: `/update/<task_id>`
   - View: `update_view()`

5. Menghapus Task
   - URL: `/delete/<task_id>`
   - View: `delete_view()`

### 3.2 Alur Category
1. Melihat Daftar Kategori
   - URL: `/categories/`
   - View: `category_list()`
   - Template: `category/index.html`

2. Operasi CRUD Kategori
   - Create: `/categories/create/`
   - Read: `/categories/<category_id>/`
   - Update: `/categories/<category_id>/update/`
   - Delete: `/categories/<category_id>/delete/`

### 3.3 Alur Comment
1. Menambah Komentar
   - URL: `/task/<task_id>/comment/add/`
   - View: `comment_create()`
   - Template: `comment/form.html`

2. Mengubah & Menghapus Komentar
   - Update: `/comment/<comment_id>/update/`
   - Delete: `/comment/<comment_id>/delete/`

## 4. Fitur Utama

### 4.1 Manajemen Task
- CRUD operasi untuk task
- Perubahan status task
- Kategorisasi task
- Tracking waktu

### 4.2 Kategorisasi
- Pengelompokan task
- Manajemen kategori
- View task per kategori

### 4.3 Sistem Komentar
- Menambah komentar
- Mengubah komentar
- Menghapus komentar

### 4.4 Interface
- Sidebar navigasi
- Responsive design
- Form validation
- Flash messages

## 5. Kesimpulan
Sistem todo-list ini menyediakan manajemen task yang efektif dengan fitur kategorisasi dan komentar. Arsitektur modular memungkinkan pengembangan lebih lanjut, sementara interface yang user-friendly memudahkan penggunaan sistem.