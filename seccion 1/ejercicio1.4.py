print("--- Validador de Contraseña ---")
password = input("Escribe tu contraseña: ")

tiene_ocho = len(password) >= 8
tiene_mayuscula = False
tiene_numero = False
tiene_especial = False

especiales = "!@#$%^&*"

for letra in password:
    if letra.isupper():
        tiene_mayuscula = True
    
    if letra.isdigit():
        tiene_numero = True
        
    if letra in especiales:
        tiene_especial = True

print("\nResultado del análisis:")

if tiene_ocho and tiene_mayuscula and tiene_numero and tiene_especial:
    print("¡Perfecto! Tu contraseña es segura.")
else:
    print("Tu contraseña necesita mejorar:")
    
    if not tiene_ocho:
        print("- Debe tener al menos 8 caracteres")
    if not tiene_mayuscula:
        print("- Le falta una letra mayúscula")
    if not tiene_numero:
        print("- Le falta al menos un número")
    if not tiene_especial:
        print("- Le falta un carácter especial (!@#$%^&*)")