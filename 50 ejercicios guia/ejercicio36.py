import math

def mostrar_menu():
    print("\n CALCULADORA AVANZADA")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Factorial")
    print("8. Salir")

def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-8): ")

        if opcion == "1":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", a + b)

        elif opcion == "2":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", a - b)

        elif opcion == "3":
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
            print("Resultado:", a * b)

        elif opcion == "4":
            a = float(input("Ingresa el dividendo: "))
            b = float(input("Ingresa el divisor: "))
            if b != 0:
                print("Resultado:", a / b)
            else:
                print(" Error: No se puede dividir por cero.")

        elif opcion == "5":
            base = float(input("Ingresa la base: "))
            exponente = float(input("Ingresa el exponente: "))
            print("Resultado:", math.pow(base, exponente))

        elif opcion == "6":
            num = float(input("Ingresa el número: "))
            if num >= 0:
                print("Resultado:", math.sqrt(num))
            else:
                print(" Error: No se puede calcular la raíz de un número negativo.")

        elif opcion == "7":
            num = int(input("Ingresa un número entero: "))
            if num >= 0:
                print("Resultado:", math.factorial(num))
            else:
                print(" Error: No se puede calcular el factorial de un número negativo.")

        elif opcion == "8":
            print(" ¡Hasta luego!")
            break

        else:
            print(" Opción inválida. Intenta de nuevo.")

calculadora()