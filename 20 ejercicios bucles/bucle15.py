lista = [1, 2, 3, 4, 5, 6]
i = 0
while i < len(lista):
    if lista[i] % 2 == 0:
        lista.remove(lista[i])
    else:
        i += 1
print(lista)  