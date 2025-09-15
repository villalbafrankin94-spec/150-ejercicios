import math

def es_primo_optimizada(numero):
    """
    Verifica si un número es primo usando una optimización:
    solo se verifica la divisibilidad hasta la raíz cuadrada del número.
    """
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0: 
        return False

    print(f"Verificando si {numero} es primo (optimizado):")
   
    for i in range(3, int(math.sqrt(numero)) + 1, 2):
        print(f"  ¿{numero} es divisible por {i}? ", end="")
        if numero % i == 0:
            print(f"Sí ({numero} / {i} = {numero // i})")
            return False
        else:
            print("No")
    print(f"  ✅ {numero} es primo")
    return True

print("GENERADOR DE NÚMEROS PRIMOS (VERIFICACIÓN OPTIMIZADA)")
print("=" * 60)

numeros_probar = [17, 25, 29, 97, 100]
for num in numeros_probar:
    resultado = es_primo_optimizada(num)
    print(f"Resultado para {num}: {resultado}\n")