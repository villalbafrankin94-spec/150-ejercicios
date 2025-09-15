import random
import string

def generar_y_evaluar_contrasena(longitud=10, incluir_mayusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = string.ascii_lowercase
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += "!@#$%^&*()_+-=[]{}|;:,.<>?/~"

    if not caracteres:
        return "Error: No hay caracteres para generar la contraseña.", "Débil", []

    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

  
    puntos = 0
    comentarios = []

    if len(contrasena) >= 8:
        puntos += 2
        comentarios.append("✅ Longitud adecuada")
    else:
        comentarios.append("❌ Muy corta (mínimo 8 caracteres)")

    if any(c.isupper() for c in contrasena):
        puntos += 1
        comentarios.append("✅ Contiene mayúsculas")
    else:
        comentarios.append("❌ Sin mayúsculas")

    if any(c.isdigit() for c in contrasena):
        puntos += 1
        comentarios.append("✅ Contiene números")
    else:
        comentarios.append("❌ Sin números")

    if any(not c.isalnum() for c in contrasena):
        puntos += 1
        comentarios.append("✅ Contiene símbolos")
    else:
        comentarios.append("❌ Sin símbolos")

    if puntos >= 4:
        fortaleza = "Muy fuerte"
    elif puntos >= 3:
        fortaleza = "Fuerte"
    elif puntos >= 2:
        fortaleza = "Moderada"
    else:
        fortaleza = "Débil"

    return contrasena, fortaleza, comentarios

print("GENERADOR Y EVALUADOR DE CONTRASEÑAS")
print("=" * 40)

contrasena_generada, fortaleza_final, comentarios_final = generar_y_evaluar_contrasena(12, True, True, True)
print(f"\nContraseña generada: {contrasena_generada}")
print(f"Fortaleza: {fortaleza_final}")
for c in comentarios_final:
    print(f"  {c}")