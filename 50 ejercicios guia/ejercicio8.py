def clasificar_nota(nota):
    if nota >= 9.0:
        return "Excelente", "¡Felicidades! Sigue así"
    elif nota >= 7.0:
        return "Buena", "Buen trabajo, puedes mejorar"
    else:
        return "Necesita mejorar", "Estudia más para la próxima"

nota_estudiante = float(input("Introduce la calificación del estudiante: "))
clasificacion, mensaje = clasificar_nota(nota_estudiante)
print(f"Tu nota es: {nota_estudiante}")
print(f"Clasificación: {clasificacion}")
print(f"Comentario: {mensaje}")