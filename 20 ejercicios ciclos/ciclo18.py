lista = [1, 2, 3, 4, 5]
for i in range(len(lista) - 1, -1, -1):
    if lista[i] % 2 == 0:
        lista.pop(i)
print(lista)  