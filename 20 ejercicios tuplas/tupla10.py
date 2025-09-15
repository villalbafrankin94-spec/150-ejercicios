tupla = ('a', 'b', 'c')
nueva = ()
for x in tupla:
    nueva += (x.upper(),)
print(nueva) 