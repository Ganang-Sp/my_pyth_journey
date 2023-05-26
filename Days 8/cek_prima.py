angka_masukkan = int(input("Masukkan Angka yang ingin di cek : "))
def cek_prima(angka):
    #10/3,10/4,10/5,10/6,10/7,10/8,10/9
    prima = True
    for x in range(2, angka):
        if angka % x == 0:
            prima = False
    if prima:
        print(f"{angka} merupakan bilangan prima")
    else:
        print(f"{angka} bukan merupakan bilangan prima")
cek_prima(angka=angka_masukkan)