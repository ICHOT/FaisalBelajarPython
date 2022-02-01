import os
import random


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


def opengame():
    command = "py MiniGame.py"
    os.system(command)


def ran():
    for randint in range(1):
        return(random.randint(10, 100))


class Player():
    def __init__(self, nama, darah):
        self.nama = nama
        self.darah = darah

    def stat_player(self):
        return f"\nNama: {self.nama}\nDarah: {600-self.darah}"

    def stat_pocong(self):
        return f"\nNama: {self.nama}\nDarah: {600-self.darah}"

    def stat_kunti(self):
        return f"\nNama: {self.nama}\nDarah: {600-self.darah}"


def skill():
    print("=============")
    print("Fire Strike")
    print("Mental Break")
    print("Flame Aura")
    print("Ethernal Prison")
    print("=============")


nama_skill = {
    'skill1': "Fire Strike",
    'skill2': "Mental Break",
    'skill3': "Flame Aura",
    'skill4': "Ethernal Prison"
}

player_name = input("Masukan Nama : ")
nama = player_name
darah_player = 300
darah_pocong = 300
darah_kunti = 300
stat_player = Player(nama, darah_player)
stat_pocong = Player("Pocong", darah_pocong)
stat_kunti = Player("Kuntilanak", darah_kunti)

# Mulai Game
print("Pilih Monster Yang Akan Di Lawan!")
print("1.Pocong")
print("2.Kunti #BELUM TERSEDIA (QUIT)")
pilihan = input("Masukan Pilihan : ")

if pilihan == "1":  # pocong
    print(stat_pocong.stat_pocong())
    print(stat_player.stat_player())

    while darah_player <= 600:
        skill()
        pilih_skill = input("Pilih Skill: ")
        if pilih_skill == "1":
            darah_player += ran()
            darah_pocong += ran()
            stat_player = Player(nama, darah_player)
            stat_pocong = Player("Pocong", darah_pocong)
            print(stat_pocong.stat_pocong())
            print(stat_player.stat_player())
            print(nama, " menggunakan skill ", nama_skill['skill1'])
        elif pilih_skill == "2":
            darah_player += ran()
            darah_pocong += ran()
            stat_player = Player(nama, darah_player)
            stat_pocong = Player("Pocong", darah_pocong)
            print(stat_pocong.stat_pocong())
            print(stat_player.stat_player())
            print(nama, " menggunakan skill ", nama_skill['skill2'])

        elif pilih_skill == "3":
            darah_player += ran()
            darah_pocong += ran()
            stat_player = Player(nama, darah_player)
            stat_pocong = Player("Pocong", darah_pocong)
            print(stat_pocong.stat_pocong())
            print(stat_player.stat_player())
            print(nama, " menggunakan skill ", nama_skill['skill3'])

        elif pilih_skill == "4":
            darah_player += ran()
            darah_pocong += ran()
            stat_player = Player(nama, darah_player)
            stat_pocong = Player("Pocong", darah_pocong)
            print(stat_pocong.stat_pocong())
            print(stat_player.stat_player())
            print(nama, " menggunakan skill ", nama_skill['skill4'])
        else:
            print("Skill Tidak Ada")
    if darah_player <= 600:
        print("Player WIN")

    elif darah_pocong <= 600:
        print("Pocong Win")

    else:
        print("Draw")
else:
    clearConsole()
