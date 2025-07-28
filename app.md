------

## app

## main.py

## Explicación detallada del código

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

- **Importación de módulos estándar:** `sys` y `os` se usan para manipular rutas y configuraciones del sistema.
- **Modificación de la ruta de búsqueda de módulos:**
   La línea `sys.path.append(...)` añade la carpeta padre del archivo actual a la lista de rutas donde Python busca módulos.
   Esto permite importar módulos que están en carpetas superiores sin errores, importante para la estructura modular del proyecto.

------

```python
from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar
import controllers.equipos as eq
import controllers.jugadores as jg
import controllers.estadisticas as es
import controllers.transferencias as tran
```

- Se importan funciones `limpiar_pantalla` y `pausar` del módulo `screencontrollers` para gestionar la consola (limpiar pantalla y pausar la ejecución esperando entrada).
- También se importan los módulos principales de la aplicación con alias:
  - `eq` para equipos
  - `jg` para jugadores
  - `es` para estadísticas
  - `tran` para transferencias
     Esto facilita llamar a funciones de esos módulos de forma abreviada y ordenada.

------

### Función `main_menu()`

```python
def main_menu():
    limpiar_pantalla()
    print(' === GESTOR DE TORNEOS ===')
    print('1. Registrar equipo')
    print('2. Listar equipos')
    print('3. Registrar jugador')
    print('4. Listar jugadores')
    print('5. Transferencia de jugador (venta o préstamo)')
    print('6. Ver estadísticas')
    print('0. Salir')
    try:
        op = int(input("\n elige una opcion :"))
        if 1 <= op <= 6:
            return op
    except:
        pass
    return None
```

- **`limpiar_pantalla()`**: limpia la consola para que el menú se vea limpio.
- Imprime el menú principal con las opciones numeradas para que el usuario elija.
- Se solicita la opción con `input()`.
- Se intenta convertir la opción a entero con `int()`.
- Si la opción está entre 1 y 6, se retorna ese número.
- Si el usuario ingresa algo inválido (no número o fuera de rango), se atrapa el error y se retorna `None` (opción inválida).
- La opción `0` (salir) no está incluida en la validación, porque se maneja directamente después.

------

### Bloque principal (punto de entrada)

```python
if __name__ == "__main__":
    while True:
        opcion = main_menu()
        if opcion == 1:
            eq.equipos()
            pausar()
        elif opcion == 2:
            eq.listar_equipos()
            pausar()
        elif opcion == 3:
            jg.jugadores()
            pausar()
        elif opcion == 4:
            jg.listar_jugadores()
            pausar()
        elif opcion == 5:
            tran.transferir_jugador()
        elif opcion == 6:
            es.estadisticas_menu()
        elif opcion == 0:
            print('\n Saliendo')
            break
        else:
            print('\n Opcion no valida')
            pausar()
```

- `if __name__ == "__main__":`
   Esto significa que el siguiente código solo se ejecuta si este archivo es el programa principal (no si se importa como módulo).
- **Bucle infinito `while True`:**
   Se ejecuta continuamente hasta que el usuario elija salir (opción 0).
- Cada vez que el bucle corre:
  - Se llama a `main_menu()` para mostrar opciones y recibir la elección del usuario.
  - Según el valor de `opcion`, se llama a la función correspondiente de cada módulo:
    - **1:** Llama a la función `equipos()` del módulo `equipos` para registrar un equipo.
    - **2:** Llama a `listar_equipos()` para mostrar los equipos guardados.
    - **3:** Llama a `jugadores()` para registrar un jugador.
    - **4:** Llama a `listar_jugadores()` para listar todos los jugadores.
    - **5:** Llama a `transferir_jugador()` para hacer transferencias entre equipos.
    - **6:** Llama a `estadisticas_menu()` para mostrar estadísticas.
  - Excepto para las opciones 5 y 6, después de ejecutar la función se llama a `pausar()` para que el usuario pueda leer la información antes de limpiar la pantalla y mostrar el menú nuevamente.
  - Si la opción es **0**, imprime "Saliendo" y sale del bucle con `break` terminando el programa.
  - Si la opción es inválida (`None` o fuera del rango), muestra mensaje de error y pausa.

------

## Resumen

