tanya_tahun = int(input("Masukkan Tahun yang Ingin di cek : "))
if tanya_tahun % 4 == 0:
    if tanya_tahun % 100 == 0:
        if tanya_tahun % 400 == 0:
            print(f"{tanya_tahun} Merupakan Tahun Kabisat")
        else:
            print(f"{tanya_tahun} Bukan Merupakan Tahun Kabisat")
    else:
        print(f"{tanya_tahun} Merupakan Tahun Kabisat")
else:
    print(f"{tanya_tahun} Bukan Merupakan Tahun Kabisat")
