tagihan = float(input("Masukkan berapa total yang harus dibayar : "))
tip = int(input("Masukkan Tip yang ingin diberikan (Misal 10, 12, 15) : "))
banyak_penanggung = int(input("Berapa orang yang bersedia untuk membayar? : "))
#((tip/100) * tagihan + tagihan) / banyak penanggung
tip_a = tip / 100
total_tagihan = tip_a * tagihan + tagihan
tanggungan_per_orang = round(total_tagihan / banyak_penanggung, 2)
tanggungan_per_orang = "{:.2f}".format(tanggungan_per_orang)
print(f"jadi masing-masing orang harus membayar {tanggungan_per_orang}$ ")  