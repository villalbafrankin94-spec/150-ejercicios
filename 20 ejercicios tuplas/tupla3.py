tupla = (1, 2, 3, 2, 4)
nueva = ()
for x in tupla:
    if x != 2:
        nueva += (x,)
print(nueva)  