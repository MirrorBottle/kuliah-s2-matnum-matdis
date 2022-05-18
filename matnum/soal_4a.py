from tabulate import tabulate 
import os
os.system("cls")

def tabel(package):
    print(tabulate(package,headers='keys', tablefmt='fancy_grid'))

x0=2
x1=3
tol=0.001
persamaan = ['x^2-2*x-2']
a = [2]
b = [3]
c = [15]


print ("*******")
print ("** BISEKSI **")
print ("*******")
diketahui = {
    "x0" : a,
    "x1" : b,
    "Fungsi" : persamaan,
    "iterasi maksimum" : c
    
}
print ("diketahui pada soal")
tabel(diketahui)
print ("iterasi akan berhenti ketika sudah mencapai iterasi maksimum atau fx lebih dari 0 atau error\n")
#n=int(input("jumlah iterasi : "))
n=15
i=0

steps = []
while i < n and abs(x1-x0 )>= tol: 
    x=(x1+x0)/2
    fx=x**2-2*x-2
    fx0=x0**2-2*x0-2
    fx1=x1**2-2*x1-2 

    steps.append([i + 1, x0, x1, x, fx0, fx1, fx, abs(x1-x0)])
    i=i+1 
    if fx0 and fx<0 :
        x0=x
    elif fx0 and fx>0:
        x1=x

print(tabulate(steps, headers=["Iterasi", "x0", "x1", "x", "fx0", "fx1", "fx", "e"], tablefmt='fancy_grid'))
