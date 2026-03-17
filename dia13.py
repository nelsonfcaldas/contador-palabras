import re

from collections import Counter

with open("texto.txt", "r") as f:
    contenido = f.read().lower()

# Quitar signos de puntuación
palabras = re.findall(r"\b\w+\b", contenido)

contador = Counter(palabras)
for palabra, freq in contador.most_common(10):
    print(palabra, ":", freq)

