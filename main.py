
class Lapangan:
    nama_aplikasi = "Penyewaan Lapangan Mini Soccer"
    lokasi = "Samarinda"
    total_lapangan = 0

    def __init__(self, nama, jenis, harga):
        self.nama = nama
        self.jenis = jenis
        self.__harga = harga
        Lapangan.total_lapangan += 1

    def tampilkan(self):
        print("Nama Lapangan :", self.nama)
        print("Jenis Lapangan:", self.jenis)
        print("Harga Sewa    :", self.__harga)

    @property
    def harga(self):
        return self.__harga

    @harga.setter
    def harga(self, harga):
        if harga > 0:
            self.__harga = harga
            print("Harga berhasil diubah")
        else:
            print("Harga harus lebih dari 0")

    @classmethod
    def ubah_lokasi(cls, lokasi_baru):
        if lokasi_baru.strip() != "":
            cls.lokasi = lokasi_baru
            print("Lokasi diubah menjadi:", cls.lokasi)
        else:
            print("Lokasi tidak boleh kosong")

    @staticmethod
    def cek_harga(harga):
        if harga > 0:
            return True
        else:
            return False


class Pelanggan:
    jenis_member = "Umum"
    status_aplikasi = "Aktif"
    total_pelanggan = 0

    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.__saldo = 0
        Pelanggan.total_pelanggan += 1

    def tambah_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print("Saldo berhasil ditambah")
        else:
            print("Jumlah saldo tidak valid")

    def tampilkan(self):
        print("Nama Pelanggan:", self.nama)
        print("No HP         :", self.no_hp)
        print("Saldo         :", self.__saldo)

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, jumlah):
        if jumlah >= 0:
            self.__saldo = jumlah
            print("Saldo berhasil diubah")
        else:
            print("Saldo tidak boleh negatif")

    @classmethod
    def ubah_status(cls, status):
        if status.strip() != "":
            cls.status_aplikasi = status
            print("Status aplikasi:", cls.status_aplikasi)
        else:
            print("Status tidak boleh kosong")

    @staticmethod
    def validasi_nama(nama):
        if nama.strip() != "":
            return True
        else:
            return False


class Penyewaan:
    nama_sistem = "Mini Soccer Booking"
    status = "Tersedia"
    total_sewa = 0

    def __init__(self, pelanggan, lapangan, jam):
        self.pelanggan = pelanggan
        self.lapangan = lapangan
        self.jam = jam
        self.__durasi = 1
        Penyewaan.total_sewa += 1

    def tampilkan(self):
        print("Pelanggan :", self.pelanggan.nama)
        print("Lapangan  :", self.lapangan.nama)
        print("Jam       :", self.jam)
        print("Durasi    :", self.__durasi, "jam")

    def hitung_total(self):
        return self.lapangan.harga * self.__durasi

    @property
    def durasi(self):
        return self.__durasi

    @durasi.setter
    def durasi(self, durasi):
        if durasi > 0:
            self.__durasi = durasi
            print("Durasi berhasil diubah")
        else:
            print("Durasi harus lebih dari 0")

    @classmethod
    def ubah_status(cls, status_baru):
        if status_baru.strip() != "":
            cls.status = status_baru
            print("Status penyewaan:", cls.status)
        else:
            print("Status tidak boleh kosong")

    @staticmethod
    def cek_jam(jam):
        if 0 <= jam <= 23:
            return True
        else:
            return False


# MAIN PROGRAM


print("==========================================")
print("   PENYEWAAN LAPANGAN MINI SOCCER")
print("==========================================")


# DATA LAPANGAN


print("\n=== DATA LAPANGAN ===")

lapangan1 = Lapangan(
    "Lapangan A",
    "Rumput Sintetis",
    150000
)

lapangan2 = Lapangan(
    "Lapangan B",
    "Rumput Sintetis",
    175000
)

