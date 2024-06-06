# Reto_12_Michael_Mora

Desarrollo reto 12, según lo aprendido en clase con Strings.

Cada punto esta debidamente comentado, por lo que creo que a este punto del curso de PdC no es necesario una explicacion mas pricisa como las que he hecho en anteriores Retos.

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

_______________________________
FIN RETO
