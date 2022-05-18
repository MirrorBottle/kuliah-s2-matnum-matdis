import math

print('============================')
print('SOAL 3B')
print('============================')

basis_data = int(input("Masukkan Total Buku Basis Data: "))
metnum = int(input("Masukkan Total Buku Metode Numerik: "))
alpro = int(input("Masukkan Total Buku Algoritma Pemrograman: "))
jaringan = int(input("Masukkan Total Buku Jaringan: "))

total_buku = basis_data + metnum + alpro + jaringan
fact_total_buku = math.factorial(basis_data) * math.factorial(metnum) * math.factorial(alpro) * math.factorial(jaringan)
total_kombinasi = math.factorial(total_buku) / fact_total_buku
print(f"Total Kombinasi: {round(total_kombinasi)}")






