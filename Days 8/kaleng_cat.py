import math
def kaleng_cat(tinggi, lebar, cakupan):
    rumus = tinggi * lebar / cakupan
    r = math.ceil(rumus)
    print(f"Kamu setidaknya harus membeli {r} kaleng cat")
tanya_t = int(input("Tinggi Dinding : "))
tanya_l = int(input("Lebar Dinding : "))
cakupan_dinding = 5
kaleng_cat(tinggi=tanya_t, lebar=tanya_l, cakupan=cakupan_dinding)