data_mahasiswa = ['180','175','170','168','159','178']
print(data_mahasiswa)
jumlah_mahasiswa = 0
jumlah_semua_tinggi_badan = 0
for d in data_mahasiswa:
    jumlah_mahasiswa += 1
    di = int(d)
    jumlah_semua_tinggi_badan += di
print(f"jumlah semua mahasiswa yang didata adalah {jumlah_mahasiswa}")
print(f"Jumlah semua tinggi badan mashasiswa adalah {jumlah_semua_tinggi_badan}")
rumus = round(jumlah_semua_tinggi_badan / jumlah_mahasiswa)
print(f"Jadi Rata-rata tinggi badan semua mahasiswa adalah {rumus}")