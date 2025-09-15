inventario = {
    "manzanas": {"precio": 1000, "stock": 10},
    "bananos": {"precio": 800, "stock": 15},
    "pan": {"precio": 1500, "stock": 20},
    "leche": {"precio": 2500, "stock": 8}
}

carrito = {}

def mostrar_inventario():
    print("\n Productos disponibles:")
    for producto, datos in inventario.items():
        print(f"- {producto.title()} | Precio: ${datos['precio']} | Stock: {datos['stock']}")

def agregar_al_carrito():
    producto = input("Producto a agregar: ").lower()
    if producto in inventario:
        cantidad = int(input("Cantidad: "))
        if cantidad <= inventario[producto]["stock"]:
            carrito[producto] = carrito.get(producto, 0) + cantidad
            inventario[producto]["stock"] -= cantidad
            print(f" {cantidad} {producto} agregado(s) al carrito.")
        else:
            print(" No hay suficiente stock.")
    else:
        print(" Producto no encontrado.")

def ver_carrito():
    print("\n Carrito de compras:")
    if not carrito:
        print("Carrito vacío.")
        return
    total = 0
    for producto, cantidad in carrito.items():
        precio_unitario = inventario[producto]["precio"]
        subtotal = precio_unitario * cantidad
        total += subtotal
        print(f"- {producto.title()} x{cantidad} = ${subtotal}")
    print(f" Total: ${total}")

def procesar_pedido():
    if not carrito:
        print(" No hay productos en el carrito.")
        return
    print("\n Procesando pedido...")
    ver_carrito()
    print(" Pedido confirmado. ¡Gracias por tu compra!")
    carrito.clear()

def menu():
    while True:
        print("\n MENÚ PRINCIPAL")
        print("1. Ver inventario")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Procesar pedido")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            mostrar_inventario()
        elif opcion == "2":
            agregar_al_carrito()
        elif opcion == "3":
            ver_carrito()
        elif opcion == "4":
            procesar_pedido()
        elif opcion == "5":
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción inválida.")

menu()
