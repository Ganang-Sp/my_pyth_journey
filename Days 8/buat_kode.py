logo = """
╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗    ╔═══╗╔══╗╔═══╗╔═══╗╔═══╗
║╔═╗║║╔═╗║║╔══╝║╔═╗║║╔═╗║║╔═╗║    ║╔═╗║╚╣╠╝║╔═╗║║╔══╝║╔═╗║
║║ ╚╝║║ ║║║╚══╗║╚══╗║║ ║║║╚═╝║    ║║ ╚╝ ║║ ║╚═╝║║╚══╗║╚═╝║
║║ ╔╗║╚═╝║║╔══╝╚══╗║║╚═╝║║╔╗╔╝    ║║ ╔╗ ║║ ║╔══╝║╔══╝║╔╗╔╝
║╚═╝║║╔═╗║║╚══╗║╚═╝║║╔═╗║║║║╚╗    ║╚═╝║╔╣╠╗║║   ║╚══╗║║║╚╗
╚═══╝╚╝ ╚╝╚═══╝╚═══╝╚╝ ╚╝╚╝╚═╝    ╚═══╝╚══╝╚╝   ╚═══╝╚╝╚═╝
"""

huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

ulangi = False
while not ulangi:
    print(logo)
    enkrip_atau_decode = input("Ketik 'enkripsi' untuk encode & 'dekripsi' untuk decode\n").lower()
    if enkrip_atau_decode == "enkripsi":
        kata = input("Masukkan Kata/Kalimat : \n")
        jumlah_shift = int(input("Jumlah Shift yang Diinginkan : \n"))
        def enkripsi(k,shift):
            enkrip = ""
            for x in kata:
                if " " == x:
                    enkrip += " "
                if x in huruf:
                    posisi = huruf.index(x)
                    posisi_baru = posisi + shift
                    kata_baru = huruf[posisi_baru]
                    enkrip += kata_baru
                else:
                    enkrip += x
            print(f"Berhasil mengubah dari {k} menjadi {enkrip}")
        enkripsi(k=kata,shift=jumlah_shift)
        tanya_user = int(input("Ketik 1 jika ingin mengulangi jika tidak ketik 0 saja : "))
        if tanya_user == 0:
            ulangi = True
        elif tanya_user == 1:
            ulangi = False
    if enkrip_atau_decode == "dekripsi":
        kd = input("Masukkan Kata/Kalimat : \n")
        sh = int(input("Jumlah Shift : \n"))
        def dekripsi(ka,shift_d):
            dekrip = ""
            for y in ka:
                if y == " ":
                    dekrip += " "
                if y in huruf:
                    posisi_awal = huruf.index(y)
                    posisi_baru = posisi_awal - shift_d
                    kd_baru = huruf[posisi_baru]
                    dekrip += kd_baru
                else:
                    dekrip += y
            print(f"Berhasil mengubah {ka} menjadi {dekrip}")
        dekripsi(ka=kd,shift_d=sh)
        tanya_user = int(input("Ketik 1 jika ingin mengulangi jika tidak ketik 0 saja : "))
        if tanya_user == 0:
            ulangi = True
        elif tanya_user == 1:
            ulangi = False