#menyediakan wadah total harga
total_harga = 0;

#Tanya pembeli mau porsi yang apa? 
tanya_pembeli = input("Ajeng pesen porsi sing nopo mas/mbak? (C/G/R)").lower()
if tanya_pembeli == 'c':
    total_harga += 5000;
elif tanya_pembeli == 'g':
    total_harga += 7000;
elif tanya_pembeli == 'r':
    total_harga += 10000;
else:
    print('Keyword salah mas/mbak dibaleni maneh programe :)')
#Tanya pembeli mau tambah topping apa saja?
tanya_pembeli2 = input("Mau tambah topping apa saja mas/mbak (endog / sosis / kabeh)? : ")
tanya_pembeli2 = tanya_pembeli2.lower()
if tanya_pembeli2 == 'endog':
    total_harga += 3000;
elif tanya_pembeli2 == 'sosis':
    total_harga += 4000;
elif tanya_pembeli2 == 'kabeh':
    total_harga += 7000;
elif tanya_pembeli2 == '':
    total_harga += 0
#Tanya Pembeli Mau tambah minum / tidak 
tanya_pembeli3 = input("""
Ajeng Ngunjuk nopo mas/mbak ? 
1. Es Teh
2. Es Jeruk
3. Es Doger
4. Tidak Pesan
Jawab : """)
if tanya_pembeli3 == '1':
    total_harga += 3000
    print(f"dadi total kabeh e {total_harga} rupiah ya Mas/Mbak :)")
elif tanya_pembeli3 == '2':
    total_harga += 4000
    print(f"dadi total kabeh e {total_harga} rupiah ya Mas/Mbak :)")
elif tanya_pembeli3 == '3':
    total_harga += 5000
    print(f"dadi total kabeh e {total_harga} rupiah ya Mas/Mbak :)")
elif tanya_pembeli3 == '4':
    print("Oalah yawis Mas/Mbak")
    print(f"dadi total kabeh e {total_harga} rupiah ya Mas/Mbak :)")
print("Matursuwun Mas/Mbak <:)")