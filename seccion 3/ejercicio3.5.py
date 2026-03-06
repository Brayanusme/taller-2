numeros_originales = []

print("Por favor, ingresa 10 números:")

for i in range(10):
    nm = float(input(f"Número {i + 1}: "))
    numeros_originales.append(nm)

lista_sin_duplicados = []

for n in numeros_originales:
    ya_existe = False
    for x in lista_sin_duplicados:
        if n == x:
            ya_existe = True
            break
    
    if not ya_existe:
        lista_sin_duplicados.append(n)

print("\n--- Resultados ---")
print(f"Lista original: {numeros_originales}")
print(f"Lista sin duplicados: {lista_sin_duplicados}")