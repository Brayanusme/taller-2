def convertir_calificacion():
    try:
        nota = float(input("Introduce la calificación numérica (0-100): "))

        if nota < 0 or nota > 100:
            print("Error: La calificación debe estar entre 0 y 100.")
            return

        if nota >= 90:
            letra = 'A'
        elif nota >= 80:
            letra = 'B'
        elif nota >= 70:
            letra = 'C'
        elif nota >= 60:
            letra = 'D'
        else:
            letra = 'F'

        print(f"La calificación equivalente es: {letra}")

    except ValueError:
        print("Error: Entrada no válida. Por favor, introduce un número.")

convertir_calificacion()