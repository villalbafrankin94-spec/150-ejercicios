limite = int(input("¿Hasta qué número quieres sumar? "))
numeros_a_sumar = list(range(1, limite + 1)) 
suma_total = sum(numeros_a_sumar) 

print(f"Sumando números del 1 al {limite}...")
print(f"\nResultado final: La suma de todos los números del 1 al {limite} es: {suma_total}")