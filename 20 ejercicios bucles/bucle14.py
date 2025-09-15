lista = [0, 0, 0, 0, 0, 0]
for i in range(0, len(lista), 2):
    lista[i:i+2] = [1, 2]
print(lista) 