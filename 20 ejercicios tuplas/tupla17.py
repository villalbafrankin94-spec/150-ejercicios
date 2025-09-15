tupla = ('hola', 'mundo')
nueva = ()
for x in tupla:
    nueva += (x[::-1],)
print(nueva)  