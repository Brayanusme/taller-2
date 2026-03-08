def obtener_saludo(hora):
    if 5 <= hora <= 12:
        return "hola buenos días"
    elif 13 <= hora <= 19:
        return "hola buenas tardes"
    elif 20 <= hora <= 24:
        return "hola buenas noches"
    else:
        return "¡Hola"  # Para horas entre 0 y 4

def main():
    print("========================================")
    print("  Generador de Saludos Personalizados")
    print("========================================")

    nombre = input("\n¿Cuál es tu nombre? ").strip()
    if not nombre:
        nombre = "amigo/a"

    while True:
        try:
            hora = int(input("¿Qué hora es? (0-24): "))
            if 0 <= hora <= 24:
                break
            else:
                print("Por favor ingresa una hora válida entre 0 y 24.")
        except ValueError:
            print("Por favor ingresa un número entero.")

    saludo = obtener_saludo(hora)
    print(f"  {saludo}, {nombre}!")

if __name__ == "__main__":
    main()