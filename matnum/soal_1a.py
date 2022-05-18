def subtitusi(x1,y1,c1,x2,y2,c2):
    print ("\nPENYELESAIAN DENGAN METODE SUBSTITUSI")
    print(f"Persamaan 1  {x1}x + {y1}y = {c1}")
    print(f"Persamaan 2  {x2}x + {y2}y = {c2}")
    print("----------------------------------")
    print(f"{x1}x = {c1} - {y1}y")
    print(f" x = ({c1} - {y1}y) / {x1}")
    print("-----------------------------------")
    print("Mencari nilai y")
    print(f"{x2}x + {y2}y = {c2}")
    print(f"{x2} * (({c1} - {y1}y)/{x1}) + {y2}y = {c2}")
    proses1_1= c1*x2
    proses1_2= y1*x2
    print(f"({proses1_1} - {proses1_2}y)/{x1} + {y2}y = {c2}")
    print(f" ------------------------- x {x1}")
    proses2_1= y2*x1
    proses2_2= c2*x1
    print(f"{proses1_1} - {proses1_2}y + {proses2_1}y = {proses2_2}")
    print(f"- {proses1_2}y + {proses2_1}y = {proses2_2} - {proses1_1}")
    proses3_1= (-proses1_2)+proses2_1
    proses3_2= proses2_2-proses1_1
    print(f"{proses3_1}y = {proses3_2}")
    print(f"y = {proses3_2} / {proses3_1}")
    y= proses3_2/proses3_1
    print(f"y = {y}")
    print("-----------------------------------")
    print ("Mencari nilai x")
    print(f"{x1}x + {y1}y = {c1}")
    proses4= y1*y
    print(f"{x1}x + {proses4} = {c1}")
    print(f"{x1}x = {c1} - {proses4}")
    proses5= c1-proses4
    print(f"{x1}x = {proses5}")
    print(f"x = {proses5} / {x1}")
    x= proses5/x1
    print(f"x = {x}")