- Este código es el **controlador principal del programa**, el que interactúa directamente con el usuario.
- Muestra un menú con opciones para gestionar las diferentes partes del sistema.
- Según la opción, llama a funciones específicas en los módulos `equipos`, `jugadores`, `transferencias` y `estadisticas`.
- Usa funciones para limpiar la pantalla y pausar para mejorar la experiencia en consola.
- Controla errores de entrada para que el programa no falle y sea fácil de usar.

------

 `sys.path.append(...)` es para poder importar módulos en carpetas superiores sin problemas, dado que la estructura del proyecto tiene varios directorios.

 pausa después de cada acción,  es para que el usuario pueda leer los mensajes antes de que la pantalla se limpie y se muestre el menú nuevamente.

------

# controllers

------

# Explicación detallada del código de los módulos `equipos()` y `listar_equipos()`

------

## Importaciones iniciales

```python
import json
import utils.corefiles as cf
import utils.screencontrollers as sc
import utils.validatedata as vd
from config import DB_PATH
import random
import os
```

- **`json`**: para manejar archivos JSON (leer y escribir).
- **`utils.corefiles as cf`**: módulo que maneja la lectura y escritura de archivos JSON en el proyecto (funciones auxiliares).
- **`utils.screencontrollers as sc`**: módulo que tiene funciones para limpiar la pantalla y pausar la consola.
- **`utils.validatedata as vd`**: módulo para validar entradas del usuario (texto, números).
- **`from config import DB_PATH`**: importa la ruta base para guardar y leer los archivos JSON.
- **`random`**: para generar un número aleatorio (ID del equipo).
- **`os`**: para manejar rutas de archivos.

------

## Función `equipos()`

Esta función sirve para **registrar un nuevo equipo** mediante interacción por consola.

```python
def equipos():
    sc.limpiar_pantalla()
```

- Primero, limpia la pantalla para que la interfaz se vea limpia y ordenada.

```python
    ideq = random.randint(1023, 9876)
```

- Genera un ID aleatorio para el equipo entre 1023 y 9876.
   Esto sirve como identificador único para cada equipo.

```python
    teamname = vd.validatetext('Nombre del Equipo :')
    fecha = vd.validateInt('año de creación del Equipo :')
    origen = vd.validatetext('país de origen del Equipo :')
    id = vd.validateInt('id de la liga del equipo :')
```

- Pide al usuario que ingrese información:
  - Nombre del equipo (solo texto válido).
  - Año de creación (solo números enteros válidos).
  - País de origen (solo texto válido).
  - ID de la liga a la que pertenece (número entero válido).
- Para cada entrada se usa una función de validación que se asegura que el dato sea correcto (sin caracteres inválidos).

```python
    eq = {
        ideq: {
            "nombre": teamname,
            "fundacion": fecha,
            "pais": origen,
            "idliga": id,
            "jugadores": []
        }
    }
```

- Se crea un diccionario con la estructura del equipo, donde la clave es el `ideq` (ID generado) y el valor es otro diccionario con los datos ingresados y un arreglo vacío para los jugadores (ya que es un equipo nuevo).

```python
    if not cf.updateJson(eq, ["equipos", "equipos"]):
        print("Equipo agregado exitosamente")
    else:
        print("No se pudo agregar el equipo")
```

- Llama a la función `updateJson` del módulo `corefiles` para actualizar el archivo `equipos.json`.
- La función `updateJson` recibe el diccionario del equipo (`eq`) y una lista `["equipos", "equipos"]` que indica dónde se actualizarán los datos (puede ser una estructura anidada).
- Si la actualización **NO** falla (`not cf.updateJson()`), imprime mensaje de éxito.
- Si falla, imprime mensaje de error.

```python
    sc.pausar()
```

- Pausa la consola para que el usuario vea el mensaje antes de continuar.

------

## Función `listar_equipos()`

Esta función sirve para **mostrar en consola la lista de equipos registrados**.

```python
def listar_equipos():
    sc.limpiar_pantalla()
    ruta = os.path.join("data", "equipos.json")
```

- Limpia la pantalla para que la lista se muestre limpia.
- Define la ruta del archivo JSON donde están guardados los equipos.

```python
    if not os.path.exists(ruta):
        print("No hay equipos registrados.")
        sc.pausar()
        return
```

- Si el archivo no existe, significa que no hay equipos registrados.
- Se avisa al usuario y se pausa para que pueda leer el mensaje, luego se sale de la función con `return`.

```python
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            equipos = datos.get("equipos", {})
    except:
        print("Error al leer el archivo de equipos.")
        sc.pausar()
        return
```

