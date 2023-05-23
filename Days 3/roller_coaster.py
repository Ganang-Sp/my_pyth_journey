tanya_tinggi_badan = int(input("Berapa Tinggi Badan Kamu? : "))
if tanya_tinggi_badan > 120:
    tanya_umur = int(input("Berapa Umur Anda? : "))
    if tanya_umur >= 10 and tanya_umur <= 15:
        print("Harga tiket : 5$")
    elif tanya_umur > 15 and tanya_umur <= 50:
        print("Harga tiket : 7$")
    else:
        print("Masih Kecil Kau Dek")
else:
    print("Minum Susu yang Banyak dulu dek!!")