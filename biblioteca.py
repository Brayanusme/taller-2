#Estructura de datos: Utilizar una lista de diccionarios para almacenar la información de los libros. Cada libro debe contener:
#id (numérico autoincremental), título, autor, año de publicación y estado de disponibilidad (True/False).
#Funciones principales: o agregar_libro(): Permite registrar un nuevo libro validando que el año sea numérico y mayor a 1900.
# o mostrar_libros(): Muestra todos los libros en formato legible: "ID: 1 - 'Cien años de soledad' (Gabriel García Márquez, 1967) 
# [Disponible]" o buscar_libro(): Permite buscar libros por título o autor, mostrando coincidencias parciales. o prestar_libro(id):
#  Cambia el estado de disponibilidad a False si el libro existe y está disponible. o devolver_libro(id): Cambia el estado de 
# disponibilidad a True. o eliminar_libro(id): Elimina un libro solo si no está prestado actualmente. o menu_principal(): Implementa 
# un menú interactivo con las opciones anteriores utilizando while para repetir hasta que se seleccione salir.
#Funciones adicionales desafiantes: o libros_por_autor(autor): Lista todos los libros de un autor específico. o estadisticas():
#  Muestra estadísticas del sistema: cantidad total de libros, libros disponibles y libros prestados. o exportar_a_txt(): 
# Guarda todos los libros en un archivo de texto llamado "biblioteca.txt".


# Lista global donde se guardan todos los libros
libros = []

# Variable para el ID autoincremental
contador_id = 1


def agregar_libro():
    #Permite registrar un nuevo libro en la biblioteca
    global contador_id

    print("\n--- AGREGAR NUEVO LIBRO ---")

    titulo = input("Ingresa el titulo del libro: ")
    autor = input("Ingresa el nombre del autor: ")

    # Validar que el año sea numerico y mayor a 1900
    while True:
        anio_texto = input("Ingresa el año de publicacion: ")

        # Verificar que sea un numero
        if not anio_texto.isdigit():
            print("Error: El año debe ser un numero. Intenta de nuevo.")
            continue

        anio = int(anio_texto)

        # Verificar que sea mayor a 1900
        if anio <= 1900:
            print("Error: El año debe ser mayor a 1900. Intenta de nuevo.")
            continue

        # Si pasa las validaciones, salir del bucle
        break

    # Crear el diccionario del libro
    libro_nuevo = {
        "id": contador_id,
        "titulo": titulo,
        "autor": autor,
        "anio": anio,
        "disponible": True
    }

    # Agregar el libro a la lista
    libros.append(libro_nuevo)

    # Incrementar el contador para el proximo libro
    contador_id = contador_id + 1

    print(f"\nLibro '{titulo}' agregado exitosamente con ID {libro_nuevo['id']}!")


def mostrar_libros():
    #Muestra todos los libros en formato legible
    print("\n--- LISTA DE LIBROS ---")

    # Verificar si hay libros registrados
    if len(libros) == 0:
        print("No hay libros registrados en la biblioteca.")
        return

    for libro in libros:
        # Determinar el estado del libro
        if libro["disponible"] == True:
            estado = "Disponible"
        else:
            estado = "Prestado"

        # Mostrar la informacion del libro en el formato pedido
        print(f"ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['anio']}) [{estado}]")


def buscar_libro():
    #Busca libros por titulo o autor, mostrando coincidencias parciales
    print("\n--- BUSCAR LIBRO ---")

    termino = input("Ingresa el titulo o autor a buscar: ")

    # Convertir a minusculas para busqueda sin importar mayusculas
    termino_lower = termino.lower()

    # Lista para guardar los resultados encontrados
    resultados = []

    for libro in libros:
        titulo_lower = libro["titulo"].lower()
        autor_lower = libro["autor"].lower()

        # Verificar si el termino aparece en el titulo o en el autor
        if termino_lower in titulo_lower or termino_lower in autor_lower:
            resultados.append(libro)

    # Mostrar resultados
    if len(resultados) == 0:
        print(f"No se encontraron libros con '{termino}'.")
    else:
        print(f"\nSe encontraron {len(resultados)} resultado(s):")
        for libro in resultados:
            if libro["disponible"] == True:
                estado = "Disponible"
            else:
                estado = "Prestado"
            print(f"ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['anio']}) [{estado}]")


