import os
class AkunBank:
    def __init__ (self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.no_pelanggan = no_pelanggan
        self.nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo

    def liat_saldo (self):
        print("saldo anda saat ini tersisa ", self.__jumlah_saldo)

    def tarik_uang (self, jumlah_uang):
        if jumlah_uang <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_uang
            print("tarik tunai sebesar", jumlah_uang, "berhasil")
        else:
            print("saldo anda tidak cukup aowkaokwoakowk")

    def transfer(self, penerima, jumlah_uang):
        if jumlah_uang <= self.__jumlah_saldo:
            self.__jumlah_saldo -= jumlah_uang
            penerima.__jumlah_saldo += jumlah_uang
            print("transfer sebesar", jumlah_uang, "rupiah kepada", penerima.nama_pelanggan, "berhasil dilakukan")
        else:
            print("transfer anda gagal")        

os.system("cls")
Akun1 = AkunBank(1234, "Faruq Al Furqon", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Maaaa", 9999999999)
base_akun = [Akun1, Akun2, Akun3]
while True:
    print("Selamat Datang di Bank jago")
    print(f"""Halo {Akun1.nama_pelanggan}, ingin melakukan apa?
    1. Lihat saldo
    2. Tarik tunai
    3. Transfer saldo
    4. Keluar""")
    masukkan = int(input("Masukkan layanan yang ingin anda pilih : "))
    if (masukkan == 1):
        Akun1.liat_saldo()
    elif (masukkan == 2):
        jumlah_tarik = int(input("Masukkan jumlah yang diambil"))
        Akun1.tarik_uang(jumlah_tarik)
    elif (masukkan == 3):
        jumlah_transfer = int(input("Masukkan jumlah uang yang ingin ditransfer"))
        no_tujuan = int(input("Masukkan nomor rekening tujuan"))
        for akun_tujuan in base_akun:
            if akun_tujuan.no_pelanggan == no_tujuan:
                Akun1.transfer(akun_tujuan, jumlah_transfer)
    elif (masukkan == 4):
        break
    print("\n")    