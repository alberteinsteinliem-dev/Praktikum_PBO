# Portal Event Mahasiswa - System Pendaftaran & Transaksi Lomba (OOP Python) 

Proyek ini merupakan implementasi program berbasis **Object-Oriented Programming (OOP)** menggunakan bahasa Python. Sistem ini dirancang untuk mengelola proses pendaftaran dan pembayaran lomba/event mahasiswa dengan menerapkan konsep **Relasi UML** dan **Inheritance (Pewarisan)** secara penuh sesuai dengan standar modul pemrograman.

---

## 🛠️ Fitur & Konsep OOP yang Diterapkan

### 1. Encapsulation & Validasi Data (Getter & Setter)
* **Private Attributes (`__`)**: Digunakan untuk melindungi data sensitif seperti `__saldo` pada `Peserta`, `__status` pada `Pendaftaran`, serta `__pin` dan `__jumlah_bayar` pada `Transaksi`.
* **Property Decorator (`@property` & `@<property>.setter`)**: Memastikan validasi data berjalan sebelum atribut diubah (misalnya pengecekan saldo/biaya bernilai positif, variabel tipe angka, serta status pendaftaran yang valid).

---

### 2. Inheritance (Pewarisan Class)
* **Superclass**: `Lomba` bertindak sebagai kelas induk yang menyimpan atribut dan metode umum (seperti `nama_lomba`, `_biaya`, `_kuota`).
* **Subclass**:
  * `LombaAkademik`: Memiliki atribut unik `bidang_studi`.
  * `LombaNonAkademik`: Memiliki atribut unik `lokasi_venue`.
* **Penggunaan `super()`**: Kedua subclass memanggil konstruktor milik parent class menggunakan `super().__init__(nama_lomba, biaya, kuota)`.
* **Protected Access Modifier (`_`)**: Atribut `_biaya` dan `_kuota` menggunakan awalan satu garis bawah `_` pada kelas `Lomba` agar dapat diakses dan diolah langsung oleh subclass-nya.
* **Method Overriding**: Method `tampilkan_info()` dari kelas `Lomba` didefinisikan ulang (*override*) pada masing-masing subclass untuk menampilkan format data spesifik.

---

### 3. Relasi UML

+-------------------+                  +---------------------+
 |      Peserta      |                  |        Lomba        |
 +-------------------+                  +---------------------+
           ^                                       ^
           | (1)                                   | (1)
           |                                       |
           +---------------[ Agregasi ]------------+
                                 |
                                 v (*)
                        +-----------------+
                        |   Pendaftaran   |
                        +-----------------+
                                 ^
                                 | (1)
                             [Asosiasi]
                                 |
                                 v (*)
                        +-----------------+
                        |    Transaksi    |
                        +-----------------+
                                 |
                            [Komposisi] (1:1)
                                 |
                                 v
                        +-----------------+
                        |      Struk      |
                        +-----------------+

* **Agregasi**:
  * Terjadi antara kelas `Pendaftaran` dengan `Peserta` & `Lomba`.
  * Objek `Peserta` dan `Lomba` dibuat secara independen di luar dan dimasukkan ke dalam `Pendaftaran`. Jika objek `Pendaftaran` dihapus, data `Peserta` dan `Lomba` tetap ada.
* **Asosiasi**:
  * Terjadi antara kelas `Transaksi` dan `Pendaftaran`.
  * Objek `Transaksi` terhubung dengan `Pendaftaran` untuk mengeksekusi validasi status dan pemotongan saldo.
* **Komposisi**:
  * Terjadi antara kelas `Transaksi` dan `Struk`.
  * Objek `Struk` diciptakan secara internal di dalam konstruktor `Transaksi`. `Struk` bergantung penuh pada siklus hidup `Transaksi`.

---

## 📁 Struktur Kelas

