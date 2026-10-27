from abc import ABC, abstractmethod

# 1. ENKAPSULASI & OPERATOR OVERLOADING
class Peserta:
    nama_instansi = "Portal Event Mahasiswa"
    total_peserta = 0

    def __init__(self, nama, email, saldo):
        self.nama = nama
        self.email = email
        self.__saldo = 0.0
        self.saldo = saldo
        Peserta.total_peserta += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):
        if not isinstance(nilai, (int, float)):
            print(f"[GAGAL] Saldo harus berupa angka! (Input: {nilai})")
            return
        if nilai < 0:
            print(f"[GAGAL] Saldo tidak boleh negatif! (Input: {nilai})")
            return
        self.__saldo = float(nilai)

    def tampilkan_profil(self):
        print(f"Peserta: {self.nama} | Email: {self.email} | Saldo: Rp {self.saldo:,.2f}")

    @classmethod
    def buat_dari_dict(cls, data):
        return cls(data["nama"], data["email"], data["saldo"])

    @staticmethod
    def validasi_email(email):
        return "@" in email and "." in email

    def __str__(self):
        return f"Peserta({self.nama}, {self.email}, Saldo: Rp {self.saldo:,.0f})"

    def __add__(self, other):
        """Operator + untuk menggabungkan saldo dua peserta"""
        if isinstance(other, Peserta):
            return self.saldo + other.saldo
        elif isinstance(other, (int, float)):
            return self.saldo + other
        return NotImplemented

    def __gt__(self, other):
        """Operator > untuk membandingkan saldo antar peserta"""
        if isinstance(other, Peserta):
            return self.saldo > other.saldo
        return NotImplemented

class Lomba(ABC):
    daftar_lomba = []
    total_lomba = 0
    biaya_admin = 5000.0

    def __init__(self, nama_lomba, biaya, kuota):
        self.nama_lomba = nama_lomba
        self._biaya = 0.0
        self._kuota = 0

        self.biaya = biaya
        self.kuota = kuota

        Lomba.daftar_lomba.append(self)
        Lomba.total_lomba += 1

    @property
    def biaya(self):
        return self._biaya

    @biaya.setter
    def biaya(self, nilai):
        if nilai < 0:
            print(f"[GAGAL] Biaya lomba '{self.nama_lomba}' tidak boleh negatif!")
            return
        self._biaya = float(nilai)

    @property
    def kuota(self):
        return self._kuota

    @kuota.setter
    def kuota(self, nilai):
        if nilai < 0:
            print(f"[GAGAL] Kuota lomba '{self.nama_lomba}' tidak boleh negatif!")
            return
        self._kuota = int(nilai)

    def kurangi_kuota(self):
        """Method konkret untuk mengurangi kuota saat ada pendaftaran berhasil"""
        if self._kuota > 0:
            self._kuota -= 1
            return True
        return False

    def proses_persiapan_lomba(self):
        """Method konkret bersama untuk inisialisasi persiapan event"""
        print(f"[PERSIAPAN] Mempersiapkan sarana & logistik untuk event: {self.nama_lomba}")

    @abstractmethod
    def tampilkan_info(self):
        """Abstract Method 1: Menampilkan informasi detail spesifik lomba"""
        pass

    @abstractmethod
    def hitung_biaya_tambahan(self):
        """Abstract Method 2: Kalkulasi biaya tambahan (fasilitas/venue)"""
        pass

class LombaAkademik(Lomba):
    def __init__(self, nama_lomba, biaya, kuota, bidang_studi):
        super().__init__(nama_lomba, biaya, kuota)
        self.bidang_studi = bidang_studi

    def tampilkan_info(self):
        print(f"[Akademik - {self.bidang_studi}] {self.nama_lomba} | Biaya Dasar: Rp {self.biaya:,.0f} | Sisa Kuota: {self.kuota}")

    def hitung_biaya_tambahan(self):
        biaya_sertifikat = 10000.0
        return biaya_sertifikat


class LombaNonAkademik(Lomba):
    def __init__(self, nama_lomba, biaya, kuota, lokasi_venue):
        super().__init__(nama_lomba, biaya, kuota)
        self.lokasi_venue = lokasi_venue

    def tampilkan_info(self):
        print(f"[Non-Akademik @ {self.lokasi_venue}] {self.nama_lomba} | Biaya Dasar: Rp {self.biaya:,.0f} | Sisa Kuota: {self.kuota}")

    def hitung_biaya_tambahan(self):
        biaya_sewa_venue = 25000.0
        return biaya_sewa_venue
    
# 2. DUCK TYPING (TIDAK ADA HUBUNGAN PEWARISAN)
class NotifikasiEmail:
    def kirim_notifikasi(self, penerima, pesan):
        print(f"[EMAIL -> {penerima}]: {pesan}")


class NotifikasiSMS:
    def kirim_notifikasi(self, penerima, pesan):
        print(f"[SMS -> {penerima}]: {pesan}")

def kirim_notifikasi_sistem(kanal_notifikasi, penerima, pesan):
    """Memanggil method 'kirim_notifikasi' tanpa peduli tipe kelasnya"""
    kanal_notifikasi.kirim_notifikasi(penerima, pesan)

# 3. RELASI UML: AGREGASI, KOMPOSISI, ASOSIASI
class Struk:
    def __init__(self, nama, event, total):
        self.nama = nama
        self.event = event
        self.total = total

    def cetak(self):
        print("-----------------------------------")
        print("         STRUK PEMBAYARAN          ")
        print("-----------------------------------")
        print(f"Nama  : {self.nama}")
        print(f"Event : {self.event}")
        print(f"Total : Rp {self.total:,.2f}")
        print("-----------------------------------\n")

