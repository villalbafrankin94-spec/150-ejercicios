tupla = (1, 2, 3)
nueva = ()
for _ in range(2):
    for x in tupla:
        nueva += (x,)
print(nueva)  