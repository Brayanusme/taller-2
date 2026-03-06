nombres = ["Ana", "Pedro", "Lucía", "Carlos", "Juan", "Sofía", "Miguel"]

busqueda = input("Ingrese el nombre que desea buscar: ")

encontrado = False

for indice, nombre in enumerate(nombres):
    if nombre.lower() == busqueda.lower():
        print(f"¡Encontrado! El nombre '{nombre}' está en la posición {indice}.")
        encontrado = True
        break  

if not encontrado:
    print(f"Lo siento, el nombre '{busqueda}' no se encuentra en la lista.")