class Pendaftaran:
    total_pendaftaran = 0
    status_default = "PENDING"

    def __init__(self, peserta, lomba):
        self.peserta = peserta
        self.lomba = lomba
        self.__status = Pendaftaran.status_default
        Pendaftaran.total_pendaftaran += 1

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status_baru):
        pilihan_valid = ["PENDING", "LUNAS", "BATAL"]
        if status_baru.upper() not in pilihan_valid:
            print(f"[GAGAL] Status '{status_baru}' tidak valid!")
            return
        self.__status = status_baru.upper()

    def proses_pendaftaran(self):
        if self.lomba.kuota <= 0:
            print(f"[GAGAL] Kuota lomba '{self.lomba.nama_lomba}' sudah habis!")
            self.status = "BATAL"
            return False

        total_biaya = self.lomba.biaya + self.lomba.hitung_biaya_tambahan() + Lomba.biaya_admin
        if self.peserta.saldo < total_biaya:
            print(f"[GAGAL] Saldo {self.peserta.nama} kurang! Butuh Rp {total_biaya:,.0f}")
            return False

        self.lomba.kurangi_kuota()
        self.status = "LUNAS"
        return True

class Transaksi:
    total_transaksi = 0

    def __init__(self, pendaftaran):
        self.pendaftaran = pendaftaran
        self.__pin = "123456"

        biaya_total = (
            pendaftaran.lomba.biaya 
            + pendaftaran.lomba.hitung_biaya_tambahan() 
            + Lomba.biaya_admin
        )
        self.jumlah_bayar = biaya_total

        self.struk = Struk(
            pendaftaran.peserta.nama, 
            pendaftaran.lomba.nama_lomba, 
            self.jumlah_bayar
        )
        Transaksi.total_transaksi += 1

    def bayar(self, input_pin):
        if input_pin != self.__pin:
            print(f"[GAGAL TRANSAKSI] PIN yang dimasukkan salah!")
            return False

        if self.pendaftaran.proses_pendaftaran():
            self.pendaftaran.peserta.saldo -= self.jumlah_bayar
            print(f"[TRANSAKSI SUKSES] Pembayaran berhasil untuk {self.pendaftaran.peserta.nama}")
            return True
        return False

    def cetak_struk_transaksi(self):
        self.struk.cetak()

if __name__ == "__main__":
    print("=========================================================")
    print(" DEMONSTRASI UTAMA PROGRAM OOP EVENT MAHASISWA ")
    print("=========================================================\n")
    print("--- 1. Pengujian Bukti Abstraksi (Abstract Base Class) ---")
    try:
        print("Mencoba menginstansiasi Abstract Class 'Lomba' secara langsung...")
        lomba_abstrak = Lomba("Lomba Murni", 50000, 10)
    except TypeError as err:
        print("[BERHASIL MUKTI] Abstract Class 'Lomba' tidak dapat diinstansiasi!")
        print(f"Error Caught: {err}\n")

    print("--- 2. Pengujian Instansiasi Subclass & Polimorfisme Pewarisan ---")
    peserta1 = Peserta("Adri", "adri@gmail.com", 150000)
    peserta2 = Peserta("Azril", "azril@gmail.com", 50000)

    lomba_akademik = LombaAkademik("KTI Nasional", 20000, kuota=2, bidang_studi="Informatika")
    lomba_non_akademik = LombaNonAkademik("Futsal Cup", 15000, kuota=1, lokasi_venue="GOR Mulawarman")

    daftar_event = [lomba_akademik, lomba_non_akademik]

    print("\nIterasi Polimorfik pada daftar lomba (Looping tanpa type check):")
    for event in daftar_event:
        event.tampilkan_info()
        event.proses_persiapan_lomba()
        tambahan = event.hitung_biaya_tambahan()
        print(f"-> Biaya Tambahan Fasilitas: Rp {tambahan:,.0f}\n")

    print("--- 3. Pengujian Polimorfisme via Duck Typing ---")
    email_service = NotifikasiEmail()
    sms_service = NotifikasiSMS()

    kirim_notifikasi_sistem(email_service, peserta1.email, "Pendaftaran Anda telah diproses.")
    kirim_notifikasi_sistem(sms_service, "08123456789", "Kode verifikasi transaksi Anda: 123456.")
    print()

    print("--- 4. Pengujian Operator Overloading ---")
    print(f"String Representation (__str__): {peserta1}")
    total_gabungan_saldo = peserta1 + peserta2  # Magic method __add__
    print(f"Penggabungan Saldo (__add__): Rp {total_gabungan_saldo:,.0f}")

    if peserta1 > peserta2:
        print(f"Hasil Perbandingan Saldo (__gt__): {peserta1.nama} memiliki saldo lebih besar dari {peserta2.nama}.\n")

    print("--- 5. Pengujian Pendaftaran & Transaksi (UML Relations) ---")
    pendaftaran1 = Pendaftaran(peserta1, lomba_akademik)

    transaksi1 = Transaksi(pendaftaran1)

    print("Eksekusi Pembayaran Transaksi:")
    if transaksi1.bayar("123456"):
        transaksi1.cetak_struk_transaksi()

    print("--- 6. Rekapitulasi Status Sistem ---")
    peserta1.tampilkan_profil()
    lomba_akademik.tampilkan_info()
    print(f"Total Peserta Terdaftar : {Peserta.total_peserta}")
    print(f"Total Lomba Dibuat      : {Lomba.total_lomba}")
    print(f"Total Transaksi Berhasil : {Transaksi.total_transaksi}")
    print("=========================================================")