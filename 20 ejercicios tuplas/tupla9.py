tupla = (2, 4, 1, 5, 3)
nueva = ()
for x in tupla:
    if x <= 3:
        nueva += (x,)
print(nueva) 