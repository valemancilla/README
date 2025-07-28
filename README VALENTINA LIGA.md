# main.py

### 1. **Importaciones y configuración de la ruta**

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
```

- **Función:**
   Ajusta la ruta del sistema para que Python pueda encontrar y cargar los módulos que están en el directorio padre.
- **¿Qué hace?:**
   Añade la carpeta padre del archivo actual al path de búsqueda de módulos de Python, para que se puedan importar los módulos que están en un nivel superior (en este caso, los módulos dentro de la carpeta `controllers`).
- **¿Qué guarda?:**
   No guarda datos, solo modifica la configuración de búsqueda de módulos en tiempo de ejecución.
- **Aplicación:**
   Esto es útil en proyectos organizados por carpetas, para poder importar módulos que están en otra carpeta sin necesidad de instalar paquetes o modificar variables externas.

------

### 2. **Importación de módulos**

```python
import controllers.equipos as equipos
import controllers.jugadores as jugadores
import controllers.transferencias as transferencias
import controllers.estadisticas as estadisticas
```

- **Función:**
   Importar funcionalidades específicas para manejar equipos, jugadores, transferencias y estadísticas.
- **¿Qué hace?:**
   Importa las funciones y clases definidas en los archivos `equipos.py`, `jugadores.py`, `transferencias.py` y `estadisticas.py` que están dentro de la carpeta `controllers`.
- **¿Qué guarda?:**
   Guarda referencias a los módulos importados bajo nombres cortos para que puedas llamar a sus funciones (por ejemplo, `equipos.registrar_equipo()`).
- **Aplicación:**
   Permite dividir la aplicación en partes separadas y organizadas, donde cada módulo tiene responsabilidades específicas.

------

### 3. **Función principal: `menu()`**

```python
def menu():
    while True:
        print("\n=== GESTOR DE TORNEOS INTERNACIONALES ===")
        print("1. Registrar equipo")
        print("2. Listar equipos")
        print("3. Registrar jugador")
        print("4. Listar jugadores")
        print("5. Transferencia de jugador (venta o préstamo)")
        print("6. Ver estadísticas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            equipos.registrar_equipo()
        elif opcion == "2":
            equipos.listar_equipos()
        elif opcion == "3":
            jugadores.registrar_jugador()
        elif opcion == "4":
            jugadores.listar_jugadores()
        elif opcion == "5":
            transferencias.realizar_transferencia()
            transferencias.listar_transferencias()
        elif opcion == "6":
            estadisticas.ver_estadisticas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
```

- **Función:**
   Controla el flujo principal del programa mostrando un menú de opciones y ejecutando las acciones que el usuario seleccione.
- **¿Qué hace?:**
  - Muestra opciones en la consola.
  - Recibe la opción que el usuario escribe.
  - Ejecuta la función correspondiente del módulo adecuado.
  - Se repite hasta que el usuario elige salir (`opción 0`).
- **¿Qué guarda?:**
   No guarda datos por sí sola, solo gestiona las llamadas a otras funciones que sí trabajan con datos.
- **Aplicación:**
   Proporciona una interfaz sencilla para que un usuario pueda interactuar con el sistema desde la terminal.

------

### 4. **Bloque para ejecutar el menú si el script es ejecutado directamente**

```python
if __name__ == "__main__":
    menu()
```

- **Función:**
   Este bloque garantiza que la función `menu()` solo se ejecute si el archivo es el programa principal que se está ejecutando, y no cuando el archivo se importa como módulo.
- **¿Qué hace?:**
   Llama a la función `menu()` para iniciar la aplicación.
- **¿Qué guarda?:**
   No guarda datos.
- **Aplicación:**
   Es una práctica estándar para scripts Python que pueden usarse como programa principal o como módulo importado.

------

# Resumen 

- Ajusta la ruta para importar módulos.
- Importa cuatro módulos responsables de distintas partes del sistema.
- Define la función `menu()` que muestra un menú en la terminal y gestiona la interacción con el usuario.
- Ejecuta la función `menu()` cuando se corre el script directamente.

------

# controllers

### Archivo: `controllers/equipos.py`

------

### Función:

```
registrar_equipo()
```

### ¿Qué hace?:

- Muestra un mensaje para que el usuario ingrese los datos de un nuevo equipo.
- Solicita al usuario, mediante la función `input_obligatorio()`, que ingrese: nombre, fecha de fundación, país y ID de liga del equipo.
- Lee el archivo JSON donde están guardados los equipos (`equipos.json`).
- Genera un nuevo ID basado en la cantidad actual de equipos.
- Crea un nuevo diccionario con los datos del equipo.
- Agrega el nuevo equipo al diccionario de equipos usando el nuevo ID como clave.
- Guarda el diccionario actualizado en el archivo JSON.
- Informa al usuario que el equipo fue registrado correctamente.

### ¿Qué guarda?:

Guarda el equipo registrado en el archivo `data/equipos.json`, actualizando el archivo con el nuevo equipo añadido.

### Aplicación:

Se utiliza para registrar nuevos equipos dentro del sistema de gestión de torneos, permitiendo mantener actualizada la base de datos de equipos.

------

### Función:

```
listar_equipos()
```

### ¿Qué hace?:

- Lee el archivo JSON con todos los equipos registrados.
- Si no hay equipos, muestra un mensaje indicando que no hay registros.
- Si hay equipos, muestra en formato tabular una lista con el ID, nombre, fecha de fundación, país y liga de cada equipo.
- El formato está diseñado para que la información quede ordenada y sea fácil de leer en la consola.

### ¿Qué guarda?:

No guarda datos, solo lee y muestra la información almacenada en `equipos.json`.

### Aplicación:

Permite al usuario visualizar fácilmente todos los equipos registrados en el sistema.

------

## estadisticas

------

### Función:

```
ver_estadisticas()
```

### ¿Qué hace?:

- Lee la información almacenada en tres archivos JSON: equipos, jugadores y transferencias.
- Muestra en consola estadísticas generales del sistema:
  - Número total de equipos registrados.
  - Número de jugadores que tiene cada equipo, agrupando por el ID del equipo.
  - Número total de transferencias registradas.
- Presenta estos datos de forma clara para que el usuario pueda entender el estado actual de los registros.

### ¿Qué guarda?:

No guarda datos, solo lee los datos existentes y muestra resultados estadísticos.

### Aplicación:

Permite visualizar estadísticas básicas sobre la base de datos del sistema de torneos, facilitando un resumen rápido para tomar decisiones o revisar el estado del sistema.

------

Aquí tienes la explicación para el módulo `jugadores.py` con las dos funciones que compartiste, siguiendo el formato que pediste:

------

### Archivo: `controllers/jugadores.py`

------

### Función:

```
registrar_jugador()
```

### ¿Qué hace?:

- Muestra un mensaje para que el usuario ingrese los datos de un nuevo jugador.
- Solicita al usuario el nombre, posición, número dorsal y el ID del equipo al que pertenece el jugador, usando la función `input_obligatorio()`.
- Lee la lista de equipos registrados para verificar que el ID del equipo exista.
- Si el equipo no existe, muestra un mensaje de error y no continúa con el registro.
- Si el equipo existe, lee el archivo JSON de jugadores y calcula un nuevo ID.
- Crea un diccionario con la información del jugador.
- Agrega el nuevo jugador al diccionario de jugadores.
- Guarda la lista actualizada en el archivo JSON.
- Informa que el jugador fue registrado correctamente.

### ¿Qué guarda?:

Guarda los datos del nuevo jugador en el archivo `data/jugadores.json`.

### Aplicación:

Permite registrar jugadores y asociarlos a un equipo dentro del sistema de gestión de torneos.

------

### Función:

```
listar_jugadores()
```

### ¿Qué hace?:

- Lee los datos de jugadores y equipos desde sus archivos JSON respectivos.
- Si no hay jugadores registrados, muestra un mensaje informativo.
- Si hay jugadores, muestra una tabla con ID, nombre, posición, número dorsal y nombre del equipo asociado.
- Para mostrar el nombre del equipo, busca en la lista de equipos usando el `equipo_id` del jugador. Si no encuentra el equipo, muestra "Desconocido".

### ¿Qué guarda?:

No guarda datos, solo lee y muestra la información almacenada.

### Aplicación:

Permite al usuario visualizar la lista completa de jugadores con detalles importantes y el equipo al que pertenecen.

------

Perfecto, aquí tienes la explicación del módulo `transferencias.py` con las dos funciones que mostraste, siguiendo el formato que pediste:

------

### Archivo: `controllers/transferencias.py`

------

### Función:

```
realizar_transferencia()
```

### ¿Qué hace?:

- Solicita al usuario ingresar el ID del jugador, el ID del equipo destino, el tipo de transferencia (venta o préstamo) y la fecha.
- Lee los datos actuales de jugadores, equipos y transferencias desde sus archivos JSON.
- Verifica que el jugador y el equipo destino existan.
- Si el tipo es "venta", actualiza el equipo del jugador en el archivo de jugadores para reflejar el cambio de equipo.
- Crea un nuevo registro de transferencia con un ID incremental.
- Guarda la nueva transferencia en el archivo JSON correspondiente.
- Informa al usuario que la transferencia fue registrada correctamente.

### ¿Qué guarda?:

Guarda la transferencia en `data/transferencias.json`. En caso de venta, también actualiza el equipo del jugador en `data/jugadores.json`.

### Aplicación:

Permite gestionar las transferencias de jugadores entre equipos, registrando la operación y actualizando el estado del jugador en el sistema.

------

### Función:

```
listar_transferencias()
```

### ¿Qué hace?:

- Lee los datos de transferencias, jugadores y equipos desde sus archivos JSON.
- Si no hay transferencias registradas, muestra un mensaje informativo.
- Si hay transferencias, muestra una tabla con el historial completo: ID, nombre del jugador, equipo origen, equipo destino, tipo de transferencia y fecha.
- Utiliza los IDs para obtener los nombres de jugadores y equipos, mostrando "Desconocido" si no encuentra algún dato.

### ¿Qué guarda?:

No guarda datos, solo muestra la información leída de los archivos JSON.

### Aplicación:

Permite al usuario consultar el historial de transferencias de jugadores en el sistema.

------

¡Claro! A continuación te explico **archivo por archivo** dentro de la carpeta `data`, incluyendo su **función**, **qué guarda** y **aplicación** dentro del sistema, como me pediste antes.

------

## 📁 Carpeta: `data`

Contiene la **base de datos en formato JSON** para tu sistema de gestión de torneos internacionales. Cada archivo representa una entidad del sistema.

------

### 1. `equipos.json`

#### 📌 Función:

Almacena todos los equipos registrados en el sistema.

#### 📂 ¿Qué guarda?:

Cada equipo con la siguiente información:

- `id`: Identificador único.
- `nombre`: Nombre del equipo.
- `fundacion`: Fecha de fundación.
- `pais`: País de origen.
- `liga_id`: Liga a la que pertenece el equipo.

#### 🧩 Aplicación:

Se usa en:

- Registro y listado de equipos.
- Asociación de jugadores, dirigentes y transferencias.
- Estadísticas por equipo.

------

### 2. `jugadores.json`

#### 📌 Función:

Guarda todos los jugadores registrados.

#### 📂 ¿Qué guarda?:

Cada jugador con:

- `id`: Identificador único.
- `nombre`: Nombre completo.
- `posicion`: Posición (portero, defensa, etc.).
- `numero`: Número de camiseta.
- `equipo_id`: ID del equipo al que pertenece.

#### 🧩 Aplicación:

Se usa para:

- Registrar jugadores.
- Listarlos por equipo.
- Controlar transferencias y estadísticas.

------

### 3. `transferencias.json`

#### 📌 Función:

Almacena el historial de transferencias (ventas o préstamos) de jugadores.

#### 📂 ¿Qué guarda?:

Cada transferencia con:

- `id`: ID de la transferencia.
- `id_jugador`: ID del jugador transferido.
- `origen`: ID del equipo anterior.
- `destino`: ID del nuevo equipo.
- `tipo`: Tipo de transferencia ("venta" o "préstamo").
- `fecha`: Fecha de la transferencia.

#### 🧩 Aplicación:

- Registrar movimientos de jugadores.
- Mostrar el historial completo.
- Permitir seguimiento y estadísticas de fichajes.

------

### 4. `dirigentes.json`

#### 📌 Función:

Almacena información de los dirigentes (presidentes, técnicos, etc.) de los equipos.

#### 📂 ¿Qué guarda?:

Cada dirigente con:

- `id`: Identificador único.
- `nombre`: Nombre completo.
- `rol`: Cargo dentro del equipo (presidente, director técnico…).
- `equipo_id`: ID del equipo al que pertenece.

#### 🧩 Aplicación:

(Actualmente no integrada en las funciones principales, pero útil para):

- Administración de equipos.
- Reportes o vistas jerárquicas del club.

------

### 5. `ligas.json`

#### 📌 Función:

Guarda las ligas disponibles en el sistema (ej. LaLiga, Premier League).

#### 📂 ¿Qué guarda?:

Cada liga con información como:

- `id`: Identificador único.
- `nombre`: Nombre de la liga.
- `pais`: País donde se disputa.

#### 🧩 Aplicación:

- Asignar equipos a ligas.
- Organizar torneos o filtrar estadísticas por liga.

------

### 6. `partidos.json`

#### 📌 Función:

Contiene los datos de partidos jugados o programados.

#### 📂 ¿Qué guarda?:

Cada partido con datos como:

- `id`: Identificador del partido.
- `equipo_local` y `equipo_visitante`: IDs de los equipos.
- `fecha`: Fecha del partido.
- `resultado`: Resultado final (opcional).

#### 🧩 Aplicación:

- Registrar y consultar resultados.
- Usar para generar estadísticas o posiciones.

------

### 7. `torneos.json`

#### 📌 Función:

Almacena la información de los torneos registrados.

#### 📂 ¿Qué guarda?:

Cada torneo con información como:

- `id`: ID del torneo.
- `nombre`: Nombre del torneo.
- `pais` o `region`: Ubicación.
- `equipos_participantes`: Lista de IDs de los equipos inscritos.

#### 🧩 Aplicación:

- Organizar competiciones.
- Agrupar partidos.
- Generar clasificaciones o fases eliminatorias.

------

¡Perfecto! Vamos ahora con la explicación del archivo `corefiles.py` que se encuentra en la carpeta `utils`, siguiendo el formato que me pediste: **función, qué hace, qué guarda y aplicación**.

------

## 📁 Carpeta: `utils`

Esta carpeta contiene funciones de utilidad que ayudan a otros módulos del sistema, como leer/guardar archivos (`corefiles.py`), validar datos (`validatedata.py`), manejar pantallas (`screencontrollers.py`) o configuraciones generales (`config.py`).

------

## 📄 Archivo: `corefiles.py`

Este archivo gestiona la lectura y escritura de archivos `.json` para que todo el sistema pueda trabajar con persistencia de datos.

------

### Función:

```
leer_json(ruta)
```

### ¿Qué hace?:

- Verifica si el archivo en la ruta especificada existe.
- Si no existe, devuelve un diccionario vacío (`{}`).
- Si existe, lo abre en modo lectura (`"r"`) y lo carga como un diccionario usando `json.load()`.

### ¿Qué guarda?:

No guarda nada, solo **lee y devuelve** los datos del archivo JSON.

### Aplicación:

Se utiliza en todos los módulos para cargar los datos actuales desde archivos JSON antes de modificarlos o consultarlos (por ejemplo: equipos, jugadores, transferencias, etc.).

------

### Función:

```
guardar_json(ruta, datos)
```

### ¿Qué hace?:

- Abre el archivo en modo escritura (`"w"`) y codificación UTF-8.
- Escribe (`dump`) los datos proporcionados en formato JSON.
- Usa `indent=4` para que el archivo sea legible y `ensure_ascii=False` para permitir caracteres especiales (como tildes o eñes).

### ¿Qué guarda?:

Guarda un diccionario de datos (`datos`) en un archivo JSON en la ruta proporcionada (`ruta`).

### Aplicación:

Se usa cada vez que se actualizan los datos del sistema (por ejemplo: al registrar un nuevo jugador o transferencia).

------

### 🔄 Resumen visual:

```python
leer_json("data/equipos.json")     # Devuelve los datos de equipos como diccionario
guardar_json("data/jugadores.json", jugadores)  # Guarda el diccionario actualizado
```

------

¡Perfecto! Ahora vamos con la explicación de `validatedata.py`, que también se encuentra en la carpeta `utils`. Como siempre, lo explico con:

- Función
- ¿Qué hace?
- ¿Qué guarda?
- Aplicación

------

## 📄 Archivo: `validatedata.py`

Este archivo contiene funciones para validar los datos ingresados por el usuario desde la consola. Su propósito principal es asegurar que no se ingresen valores vacíos o inválidos.

------

### ✅ Función: `input_obligatorio(mensaje)`

### 📌 ¿Qué hace?:

- Muestra un mensaje en consola (pasado como parámetro).
- Espera que el usuario escriba una respuesta.
- Si el usuario deja el campo vacío, vuelve a pedir el dato hasta que lo complete correctamente.
- Finalmente devuelve el valor ingresado (limpio).

### 💾 ¿Qué guarda?:

No guarda nada directamente, pero **retorna** el valor ingresado por el usuario para que otras funciones lo usen (por ejemplo, al crear un jugador o un equipo).

### 🧩 Aplicación:

Usado para validar que los campos requeridos **no estén vacíos** cuando el usuario está registrando:

- Un equipo (`nombre`, `fundación`, etc.).
- Un jugador (`nombre`, `posición`, etc.).
- Una transferencia (`tipo`, `fecha`, etc.).

Esto evita que se ingresen datos incompletos que pueden romper la lógica del sistema.

------

### 🧠 Ejemplo de uso:

```python
nombre = input_obligatorio("Nombre del jugador: ")
# Si el usuario no escribe nada, seguirá preguntando hasta que escriba algo.
```

------

### 💡 Posible mejora futura:

Se podrían agregar otras funciones para:

- Validar fechas (formato correcto).
- Validar números enteros (ej. número de camiseta).
- Validar que un ID exista antes de usarlo.

------

¡Perfecto! Gracias por mostrar el contenido de `screencontrollers.py`. Ahora te explico este archivo según el formato que usas: **Función, Qué hace, Qué guarda y Aplicación**.

------

## 📄 Archivo: `screencontrollers.py`

Este archivo contiene funciones auxiliares para mejorar la experiencia del usuario en la terminal.

------

### ✅ Función: `limpiar_pantalla()`

#### 📌 ¿Qué hace?

Limpia la consola o terminal para que el contenido anterior desaparezca, dejando la pantalla limpia para mostrar nueva información.

- Usa `os.system('cls')` si estás en **Windows**.
- Usa `os.system('clear')` si estás en **Linux o MacOS**.

#### 💾 ¿Qué guarda?

No guarda nada. Solo **limpia la pantalla de salida**.

#### 🧩 Aplicación:

- Mejora la presentación del menú.
- Se puede usar antes de mostrar formularios o listados grandes.

------

### ✅ Función: `pausar_pantalla()`

#### 📌 ¿Qué hace?

Hace una **pausa en la ejecución** del programa hasta que el usuario presione la tecla `Enter`.

#### 💾 ¿Qué guarda?

Tampoco guarda nada. Solo **espera la interacción del usuario**.

#### 🧩 Aplicación:

- Permite que el usuario **lea un mensaje o resultado** antes de volver al menú.
- Muy útil después de mostrar un listado o registrar un dato.

------

### 🧠 Ejemplo de uso integrado:

```python
from utils.screencontrollers import limpiar_pantalla, pausar_pantalla

def menu():
    while True:
        limpiar_pantalla()
        print("=== MENÚ PRINCIPAL ===")
        print("1. Registrar jugador")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_jugador()
            pausar_pantalla()
        elif opcion == "0":
            break
```

------

## 📄 Archivo: `config.py`

### Función:

Contiene **constantes o configuraciones globales** del sistema que pueden reutilizarse en distintos módulos.

### ¿Qué hace?:

Define rutas, colores, nombres de archivos, opciones de menú u otras variables reutilizables.

### ¿Qué guarda?:

No guarda datos dinámicos, pero define valores estáticos que sirven como referencia en todo el sistema.

### Aplicación:

- Centraliza configuraciones.
- Facilita el mantenimiento (ej. si cambias la carpeta `"data"` por otra, solo la cambias aquí).
- Evita repetir cadenas largas o rutas en muchos archivos.

------

### Ejemplo típico de contenido:

```
pythonCopiarEditarDATA_PATH = "data"
ARCHIVO_EQUIPOS = "equipos.json"
ARCHIVO_JUGADORES = "jugadores.json"
ARCHIVO_TORNEOS = "torneos.json"
```

Luego podrías usarlo así:

```
pythonCopiarEditarfrom utils.config import DATA_PATH, ARCHIVO_EQUIPOS
ruta = os.path.join(DATA_PATH, ARCHIVO_EQUIPOS)
```