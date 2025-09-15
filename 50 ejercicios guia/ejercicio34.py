import math

def calcular_distancia(ciudad1, ciudad2):
    x1, y1 = ciudad1
    x2, y2 = ciudad2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distancia, 2)

def calcular_distancia_total_ruta(ciudades, ruta_indices):
    distancia_total = 0
    for i in range(len(ruta_indices)):
        ciudad_actual = ciudades[ruta_indices[i]]
        siguiente_ciudad = cities[ruta_indices[(i + 1) % len(ruta_indices)]]
        distancia_total += calcular_distancia(ciudad_actual, siguiente_ciudad)
    return round(distancia_total, 2)

def algoritmo_vecino_mas_cercano(ciudades):
    """
    Implementa el algoritmo heurístico del Vecino Más Cercano para TSP.
    Comienza en una ciudad aleatoria y siempre va a la ciudad no visitada más cercana.
    """
    num_ciudades = len(ciudades)
    if num_ciudades < 2:
        return [0], 0.0

    mejor_ruta = []
    mejor_distancia = float('inf')

    
    for inicio_idx in range(num_ciudades):
        ruta_actual = [inicio_idx]
        visitadas = {inicio_idx}
        distancia_actual = 0
        ciudad_actual_idx = inicio_idx

        print(f"\nIniciando desde la ciudad {inicio_idx} ({ciudades[inicio_idx]}):")

        while len(visitadas) < num_ciudades:
            siguiente_ciudad_idx = -1
            min_distancia_a_vecino = float('inf')

            for i in range(num_ciudades):
                if i not in visitadas:
                    dist = calcular_distancia(ciudades[ciudad_actual_idx], ciudades[i])
                    print(f"  Desde {ciudad_actual_idx} a {i}: {dist}")
                    if dist < min_distancia_a_vecino:
                        min_distancia_a_vecino = dist
                        siguiente_ciudad_idx = i

            if siguiente_ciudad_idx != -1:
                ruta_actual.append(siguiente_ciudad_idx)
                visitadas.add(siguiente_ciudad_idx)
                distancia_actual += min_distancia_a_vecino
                ciudad_actual_idx = siguiente_ciudad_idx
            else:
                break

        
        distancia_actual += calcular_distancia(ciudades[ciudad_actual_idx], ciudades[inicio_idx])
        print(f"  Volviendo a la ciudad de inicio {inicio_idx}: {calcular_distancia(ciudades[ciudad_actual_idx], ciudades[inicio_idx])}")

        print(f"Ruta encontrada desde {inicio_idx}: {ruta_actual} -> {inicio_idx}, Distancia: {distancia_actual}")

        if distancia_actual < mejor_distancia:
            mejor_distancia = distancia_actual
            mejor_ruta = ruta_actual

    return mejor_ruta, mejor_distancia


cities = {
    0: (0, 0),
    1: (1, 5),
    2: (5, 1),
    3: (6, 6),
    4: (2, 3)
}

print("OPTIMIZADOR DE RUTAS (ALGORITMO VECINO MÁS CERCANO)")
print("=" * 60)
print("Ciudades:", cities)

mejor_ruta_nn, mejor_distancia_nn = algoritmo_vecino_mas_cercano(cities)

print(f"\nMejor ruta encontrada (Vecino Más Cercano): {mejor_ruta_nn}")
print(f"Distancia total: {mejor_distancia_nn}")