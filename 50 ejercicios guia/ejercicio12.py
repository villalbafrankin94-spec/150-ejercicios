numero = int(input("¿De qué número quieres la tabla de multiplicar? "))
print(f"Tabla de multiplicar del {numero}:")
print("=" * 25)
for multiplicador in range(1, 11):
    resultado = numero * multiplicador
    print(f"{numero} x {multiplicador} = {resultado}")
print("=" * 25)
print("¡Tabla completa!")