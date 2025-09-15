calificaciones = [8.5, 9.2, 7.8, 9.5, 6.9, 8.8, 9.1, 7.5]


aprobadas = list(filter(lambda x: x >= 7.0, calificaciones))
num_aprobadas = len(aprobadas)

print("Calificaciones del estudiante:", calificaciones)
print(f"\nMaterias aprobadas: {num_aprobadas} de {len(calificaciones)}")