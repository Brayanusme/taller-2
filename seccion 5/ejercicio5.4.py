def es_palindromo(texto):
    # Convertir a minúsculas
    texto = texto.lower()

    # Quitar espacios, signos de puntuación y caracteres especiales
    texto_limpio = ""
    for letra in texto:
        if letra.isalpha() or letra.isdigit():
            texto_limpio = texto_limpio + letra

    # Invertir el texto limpio
    texto_invertido = ""
    for i in range(len(texto_limpio) - 1, -1, -1):
        texto_invertido = texto_invertido + texto_limpio[i]

    # Comparar el texto limpio con el invertido
    if texto_limpio == texto_invertido:
        return True
    else:
        return False


# Pedir dato al usuario
texto = input("Ingresa una palabra o frase: ")

resultado = es_palindromo(texto)

if resultado == True:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")