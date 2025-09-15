limite = int(input("¿Hasta qué número quieres buscar pares? "))
pares_encontrados = []
print(f"Buscando números pares entre 1 y {limite}:")
for numero in range(1, limite + 1):
    if numero % 2 == 0:
        pares_encontrados.append(numero)
print("Números pares:", pares_encontrados)
print(f"\nResumen: Se encontraron {len(pares_encontrados)} números pares.")