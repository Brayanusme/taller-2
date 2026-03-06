entrada = input("Ingresa una lista de números separados por comas (ej: 10, 5, 20.5, 8): ")

numeros = [float(n.strip()) for n in entrada.split(",")]

suma_total = sum(numeros)
valor_maximo = max(numeros)
valor_minimo = min(numeros)

promedio = suma_total / len(numeros)

print("\n--- Resultados del Análisis ---")
print(f" Lista de números: {numeros}")
print(f" Suma total: {suma_total}")
print(f" Valor máximo: {valor_maximo}")
print(f" Valor mínimo: {valor_minimo}")
print(f"Promedio: {promedio:.22f}") 