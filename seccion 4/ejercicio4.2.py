directorio = {}

while True:
    print("\n--- GESTIÓN DE CONTACTOS ---")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Mostrar todos")
    print("5. Salir")
    
    opcion = input("Elige una opción (1-5): ")

    if opcion == "1":
        nombre = input("Nombre del contacto: ").strip()
        telefono = input("Número telefónico: ").strip()
        directorio[nombre] = telefono
        print(f"¡Contacto '{nombre}' guardado con éxito!")

    elif opcion == "2":
        nombre = input("Nombre a buscar: ").strip()
        if nombre in directorio:
            print(f" El teléfono de {nombre} es: {directorio[nombre]}")
        else:
            print(" El contacto no existe.")

    elif opcion == "3":
        nombre = input("Nombre del contacto a borrar: ").strip()
        if nombre in directorio:
            del directorio[nombre]
            print(f" Contacto '{nombre}' eliminado.")
        else:
            print(" No se encontró ese nombre.")

    elif opcion == "4":
        if not directorio:
            print("La agenda está vacía.")
        else:
            print("\n--- LISTA DE CONTACTOS ---")
            for nombre, tel in directorio.items():
                print(f" {nombre}: {tel}")

    elif opcion == "5":
        print("Saliendo del sistema... ¡Hasta luego!")
        break
    
    else:
        print("Opción no válida, intenta de nuevo.")