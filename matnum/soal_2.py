#soal P1(1, 1.5), P2(2, 2.1), P3(5, 4.2); X = 3.2; Y = ?

#import library untuk dataset x dan y
#pip install numpy
import numpy as np

#Import library matplotlib untuk grafik cartesius
#pip intall matplotlib
import matplotlib.pyplot as plt

#import library dari scipy untuk membuat garis curvy
#pip intsall scipy
from scipy.interpolate import make_interp_spline

#Deklarasi dan Awal Program
P = [[], [], []]
x = 0
print("\n==Penghitung Interpolasi Kuadrattik==")

#Perulangan Input 3 titik dan niai x unutk mencari nilai y
for x in range(3):
    inp = float(input(
        "\n Masukan nilai x titik "+str(x+1)+" : "
    ))
    P[x].append(inp)
    inp = float(input(
        " Masukan nilai y titik "+str(x+1)+" : "
    ))
    P[x].append(inp)
    print(" > Titik"+str(x+1), "(P"+str(x+1)+") = (", P[x][0], ";", P[x][1], ")")
x = float(input(
    "\n Masukan nilai x : "
))
print(" > Nilai x = "+str(x))

#Penerapan Rumus
x1 = P[0][0]
y1 = P[0][1]
x2 = P[1][0]
y2 = P[1][1]
x3 = P[2][0]
y3 = P[2][1]
y = (y1*(x-x2)*(x-x3)) / ((x1-x2)*(x1-x3)) + (y2*(x-x1)*(x-x3)) / ((x2-x1)*(x2-x3)) + (y3*(x-x1)*(x-x2)) / ((x3-x1)*(x3-x2))

#Penerapan Grafik Kordinat
x_axis = [x1, x2, x3, x]
y_axis = [y1, y2, y3, y]

#prosedur partisi quicksort
def partisi(kiri, kanan, arrayx, arrayy):
    pivot, ptr = arrayx[kanan], kiri
    for i in range(kiri, kanan):
        if arrayx[i] <= pivot:
            arrayx[i], arrayx[ptr] = arrayx[ptr], arrayx[i]
            arrayy[i], arrayy[ptr] = arrayy[ptr], arrayy[i]
            ptr += 1
    arrayx[ptr], arrayx[kanan] = arrayx[kanan], arrayx[ptr]
    arrayy[ptr], arrayy[kanan] = arrayy[kanan], arrayy[ptr]
    return ptr

#prosedur pengurutan garis titik
def quicksort(kiri, kanan, arrayx, arrayy, xy):
    if len(arrayx) == 1:
        return arrayx
    if kiri < kanan:
        pi = partisi(kiri, kanan, arrayx, arrayy)
        quicksort(kiri, pi-1, arrayx, arrayy, "x")
        quicksort(pi+1, kanan, arrayx, arrayy, "x")
    if xy == "x":
        return arrayx
    else:
        return arrayy

x_axis = quicksort(0, len(x_axis)-1, x_axis, y_axis, "x")
y_axis = quicksort(0, len(x_axis)-1, x_axis, y_axis, "y")
X = np.array(x_axis)
Y = np.array(y_axis)

X_Y_Spline = make_interp_spline(X, Y)
X_ = np.linspace(X.min(), X.max(), 500)
Y_ = X_Y_Spline(X_)

plt.title("Grafik Hasil")
plt.scatter(x_axis, y_axis, color="darkblue", marker='o', label='Titik(P)')
plt.plot(X_, Y_)

plt.xlabel('Nilai X')
plt.ylabel('Nilai Y')

plt.grid(True)
plt.legend()

#Hasil
print("\n Nilai y adalah : "+str(y)+"\n > Titik ( "+str(x)+"; "+str(y)+" )")
plt.show()
