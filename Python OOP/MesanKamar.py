

class Info():
    def __init__(self, pemesan, kode_kamar, harga_kamar):
        self.pemesan = pemesan
        self.kode_kamar = kode_kamar
        self.harga_kamar = harga_kamar

    def info_pesanan(self):
        return f"Pemesan: {self.pemesan}, Kode: {self.kode_kamar}, Harga: Rp.{self.harga_kamar}"


def jenis_kamar():
    print("\n1. Reguler")
    print("2. VIP-Bronze")
    print("3. VIP-Silver")
    print("4. VIP-Gold")
    print("5. VIP-Diamond")


Reguler = 90000
Bronze = 130000
Silver = 165000
Gold = 250000
Diamond = 435000

harga = {
    'Reguler': 90000,
    'Bronze': 130000,
    'Silver': 165000,
    'Gold': 250000,
    'Diamond': 435000
}
kode = {
    'Reguler': 'Reguler',
    'Bronze': 'Bronze',
    'Silver': 'Silver',
    'Gold': 'Gold',
    'Diamond': 'Diamond'
}


nama = input("Nama: ")
harga = 0
pesanan_info = Info(nama, kode, harga)
print("Pesan Kamar")

jumlah_kamar = input("Jumlah Kamar:")
kamar = int(jumlah_kamar)
x = 1
y = 1
while x <= kamar:

    jenis_kamar()
    kode_kamar = input("jenis kamar: ")
    if kode_kamar == "1":
        harga = harga + Reguler
        pesanan_info = Info(nama, kode['Reguler'], Reguler)
        x = x + 1
    elif kode_kamar == "2":
        harga = harga + Bronze
        pesanan_info = Info(nama, kode['Bronze'], Bronze)
        x = x + 1
    elif kode_kamar == "3":
        harga = harga + Silver
        pesanan_info = Info(nama, kode['Silver'], Silver)
        x = x + 1
    elif kode_kamar == "4":
        harga = harga + Gold
        pesanan_info = Info(nama, kode['Gold'], Gold)
        x = x + 1
    elif kode_kamar == "5":
        harga = harga + Diamond
        pesanan_info = Info(nama, kode['Diamond'], Diamond)
        x = x + 1
    else:
        print("Kode Kamar ", kode_kamar, " Tidak Tersedia")


# def info(func):
#   def warper():
print("\n===========================================")

print(pesanan_info.info_pesanan())
print("===========================================")
print("Total: Rp.", harga)

# print(pesanan_info.info_pesanan())


# say()
