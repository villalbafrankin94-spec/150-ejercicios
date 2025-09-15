from collections import Counter

animales = ["perro", "gato", "pájaro", "pez", "hamster", "conejo", "gato"]
print("Lista de animales:", animales)

animal_buscado = "gato"
conteo_animales = Counter(animales) 

if animal_buscado in conteo_animales:
    print(f"\n✅ {animal_buscado} está en la lista.")
    print(f"Aparece {conteo_animales[animal_buscado]} veces en total.")
else:
    print(f"\n❌ {animal_buscado} no está en la lista.")


buscados = ["gato", "serpiente", "pájaro"]
print(f"\nBuscando: {buscados}")
for animal in buscados:
    if animal in conteo_animales:
        print(f"✅ {animal} encontrado ({conteo_animales[animal]} veces).")
    else:
        print(f"❌ {animal} no encontrado.")