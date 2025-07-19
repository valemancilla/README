# **README**

## *ejercicio1*

#### 1. frase = input("Escribe una frase: ")

- **Función:** input()
- **¿Qué hace?:** Le pide al usuario que escriba algo (una frase).
- **¿Qué guarda?:** El texto que el usuario escribe se guarda en la variable llamada `frase`.
- **Aplicación:** Capturar datos del usuario.

#### 2.total_caracteres = len(frase)

- **Función:** `len()`
- **¿Qué hace?:** Cuenta **cuántos caracteres** tiene la frase.
- **Incluye:** Letras, espacios, signos de puntuación, etc.
- **¿Qué guarda?:** El total de caracteres en la variable `total_caracteres`.

#### 3. espacios = frase.count(" ")

- **Función:** `.count()`
- **¿Qué hace?:** Cuenta **cuántas veces aparece un espacio** (`" "`) en la frase.
- **¿Qué guarda?:** El número total de espacios en la variable `espacios`.

#### 4. print(f"La frase tiene {total_caracteres} caracteres en total.")

- **Función:** `print()` y f-string
- **¿Qué hace?:** Muestra en pantalla el total de caracteres.
- **`f"texto {variable}"`**: Es una forma moderna de combinar texto con valores de variables.

#### 5. print(f"La frase tiene {espacios} espacios.")

- **Función:** `print()` y f-string
- **¿Qué hace?:** Muestra en pantalla cuántos espacios tiene la frase.

### ¿Para qué sirve este código?

- Te ayuda a:

  - Saber el **tamaño total** de un texto.
  - Saber cuántos **espacios** contiene.

- Puede usarse para tareas como:

  - Contar palabras (de forma básica).
  - Analizar mensajes.
  - Procesamiento de texto.

  ## *ejercicio2*

  ### 1. `nombre = input("Escribe tu nombre completo: ")`

  - **Función usada:** `input()`
  - **¿Qué hace?:** Pide al usuario que escriba su nombre completo.
  - **¿Qué devuelve?:** Una cadena de texto (string) con lo que el usuario escribió.
  - **¿Dónde se guarda?:** En la variable `nombre`.

   **Aplicación:** Se usa para capturar datos desde el teclado, como nombres, edades, contraseñas, etc.

  

  ### 2. `if nombre.replace(" ", "").isalpha():`

  #### a. `nombre.replace(" ", "")`

  - **Función usada:** `.replace(" ", "")`
  - **¿Qué hace?:** Quita todos los espacios del texto.
  - **Ejemplo:** `"Juan Carlos"` → `"JuanCarlos"`
  - **¿Para qué?:** Para que los espacios no afecten la validación de letras.

  #### b. `.isalpha()`

  - **Función usada:** `.isalpha()`
  - **¿Qué hace?:** Verifica que **todos los caracteres sean letras** (sin números, ni símbolos).
  - **Ejemplo:**
    - `"JuanCarlos"` → ✅
    - `"Juan123"` → ❌

   **Aplicación:** Muy útil para validar nombres, apellidos, ciudades, etc. que solo deben contener letras.

  ### 3.`if nombre.istitle():`

  - **Función usada:** `.istitle()`
  - **¿Qué hace?:** Verifica que **cada palabra** del nombre comience con **mayúscula**.
  - **Ejemplo:**
    - `"Juan Carlos"` → ✅
    - `"juan carlos"` → ❌
    - `"JUAN CARLOS"` → ❌

   **Aplicación:** Se usa para validar que nombres estén bien escritos, por ejemplo al registrar usuarios o llenar formularios.

  

  ### 4. `print("El nombre es válido.")`

  - **Función usada:** `print()`
  - **¿Qué hace?:** Muestra un mensaje en pantalla.
  - **¿Cuándo se ejecuta?:** Si el nombre tiene solo letras **y** está bien capitalizado (con mayúsculas al inicio de cada palabra).

  **Aplicación:** Confirmar que el dato ingresado por el usuario es correcto.

  ### 5. `else:  # de istitle()`

  - **Función:** `else`
  - **¿Qué hace?:** Se ejecuta **si el nombre tiene solo letras** pero **no está bien capitalizado**.
  - **Aplicación:** Mostrar advertencia si no hay mayúsculas en los nombres.

  ### 6. `else:  # de isalpha()`

  - **Función:** `else`
  - **¿Qué hace?:** Se ejecuta si el nombre contiene números, símbolos o signos raros.
  - **Aplicación:** Validar que el usuario no haya escrito caracteres incorrectos.

  ### ¿Para qué sirve este código?

   Este código se usa para **verificar que un nombre completo esté bien escrito**, usando solo letras y con las **mayúsculas al inicio de cada palabra**.

  ## *ejercicio3*

  ### 1. `palabra = input("Escribe una palabra: ")`

  - **Función usada:** `input()`

  - **¿Qué hace?:** Muestra el mensaje `"Escribe una palabra: "` y espera a que el usuario escriba algo.

  - **¿Qué guarda?:** El texto que el usuario escribió se guarda en la variable `palabra`.

  - **Aplicación:** Captura datos desde el teclado.

    ### 2.`invertida = palabra[::-1]`

    - **Función usada:** `[::-1]` → Esto se llama **slicing** (rebanado de cadenas)
    - **¿Qué hace?:** Invierte el texto.
      - `palabra[start:stop:step]` es la estructura general del slicing.
      - En este caso, `[::-1]` significa:
        - `start` = desde el final,
        - `step = -1` → va hacia atrás.
    - **¿Qué guarda?:** La versión invertida de la palabra original en la variable `invertida`.

    - **Aplicación:** Muy útil para:

      - Ver si una palabra es un **palíndromo** (como "oso" o "reconocer").
      - Procesar texto, analizar cadenas.
      - Juegos de palabras, cifrados, etc.

      ### 3.`print(f"La palabra invertida es: {invertida}")`

      - **Función usada:** `print()` con **f-string**

      - **¿Qué hace?:** Muestra el mensaje `"La palabra invertida es: "` junto con el valor de `invertida`.

      - **f-string:** Es una forma moderna de insertar variables dentro de un texto.

      - **Aplicación:**

        Sirve para:

        - Mostrar resultados de forma clara y personalizada.
        - Combinar texto fijo con valores que pueden cambiar.
        - Informar al usuario lo que ha pasado en el programa.

        ## **ejercicio4*

        ### 1. `frase = input("Escribe una frase: ")`

        - **Función usada:** `input()`
        - **¿Qué hace?:** Pide al usuario que escriba una frase.
        - **¿Qué guarda?:** El texto ingresado se guarda en la variable `frase`.
        - **Aplicación:** Captura de datos por teclado.

        ### 2.`frase_cifrada = frase.replace("a", "*")...`

        #### **Función principal usada:** `.replace()`

        - **¿Qué hace?:** Va reemplazando cada vocal (minúscula y luego mayúscula) por el símbolo `*`.
        - Se aplican varias `.replace()` seguidas. Cada una toma el resultado de la anterior.

        #### ✅ Reemplazos:

        ```
        pythonCopiarEditarfrase.replace("a", "*")        # cambia todas las "a"
        .replace("e", "*")             # luego cambia todas las "e"
        .replace("i", "*")             # y así sucesivamente...
        ```

        Después, también se reemplazan las mayúsculas:

        ```
        python
        
        
        CopiarEditar
        frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*")...
        ```

