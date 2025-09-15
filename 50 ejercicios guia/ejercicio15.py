import random
numero_secreto = random.randint(1, 10) 
intentos_maximos = 3
adivinado = False

print("¡Bienvenido al juego de adivinanza!")
print(f"Tienes {intentos_maximos} intentos para adivinar el número del 1 al 10")

for intento_actual in range(1, intentos_maximos + 1):
    print(f"\n--- Intento {intento_actual} de {intentos_maximos} ---")
    try:
        adivinanza = int(input("Tu adivinanza: "))
        if adivinanza == numero_secreto:
            print(f"¡GANASTE! El número era {numero_secreto}")
            adivinado = True
            break
        elif adivinanza < numero_secreto:
            print("El número es mayor")
        else:
            print("El número es menor")
    except ValueError:
        print("Entrada inválida. Por favor, introduce un número.")

if not adivinado:
    print(f"\n¡Se acabaron los intentos! El número era {numero_secreto}")