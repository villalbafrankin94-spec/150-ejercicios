import bisect

def busqueda_bisect(lista_ordenada, elemento_buscado):
    """
    Implementa búsqueda binaria usando el módulo 'bisect' de Python.
    La lista debe estar ordenada previamente.
    """
    print(f"Buscando {elemento_buscado} en: {lista_ordenada}")
   
    posicion = bisect.bisect_left(lista_ordenada, elemento_buscado)

    if posicion < len(lista_ordenada) and lista_ordenada[posicion] == elemento_buscado:
        print(f"✅ ¡Encontrado! {elemento_buscado} está en posición {posicion} (usando bisect).")
        return posicion
    else:
        print(f"❌ {elemento_buscado} no está en la lista (usando bisect).")
        return -1

numeros_ordenados = [11, 22, 25, 34, 44, 55, 66, 77, 88, 99]
buscar = 55
print("BÚSQUEDA BINARIA CON MÓDULO BISECT")
print("=" * 45)
busqueda_bisect(numeros_ordenados, buscar)
busqueda_bisect(numeros_ordenados, 42) 