###                  aplicación: 

​                El uso de `.replace()` seguido para cambiar vocales por `*` sirve principalmente para: 

​                 Cifrar palabras de forma visual (ocultar vocales)

​                     Crear juegos o ejercicios con texto

​                     Practicar procesamiento y modificación de cadenas

​                     Aplicar filtros o máscaras a contenido escrito

### 3.   `print(f"La frase cifrada es: {frase_cifrada}")`

- **Función usada:** `print()` con `f-string`
- **¿Qué hace?:** Muestra el mensaje junto con la frase modificada.
- **Aplicación:** Mostrar el resultado al usuario de manera clara y personalizada.

###  ¿Para qué sirve este código?

El código **cifra una frase** escrita por el usuario, reemplazando **todas las vocales (mayúsculas y minúsculas)** por el símbolo `*`.

## *ejercicio5*

### 1.`frase = input("Escribe una frase: ")`

- **Función usada:** `input()`

- **¿Qué hace?:** Pide al usuario que escriba una frase.

- **¿Qué guarda?:** El texto ingresado se almacena en la variable `frase`.

- **Aplicación:** Captura de datos por teclado.

  ### 2.`frase.count("a") + frase.count("A")` *(y lo mismo con e, i, o, u)*

  - **Función usada:** `.count("x")`
  - **¿Qué hace?:** Cuenta cuántas veces aparece una letra específica en el texto que escribió el usuario.
     En este caso, cuenta la letra `"a"` y la letra `"A"` dentro de la variable `frase`.
  - **¿Por qué se usa dos veces (mayúscula y minúscula)?:** Porque `.count("a")` **solo cuenta las "a" minúsculas**, y `.count("A")` **solo cuenta las "A" mayúsculas**. Al sumarlas, obtienes el total de vocales **sin importar si están en mayúscula o minúscula**.
  - **Aplicación :**Se usa para **contar cuántas veces aparece una vocal** (tanto en minúscula como en mayúscula) dentro de una frase. Sirve para análisis de texto, actividades educativas, juegos con letras y estadísticas de uso de vocales.

  ### 3.`total_vocales = a + e + i + o + u`

  - **¿Qué hace?:** Suma los valores que guardan las variables `a`, `e`, `i`, `o`, y `u`, que representan la cantidad de veces que aparece cada vocal (tanto en minúscula como en mayúscula) en la frase.
  -  **Función usada:** Operador de suma (`+`)**
  - **Aplicación:** Saber cuántas vocales hay en total en la frase.

  ### 4. `print(f"La frase tiene {total_vocales} vocales.")`

  - **Función usada:** `print()` con `f-string`
  - **¿Qué hace?:** Muestra el total de vocales en pantalla, insertando el valor de `total_vocales` dentro del mensaje.
  - **Aplicación:** Mostrar resultados personalizados al usuario.

  ## *ejercicio6*

  ### 1.`telefono = input("Escribe un número de teléfono de 10 dígitos: ")`

  - **Función usada:** `input()`
  - **¿Qué hace?:** Muestra un mensaje al usuario y guarda lo que escriba en la variable `telefono`.
  - **Aplicación:** Capturar el número telefónico como texto.

  ### 2. `if len(telefono) == 10 and telefono.isdigit():`

  - **Funciones usadas:** `len()` y `isdigit()`
  - **¿Qué hace?:**
    - `len(telefono) == 10`: Verifica que el número tenga exactamente 10 caracteres.
    - `telefono.isdigit()`: Verifica que todos los caracteres sean números (0–9).
  - **Aplicación:** Validar que el dato ingresado es un **número telefónico válido** de 10 dígitos.

  ### 3.`telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"`

  - **Funciones usadas:** slicing (`[:]`) y `f-string`

  - **¿Qué hace?:** Toma el número y lo divide en partes para mostrarlo con el formato típico:
     `(código de área) xxx-xxxx`

    Si el número es `"3001234567"`, se muestra así:
     `(300) 123-4567`

  - `telefono[:3]` → primeros 3 dígitos
  - `telefono[3:6]` → siguientes 3
  - `telefono[6:]` → últimos 4
  - **Aplicación:** Mejorar la presentación del número (más fácil de leer).

  ### 4. `print(f"El número formateado es: {telefono_formateado}")`

  - **Función usada:** `print()` con `f-string`
  - **¿Qué hace?:** Muestra el número ya formateado al usuario.
  - **Aplicación:** Dar una respuesta clara, ordenada y visualmente amigable.

  ### 5.`else: print("El número debe tener exactamente 10 dígitos.")`

  - **¿Qué hace?:** Si el número **no tiene 10 dígitos** o **tiene letras u otros símbolos**, muestra un mensaje de error.
  - **Aplicación:** Validar entrada incorrecta y evitar errores en el formato.

