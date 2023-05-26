from gambar_hangman import HANGMANPICS, logo
import random
import os

print(logo)
kata = ["singa","kucing","kelinci"]
kata_yang_dipilih = random.choice(kata)

nyawa = 6
tampilan = []
for x in range(len(kata_yang_dipilih)):
    tampilan += "_"

ulangi = True
while ulangi:
    tebakan_user = input("Tebak Huruf : ")
    os.system('cls')
    if tebakan_user in tampilan:
        print(f"Tebakanmu {tebakan_user} sudah masuk, jadi mohon untuk tidak diulang :)")

    for y in range(len(kata_yang_dipilih)):
        posisi = kata_yang_dipilih[y]
        if tebakan_user == posisi:
            tampilan[y] = tebakan_user
            print(f"Nyawa tersisa = {nyawa}")

    print(' '.join(tampilan))
    if tebakan_user not in kata_yang_dipilih:
        nyawa -= 1
        print(f"Nyawa tersisa = {nyawa}")
        if nyawa == 0:
            ulangi = False
            print("\nNyawa Habis")
            print(f"\nJawaban yang benar adalah {kata_yang_dipilih.upper()}")
            print("_______________")
            print("| Kamu Kalah  |")
            print("|_____________|")
    if "_" not in tampilan:
        os.system('cls')
        print(f"Jawabanya adalah {kata_yang_dipilih}")
        ulangi = False
        print("_______________")
        print("| Kamu Menang |")
        print("|_____________|")
    print(HANGMANPICS[nyawa])

        