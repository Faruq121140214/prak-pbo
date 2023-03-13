class Orang:

    def __init__(self,nama,nim,kelas,jumlah_sks,):
        self.nama = nama
        self.nim = nim
        self.kelas = kelas
        self.jumlah_sks = jumlah_sks

    def manggil_orang(self):
        print("hai", self.nama, "dengan nim", self.nim, "anak dari kelas", self.kelas, "lagi di", self.jumlah_sks, "sks kan?")

orang1 = Orang("Uber", 23002, "RB", 20)

orang1.manggil_orang()