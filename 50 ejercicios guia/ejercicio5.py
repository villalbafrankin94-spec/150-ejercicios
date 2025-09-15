calificaciones = []
for i in range(3):
    nota = float(input(f"Introduce la calificación {i+1}: "))
    calificaciones.append(nota)

suma_notas = sum(calificaciones)
promedio = suma_notas / len(calificaciones)
print("Calificaciones:", *calificaciones) 
print(f"Promedio: {promedio:.2f}")