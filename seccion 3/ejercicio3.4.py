while True:
    try:
        numero = int(input("\n¿De qué número deseas ver la tabla de multiplicar?: "))
        
        print(f"\n--- Tabla del {numero} ---")
        
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
            
        print("-" * 20)
        
    except ValueError:
        print("¡Error! Por favor ingresa un número entero válido.")
        continue

    continuar = input("¿Deseas generar otra tabla? (s/n): ").lower()
    
    if continuar != 's':
        print("¡Gracias por usar el programa! Hasta pronto.")
        break