def prestar_libro(id_libro):
    #Cambia el estado de disponibilidad a False si el libro existe y esta disponible
    print(f"\n--- PRESTAR LIBRO ID: {id_libro} ---")

    # Buscar el libro por ID
    libro_encontrado = None
    for libro in libros:
        if libro["id"] == id_libro:
            libro_encontrado = libro
            break

    # Verificar si el libro existe
    if libro_encontrado == None:
        print(f"Error: No existe un libro con ID {id_libro}.")
        return

    # Verificar si el libro esta disponible
    if libro_encontrado["disponible"] == False:
        print(f"Error: El libro '{libro_encontrado['titulo']}' ya esta prestado.")
        return

    # Cambiar el estado a no disponible
    libro_encontrado["disponible"] = False
    print(f"El libro '{libro_encontrado['titulo']}' ha sido prestado exitosamente.")


def devolver_libro(id_libro):
    #Cambia el estado de disponibilidad a True
    print(f"\n--- DEVOLVER LIBRO ID: {id_libro} ---")

    # Buscar el libro por ID
    libro_encontrado = None
    for libro in libros:
        if libro["id"] == id_libro:
            libro_encontrado = libro
            break

    # Verificar si el libro existe
    if libro_encontrado == None:
        print(f"Error: No existe un libro con ID {id_libro}.")
        return

    # Verificar si el libro realmente estaba prestado
    if libro_encontrado["disponible"] == True:
        print(f"El libro '{libro_encontrado['titulo']}' ya estaba disponible, no estaba prestado.")
        return

    # Cambiar el estado a disponible
    libro_encontrado["disponible"] = True
    print(f"El libro '{libro_encontrado['titulo']}' ha sido devuelto exitosamente.")


def eliminar_libro(id_libro):
    #Elimina un libro solo si no esta prestado actualmente
    print(f"\n--- ELIMINAR LIBRO ID: {id_libro} ---")

    # Buscar el libro por ID
    libro_encontrado = None
    indice = 0
    for i in range(len(libros)):
        if libros[i]["id"] == id_libro:
            libro_encontrado = libros[i]
            indice = i
            break

    # Verificar si el libro existe
    if libro_encontrado == None:
        print(f"Error: No existe un libro con ID {id_libro}.")
        return

    # Verificar si el libro esta prestado
    if libro_encontrado["disponible"] == False:
        print(f"Error: No se puede eliminar '{libro_encontrado['titulo']}' porque esta prestado.")
        return

    # Confirmar antes de eliminar
    confirmacion = input(f"¿Estas seguro de eliminar '{libro_encontrado['titulo']}'? (s/n): ")
    if confirmacion.lower() != "s":
        print("Eliminacion cancelada.")
        return

    # Eliminar el libro de la lista
    libros.pop(indice)
    print(f"El libro '{libro_encontrado['titulo']}' ha sido eliminado exitosamente.")


def libros_por_autor(autor):
    #Lista todos los libros de un autor especifico
    print(f"\n--- LIBROS DE: {autor} ---")

    autor_lower = autor.lower()
    resultados = []

    for libro in libros:
        if autor_lower in libro["autor"].lower():
            resultados.append(libro)

    if len(resultados) == 0:
        print(f"No se encontraron libros del autor '{autor}'.")
    else:
        print(f"Se encontraron {len(resultados)} libro(s):")
        for libro in resultados:
            if libro["disponible"] == True:
                estado = "Disponible"
            else:
                estado = "Prestado"
            print(f"  - ID: {libro['id']} | '{libro['titulo']}' ({libro['anio']}) [{estado}]")


