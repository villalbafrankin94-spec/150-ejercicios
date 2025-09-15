lista = [3, 7, 2, 9, 4]
i = 0
while i < len(lista):
    if lista[i] > 5:
        lista.pop(i)
    else:
        i += 1
print(lista)  