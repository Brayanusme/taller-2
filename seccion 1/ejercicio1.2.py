
print("============================================")
print("Calculadora basica. ")
print("Crado por Brayan Usme Gaviria. ")
print("============================================")

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
op = str(input("Ingrese el tipo de operación matemática (no el simbolo): "))

op = op.lower()

match op:
    case "suma":
        print(f"La suma es: {n1 + n2}")
    case "resta":
        print(f"La resta es: {n1 - n2}")
    case "multiplicacion":
        print(f"La multiplicación es: {n1 * n2}")
    case "division":
        if n1 == 0 or n2 == 0:
            print(f"Error al dividir: {ZeroDivisionError}") 
        else:
            print(f"La division es: {n1 / n2}")