def simulador_descuentos():
    print("--- Sistema de Simulación de Descuentos ---")
    
    try:
        monto_original = float(input("Introduce el monto de la compra: "))
        if monto_original < 0:
            print("Error: El monto no puede ser negativo.")
            return

        categoria = input("Introduce tu categoría (A, B, C): ").upper()

        if categoria == 'A':
            porcentaje = 0.20  
        elif categoria == 'B':
            porcentaje = 0.15  
        elif categoria == 'C':
            porcentaje = 0.10  
        else:
            porcentaje = 0.00  
            print("Categoría no sujeta a descuentos.")

        ahorro = monto_original * porcentaje
        monto_final = monto_original - ahorro

        print("-" * 30)
        print(f"Monto Original: ${monto_original:.2f}")
        print(f"Categoría aplicada: {categoria}")
        print(f"Ahorro total: ${ahorro:.2f} ({int(porcentaje * 100)}%)")
        print(f"Monto final a pagar: ${monto_final:.2f}")
        print("-" * 30)

    except ValueError:
        print("Error: Por favor, ingresa un monto numérico válido.")

simulador_descuentos()  