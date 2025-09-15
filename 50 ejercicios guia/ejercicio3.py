def calcular_area_rectangulo(base, altura):
    return base * altura

base_rect = float(input("Introduce la base del rectángulo: "))
altura_rect = float(input("Introduce la altura del rectángulo: "))
area_calculada = calcular_area_rectangulo(base_rect, altura_rect)
print(f"Rectángulo de {base_rect}x{altura_rect}")
print(f"El área es: {area_calculada} unidades cuadradas")