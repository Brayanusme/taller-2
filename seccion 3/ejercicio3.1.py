n = int(input("Introduce un número entero positivo: "))

print(f"Números pares desde 1 hasta {n}:")

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)