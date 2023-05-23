#welcoming
print(" _________________________________________________ ")
print(" | Selamat Datang di Permainan sederhana Saya :v | ")
print(" |_______________________________________________| ")
#tanya mulai / keluar
print("""
1. Mulai
2. Keluar
""")
tanya_user = int(input("Pilihan : "))
if tanya_user == 1:
    tanya_nama = input("Siapa nama anda? : ")
    tanya_nama_putri = input("Siapa Nama Pacar/Crush/Istri anda? : ")
    print(f"Selamat Bermain {tanya_nama} :) ")
    #Kamu tiba tiba di tendang keluar dari negeri kahyangan dan tuan putri dari kerajaanmu terancam akan direbut oleh monster berinisial S
    print(f"Disuatu hari, negeri kahyangan kedatangan tamu tak diundang \nseorang raja kahyangan yang bernama {tanya_nama} dipaksa keluar dari negeri kahyangan \nputri {tanya_nama_putri} yang akan menjadi istri raja {tanya_nama} terancam akan direbut oleh sesorang yang berinisial S")
    #tanya user mau maju terus / mundur?
    print("Kamu terhempas ke planet yang bernama BUMI")
    tanya_user2 = input("Apakah kamu akan terus maju / mundur begitu saja? (Maju atau Mundur) : ").lower()
    if tanya_user2 == 'maju':
        print(f"Kamu memutuskan untuk terus maju karena di sana ada putri {tanya_nama_putri}, calon istri kamu yang sedang dalam bahaya :v ")
        #waow kamu menemukan 3 kotak yang salah satunya berisikan kekuatan spesial tetapi kotak yang lainya tidak diketahui isinya
        print("Tiba - tiba kamu menemukan 3 kotak yang salah satunya berisikan kekuatan spesial tetapi kotak yang lainya tidak diketahui isinya")
        print("1. Kotak Bronze ")
        print("2. Kotak Silver ")
        print("3. Kotak Gold ")
        tanya_user3 = input("Kotak mana yang akan kamu pilih? ")
        if tanya_user3 == '1':
            print("Kamu dikejutkan dengan sejumlah kawanan ular beracun di dalamnya, kamu tergigit dan modar ")
            print("-------------- GAME OVER --------------")
            print("_____ TERIMAKASIH SUDAH MAU MAIN ______")
        elif tanya_user3 == '2':
            #kamu mendapat kekuatan terbang dan kekuatan tak terkalahkan
            print("Kamu melihat semacam benda yang bersinar terang kemudian seperti masuk kedalam tubuhmu, kamu pun mendapat kekuatan terbang dan kekuatan yang tak terkalahkan")
            print("Lalu apa yang ingin kamu lakukan sekarang ? ")
            print("1. Terbang ke kahyangan")
            print(f"2. Lupakan Putri {tanya_nama_putri} dan pergi senang-senang sendiri di Bumi")
            tanya_user4 = input("Pilihan : ")
            if tanya_user4 == '1':
                print(f"Kamu berhasil terbang dan menemukan {tanya_nama_putri} calon istrimu yang akan dibawa pergi oleh seseorang yang berinisial S tersebut")
                print("Kamu menghampiri seseorang berinisial S tersebut dan")
                input("Tekan Enter Untuk Menghajar Seseorang tersebut")
                print("Booom")
                input("(Enter)")
                print("Paaawww")
                input("(Enter)")
                print("Sesorang yang berusaha untuk membawa calon istrimu tersebut terhempas jauh dari kahyangan")
                print(f"Singkat cerita kamu dan {tanya_nama_putri} pun melanjutkan pernikahan dan Bahagia Selamanya :)")
                print("------------------ HAPPY ENDING ------------------")
                input("Tekan Tombol ENTER untuk Keluar")
                print("-------------- GAME OVER --------------")
                print("_____ TERIMAKASIH SUDAH MAU MAIN ______")
            else:
                print("Cihhh, Dasar pengecut ")
                print("-------------- GAME OVER --------------")
                print("_____ TERIMAKASIH SUDAH MAU MAIN ______")
        elif tanya_user3 == '3':
            print("Kamu terkena sihir yang sangat kuat sehingga kamu pun menjadi lupa ingatan selamanya")
            print("-------------- GAME OVER --------------")
            print("_____ TERIMAKASIH SUDAH MAU MAIN ______")
    else:
        print("Cihhh, Dasar pengecut ")
        print("-------------- GAME OVER --------------")
        print("_____ TERIMAKASIH SUDAH MAU MAIN ______")