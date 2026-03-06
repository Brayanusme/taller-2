print("============================================")
print("validacion de correo. ")
print("Crado por Brayan Usme Gaviria. ")
print("============================================")
correo = input("Ingrese un correo electrónico: ")

if " " in correo:
    print("Error: El correo no debe contener espacios.")

elif "@" not in correo or "." not in correo:
    print("Error: El correo debe contener '@' y '.'")

else:
    posicion_arroba = correo.find("@")
    posicion_punto = correo.rfind(".")

    if posicion_arroba == 0:
        print("Error: No puede comenzar con '@'.")

    elif posicion_arroba == len(correo) - 1:
        print("Error: No puede terminar con '@'.")

    elif posicion_punto < posicion_arroba:
        print("Error: El '.' debe estar después del '@'.")

    elif posicion_punto == len(correo) - 1:
        print("Error: No puede terminar con '.'")

    else:
        print("El correo tiene un formato básico correcto.")