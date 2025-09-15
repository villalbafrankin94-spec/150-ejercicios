def calculadora(num1, num2, operacion):
    """Realiza una operación matemática básica entre dos números."""
    if operacion == '+':
        return num1 + num2
    elif operacion == '-':
        return num1 - num2
    elif operacion == '*':
        return num1 * num2
    elif operacion == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: No se puede dividir entre cero"
    else:
        return "Operación no válida"

num1 = 15
num2 = 3
print("CALCULADORA CON UNA FUNCIÓN ÚNICA")
print(f"{num1} + {num2} = {calculadora(num1, num2, '+')}")
print(f"{num1} / 0 = {calculadora(num1, 0, '/')}")