- Intenta abrir y cargar el archivo JSON.
- Extrae el diccionario con clave `"equipos"` (si no existe, devuelve diccionario vacío).
- Si hay algún error (por ejemplo, archivo corrupto), muestra mensaje de error y sale.

```python
    if len(equipos) == 0:
        print("No hay equipos registrados.")
```

- Si el diccionario está vacío, significa que no hay equipos para mostrar.

```python
    else:
        print("Lista de equipos:")
        for i, (id_equipo, equipo) in enumerate(equipos.items(), 1):
            try:
                print(f"{i}. {equipo['nombre']} (ID: {id_equipo}) - Fundación: {equipo['fundacion']}, País: {equipo['pais']}, Liga: {equipo['idliga']}")
            except:
                print(f"{i}. Datos incompletos para el equipo con ID {id_equipo}")
```

- Si hay equipos, imprime encabezado.
- Itera sobre cada equipo con su ID.
- Intenta imprimir la información del equipo: nombre, ID, año fundación, país e ID liga.
- Si falta algún dato, atrapa el error y avisa que los datos están incompletos para ese equipo.

------

# Resumen 

- **¿Qué hace la función `equipos()`?**
   Permite registrar un nuevo equipo pidiendo datos validados, genera un ID único, y lo guarda en el archivo JSON.
- **¿Qué hace la función `listar_equipos()`?**
   Muestra todos los equipos registrados leyendo el archivo JSON, con manejo de errores si no hay datos o archivo corrupto.
- **¿Cómo se asegura la calidad de datos?**
   Usando funciones de validación (`validatetext` y `validateInt`) para que el usuario solo ingrese valores válidos.
- **¿Cómo maneja errores?**
   Con bloques `try-except` para evitar que el programa crashee al leer archivos o imprimir datos incompletos.
- **¿Cómo mejora la experiencia en consola?**
   Limpia la pantalla antes de mostrar datos y pausa después para que el usuario pueda leer la información.

------

# controllers 

## estadísticas

Este módulo permite gestionar partidos de fútbol dentro del sistema: programar partidos, registrar resultados y ver estadísticas.

------

## Importaciones y variables globales

```python
import os
import sys
import utils.corefiles as cf
import utils.screencontrollers as sc

Equipos = []
Partidos = []
```

- Se importan módulos necesarios:
  - `os` y `sys` para manejo de sistema y rutas (no usados explícitamente aquí, pero común en módulos).
  - `utils.corefiles` como `cf` para manejar lectura y escritura JSON.
  - `utils.screencontrollers` como `sc` para limpiar pantalla y pausar la consola.
- Se definen listas globales vacías `Equipos` y `Partidos`, aunque en este código no se usan directamente (podrían ser reliquias o usadas en otra parte).

------

## Función `programar_fecha()`

Esta función permite **programar un nuevo partido** entre dos equipos.

```python
def programar_fecha():
    sc.limpiar_pantalla()
```

- Limpia la pantalla para que el menú o formulario se vea limpio.

```python
    data = cf.readJson("equipos")
    equipos = data.get("equipos", {})
```

- Lee el archivo JSON de equipos (`equipos.json`) usando la función `readJson` del módulo corefiles.
- Extrae el diccionario que contiene todos los equipos. Si no hay, devuelve diccionario vacío.

```python
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar()
        return
```

- Si no hay equipos registrados, muestra mensaje, pausa para que el usuario lo vea y termina la función (no se puede programar partidos sin equipos).

```python
    print("Equipos disponibles:")
    for id, equipo in equipos.items():
        print(f"ID: {id} - Nombre: {equipo.get('nombre', 'Sin nombre')}")
```

- Muestra en consola una lista de todos los equipos con su ID y nombre (o "Sin nombre" si falta ese dato).

```python
    local_id = input("ID del equipo local: ")
    visitante_id = input("ID del equipo visitante: ")
```

- Solicita al usuario que ingrese el ID del equipo local y del visitante para el partido.

```python
    if local_id == visitante_id:
        print("Un equipo no puede jugar contra sí mismo.")
        sc.pausar()
        return
```

- Valida que los dos equipos sean diferentes (no puede haber partido contra sí mismo).

```python
    if local_id not in equipos or visitante_id not in equipos:
        print("Alguno de los equipos no está registrado.")
        sc.pausar()
        return
```

