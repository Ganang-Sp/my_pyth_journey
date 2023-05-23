import random
import ascii

#tanya pilihan user
pilihan_user = int(input("Pilih (0 untuk Gunting, 1 untuk Batu, 2 untuk Kertas) : "))
pilihan_komputer = random.randint(0,2)
if pilihan_user == 0 and pilihan_komputer == 1:
    print(f"Pilihanmu : {ascii.gunting} \n Pilihan Komputer : {ascii.batu}")
    print("KAMU KALAH")
elif pilihan_user == 0 and pilihan_komputer == 2:
    print(f"Pilihanmu : {ascii.gunting} \n Pilihan Komputer : {ascii.kertas}")
    print("KAMU MENANG")
elif pilihan_user == 0 and pilihan_komputer == 0:
    print(f"Pilihanmu : {ascii.gunting} \n Pilihan Komputer : {ascii.gunting}")
    print("WAOW SERI!!")
elif pilihan_user == 1 and pilihan_komputer == 1:
    print(f"Pilihanmu : {ascii.batu} \n Pilihan Komputer : {ascii.batu}")
    print("WAOW SERI")
elif pilihan_user == 1 and pilihan_komputer == 2:
    print(f"Pilihanmu : {ascii.batu} \n Pilihan Komputer : {ascii.kertas}")
    print("KAMU KALAH")
elif pilihan_user == 1 and pilihan_komputer == 0:
    print(f"Pilihanmu : {ascii.batu} \n Pilihan Komputer : {ascii.gunting}")
    print("KAMU MENANG")
elif pilihan_user == 2 and pilihan_komputer == 1:
    print(f"Pilihanmu : {ascii.kertas} \n Pilihan Komputer : {ascii.batu}")
    print("KAMU MENANG")
elif pilihan_user == 2 and pilihan_komputer == 2:
    print(f"Pilihanmu : {ascii.kertas} \n Pilihan Komputer : {ascii.kertas}")
    print("WAOW SERI!!")
elif pilihan_user == 2 and pilihan_komputer == 0:
    print(f"Pilihanmu : {ascii.kertas} \n Pilihan Komputer : {ascii.gunting}")
    print("KAMU KALAH")