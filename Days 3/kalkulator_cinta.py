#tanya nama yang ingin di uji coba
nama1 = input("Masukkan nama kamu : ")
nama2 = input("Masukkan nama dia : ")
nlc1 = nama1.lower()
nlc2 = nama2.lower()
nlc3 = f"{nlc1} {nlc2}"
#cinta sejati
c1 = nlc3.count('c')
i1 = nlc3.count('i')
n1 = nlc3.count('n')
t1 = nlc3.count('t')
a1 = nlc3.count('a')

s2 = nlc3.count('s')
e2 = nlc3.count('e')
j2 = nlc3.count('j')

cinta1 = c1 + i1 + n1 + t1 + a1
sejati2 = s2 + e2 + j2  
cc = cinta1 + sejati2
print(cc)

if cc >= 0 and cc < 5:
    print("hubungan anda layak untuk dipertahankan")
elif cc > 5 and cc < 20:
    print("Hubungan anda sudah toxic")
elif cc >= 20:
    print("Anda berdua merupakan pasangan yang sweet like cola and mentos :v")
else:
    print("Dahla putus aja")