x = int(input("Masukan bilangan 1 : "))
y = int(input("Masukan bilangan 2 : "))
z = int(input("Masukan bilangan 3 : "))
if (x < y) and (x < z):
    if (y < z):
       print(x,y,z)
    else:
        print(x,z,y)
elif (y < x) and (y < z):
    if (x < z):
        print(y,x,z)
    else:
        print(y,z,x)
elif (z < x) and (z < y):
    if (x < y):
        print(z,x,y)
    else:
        print(z,y,x)