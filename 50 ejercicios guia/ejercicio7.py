def calcular_descuento(precio_total):
    if precio_total > 200:
        return precio_total * 0.15  
    elif precio_total > 100:
        return precio_total * 0.10 
    else:
        return 0

precio_compra = float(input("Introduce el total de la compra: $"))
descuento_aplicado = calcular_descuento(precio_compra)
precio_final = precio_compra - descuento_aplicado

if descuento_aplicado > 0:
    print(f"¡Felicidades! Tienes un descuento de ${descuento_aplicado:.2f}")
else:
    print("No hay descuento disponible para este monto.")
print(f"Precio original: ${precio_compra:.2f}")
print(f"Precio final: ${precio_final:.2f}")