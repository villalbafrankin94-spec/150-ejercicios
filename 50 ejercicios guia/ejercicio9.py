numero_secreto = 7
intentos = 0
adivinado = False

print("¡Adivina el número secreto entre 1 y 10!")
while not adivinado:
    try:
        adivinanza = int(input("Tu adivinanza: "))
        intentos += 1
        if adivinanza == numero_secreto:
            print(f"¡FELICIDADES! Adivinaste el número en {intentos} intentos.")
            adivinado = True
        elif adivinanza < numero_secreto:
            print("Tu número es menor. Intenta con uno más grande.")
        else:
            print("Tu número es mayor. Intenta con uno más pequeño.")
    except ValueError:
        print("Por favor, introduce un número válido.")