- Valida que ambos IDs existan en la lista de equipos registrados.

```python
    fecha = input("Fecha del partido: ")
```

- Solicita al usuario la fecha del partido (texto libre, no validado explícitamente aquí).

```python
    nuevo_partido = {
        "fecha": fecha,
        "local": local_id,
        "visitante": visitante_id,
        "goles_local": None,
        "goles_visitante": None
    }
```

- Crea un diccionario con la información del partido programado:
  - Fecha.
  - ID equipo local.
  - ID equipo visitante.
  - Goles inicializados en `None` porque aún no se juega ni registra el resultado.

```python
    datos = cf.readJson("partidos")
    datos.append(nuevo_partido)
    cf.writeJson("partidos", datos)
```

- Lee la lista de partidos guardados.
- Agrega el nuevo partido al final.
- Escribe de nuevo la lista actualizada en el archivo `partidos.json`.

```python
    print("Partido programado exitosamente.")
    sc.pausar()
```

- Mensaje de confirmación y pausa para que el usuario lo lea.

------

## Función `registrar_marcador()`

Esta función permite **ingresar los resultados (goles) de un partido programado**.

```python
def registrar_marcador():
    sc.limpiar_pantalla()
```

- Limpia pantalla para presentación limpia.

```python
    datos = cf.readJson("partidos")
    equipos = cf.readJson("equipos").get("equipos", {})
```

- Carga la lista de partidos programados.
- Carga la lista de equipos para mostrar nombres amigables.

```python
    if not datos:
        print("No hay partidos programados.")
        sc.pausar()
        return
```

- Si no hay partidos, avisa y termina la función.

```python
    for i, p in enumerate(datos):
        local = equipos.get(p['local'], {}).get('nombre', 'Desconocido')
        visitante = equipos.get(p['visitante'], {}).get('nombre', 'Desconocido')
        print(f"{i + 1}. {local} vs {visitante} - Fecha: {p['fecha']}")
```

- Muestra una lista numerada de todos los partidos programados con los nombres de equipos (o "Desconocido" si no encuentra el equipo).
- Esto permite al usuario elegir fácilmente el partido.

```python
    try:
        idx = int(input("Seleccione el número del partido: ")) - 1
        if idx < 0 or idx >= len(datos):
            raise ValueError
    except:
        print("Selección inválida.")
        sc.pausar()
        return
```

- Solicita al usuario que seleccione el partido por número.
- Valida que el número esté dentro del rango correcto.
- Si la selección es inválida, muestra error y termina la función.

```python
    try:
        goles_local = int(input("Goles del equipo local: "))
        goles_visitante = int(input("Goles del equipo visitante: "))
    except:
        print("Los goles deben ser números enteros.")
        sc.pausar()
        return
```

- Solicita los goles anotados por cada equipo y valida que sean números enteros.
- Si no, muestra error y termina la función.

```python
    datos[idx]['goles_local'] = goles_local
    datos[idx]['goles_visitante'] = goles_visitante

    cf.writeJson("partidos", datos)
```

- Actualiza el partido seleccionado con los goles ingresados.
- Guarda la lista actualizada en el archivo `partidos.json`.

```python
    print("Marcador registrado correctamente.")
    sc.pausar()
```

- Mensaje de éxito y pausa.

------

## Función `ver_estadisticas()`

Esta función muestra un resumen con los resultados de los partidos.

```python
def ver_estadisticas():
    sc.limpiar_pantalla()
    datos = cf.readJson("partidos")
    equipos = cf.readJson("equipos").get("equipos", {})
```

- Limpia pantalla.
- Carga los partidos y los equipos.

```python
    if not datos:
        print("No hay partidos registrados.")
    else:
        print("Estadísticas de partidos:")
        for p in datos:
            local = equipos.get(p['local'], {}).get('nombre', 'Desconocido')
            visitante = equipos.get(p['visitante'], {}).get('nombre', 'Desconocido')
            marcador = f"{p.get('goles_local', '-')} - {p.get('goles_visitante', '-')}"
            print(f"{p['fecha']}: {local} vs {visitante} Resultado: {marcador}")
```

- Si no hay partidos, avisa.
- Si hay, imprime una línea por partido con:
   Fecha, equipos local y visitante, y el marcador (muestra "-" si no hay goles registrados aún).

```python
    sc.pausar()
```

- Pausa para que el usuario lea los datos.

------

