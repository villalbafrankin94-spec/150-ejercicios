def ordenamiento_burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

numeros = [64, 34, 25, 12, 22, 11, 90]
print("Lista original:", numeros)

numeros_ordenados = ordenamiento_burbuja(numeros.copy())
print("Ordenada ascendente (Burbuja):", numeros_ordenados)


numeros_descendente = ordenamiento_burbuja(numeros.copy())
numeros_descendente.reverse()
print("Ordenada descendente (Burbuja + Reverse):", numeros_descendente)