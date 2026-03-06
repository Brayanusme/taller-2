def calcular_promedio(numeros):
    if len(numeros) == 0:
        return "Error: la lista está vacía"

    suma = 0
    for numero in numeros:
        suma = suma + numero

    promedio = suma / len(numeros)
    return promedio


# Pedir datos al usuario
cantidad = int(input("¿Cuántos números quieres ingresar? "))

lista = []
for i in range(cantidad):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    lista.append(numero)

resultado = calcular_promedio(lista)
print("El promedio es:", resultado)