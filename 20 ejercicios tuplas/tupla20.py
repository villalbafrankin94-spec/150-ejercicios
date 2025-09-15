tupla = ('manzana', 'pera', 'mango', 'uva')
nueva = ()
for x in tupla:
    if x.startswith('m'):
        nueva += (x.upper(),)
    else:
        nueva += (x,)
print(nueva)  