from datetime import datetime

libros = []
usuarios = []
prestamos = []

def registrar_libro():
    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    categoria = input("Categoría: ")
    estado = "Disponible"
    libro = {
        "id": len(libros) + 1,
        "titulo": titulo,
        "autor": autor,
        "categoria": categoria,
        "estado": estado
    }
    libros.append(libro)
    print(" Libro registrado.")

def registrar_usuario():
    nombre = input("Nombre del usuario: ")
    documento = input("Documento: ")
    correo = input("Correo: ")
    usuario = {
        "id": len(usuarios) + 1,
        "nombre": nombre,
        "documento": documento,
        "correo": correo
    }
    usuarios.append(usuario)
    print(" Usuario registrado.")

def realizar_prestamo():
    id_usuario = int(input("ID del usuario: "))
    id_libro = int(input("ID del libro: "))
    fecha_prestamo = datetime.now().strftime("%Y-%m-%d")
    fecha_devolucion = input("Fecha estimada de devolución (YYYY-MM-DD): ")

    libro = next((l for l in libros if l["id"] == id_libro), None)
    if libro and libro["estado"] == "Disponible":
        libro["estado"] = "Prestado"
        prestamo = {
            "id": len(prestamos) + 1,
            "id_usuario": id_usuario,
            "id_libro": id_libro,
            "fecha_prestamo": fecha_prestamo,
            "fecha_devolucion": fecha_devolucion,
            "estado": "Activo"
        }
        prestamos.append(prestamo)
        print(" Préstamo registrado.")
    else:
        print(" Libro no disponible.")

def registrar_devolucion():
    id_prestamo = int(input("ID del préstamo: "))
    prestamo = next((p for p in prestamos if p["id"] == id_prestamo), None)
    if prestamo and prestamo["estado"] == "Activo":
        prestamo["estado"] = "Finalizado"
        libro = next((l for l in libros if l["id"] == prestamo["id_libro"]), None)
        if libro:
            libro["estado"] = "Disponible"
        print(" Devolución registrada.")
    else:
        print(" Préstamo no encontrado o ya finalizado.")


def consultar_libros_disponibles():
    disponibles = [l for l in libros if l["estado"] == "Disponible"]
    print("\n Libros disponibles:")
    for l in disponibles:
        print(f"{l['id']}. {l['titulo']} - {l['autor']} ({l['categoria']})")

def generar_reporte_prestamos():
    print("\n📋 Reporte de préstamos:")
    for p in prestamos:
        usuario = next((u for u in usuarios if u["id"] == p["id_usuario"]), {})
        libro = next((l for l in libros if l["id"] == p["id_libro"]), {})
        print(f"Préstamo #{p['id']}: {usuario.get('nombre')} → {libro.get('titulo')} | {p['fecha_prestamo']} → {p['fecha_devolucion']} | Estado: {p['estado']}")

def menu():
    while True:
        print("\n MENÚ PRINCIPAL")
        print("1. Registrar libro")
        print("2. Registrar usuario")
        print("3. Realizar préstamo")
        print("4. Registrar devolución")
        print("5. Consultar libros disponibles")
        print("6. Generar reporte de préstamos")
        print("7. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            registrar_usuario()
        elif opcion == "3":
            realizar_prestamo()
        elif opcion == "4":
            registrar_devolucion()
        elif opcion == "5":
            consultar_libros_disponibles()
        elif opcion == "6":
            generar_reporte_prestamos()
        elif opcion == "7":
            print(" ¡Hasta luego!")
            break
        else:
            print(" Opción inválida.")

menu()
