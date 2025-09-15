def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp_valor = float(input("Introduce el valor de la temperatura: "))
unidad_origen = input("¿Es Celsius (C) o Fahrenheit (F)? ").upper()

if unidad_origen == 'C':
    resultado = celsius_a_fahrenheit(temp_valor)
    print(f"{temp_valor} grados Celsius equivalen a {resultado:.1f} grados Fahrenheit")
elif unidad_origen == 'F':
    resultado = fahrenheit_a_celsius(temp_valor)
    print(f"{temp_valor} grados Fahrenheit equivalen a {resultado:.1f} grados Celsius")
else:
    print("Unidad no reconocida. Por favor, usa 'C' o 'F'.")