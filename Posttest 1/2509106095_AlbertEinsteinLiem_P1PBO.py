class Peserta:
    nama_instansi = "Portal Event Mahasiswa"
    total_peserta = 0
    minimal_usia = 15

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
        print(f"[SUKSES] Saldo {self.nama} diperbarui menjadi: Rp {self.__saldo}")

    def tampilkan_profil(self):
        print(f"Peserta: {self.nama} | Email: {self.email} | Saldo: Rp {self.saldo}")

    @classmethod
    def buat_dari_dict(cls, data):
        return cls(data["nama"], data["email"], data["saldo"])

    @staticmethod
    def validasi_email(email):
        return "@" in email and "." in email
    
class Lomba:

    daftar_lomba = []
    total_lomba = 0
    biaya_admin = 5000.0

    def __init__(self, nama_lomba, biaya, kuota):

        self.nama_lomba = nama_lomba
        self.__biaya = 0.0
        self.__kuota = 0

        self.biaya = biaya
        self.kuota = kuota

        Lomba.daftar_lomba.append(self)
        Lomba.total_lomba += 1

    @property
    def biaya(self):
        return self.__biaya

    @biaya.setter
    def biaya(self, nilai):
        if nilai < 0:
            print(f"[GAGAL] Biaya lomba '{self.nama_lomba}' tidak boleh negatif!")
            return
        self.__biaya = float(nilai)

    @property
    def kuota(self):
        return self.__kuota

    @kuota.setter
    def kuota(self, nilai):
        if nilai < 0:
            print(f"[GAGAL] Kuota lomba '{self.nama_lomba}' tidak boleh negatif!")
            return
        self.__kuota = int(nilai)

    def kurangi_kuota(self):
        if self.__kuota > 0:
            self.__kuota -= 1
            return True
        return False

    @classmethod
    def cari_lomba(cls, keyword):
        print(f"\n--- Hasil Pencarian Lomba dengan kata kunci '{keyword}' ---")
        ditemukan = False
        for lomba in cls.daftar_lomba:
            if keyword.lower() in lomba.nama_lomba.lower():
                print(f"Lomba: {lomba.nama_lomba} | Biaya: Rp {lomba.biaya} | Sisa Kuota: {lomba.kuota}")
                ditemukan = True
        if not ditemukan:
            print("Lomba tidak ditemukan.")

    @staticmethod
    def hitung_total_biaya(biaya_lomba, admin):
        return biaya_lomba + admin

class Pendaftaran:

    total_pendaftaran = 0
    status_default = "PENDING"
    kategori_pendaftaran = "Online"

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
        print(f"[INFO] Status pendaftaran {self.peserta.nama} diubah ke: {self.__status}")

    def proses_pendaftaran(self):
        if self.lomba.kuota <= 0:
            print(f"[GAGAL] Kuota lomba '{self.lomba.nama_lomba}' sudah habis!")
            self.status = "BATAL"
            return False

        total = Lomba.hitung_total_biaya(self.lomba.biaya, Lomba.biaya_admin)
        if self.peserta.saldo < total:
            print(f"[GAGAL] Saldo {self.peserta.nama} kurang! Butuh Rp {total}")
            return False

        self.lomba.kurangi_kuota()
        self.status = "LUNAS"
        return True

    @classmethod
    def ubah_kategori(cls, kategori_baru):
        cls.kategori_pendaftaran = kategori_baru
        print(f"[INFO] Kategori pendaftaran diubah menjadi: {cls.kategori_pendaftaran}")

    @staticmethod
    def buat_kode_daftar(id_peserta, id_lomba):
        return f"REG-{id_peserta}{id_lomba}"

class Transaksi:

    total_transaksi = 0
    pajak = 0.0
    mata_uang = "IDR"

    def __init__(self, pendaftaran):
        self.pendaftaran = pendaftaran
        self.__pin = "123456"
        self.__jumlah_bayar = 0.0

        biaya = Lomba.hitung_total_biaya(pendaftaran.lomba.biaya, Lomba.biaya_admin)
        self.jumlah_bayar = biaya

        Transaksi.total_transaksi += 1

    @property
    def jumlah_bayar(self):
        return self.__jumlah_bayar

    @jumlah_bayar.setter
    def jumlah_bayar(self, nilai):
        if nilai <= 0:
            print("[GAGAL] Jumlah bayar harus lebih besar dari 0!")
            return
        self.__jumlah_bayar = float(nilai)

    def bayar(self, input_pin):
        if input_pin != self.__pin:
            print(f"[GAGAL TRANSAKSI] PIN yang dimasukkan salah!")
            return False

        if self.pendaftaran.proses_pendaftaran():
            self.pendaftaran.peserta.saldo -= self.jumlah_bayar
            print(f"[TRANSAKSI SUKSES] Pembayaran berhasil untuk {self.pendaftaran.peserta.nama}\n")
            return True
        return False

    @classmethod
    def set_pajak(cls, nilai_pajak):
        cls.pajak = nilai_pajak
        print(f"[INFO] Pajak transaksi diubah ke: {cls.pajak}")

    @staticmethod
    def cetak_struk(nama, event, total):
        print("-----------------------------------")
        print("        STRUK PEMBAYARAN           ")
        print("-----------------------------------")
        print(f"Nama  : {nama}")
        print(f"Event : {event}")
        print(f"Total : Rp {total}")
        print("-----------------------------------\n")

if __name__ == "__main__":
    print("=== DEMONSTRASI PROGRAM OOP ===\n")

    print("--- 1. Membuat Objek ---")
    peserta1 = Peserta("Adri", "adri@gmail.com", 150000)
    data_p2 = {"nama": "Azril", "email": "azril@gmail.com", "saldo": 50000}
    peserta2 = Peserta.buat_dari_dict(data_p2)

    lomba1 = Lomba("Lomba Makan Kerupuk", 20000, kuota=2)
    lomba2 = Lomba("Lomba Balap Karung", 15000, kuota=1)

    pendaftaran1 = Pendaftaran(peserta1, lomba1)
    pendaftaran2 = Pendaftaran(peserta2, lomba2)

    transaksi1 = Transaksi(pendaftaran1)
    transaksi2 = Transaksi(pendaftaran2)

    print("\n--- 2. Pengujian Setter dan Validasi Data ---")
    peserta2.saldo = 100000
    peserta1.saldo = -20000
    peserta1.saldo = "Seratus"
    pendaftaran1.status = "LULUS"

    print("\n--- 3. Peragaan Pemanggilan Method ---")

    print(f"Validasi Email 'adri@gmail.com': {Peserta.validasi_email(peserta1.email)}")
    print(f"Kode Pendaftaran Generated: {Pendaftaran.buat_kode_daftar(101, 202)}")

    Lomba.cari_lomba("Kerupuk")
    Transaksi.set_pajak(0.02)

    print("\n--- 4. Eksekusi Transaksi ---")

    print("Mencoba bayar dengan PIN salah:")
    transaksi1.bayar("000000")

    print("Mencoba bayar dengan PIN benar:")
    if transaksi1.bayar("123456"):
        Transaksi.cetak_struk(peserta1.nama, lomba1.nama_lomba, transaksi1.jumlah_bayar)

    print("--- 5. Rekap Atribut Kelas ---")
    print(f"Nama Instansi  : {Peserta.nama_instansi}")
    print(f"Total Peserta  : {Peserta.total_peserta}")
    print(f"Total Lomba    : {Lomba.total_lomba}")
    print(f"Total Transaksi: {Transaksi.total_transaksi}")