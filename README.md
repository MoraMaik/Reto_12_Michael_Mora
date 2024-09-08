# Reto_12_Michael_Mora

Desarrollo reto 12, según lo aprendido en clase con Strings.

El punto dos esta debidamente comentado y con una breve explicacion de mi parte.

_______________________________
## **Punto 1**

**Instrucciones:** Consulte que hacen los siguientes métodos de strings en python: endswith, startswith, isalpha, isalnum, isdigit, isspace, istitle, islower, isupper.

### 1. `endswith`

+ Descripción: Verifica si una cadena termina con una subcadena especificada.
+ Sintaxis: `str.endswith(suffix[, start[, end]])`
+ Ejemplo:

```Python
s = "Hola Mundo"
resultado = s.endswith("Mundo")  # True
```

### 2. `startswith`

+ Descripción: Verifica si una cadena comienza con una subcadena especificada.
+ Sintaxis: `str.startswith(prefix[, start[, end]])`
+ Ejemplo:

```Python
s = "Hola Mundo"
resultado = s.startswith("Hola")  # True
```

### 3. `isalpha`

+ Descripción: Verifica si todos los caracteres en la cadena son alfabéticos (letras) y no están vacíos.
+ Sintaxis: `str.isalpha()`
+ Ejemplo:

```Python
s = "Hola"
resultado = s.isalpha()  # True

s = "Hola123"
resultado = s.isalpha()  # False
```

### 4. `isalnum`

+ Descripción: Verifica si todos los caracteres en la cadena son alfanuméricos (letras o números) y no están vacíos.
+ Sintaxis: `str.isalnum()`
+ Ejemplo:

```python
s = "Hola123"
resultado = s.isalnum()  # True

s = "Hola 123"
resultado = s.isalnum()  # False (por el espacio)
```

### 5. `isdigit`

+ Descripción: Verifica si todos los caracteres en la cadena son dígitos (números) y no están vacíos.
+ Sintaxis: `str.isdigit()`
+ Ejemplo:

```python
s = "12345"
resultado = s.isdigit()  # True

s = "123a"
resultado = s.isdigit()  # False
```

### 6. `isspace`

+ Descripción: Verifica si todos los caracteres en la cadena son espacios en blanco (espacios, tabulaciones, saltos de línea) y no están vacíos.
+ Sintaxis: `str.isspace()`
+ Ejemplo:

```python
s = "   "
resultado = s.isspace()  # True

s = "Hola Mundo"
resultado = s.isspace()  # False

```

### 7. `istitle`

+ Descripción: Verifica si la cadena sigue las reglas de un título (cada palabra comienza con una letra mayúscula seguida de letras minúsculas).
+ Sintaxis: `str.istitle()`
+ Ejemplo:

```python
s = "Hola Mundo"
resultado = s.istitle()  # True

s = "hola Mundo"
resultado = s.istitle()  # False
```

### 8. `islower`

+ Descripción: Verifica si todos los caracteres en la cadena están en minúsculas y hay al menos un carácter que sea una letra.
+ Sintaxis: `str.islower()`
+ Ejemplo:

```python
s = "hola mundo"
resultado = s.islower()  # True

s = "Hola Mundo"
resultado = s.islower()  # False

```

### 9. `isupper`

+ Descripción: Verifica si todos los caracteres en la cadena están en mayúsculas y hay al menos un carácter que sea una letra.
+ Sintaxis: `str.isupper()`
+ Ejemplo:

```python
s = "HOLA MUNDO"
resultado = s.isupper()  # True

s = "Hola Mundo"
resultado = s.isupper()  # False

```

_______________________________
## **Punto 2**

**Instrucciones:** Procesar el [archivo](http://https://www.py4e.com/code3/mbox.txt "archivo")
 y extraer:

+ Cantidad de vocales
+ Cantidad de consonantes
+ Listado de las 50 palabras que más se repiten

### Desarrollo
Como contar manualmente esto tomaria bastante tiempo, vamos a desarrollar un script para procesar el contenido de la página y extraer la cantidad de vocales, consonantes y el listado de las 50 palabras que más se repiten. Para esto, seguiremos estos pasos:

1. Descargar el contenido de la página.
2. Contar la cantidad de vocales y consonantes.
3. Encontrar las 50 palabras más repetidas.
   
 **Paso 1**: Descargar el contenido de la página
Podemos usar el módulo `requests` para descargar el contenido de la página.

Aqui es importante indicar que si no lo tienes instalado ejecutes esto:

```python
pip install requests
```
En dado caso que ya este instalado verificalo ejecutando esto:

```python
import requests
print(requests.__version__)
```
Si  no arroja errores, `requests` está instalado correctamente. Si hay un error, significará que la instalación no se realizó correctamente.

  **Paso 2**: Contar la cantidad de vocales y consonantes
  
Definimos las vocales y consonantes, y luego iteramos sobre el contenido del texto para contar las ocurrencias de cada una.

**Paso 3**: Encontrar las 50 palabras más repetidas

Usamos el módulo `collections` para contar la frecuencia de las palabras.

#### Programa:

```python

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

```

**Explicacion**:

1. Descargar el contenido:

+ Usamos `requests.get(url)` para obtener el contenido de la pagina.
+ Guardamos el contenido en la variable `texto`.

2. Contar vocales y consonantes:

+ iteramos sobre cada caracter del texto.
+ incrementamos los contadores `contador_vocales` y `contador_consonantes` según corresponda.

3. Remover signos de puntuación y contar palabras:

+ Utilizamos `str.maketrans` y `str.translate` para remover signos de puntuacion.
+ convertimos el texto a minúsculas y lo dividimos en palabras usando `split()`.
+ usamos `Counter` para contar la frecuencia de cada palabra.
+ Obtenemos las 50 palabras más comunes con `most_common(50)`.


_______________________________
FIN RETO