## Función `estadisticas_menu()`

Es el menú principal para interactuar con las funciones anteriores.

```python
def estadisticas_menu():
    while True:
        sc.limpiar_pantalla()
        print("=== MENÚ DE ESTADÍSTICAS ===")
        print("1. Programar Fecha de Partido")
        print("2. Registrar Marcador")
        print("3. Ver Estadísticas de Partidos")
        print("0. Volver al Menú Principal")
        opcion = input("Seleccione una opción: ")
```

- Bucle infinito que limpia pantalla y muestra las opciones disponibles.
- Pide al usuario que seleccione opción.

```python
        if opcion == "1":
            programar_fecha()
        elif opcion == "2":
            registrar_marcador()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "0":
            break
        else:
            print("Opción inválida.")
            sc.pausar()
```

- Según la opción, llama a la función correspondiente.
- La opción "0" rompe el ciclo y regresa al menú principal (sale de este menú).
- Para opciones no válidas muestra mensaje y pausa.

------

# Resumen para explicar sin que te pregunten

- Este módulo administra partidos y sus estadísticas básicas.
- Permite programar partidos entre equipos existentes, asegurándose que los equipos sean válidos y distintos.
- Permite registrar resultados con goles, validando que sean números enteros.
- Permite consultar un resumen de partidos y resultados.
- El menú es un bucle que permite usar estas funciones fácilmente desde consola.
- Usa los módulos auxiliares para limpiar pantalla, pausar y manejar archivos JSON.
- Tiene manejo de errores para evitar que el programa se caiga con entradas inválidas o datos faltantes.

------

------

# controllers

## **jugadores**

Este módulo permite **registrar jugadores** en la base de datos y **listar jugadores** registrados. También vincula al jugador con el equipo al que pertenece.

------

## Importaciones

```python
import random

import utils.corefiles as cf
import utils.screencontrollers as sc
import utils.validatedata as vd
```

- `random`: para generar un ID único aleatorio para cada jugador.
- `utils.corefiles` (`cf`): para leer y actualizar archivos JSON (manejo de la base de datos).
- `utils.screencontrollers` (`sc`): para limpiar pantalla y pausar la consola.
- `utils.validatedata` (`vd`): para validar las entradas del usuario (texto y números).

------

## Función `jugadores()`

Esta función permite **registrar un nuevo jugador**.

```python
def jugadores():
    sc.limpiar_pantalla()
```

- Limpia la pantalla para mostrar el formulario de registro limpio.

```python
    idjg = random.randint(1023, 9876)
```

- Genera un número aleatorio entre 1023 y 9876 que se usará como ID único para el jugador.

```python
    nombrejug = vd.validatetext("Nombre del jugador:")
    posicion = vd.validatetext("Posición del jugador:")
    dorsal = vd.validateInt("Número del dorsal:")
    idliga = vd.validateInt("ID del equipo al que pertenece:")
```

- Solicita y valida la entrada de datos del jugador:
  - Nombre (texto).
  - Posición (texto, ej. defensa, delantero).
  - Número de dorsal (entero).
  - ID del equipo al que pertenece (entero). Se asume que corresponde a un campo "idliga" de un equipo.

```python
    nuevo_jugador = {
        idjg: {
            "nombre": nombrejug,
            "posicion": posicion,
            "dorsal": dorsal,
            "ideq": idliga
        }
    }
```

- Crea un diccionario con la estructura del jugador:
  - La clave es el ID generado aleatoriamente.
  - Los valores son un diccionario con nombre, posición, dorsal y el ID del equipo.

```python
    if not cf.updateJson(nuevo_jugador, ["jugadores"]):
        print("Jugador agregado exitosamente a la base de datos.")
```

- Usa la función `updateJson` para agregar este nuevo jugador al archivo `jugadores.json`.
- `updateJson` devuelve `False` si la operación fue exitosa (es un detalle de implementación).
- Si fue exitoso, muestra mensaje.

------

### Vinculación del jugador al equipo

Después de agregar al jugador, el código intenta **vincular al jugador con su equipo**.

```python
        equipos_data = cf.readJson("equipos")
        equipos_dict = equipos_data.get("equipos", {})
        id_equipo = None
```

- Lee los datos de equipos del archivo `equipos.json`.
- Extrae el diccionario de equipos.
- Inicializa variable `id_equipo` para almacenar la clave del equipo encontrado.

