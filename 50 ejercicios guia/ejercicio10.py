def validar_contrasena(contrasena):
    longitud_minima = 8
    tiene_mayuscula = any(c.isupper() for c in contrasena)
    tiene_minuscula = any(c.islower() for c in contrasena)
    tiene_numero = any(c.isdigit() for c in contrasena)
    tiene_simbolo = any(not c.isalnum() for c in contrasena) 

    if len(contrasena) < longitud_minima:
        return "La contraseña es muy corta (mínimo 8 caracteres)."
    if not tiene_mayuscula:
        return "La contraseña debe contener al menos una letra mayúscula."
    if not tiene_minuscula:
        return "La contraseña debe contener al menos una letra minúscula."
    if not tiene_numero:
        return "La contraseña debe contener al menos un número."
    if not tiene_simbolo:
        return "La contraseña debe contener al menos un símbolo."
    return "La contraseña es segura."

contrasena_usuario = input("Introduce tu contraseña: ")
print(validar_contrasena(contrasena_usuario))