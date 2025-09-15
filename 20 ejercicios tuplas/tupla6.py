tupla = (1, 2, 3, 4, 5, 6)
nueva = ()
for x in tupla:
    if x % 2 == 0:
        nueva += (x,)
print(nueva)  