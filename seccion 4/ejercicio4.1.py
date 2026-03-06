ent1 = input("Ingresa los elementos de la primera lista: ")
ent2 = input("Ingresa los elementos de la segunda lista: ")

lista1 = ent1.split()
lista2 = ent2.split()

comunes = []
solo_lista1 = []
solo_lista2 = []

for elemento in lista1:
    if elemento in lista2:
        if elemento not in comunes:
            comunes.append(elemento)
    else:
        if elemento not in solo_lista1:
            solo_lista1.append(elemento)

for elemento in lista2:
    if elemento not in lista1:
        if elemento not in solo_lista2:
            solo_lista2.append(elemento)

print("\n--- Resultados ---")
print(f"Elementos comunes: {comunes}")
print(f"Solo en la primera lista: {solo_lista1}")
print(f"Solo en la segunda lista: {solo_lista2}")