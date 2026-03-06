print("============================================")
print("Confirmacion de datos personales. ")
print("Crado por Brayan Usme Gaviria. ")
print("============================================")

n = input("Ingrese su nombre: ")
e = int(input("Ingrese su edad: "))
c = input("Ingrese la ciudad en la que vive: ")
if (e < 0):
    print("La edad no es valida...")
else:
    print(f"Bienvenido {n}, con {e} años, de la ciudad {c}")