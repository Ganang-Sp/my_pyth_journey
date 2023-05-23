berat_badan = int(input("Masukkan berat badan antum : "));
tinggi_badan = input("Masukkan tinggi badanmu (dalam satuan meter contoh 1.8/1.9/1.7) : ");
t = float(tinggi_badan);
rumus = berat_badan / (t ** 2);
if rumus < 18.5:
    print("UnderWeight");
elif rumus > 18.5 and rumus < 25:
    print("Normal Weight");
elif rumus > 25 and rumus < 30:
    print("OverWeigt");
elif rumus > 30 and rumus < 35:
    print("Obesitas");
else:
    print("Obesitas Berat");