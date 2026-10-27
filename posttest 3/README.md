# Portal Event Mahasiswa - Sistem Pendaftaran & Transaksi Lomba

Aplikasi ini adalah sistem pengelolaan pendaftaran dan transaksi lomba berbasis Pemrograman Berorientasi Objek (OOP) dengan Python. Sistem ini menangani pendataan peserta, pembedaan jenis lomba, alur pendaftaran, pembayaran berbasis saldo dan PIN, pencetakan struk, hingga pengiriman notifikasi otomatis.

---

## 1. Class Diagram & Penjelasan Relasi UML

### Class Diagram
![Class Diagram](Untitled Diagram.drawio)

### Penjelasan Relasi Antar Kelas:

* **Agregasi (Pendaftaran ──◇ Peserta & Lomba)**
  Kelas `Pendaftaran` menerima objek `Peserta` dan `Lomba` dari luar. Kedua objek ini berdiri sendiri, sehingga jika data pendaftaran dihapus, data peserta dan data lomba tetap ada di sistem.

* **Komposisi (Transaksi ──◆ Struk)**
  Objek `Struk` dibuat langsung di dalam fungsi pembentuk (`__init__`) milik kelas `Transaksi`. Keberadaan struk bergantung penuh pada transaksi; jika transaksi dihapus, objek struk juga otomatis hancur.

* **Asosiasi (Transaksi ──> Pendaftaran)**
  Kelas `Transaksi` terhubung ke kelas `Pendaftaran` untuk mengecek ketersediaan kuota, memeriksa kecukupan saldo, dan memperbarui status pendaftaran menjadi LUNAS.

---

## 2. Penerapan Abstraksi (Abstract Base Class)

* **Abstract Class (`Lomba`)**: Menggunakan modul `abc` agar kelas `Lomba` hanya menjadi cetakan utama dan tidak bisa diinstansiasi secara langsung.
* **Abstract Method**:
  1. `tampilkan_info()`: Wajib diisi oleh tiap subclass untuk menampilkan rincian lomba.
  2. `hitung_biaya_akhir()`: Wajib diisi oleh tiap subclass untuk menghitung total biaya setelah diskon atau tambahan biaya.
* **Subclass**: Kelas `LombaAkademik` dan `LombaNonAkademik` mengimplementasikan kedua method abstrak di atas dengan aturan perhitungannya masing-masing.
* **Method Konkret**: Method `kurangi_kuota()` ada di kelas induk `Lomba` dan digunakan bersama oleh semua subclass untuk mengurangi sisa kuota lomba.

---

## 3. Penerapan Polimorfisme

* **Polimorfisme via Pewarisan**: Method `tampilkan_info()` di-override oleh `LombaAkademik` dan `LombaNonAkademik`. Pemanggilannya dilakukan secara fleksibel menggunakan satu perulangan `for`.
* **Duck Typing**: Terdapat kelas `NotifikasiEmail` dan `NotifikasiSMS` yang berdiri sendiri tanpa induk yang sama, namun keduanya memiliki method `kirim()`. Keduanya dipanggil melalui satu fungsi umum `kirim_pemberitahuan()`.
* **Operator Overloading**:
  * `__str__`: Mengubah bentuk objek lomba menjadi teks nama dan harganya.
  * `__gt__`: Membandingkan mana lomba yang harganya lebih mahal (`lomba1 > lomba2`).
  * `__add__`: Memudahkan fitur isi ulang saldo peserta (`peserta1 + 25000`).

---

## 4. Bukti Output Program

Berikut adalah hasil eksekusi program dari terminal:

```text
==================================================
      DEMONSTRASI PROGRAM OOP
==================================================

--- 1. BUKTI ABSTRAKSI (ABSTRACT CLASS CANNOT BE INSTANTIATED) ---
[SUCCESS CHECK] Gagal instansiasi Lomba! TypeError terdeteksi:
Error: Can't instantiate abstract class Lomba with abstract methods hitung_biaya_akhir, tampilkan_info

--- 2. POLIMORFISME VIA PEWARISAN (LOOP SUBCLASS) ---
Memanggil tampilkan_info() lewat loop terpadu:
[Akademik - Informatika] KTI Nasional | Biaya Dasar: Rp 20000.0 | Biaya Akhir: Rp 18000.0 | Sisa Kuota: 2
[Non-Akademik @ GOR Mulawarman] Futsal Cup | Biaya Dasar: Rp 15000.0 | Biaya Akhir: Rp 15000.0 | Sisa Kuota: 1

--- 3. OPERATOR OVERLOADING ---
Apakah 'KTI Nasional' lebih mahal dari 'Futsal Cup'? True
String representation lomba1: KTI Nasional (Biaya: Rp 20000.0)
[SUKSES] Top-up Rp 25000 berhasil. Saldo Adri sekarang: Rp 175000.0

--- 4. DUCK TYPING ---
Memanggil kirim_pemberitahuan() untuk dua kelas berbeda:
[EMAIL -> adri@gmail.com] Pendaftaran Anda Berhasil!
[WHATSAPP -> 08123456789] Tiket Lomba Anda Sudah Aktif!

--- 5. PROSES PENDAFTARAN & TRANSAKSI ---
[TRANSAKSI SUKSES] Pembayaran berhasil untuk Adri

-----------------------------------
         STRUK PEMBAYARAN          
-----------------------------------
Nama  : Adri
Event : KTI Nasional
Total : Rp 23000.0
-----------------------------------

--- REKAP ATRIBUT KELAS ---
Total Peserta  : 1
Total Lomba    : 2
Total Transaksi: 1

5. Prinsip SOLID
Single Responsibility Principle (SRP): Kelas Transaksi fokus mengurus pembayaran, sedangkan urusan format cetak tampilan diserahkan ke kelas Struk.

Open/Closed Principle (OCP): Jika ingin menambah jenis lomba baru (misal LombaSeni), kita cukup membuat subclass baru tanpa perlu mengedit kode di kelas Lomba.

Dependency Inversion Principle (DIP): Kelas Pendaftaran menerima objek berbasis abstrak Lomba, bukan terikat mati pada salah satu jenis lomba saja.