| Kelas | Tipe/Peran | Deskripsi Utama |
| :--- | :--- | :--- |
| **`Peserta`** | Independent Class | Mengelola identitas peserta, validasi format email, dan verifikasi saldo. |
| **`Lomba`** | Superclass (Parent) | Kelas induk untuk event/lomba dengan fungsi pencarian dan manajemen kuota. |
| **`LombaAkademik`** | Subclass (Child) | Turunan `Lomba` untuk kompetisi akademik (memiliki `bidang_studi`). |
| **`LombaNonAkademik`**| Subclass (Child) | Turunan `Lomba` untuk kompetisi non-akademik (memiliki `lokasi_venue`). |
| **`Pendaftaran`** | Aggregator Class | Mengintegrasikan peserta dan lomba serta memverifikasi sisa kuota. |
| **`Struk`** | Component Class | Dicetak sebagai bukti pembayaran fisik/digital. |
| **`Transaksi`** | Composite Class | Memproses verifikasi PIN, eksekusi pendaftaran, pemotongan saldo, dan penerbitan `Struk`. |

---

## 🚀 Alur Kerja Sistem (Workflow)

1. **Inisialisasi Data**:
   * Membuat objek `Peserta` (bisa via konstruktor biasa atau kelas metode `buat_dari_dict`).
   * Membuat objek dari subclass `LombaAkademik` atau `LombaNonAkademik`.
2. **Proses Pendaftaran (Agregasi)**:
   * Menghubungkan objek `Peserta` dan `Lomba` ke dalam objek `Pendaftaran`. Status awal otomatis bernilai `"PENDING"`.
3. **Pembentukan Transaksi (Asosiasi & Komposisi)**:
   * Membuat objek `Transaksi` berbasis `Pendaftaran`.
   * Secara otomatis mengkalkulasi total biaya (Biaya Lomba + Biaya Admin) dan membentuk objek `Struk`.
4. **Verifikasi & Eksekusi Pembayaran**:
   * Pengguna memasukkan PIN keamanan.
   * Sistem mengecek kecocokan PIN.
   * Jika PIN sesuai, kelas `Pendaftaran` memverifikasi ketersediaan kuota dan kesesuaian saldo.
   * Jika memenuhi syarat, kuota lomba dikurangi, status pendaftaran berubah menjadi `"LUNAS"`, saldo peserta dipotong, dan struk pembayaran dapat dicetak.

---

## 💻 Cara Menjalankan Program

### Prasyarat
* Python 3.x telah terinstal di perangkat Anda.

### Langkah Eksekusi
1. Simpan kode ke dalam file bernama `main.py`.
2. Buka terminal/command prompt pada direktori tempat file disimpan.
3. Jalankan perintah berikut:

```bash
python main.py

📤 Contoh Output Konsol

=== DEMONSTRASI PROGRAM OOP (UML & INHERITANCE) ===

--- 1. Membuat Objek Peserta & Subclass Lomba ---
[SUKSES] Saldo Adri diperbarui menjadi: Rp 150000.0
[SUKSES] Saldo Azril diperbarui menjadi: Rp 50000.0

--- 2. Pengujian Method Overriding ---
[Akademik - Informatika] KTI Nasional | Biaya: Rp 20000.0 | Sisa Kuota: 2
[Non-Akademik @ GOR Mulawarman] Futsal Cup | Biaya: Rp 15000.0 | Sisa Kuota: 1

--- 3. Pendaftaran & Transaksi (Agregasi & Asosiasi) ---

--- 4. Eksekusi Pembayaran & Cetak Struk (Komposisi) ---
[INFO] Status pendaftaran Adri diubah ke: LUNAS
[TRANSAKSI SUKSES] Pembayaran berhasil untuk Adri

-----------------------------------
        STRUK PEMBAYARAN           
-----------------------------------
Nama  : Adri
Event : KTI Nasional
Total : Rp 25000.0
-----------------------------------

--- 5. Rekap Atribut Kelas ---
Nama Instansi  : Portal Event Mahasiswa
Total Peserta  : 2
Total Lomba    : 2
Total Transaksi: 1
