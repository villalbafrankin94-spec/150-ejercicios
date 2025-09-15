tupla = (0, 1, '', 'texto')
nueva = ()
for x in tupla:
    nueva += (bool(x),)
print(nueva) 