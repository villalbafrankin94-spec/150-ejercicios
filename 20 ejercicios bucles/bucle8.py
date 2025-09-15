lista = [1, 2, 3, 4, 5, 6]
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        lista[i] = 0
print(lista)  