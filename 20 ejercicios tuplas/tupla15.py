tupla = ('manzana', 'pera', 'uva', 'kiwi')
nueva = ()
for x in tupla:
    if 'a' in x:
        nueva += (x,)
print(nueva)  