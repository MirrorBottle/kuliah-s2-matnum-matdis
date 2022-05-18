import math

print('============================')
print('SOAL 3A')
print('============================')

basis_data = math.factorial(int(input("Masukkan Total Buku Basis Data: ")))
metnum = math.factorial(int(input("Masukkan Total Buku Metode Numerik: ")))
alpro = math.factorial(int(input("Masukkan Total Buku Algoritma Pemrograman: ")))
jaringan = math.factorial(int(input("Masukkan Total Buku Jaringan: ")))

total_kombinasi = basis_data * metnum * alpro * jaringan

print(f"Total Kombinasi: {total_kombinasi}")






