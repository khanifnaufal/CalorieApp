📊 Aplikasi Hitung Kalori Harian (TDEE Calculator)

Aplikasi desktop sederhana yang dibangun dengan Python dan CustomTkinter untuk menghitung perkiraan Basal Metabolic Rate (BMR) dan Total Daily Energy Expenditure (TDEE), menggunakan rumus Mifflin-St Jeor.

Proyek ini bertujuan untuk mendemonstrasikan kemampuan pengembangan aplikasi full-stack mini, penggunaan library GUI modern, dan pemisahan logika bisnis (di calculator.py) dari antarmuka pengguna (di gui_app.py).

✨ Fitur Utama

Perhitungan Akurat: Menggunakan rumus Mifflin-St Jeor untuk BMR, yang dianggap lebih akurat dibandingkan rumus lama.

Penyesuaian TDEE: Hasil BMR disesuaikan dengan level aktivitas (Sedentari, Ringan, Sedang, Berat, Sangat Berat) untuk mendapatkan TDEE.

Validasi Input: Menangani error dan memberikan peringatan jika input yang dimasukkan tidak valid (bukan angka atau angka negatif).

UI Modern: Menggunakan CustomTkinter untuk tampilan yang bersih, flat design, dan responsif terhadap tema sistem (gelap/terang).

🛠️ Teknologi yang Digunakan

Bahasa Pemrograman: Python

Antarmuka Pengguna (GUI): CustomTkinter (Ekstensi modern dari Tkinter)

Pengemasan (Opsional): PyInstaller (untuk membuat file .exe mandiri)

🚀 Cara Menjalankan Aplikasi

Ikuti langkah-langkah berikut untuk mengunduh dan menjalankan aplikasi ini secara lokal.

1. Kloning Repositori

git clone https://github.com/khanifnaufal/CalorieApp.git
cd CALORIE_APP


2. Instalasi Dependensi

Proyek ini hanya membutuhkan customtkinter.

pip install customtkinter


3. Eksekusi Aplikasi

Jalankan file utama gui_app.py di terminal Anda:

python gui_app.py


📦 Mengemas Menjadi File .EXE (Windows)

Jika Anda ingin membuat file executable yang dapat dijalankan tanpa perlu menginstal Python, ikuti langkah berikut (membutuhkan PyInstaller):

1. Instal PyInstaller

pip install pyinstaller


2. Kompilasi

Jalankan perintah pengemasan dari direktori proyek:

pyinstaller --onefile --windowed [.py


Dibuat dengan ❤️ oleh [Nama/Username Anda]