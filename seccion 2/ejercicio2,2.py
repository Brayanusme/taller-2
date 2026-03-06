def calculadora():
    print("=" * 40)
    print("        CALCULADORA SIMPLE")
    print("=" * 40)

    while True:
        try:
            num1 = float(input("\nIngresa el primer número: "))
            break
        except ValueError:
            print("⚠ Error: Por favor ingresa un número válido.")

    while True:
        try:
            num2 = float(input("Ingresa el segundo número: "))
            break
        except ValueError:
            print("⚠ Error: Por favor ingresa un número válido.")

    print("\nOperaciones disponibles: +  -  *  /")
    while True:
        operacion = input("Ingresa la operación: ").strip()
        if operacion in ("+", "-", "*", "/"):
            break
        print("⚠ Error: Operación no válida. Usa +, -, * o /")

    if operacion == "+":
        resultado = num1 + num2
        simbolo = "+"
    elif operacion == "-":
        resultado = num1 - num2
        simbolo = "-"
    elif operacion == "*":
        resultado = num1 * num2
        simbolo = "*"
    elif operacion == "/":
        if num2 == 0:
            print("\n Error: No se puede dividir entre cero.")
            return
        resultado = num1 / num2
        simbolo = "/"
    n1 = int(num1) if num1.is_integer() else num1
    n2 = int(num2) if num2.is_integer() else num2
    res = int(resultado) if isinstance(resultado, float) and resultado.is_integer() else resultado

    print("\n" + "=" * 40)
    print(f"  {n1} {simbolo} {n2} = {res}")
    print("=" * 40)


if __name__ == "__main__":
    while True:
        calculadora()
        repetir = input("\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
        if repetir != "s":
            print("\n Hasta luego  ")
            break