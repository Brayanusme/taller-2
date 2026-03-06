def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre cero"
    return a / b


def menu():
    print("=== CALCULADORA ===")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "5":
        print("¡Hasta luego!")
        return False

    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida")
        return True

    a = float(input("Ingresa el primer número: "))
    b = float(input("Ingresa el segundo número: "))

    if opcion == "1":
        print("Resultado:", sumar(a, b))
    elif opcion == "2":
        print("Resultado:", restar(a, b))
    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))
    elif opcion == "4":
        print("Resultado:", dividir(a, b))

    return True


# Bucle principal
continuar = True
while continuar:
    print()
    continuar = menu()