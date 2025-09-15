def saludar(nombre="Mundo"): 
    """Esta función saluda a una persona por su nombre, o al mundo si no se especifica."""
    mensaje = f"¡Hola {nombre}! ¿Cómo estás?"
    return mensaje

print("Usando mi función de saludo:")
print(saludar("Ana"))
print(saludar()) 