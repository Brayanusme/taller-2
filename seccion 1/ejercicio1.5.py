print("--- MI CONVERTIDOR ---")
print("1 - De Celsius a Fahrenheit")
print("2 - De Kilómetros a Millas")
print("3 - De Kilogramos a Libras")

opcion = input("¿Qué quieres hacer? (1, 2 o 3): ")

if opcion == "1":
    celsius = float(input("Escribe los grados Celsius: "))
    resultado = (celsius * 1.8) + 32
    print("El resultado es:", round(resultado, 2), "grados Fahrenheit")

elif opcion == "2":
    km = float(input("Escribe los kilómetros: "))
    resultado = km * 0.62
    print("El resultado es:", round(resultado, 2), "millas")

elif opcion == "3":
    kg = float(input("Escribe los kilogramos: "))
    resultado = kg * 2.20
    print("El resultado es:", round(resultado, 2), "libras")

else:
    print("Esa opción no existe, intenta de nuevo.")