¿PARA QUÉ SIRVE ESTE CÓDIGO?

Este código sirve para **validar** si un número de teléfono tiene exactamente 10 dígitos y, si es correcto, **mostrarlo con el formato (XXX) XXX-XXXX**.

## *ejercicio7*

### 1. `palabra = input("Escribe una palabra: ").lower()`

- **Funciones usadas:** `input()` y `.lower()`
- **¿Qué hace?:**
  - `input(...)` pide una palabra al usuario.
  - `.lower()` convierte toda la palabra a minúsculas para que no haya diferencia entre `"Ana"` y `"ana"`.
- **Aplicación:** Permite comparar la palabra sin importar si se escribió con mayúsculas o minúsculas.

### 2.`invertida = palabra[::-1]`

- **Función usada:** slicing `[::-1]`
- **¿Qué hace?:** Invierte la palabra.
- **Aplicación:** Permite comparar la palabra al derecho y al revés.

###  3.`if palabra == invertida:`

- **Función usada:** `if` (condicional)
- **¿Qué hace?:** Compara la palabra original (ya en minúscula) con su versión invertida.
- **Aplicación:** Verifica si la palabra **se lee igual al derecho que al revés**.

### 4.`print("La palabra es un palíndromo.")` 

**Función usada:** `print()`

 **¿Qué hace?:**Muestra en pantalla el mensaje cuando la palabra es un palíndromo.

 **Aplicación:**Comunicarle al usuario el resultado de la evaluación.

### 5.`else:`

 **Función usada:** `else`

 **¿Qué hace?:**Se ejecuta si la condición del `if` **no se cumple** (es decir, si la palabra no es igual a la invertida).

 **Aplicación:**Garantiza que el programa siempre dé una respuesta, ya sea positiva o negativa.

 `print("La palabra no es un palíndromo.")`

 **Función usada:** `print()`

 **¿Qué hace?:**Muestra en pantalla un mensaje si la palabra **no es un palíndromo**.

### ¿PARA QUÉ SIRVE ESTE CÓDIGO?

Este código sirve para **verificar si una palabra es un palíndromo**, es decir, si **se lee igual de izquierda a derecha que de derecha a izquierda**.