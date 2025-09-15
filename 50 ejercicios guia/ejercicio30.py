def calcular_similitud_jaccard(gustos1, gustos2):
    """
    Calcula la similitud entre dos usuarios usando el coeficiente de Jaccard.
    Jaccard = (Intersección de gustos True) / (Unión de gustos True)
    """
    set1_true = {k for k, v in gustos1.items() if v}
    set2_true = {k for k, v in gustos2.items() if v}

    interseccion = len(set1_true.intersection(set2_true))
    union = len(set1_true.union(set2_true))

    if union == 0:
        return 0.0 
    return round(interseccion / union, 2)

def encontrar_usuarios_similares_jaccard(usuario_objetivo, base_usuarios, umbral=0.3):
    similares = []
    print(f"Buscando usuarios similares a '{usuario_objetivo}' (Jaccard)")
    print(f"Umbral de similitud: {umbral}")
    print("-" * 40)
    gustos_objetivo = base_usuarios[usuario_objetivo]

    for nombre_usuario, gustos_usuario in base_usuarios.items():
        if nombre_usuario != usuario_objetivo:
            similitud = calcular_similitud_jaccard(gustos_objetivo, gustos_usuario)
            print(f"  {nombre_usuario}: similitud Jaccard = {similitud}")
            if similitud >= umbral:
                similares.append((nombre_usuario, similitud))

    similares.sort(key=lambda x: x[1], reverse=True)
    return similares


usuarios = {
    "Ana": {"acción": True, "comedia": True, "drama": False, "terror": False, "ciencia_ficción": True},
    "Carlos": {"acción": True, "comedia": False, "drama": True, "terror": False, "ciencia_ficción": True},
    "María": {"acción": False, "comedia": True, "drama": True, "terror": True, "ciencia_ficción": False},
    "Pedro": {"acción": True, "comedia": True, "drama": False, "terror": False, "ciencia_ficción": False},
    "Laura": {"acción": False, "comedia": True, "drama": True, "terror": False, "ciencia_ficción": True}
}

print("SISTEMA DE RECOMENDACIONES (JACCARD)")
print("=" * 40)

usuario_objetivo = "Ana"
similares = encontrar_usuarios_similares_jaccard(usuario_objetivo, usuarios, 0.4)

print(f"\nUsuarios similares a {usuario_objetivo}:")
for similar, similitud in similares:
    print(f"  - {similar}: {similitud * 100:.0f}% similar")