tupla = (1, -2, 3, -4)
nueva = ()
for x in tupla:
    nueva += (-x,)
print(nueva)  