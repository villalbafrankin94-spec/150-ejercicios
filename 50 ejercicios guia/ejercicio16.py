colores_input = input("Introduce tus colores favoritos separados por comas: ")
colores = [c.strip() for c in colores_input.split(',')] 

print("Mis colores favoritos son:")
print("Lista completa:", ", ".join(colores))
print("Total de colores:", len(colores))
if colores:
    print("Primer color:", colores[0])
    print("Último color:", colores[-1])