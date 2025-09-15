from collections import Counter
import heapq

class NodoHuffman:
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    
    def __lt__(self, other):
        return self.freq < other.freq

def construir_arbol_huffman(texto):
    frecuencias = Counter(texto)
    cola_prioridad = [NodoHuffman(char, freq) for char, freq in frecuencias.items()]
    heapq.heapify(cola_prioridad)

    while len(cola_prioridad) > 1:
        nodo1 = heapq.heappop(cola_prioridad)
        nodo2 = heapq.heappop(cola_prioridad)
        nodo_combinado = NodoHuffman(None, nodo1.freq + nodo2.freq, nodo1, nodo2)
        heapq.heappush(cola_prioridad, nodo_combinado)

    return cola_prioridad[0]

def generar_codigos_huffman(arbol, prefijo="", codigos={}):
    if arbol.char is not None:
        codigos[arbol.char] = prefijo
    else:
        generar_codigos_huffman(arbol.left, prefijo + "0", codigos)
        generar_codigos_huffman(arbol.right, prefijo + "1", codigos)
    return codigos

def comprimir_huffman(texto):
    if not texto:
        return "", {}

    arbol = construir_arbol_huffman(texto)
    codigos = generar_codigos_huffman(arbol)

    texto_comprimido = "".join(codigos[char] for char in texto)
    return texto_comprimido, codigos

def descomprimir_huffman(texto_comprimido, codigos):
    if not texto_comprimido:
        return ""

    
    codigos_inverso = {v: k for k, v in codigos.items()}
    texto_descomprimido = []
    prefijo_actual = ""

    for bit in texto_comprimido:
        prefijo_actual += bit
        if prefijo_actual in codigos_inverso:
            texto_descomprimido.append(codigos_inverso[prefijo_actual])
            prefijo_actual = ""
    return "".join(texto_descomprimido)

print("SISTEMA DE COMPRESIÓN DE TEXTO (HUFFMAN)")
print("=" * 50)

texto_original = "abracadabra"
print(f"Texto original: '{texto_original}'")

texto_comprimido, codigos_huffman = comprimir_huffman(texto_original)
print(f"Códigos Huffman: {codigos_huffman}")
print(f"Texto comprimido: '{texto_comprimido}'")
print(f"Longitud original: {len(texto_original) * 8} bits (si cada char es 8 bits)")
print(f"Longitud comprimida: {len(texto_comprimido)} bits")

texto_descomprimido = descomprimir_huffman(texto_comprimido, codigos_huffman)
print(f"Texto descomprimido: '{texto_descomprimido}'")
print(f"Descompresión exitosa: {texto_original == texto_descomprimido}")