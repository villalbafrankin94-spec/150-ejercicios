import re

class AnalizadorDeTexto:
    def __init__(self, texto):
        self.texto = texto.lower() 

    def contar_palabras(self):
        palabras = re.findall(r'\b\w+\b', self.texto) 
        return len(palabras)

    def contar_caracteres(self, incluir_espacios=True):
        if incluir_espacios:
            return len(self.texto)
        else:
            return len(self.texto.replace(' ', ''))

    def es_palindromo(self):
        texto_limpio = re.sub(r'[^a-z0-9]', '', self.texto) 
        return texto_limpio == texto_limpio[::-1]

mi_texto = "Anita lava la tina. Esto es un ejemplo."
analizador = AnalizadorDeTexto(mi_texto)
print(f"Texto: '{mi_texto}'")
print(f"Palabras: {analizador.contar_palabras()}")
print(f"Caracteres (con espacios): {analizador.contar_caracteres()}")
print(f"¿Es palíndromo?: {analizador.es_palindromo()}")

palindromo_ej = "Anita lava la tina"
analizador_pal = AnalizadorDeTexto(palindromo_ej)
print(f"\nTexto: '{palindromo_ej}'")
print(f"¿Es palíndromo?: {analizador_pal.es_palindromo()}")