```python
        for clave, datos in equipos_dict.items():
            if isinstance(datos, dict) and datos.get("idliga") == idliga:
                id_equipo = clave
                break
```

- Recorre todos los equipos buscando aquel cuyo campo `"idliga"` sea igual al `idliga` que el usuario ingresó para el jugador.
- Si encuentra uno, guarda su clave y termina el ciclo.

```python
        if id_equipo:
            if "jugadores" not in equipos_dict[id_equipo]:
                equipos_dict[id_equipo]["jugadores"] = []

            equipos_dict[id_equipo]["jugadores"].append(idjg)
            equipos_data["equipos"] = equipos_dict
            cf.writeJson("equipos", equipos_data)
```

- Si encontró un equipo válido:
  - Verifica si el equipo ya tiene la lista `"jugadores"`; si no, la crea.
  - Añade el ID del nuevo jugador a la lista de jugadores del equipo.
  - Actualiza el diccionario completo y escribe de nuevo en el archivo `equipos.json`.

```python
        else:
            print(f"No se encontró el equipo con idliga {idliga} para vincular el jugador.")
```

- Si no encontró el equipo con ese `idliga`, muestra un mensaje de error (posible que el usuario ingresó un ID incorrecto).

------

### Si no se pudo agregar el jugador

```python
    else:
        print("No se pudo agregar el jugador.")
```

- Si la función `updateJson` devolvió `True` (falló la actualización), muestra error.

```python
    sc.pausar()
```

- Pausa para que el usuario vea los mensajes.

------

## Función `listar_jugadores()`

Esta función muestra la lista de jugadores registrados.

```python
def listar_jugadores():
    sc.limpiar_pantalla()
```

- Limpia pantalla.

```python
    datos = cf.readJson("jugadores")
    jugadores = datos.get("jugadores", {})
```

- Lee el archivo `jugadores.json`.
- Extrae el diccionario de jugadores.

```python
    if not jugadores:
        print("No hay jugadores registrados.")
```

- Si no hay jugadores, muestra mensaje.

```python
    else:
        print("Lista de jugadores:\n")
        for i, (id_jugador, jugador) in enumerate(jugadores.items(), 1):
            nombre = jugador.get("nombre", "Desconocido")
            posicion = jugador.get("posicion", "Desconocida")
            dorsal = jugador.get("dorsal", "Sin número")
            idequipo = jugador.get("ideq", "Sin equipo")

            print(f"{i}. {nombre} (ID: {id_jugador}) - Posición: {posicion}, Dorsal: {dorsal}, ID Equipo: {idequipo}")
```

- Si hay jugadores, los recorre mostrando:
  - Índice enumerado.
  - Nombre (o "Desconocido" si falta).
  - Posición (o "Desconocida").
  - Dorsal (o "Sin número").
  - ID del equipo (o "Sin equipo").
- Lo imprime en formato claro para el usuario.

```python
    sc.pausar()
```

- Pausa para que el usuario lea la lista.

------

# Resumen para explicar sin que te pregunten

- La función `jugadores()` registra un nuevo jugador pidiendo datos validados, crea un ID aleatorio y lo guarda en `jugadores.json`.
- Luego, busca el equipo correspondiente por `idliga` y si lo encuentra, agrega el ID del jugador a la lista de jugadores del equipo en `equipos.json`.
- Si algo falla, muestra mensajes de error.
- La función `listar_jugadores()` lee todos los jugadores y los muestra ordenadamente, con todos los datos principales.
- Usa módulos auxiliares para manejar archivos, limpiar pantalla y validar datos, haciendo el programa más limpio y modular.

------

# controllers

------

## transferencias

Esta función se encarga de **transferir un jugador** de un equipo a otro dentro del sistema. Realiza validaciones para asegurar que los datos sean correctos y que la transferencia sea posible.

------

### Importaciones usadas

```python
import utils.corefiles as cf
import utils.screencontrollers as sc
```

- `cf` (corefiles): módulo encargado de leer y escribir archivos JSON (la "base de datos").
- `sc` (screencontrollers): módulo para limpiar pantalla y pausar consola.

------

### Paso a paso del código

```python
def transferir_jugador():
    sc.limpiar_pantalla()
```

- Limpia la pantalla para mostrar un menú limpio.

```python
    equipos = cf.readJson("equipos")
```

