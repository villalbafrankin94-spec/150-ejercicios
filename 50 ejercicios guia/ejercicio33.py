import random
import time
import os 

def crear_tablero(filas, columnas, densidad=0.3):
    tablero = []
    for _ in range(filas):
        fila = [1 if random.random() < densidad else 0 for _ in range(columnas)]
        tablero.append(fila)
    return tablero

def contar_vecinos_vivos(tablero, fila, columna):
    filas = len(tablero)
    columnas = len(tablero[0])
    vecinos_vivos = 0
    for df in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if df == 0 and dc == 0:
                continue
            nueva_fila, nueva_columna = fila + df, columna + dc
            if 0 <= nueva_fila < filas and 0 <= nueva_columna < columnas:
                vecinos_vivos += tablero[nueva_fila][nueva_columna]
    return vecinos_vivos

def aplicar_reglas(tablero):
    filas = len(tablero)
    columnas = len(tablero[0])
    nuevo_tablero = [[0 for _ in range(columnas)] for _ in range(filas)]

    for i in range(filas):
        for j in range(columnas):
            vecinos = contar_vecinos_vivos(tablero, i, j)
            celula_actual = tablero[i][j]

            if celula_actual == 1: 
                if vecinos < 2 or vecinos > 3:
                    nuevo_tablero[i][j] = 0 
                else:
                    nuevo_tablero[i][j] = 1
            else: 
                if vecinos == 3:
                    nuevo_tablero[i][j] = 1 
    return nuevo_tablero

def mostrar_tablero_visual(tablero, generacion):
    os.system('cls' if os.name == 'nt' else 'clear') 
    print(f"--- Juego de la Vida de Conway ---")
    print(f"Generación: {generacion}")
    print("-" * (len(tablero[0]) * 2 + 2))
    for fila in tablero:
        print("|" + "".join(["██" if cell == 1 else "  " for cell in fila]) + "|")
    print("-" * (len(tablero[0]) * 2 + 2))

def simular_juego_de_la_vida(filas, columnas, generaciones, densidad_inicial=0.3, velocidad=0.5):
    tablero = crear_tablero(filas, columnas, densidad_inicial)
    for gen in range(generaciones):
        mostrar_tablero_visual(tablero, gen)
        tablero = aplicar_reglas(tablero)
        time.sleep(velocidad) 


def crear_patron_glider(filas, columnas):
    tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
    if filas >= 3 and columnas >= 3:
        tablero[0][1] = 1
        tablero[1][2] = 1
        tablero[2][0] = 1
        tablero[2][1] = 1
        tablero[2][2] = 1
    return tablero

print("JUEGO DE LA VIDA DE CONWAY (VISUALIZADO)")
print("=" * 40)



filas_glider, columnas_glider = 10, 10
tablero_glider = crear_patron_glider(filas_glider, columnas_glider)
print("\nSimulando Glider:")
for gen in range(15):
    mostrar_tablero_visual(tablero_glider, gen)
    tablero_glider = aplicar_reglas(tablero_glider)
    time.sleep(0.3)