inventario = [
    {"nombre": "teclado", "precio": 25.50, "stock": 10},
    {"nombre": "mouse", "precio": 15.00, "stock": 20},
    {"nombre": "monitor", "precio": 150.00, "stock": 5}
]

busqueda = input("Ingrese el nombre del producto a actualizar: ").lower().strip()
encontrado = False

for producto in inventario:
    if producto["nombre"] == busqueda:
        print(f"Producto encontrado. Precio actual: ${producto['precio']}")
        
        nuevo_precio = float(input("Ingrese el nuevo precio: "))
        producto["precio"] = nuevo_precio
        
        encontrado = True
        print(" ¡Precio actualizado con éxito!")
        break  

if not encontrado:
    print(" Lo sentimos, el producto no está en el inventario.")

print("\nInventario actualizado:")
for p in inventario:
    print(f"- {p['nombre'].capitalize()}: ${p['precio']} (Stock: {p['stock']})")