lista = [1, 2, 3]
for i in range(4, 7):
    lista[len(lista):] = [i]
print(lista)  