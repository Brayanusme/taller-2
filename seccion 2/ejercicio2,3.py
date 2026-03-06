def calculadora():
    while True:
        print("\n--- Menú de Calculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == '5':
            print("¡Hasta luego! Gracias por usar la calculadora.")
            break 

        if opcion in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if opcion == '1':
                    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
                elif opcion == '2':
                    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
                elif opcion == '3':
                    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
                elif opcion == '4':
                    if num2 != 0:
                        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
                    else:
                        print("Error: No se puede dividir entre cero.")
            except ValueError:
                print("Error: Por favor, ingresa números válidos.")
        else:
            print("Opción no válida. Intenta de nuevo.")

calculadora()