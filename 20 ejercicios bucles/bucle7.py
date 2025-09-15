lista = ['a', 'c', 'e']
for i, letra in enumerate(['b', 'd']):
    lista.insert(2*i + 1, letra)
print(lista)  