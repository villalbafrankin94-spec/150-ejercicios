import re
from collections import Counter


class AnalizadorNLP:
    def __init__(self, texto):
        self.texto_original = texto
        self.texto_lower = texto.lower()
     

    def analizar_estructura(self):
      
        oraciones = re.split(r'[.!?]+', self.texto_original)
        oraciones = [s.strip() for s in oraciones if s.strip()]
        palabras = re.findall(r'\b\w+\b', self.texto_lower)

        parrafos = [p.strip() for p in self.texto_original.split('\n\n') if p.strip()]

        return {
            'caracteres_total': len(self.texto_original),
            'palabras': len(palabras),
            'oraciones': len(oraciones),
            'párrafos': len(parrafos)
        }

    def encontrar_entidades_nombradas(self):
       
        patron_nombre_propio = r'\b[A-Z][a-z]+\b'
        return list(set(re.findall(patron_nombre_propio, self.texto_original)))

    def encontrar_palabras_clave(self, n=5):
        palabras = re.findall(r'\b\w+\b', self.texto_lower)
        
        frecuencias = Counter(palabras) 
        return frecuencias.most_common(n)

    def analizar_sentimiento_avanzado(self):
        
        palabras_positivas = {'excelente', 'genial', 'feliz', 'increíble', 'bueno'}
        palabras_negativas = {'terrible', 'malo', 'triste', 'horrible', 'decepcionado'}

        palabras_en_texto = set(re.findall(r'\b\w+\b', self.texto_lower))

        puntuacion_positiva = len(palabras_en_texto.intersection(palabras_positivas))
        puntuacion_negativa = len(palabras_en_texto.intersection(palabras_negativas))

        if puntuacion_positiva > puntuacion_negativa:
            return "Positivo"
        elif puntuacion_negativa > puntuacion_positiva:
            return "Negativo"
        else:
            return "Neutral"

    def generar_resumen_nlp(self):
        estructura = self.analizar_estructura()
        palabras_clave = self.encontrar_palabras_clave(3)
        sentimiento = self.analizar_sentimiento_avanzado()

        resumen = [
            f"Análisis del texto:",
            f"- Caracteres totales: {estructura['caracteres_total']}",
            f"- Palabras: {estructura['palabras']}",
            f"- Oraciones: {estructura['oraciones']}",
            f"- Párrafos: {estructura['párrafos']}",
            f"- Sentimiento general: {sentimiento}",
            f"- Palabras clave principales: {', '.join([p[0] for p in palabras_clave])}"
        ]
        return "\n".join(resumen)

texto_ejemplo = """
La programación es excelente y muy divertida. Me encanta resolver problemas.
Aunque a veces es un poco frustrante, el resultado final es increíble.
Este es un buen ejemplo de texto.
"""
analizador = AnalizadorNLP(texto_ejemplo)
print("ANALIZADOR DE TEXTO (ENFOQUE NLP BÁSICO)")
print("=" * 50)
print(analizador.generar_resumen_nlp())