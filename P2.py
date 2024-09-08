
# Reto 12 - programa

import requests # verificar que 'request' esta instalado, si no instalarlo
from collections import Counter
import string

# descargar el contenido de la pagina/archivo 

url = 'https://www.py4e.com/code3/mbox.txt'
response = requests.get(url)
texto = response.text

# definir vocales y consonantes

vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

# inicializar contadores
contador_vocales = 0
contador_consonantes = 0

# contar vocales y consonantes
for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1
    elif caracter in consonantes:
        contador_consonantes += 1

# remover signos de puntuacion para la parte de contar palabras, en este caso no seria necesario porque esta en ingles

translator = str.maketrans('', '', string.punctuation)
texto_limpio = texto.translate(translator)

# convertir el texto a minusculas y dividir en palabras

palabras = texto_limpio.lower().split()

# contar frecuencia de palabras
contador_palabras = Counter(palabras)


# obtener las 50 palabras más comunes

palabras_comunes = contador_palabras.most_common(50)

# imprimir resultados 1 , 2 , 3

print(f"Cantidad de vocales: {contador_vocales}") #1

print(f"Cantidad de consonantes: {contador_consonantes}") #2

print("\nLas 50 palabras que más se repiten son:") #3

for palabra, frecuencia in palabras_comunes:
    print(f"{palabra}: {frecuencia}")
