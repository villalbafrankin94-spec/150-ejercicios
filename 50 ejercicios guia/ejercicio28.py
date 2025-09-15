from collections import Counter

def contar_frecuencias_counter(lista):
    """
    Cuenta la frecuencia de cada elemento en la lista usando collections.Counter.
    Retorna un objeto Counter (que se comporta como un diccionario).
    """
    print(f"Analizando lista: {lista}")
    frecuencias = Counter(lista)
    return frecuencias

def mostrar_estadisticas_counter(frecuencias):
    """Muestra estadísticas detalladas de un objeto Counter."""
    print("\n" + "=" * 40)
    print("ESTADÍSTICAS DE FRECUENCIA (CON COUNTER)")
    print("=" * 40)

    total_elementos = sum(frecuencias.values())
    elementos_unicos = len(frecuencias)
    print(f"Total de elementos: {total_elementos}")
    print(f"Elementos únicos: {elementos_unicos}")

    print("\nFrecuencias (ordenadas por cantidad):")
    
    for elemento, frecuencia in frecuencias.most_common():
        porcentaje = (frecuencia / total_elementos) * 100
        barra = "█" * frecuencia 
        print(f"  {elemento:>3}: {frecuencia:>2} veces ({porcentaje:4.1f}%) {barra}")

    if frecuencias:
        mas_frecuente, max_freq = frecuencias.most_common(1)[0]
        print(f"\nElemento más frecuente: {mas_frecuente} ({max_freq} veces)")

print("CONTADOR DE FRECUENCIAS (CON COUNTER)")
print("=" * 30)

numeros = [1, 2, 3, 2, 1, 4, 2, 5, 2, 1, 3, 2]
frecuencias_num = contar_frecuencias_counter(numeros)
mostrar_estadisticas_counter(frecuencias_num)

texto = "programacion"
letras = list(texto)
print(f"\nAnalizando la palabra: '{texto}'")
frecuencias_letras = contar_frecuencias_counter(letras)
mostrar_estadisticas_counter(frecuencias_letras)