lapangan1.tampilkan()
print()
lapangan2.tampilkan()

print("\nTotal lapangan:", Lapangan.total_lapangan)



# CLASS METHOD LAPANGAN


print("\n=== CLASS METHOD LAPANGAN ===")

Lapangan.ubah_lokasi("Samarinda Seberang")



# STATIC METHOD LAPANGAN


print("\n=== STATIC METHOD LAPANGAN ===")

print(
    "Cek harga 150000:",
    Lapangan.cek_harga(150000)
)

print(
    "Cek harga -50000:",
    Lapangan.cek_harga(-50000)
)



# SETTER LAPANGAN


print("\n=== SETTER LAPANGAN ===")

print("Harga awal:", lapangan1.harga)

lapangan1.harga = 200000

print("Harga setelah diubah:", lapangan1.harga)

lapangan1.harga = -10000

print("Harga setelah input salah:", lapangan1.harga)



# DATA PELANGGAN


print("\n=== DATA PELANGGAN ===")

pelanggan1 = Pelanggan(
    "Andhika",
    "081234567890"
)

pelanggan2 = Pelanggan(
    "Bima",
    "082345678901"
)

pelanggan1.tampilkan()
print()
pelanggan2.tampilkan()

print(
    "\nTotal pelanggan:",
    Pelanggan.total_pelanggan
)



# INSTANCE METHOD PELANGGAN


print("\n=== INSTANCE METHOD PELANGGAN ===")

pelanggan1.tambah_saldo(500000)

print(
    "Saldo Andhika:",
    pelanggan1.saldo
)


# CLASS METHOD PELANGGAN


print("\n=== CLASS METHOD PELANGGAN ===")

Pelanggan.ubah_status("Aktif")



# STATIC METHOD PELANGGAN


print("\n=== STATIC METHOD PELANGGAN ===")

print(
    "Nama Andhika valid:",
    Pelanggan.validasi_nama("Andhika")
)

print(
    "Nama kosong valid:",
    Pelanggan.validasi_nama("")
)



# SETTER PELANGGAN


print("\n=== SETTER PELANGGAN ===")

pelanggan1.saldo = 750000

print(
    "Saldo baru:",
    pelanggan1.saldo
)

pelanggan1.saldo = -100000

print(
    "Saldo setelah input salah:",
    pelanggan1.saldo
)



# DATA PENYEWAAN

print("\n=== DATA PENYEWAAN ===")

sewa1 = Penyewaan(
    pelanggan1,
    lapangan1,
    19
)

sewa2 = Penyewaan(
    pelanggan2,
    lapangan2,
    20
)

sewa1.tampilkan()

print(
    "Total biaya:",
    sewa1.hitung_total()
)

print()

sewa2.tampilkan()

print(
    "Total biaya:",
    sewa2.hitung_total()
)

print(
    "\nTotal penyewaan:",
    Penyewaan.total_sewa
)


# CLASS METHOD PENYEWAAN


print("\n=== CLASS METHOD PENYEWAAN ===")

Penyewaan.ubah_status("Sedang Berjalan")



# STATIC METHOD PENYEWAAN

print("\n=== STATIC METHOD PENYEWAAN ===")

print(
    "Jam 19 valid:",
    Penyewaan.cek_jam(19)
)

print(
    "Jam 30 valid:",
    Penyewaan.cek_jam(30)
)



# SETTER PENYEWAAN


print("\n=== SETTER PENYEWAAN ===")

print(
    "Durasi awal:",
    sewa1.durasi
)

sewa1.durasi = 2

print(
    "Durasi setelah diubah:",
    sewa1.durasi
)

print(
    "Total biaya baru:",
    sewa1.hitung_total()
)

sewa1.durasi = -2

print(
    "Durasi setelah input salah:",
    sewa1.durasi
)



# SELESAI


print("\n==========================================")
print("       PROGRAM SELESAI DIJALANKAN")
print("==========================================")