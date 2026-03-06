suma_total = 0

print("--- Sumadora Continua ---")
print("Introduce los números que quieras. Ingresa el 0 para terminar.")

while True:
    numero = float(input("Ingresa un número: "))
    
    if numero == 0:
        break
    
    suma_total += numero

print("-" * 25)
print(f"La suma total de los números ingresados es: {suma_total}")