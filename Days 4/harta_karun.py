baris1 = ['O', 'O', 'O']
baris2 = ['O', 'O', 'O']
baris3 = ['O', 'O', 'O']
peta = [baris1, baris2, baris3]
peta_rapi = f"{peta[0]} \n{peta[1]} \n{peta[2]}"
print(peta_rapi)
tanya_user = input("Kolom?Baris? (maksimal 33) : ")
# tanya_user[0] #3
# tanya_user[1] #2
vertikal = int(tanya_user[0])
horizontal = int(tanya_user[1])

baris_yang_dipilih = peta[horizontal - 1]
baris_yang_dipilih[vertikal - 1] = 'X'

peta_rapi = f"{peta[0]} \n{peta[1]} \n{peta[2]}"
print(peta_rapi)
