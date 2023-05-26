def identitas(nama, lokasi, umur):
    print(f"Nama = {nama}")
    print(f"Tempat Lahir = {lokasi}")
    print(f"Lahir Tahun = {umur}")
tanya_nama = input("Siapa Nama Anda? : ")
tanya_tempat = input("Tempat Lahir Anda? : ")
tanya_umur = int(input("Lahir Pada Tahun? : "))
identitas(tanya_nama, tanya_tempat, tanya_umur)