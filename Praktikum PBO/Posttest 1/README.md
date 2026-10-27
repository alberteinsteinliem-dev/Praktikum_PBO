# Laporan & Dokumentasi Program Sistem Manajemen Event dan Lomba (OOP Python) 
Dokumentasi ini dibuat untuk menjelaskan struktur program, implementasi materi Object-Oriented Programming (OOP), serta panduan pengujian program Sistem Manajemen Pendaftaran Event dan Lomba. Program ini dibuat menggunakan bahasa Pemrograman Python berbasis pendekatan OOP.

## 1. Penjelasan Program
Program ini dirancang untuk mensimulasikan sistem registrasi event/lomba secara digital. Sistem ini memungkinkan pengguna untuk:
* Mendaftarkan akun peserta dan mengelola saldo digital.
* Mengelola data event/lomba serta ketersediaan kuotanya.
* Memproses pendaftaran peserta ke lomba yang dipilih.
* Melakukan pembayaran transaksi menggunakan PIN validasi dan pemotongan saldo.

## 2. Implementasi Modul OOP

### Modul 1: Class & Object
Program menggunakan 4 class utama yang saling berinteraksi:
1. `Peserta` — Memodelkan data diri pengguna dan saldo.
2. `Lomba` — Memodelkan informasi event/lomba, biaya, dan kuota.
3. `Pendaftaran` — Menghubungkan objek `Peserta` dan `Lomba` untuk proses validasi registrasi.
4. `Transaksi` — Mengelola verifikasi keamanan (PIN) dan pembayaran akhir.

### Modul 2: Atribut & Method
1. **Atribut Kelas**:
   * `Peserta.nama_instansi`, `Peserta.total_peserta`, `Peserta.minimal_usia`
   * `Lomba.daftar_lomba`, `Lomba.total_lomba`, `Lomba.biaya_admin`
   * `Pendaftaran.total_pendaftaran`, `Pendaftaran.status_default`, `Pendaftaran.kategori_pendaftaran`
   * `Transaksi.total_transaksi`, `Transaksi.pajak`, `Transaksi.mata_uang`
2. **Atribut Instance**:
   * Public: `nama`, `email`, `nama_lomba`, `peserta`, `lomba`.
   * Private: `__saldo`, `__biaya`, `__kuota`, `__status`, `__pin`, `__jumlah_bayar`.
3. **Jenis Method**:
   * **Instance Method**: `tampilkan_profil()`, `kurangi_kuota()`, `proses_pendaftaran()`, `bayar()`.
   * **Class Method (`@classmethod`)**: `buat_dari_dict()`, `cari_lomba()`, `ubah_kategori()`, `set_pajak()`.
   * **Static Method (`@staticmethod`)**: `validasi_email()`, `hitung_total_biaya()`, `buat_kode_daftar()`, `cetak_struk()`.

### Modul 3: Encapsulation & Property
* Pembungkusan atribut sensitif/kritis menggunakan akses privat (`__`).
* Implementasi **Getter** (`@property`) untuk membaca nilai private.
* Implementasi **Setter** (`@<nama_properti>.setter`) untuk memperbarui nilai private dengan validasi data (menolak nilai negatif, tipe data salah, atau nilai di luar batas konvensi).

## 3. Struktur Class & Relasi Objek

| Nama Class | Atribut Private | Getter & Setter | Fungsi Utama |
| :--- | :--- | :--- | :--- |
| **Peserta** | `__saldo` | `saldo` | Mengelola data peserta dan saldo digital. |
| **Lomba** | `__biaya`, `__kuota` | `biaya`, `kuota` | Mengelola data event, biaya dasar, dan stok kuota. |
| **Pendaftaran** | `__status` | `status` | Memvalidasi kecukupan saldo & kuota peserta. |
| **Transaksi** | `__pin`, `__jumlah_bayar` | `jumlah_bayar` | Memverifikasi PIN dan melakukan pemotongan saldo. |

## 4. Panduan Pengujian Program
### Cara Menjalankan Program
Pastikan Python sudah terinstal di perangkat kamu, lalu jalankan perintah berikut di terminal:
```bash
python nama_file.py
