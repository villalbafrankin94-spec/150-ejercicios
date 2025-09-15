def ordenamiento_seleccion(lista):
    n = len(lista)
    lista_copia = lista.copy()
    comparaciones = 0
    intercambios = 0
    print(f"Lista original: {lista_copia}")
    print("\nProceso paso a paso (Selección):")

    for i in range(n):
        min_idx = i
        print(f"\n--- Pasada {i + 1} ---")
        print(f"Buscando el mínimo desde el índice {i} ({lista_copia[i]})")
        for j in range(i + 1, n):
            comparaciones += 1
            print(f"  Comparando {lista_copia[j]} con {lista_copia[min_idx]} (mínimo actual)")
            if lista_copia[j] < lista_copia[min_idx]:
                min_idx = j
                print(f"  Nuevo mínimo encontrado: {lista_copia[min_idx]} en índice {min_idx}")

        if min_idx != i:
            lista_copia[i], lista_copia[min_idx] = lista_copia[min_idx], lista_copia[i]
            intercambios += 1
            print(f"  Intercambio realizado: {lista_copia[i]} <-> {lista_copia[min_idx]} -> {lista_copia}")
        else:
            print(f"  No se necesita intercambio en esta pasada (el elemento ya está en su lugar).")
        print(f"Estado después de pasada {i + 1}: {lista_copia}")

    print(f"\nResultado final: {lista_copia}")
    print(f"Estadísticas:")
    print(f"  - Total de comparaciones: {comparaciones}")
    print(f"  - Total de intercambios: {intercambios}")
    return lista_copia

numeros = [64, 34, 25, 12, 22, 11, 90]
print("ALGORITMO DE ORDENAMIENTO POR SELECCIÓN")
print("=" * 50)
resultado = ordenamiento_seleccion(numeros)