def estadisticas():
    #Muestra estadisticas del sistema
    print("\n--- ESTADISTICAS DE LA BIBLIOTECA ---")

    total = len(libros)
    disponibles = 0
    prestados = 0

    for libro in libros:
        if libro["disponible"] == True:
            disponibles = disponibles + 1
        else:
            prestados = prestados + 1

    print(f"Total de libros registrados : {total}")
    print(f"Libros disponibles          : {disponibles}")
    print(f"Libros prestados            : {prestados}")

    if total > 0:
        porcentaje_disponible = (disponibles / total) * 100
        print(f"Porcentaje disponible       : {porcentaje_disponible:.1f}%")


def exportar_a_txt():
    #Guarda todos los libros en un archivo de texto llamado biblioteca.txt
    print("\n--- EXPORTAR A TXT ---")

    if len(libros) == 0:
        print("No hay libros para exportar.")
        return

    try:
        archivo = open("biblioteca.txt", "w", encoding="utf-8")

        archivo.write("============================\n")
        archivo.write("   CATALOGO DE BIBLIOTECA   \n")
        archivo.write("============================\n\n")

        for libro in libros:
            if libro["disponible"] == True:
                estado = "Disponible"
            else:
                estado = "Prestado"

            linea = f"ID: {libro['id']} - '{libro['titulo']}' ({libro['autor']}, {libro['anio']}) [{estado}]\n"
            archivo.write(linea)

        archivo.write(f"\nTotal de libros: {len(libros)}\n")
        archivo.close()

        print("Los libros se exportaron correctamente al archivo 'biblioteca.txt'.")

    except Exception as error:
        print(f"Error al exportar: {error}")


def menu_principal():
    #Menu interactivo principal del sistema
    print("\n========================================")
    print("   BIENVENIDO AL SISTEMA DE BIBLIOTECA  ")
    print("========================================")

    # Agregar algunos libros de ejemplo para probar
    libros.append({"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "anio": 1967, "disponible": True})
    libros.append({"id": 2, "titulo": "El amor en los tiempos del colera", "autor": "Gabriel García Márquez", "anio": 1985, "disponible": True})
    libros.append({"id": 3, "titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": 1905, "disponible": False})
    libros.append({"id": 4, "titulo": "1984", "autor": "George Orwell", "anio": 1949, "disponible": True})

    global contador_id
    contador_id = 5  # El siguiente ID disponible

    # Bucle principal del menu
    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1. Agregar libro")
        print("2. Mostrar todos los libros")
        print("3. Buscar libro")
        print("4. Prestar libro")
        print("5. Devolver libro")
        print("6. Eliminar libro")
        print("7. Libros por autor")
        print("8. Estadisticas")
        print("9. Exportar a TXT")
        print("0. Salir")

        opcion = input("\nElige una opcion: ")

        if opcion == "1":
            agregar_libro()

        elif opcion == "2":
            mostrar_libros()

        elif opcion == "3":
            buscar_libro()

        elif opcion == "4":
            mostrar_libros()
            try:
                id_ingresado = int(input("\nIngresa el ID del libro a prestar: "))
                prestar_libro(id_ingresado)
            except ValueError:
                print("Error: El ID debe ser un numero.")

        elif opcion == "5":
            mostrar_libros()
            try:
                id_ingresado = int(input("\nIngresa el ID del libro a devolver: "))
                devolver_libro(id_ingresado)
            except ValueError:
                print("Error: El ID debe ser un numero.")

        elif opcion == "6":
            mostrar_libros()
            try:
                id_ingresado = int(input("\nIngresa el ID del libro a eliminar: "))
                eliminar_libro(id_ingresado)
            except ValueError:
                print("Error: El ID debe ser un numero.")

        elif opcion == "7":
            autor_buscar = input("\nIngresa el nombre del autor: ")
            libros_por_autor(autor_buscar)

        elif opcion == "8":
            estadisticas()

        elif opcion == "9":
            exportar_a_txt()

        elif opcion == "0":
            print("\nGracias por usar el Sistema de Biblioteca. ¡Hasta pronto!")
            break

        else:
            print("Opcion no valida. Por favor elige un numero del 0 al 9.")


# Punto de entrada del programa
if __name__ == "__main__":
    menu_principal()