- Lee el archivo `equipos.json` usando la función `readJson` y guarda el contenido en la variable `equipos`.
- `equipos` debe ser un diccionario donde la clave es el ID del equipo y el valor es otro diccionario con los datos del equipo, incluyendo la lista de jugadores.

------

### Verificación de equipos disponibles

```python
    if not equipos:
        print("No hay equipos registrados.")
        sc.pausar()
        return
```

- Si no existen equipos registrados (el diccionario está vacío o es None), muestra mensaje y finaliza la función para evitar errores.

```python
    print("=== Equipos Disponibles ===")
    for eid, equipo in equipos.items():
        print(f"ID: {eid} - {equipo.get('nombre', 'Sin Nombre')}")
```

- Lista todos los equipos disponibles con su ID y nombre.
- Usa `.get()` para evitar errores en caso de que el nombre no esté definido.

------

### Entrada de datos de transferencia

```python
    equipo_origen = input("ID del equipo de origen: ")
    equipo_destino = input("ID del equipo de destino: ")
```

- El usuario ingresa el ID del equipo de donde se transferirá el jugador (equipo origen).
- Luego ingresa el ID del equipo que recibirá al jugador (equipo destino).

------

### Validaciones de entrada

```python
    if equipo_origen == equipo_destino:
        print("El equipo de origen y destino no pueden ser el mismo.")
        sc.pausar()
        return
```

- Verifica que el equipo de origen y destino no sean el mismo, ya que no tendría sentido transferir a un jugador al mismo equipo.

```python
    if equipo_origen not in equipos or equipo_destino not in equipos:
        print("Alguno de los equipos no existe.")
        sc.pausar()
        return
```

- Verifica que ambos IDs de equipo existan en la base de datos. Si alguno no está, muestra error y termina.

------

### Obtención y validación de jugadores en equipo origen

```python
    jugadores_origen = equipos[equipo_origen].get("jugadores", {})
    if not jugadores_origen:
        print("El equipo de origen no tiene jugadores.")
        sc.pausar()
        return
```

- Obtiene la lista (diccionario) de jugadores del equipo origen.
- Si no tiene jugadores (lista vacía o inexistente), muestra mensaje y termina.

------

### Mostrar jugadores para elegir quién transferir

```python
    print("\n=== Jugadores en el equipo de origen ===")
    for jid, jugador in jugadores_origen.items():
        print(f"ID: {jid} - {jugador.get('nombre', 'Sin Nombre')}")
```

- Muestra todos los jugadores disponibles para transferencia con su ID y nombre.

```python
    jugador_id = input("ID del jugador a transferir: ")
```

- El usuario ingresa el ID del jugador que quiere transferir.

```python
    if jugador_id not in jugadores_origen:
        print("El jugador no existe en el equipo de origen.")
        sc.pausar()
        return
```

- Valida que el jugador ingresado realmente exista en el equipo origen.

------

### Transferencia del jugador

```python
    jugador = jugadores_origen.pop(jugador_id)
```

- Elimina al jugador del diccionario de jugadores del equipo origen y guarda la información del jugador en `jugador`.
- `.pop()` devuelve el valor asociado al `jugador_id` y lo elimina del diccionario.

```python
    equipos[equipo_destino].setdefault("jugadores", {})[jugador_id] = jugador
```

- En el equipo destino, se asegura que exista la clave `"jugadores"` con un diccionario (si no existe, la crea vacía con `setdefault`).
- Luego, añade al jugador con su `jugador_id` y los datos que tenía.

------

### Guardar cambios y mostrar mensaje

```python
    cf.writeJson("equipos", equipos)
```

- Guarda la estructura actualizada de equipos (con el jugador transferido) en el archivo `equipos.json`.

```python
    print(f"\n Jugador '{jugador['nombre']}' transferido correctamente.")
    sc.pausar()
```

- Muestra mensaje de confirmación con el nombre del jugador transferido.
- Pausa para que el usuario lea el mensaje.

------

# Resumen 

- Lee la base de datos de equipos.
- Lista equipos disponibles y pide IDs de origen y destino.
- Valida que los IDs sean correctos y que no sean el mismo equipo.
- Obtiene jugadores del equipo origen, muestra la lista y pide el ID del jugador a transferir.
- Valida que el jugador exista en el equipo origen.
- Elimina al jugador del equipo origen y lo agrega al equipo destino.
- Guarda los cambios en el archivo JSON.
- Mensaje de éxito y pausa.

------

