------

## 🌟 ¿Qué hace este programa?

Este programa es como un **sistema para administrar un torneo de fútbol**. Te deja registrar equipos, jugadores, partidos, ver estadísticas y hacer transferencias de jugadores entre equipos.

------

## 🧠 ¿Cómo funciona?

### 1. **Menú principal**

Cuando abres el programa, ves un menú con varias opciones, como:

- Registrar un equipo
- Ver todos los equipos
- Registrar un jugador
- Ver todos los jugadores
- Hacer transferencias de jugadores
- Ver estadísticas
- Salir

Solo tienes que escribir el número de la opción que quieres usar.

------

### 2. **Registrar equipo**

Cuando eliges registrar un equipo, el programa:

- Limpia la pantalla
- Te pide datos como:
  - Nombre del equipo
  - Año en que se creó
  - País de origen
  - Número de la liga
- Crea un número único (ID) para ese equipo
- Guarda todo eso en un archivo llamado `equipos.json`
- Te dice si se guardó bien

------

### 3. **Ver equipos**

Si eliges ver los equipos, el programa:

- Limpia la pantalla
- Busca los equipos guardados en el archivo
- Muestra en pantalla cada equipo con su nombre, país, año y liga
- Si no hay equipos, te avisa

------

### 4. **Registrar jugador**

Si eliges registrar un jugador:

- Limpia la pantalla
- Pide datos como:
  - Nombre
  - Posición (por ejemplo: defensa)
  - Número del uniforme (dorsal)
  - ID del equipo donde va a jugar
- Le crea un ID único
- Guarda todo en `jugadores.json`
- Y también lo añade al equipo correspondiente

------

### 5. **Ver jugadores**

Muestra todos los jugadores registrados, uno por uno, con su nombre, posición, número, y equipo al que pertenecen.

------

### 6. **Transferir jugador**

Esta opción permite cambiar a un jugador de un equipo a otro:

- Muestra los equipos
- Te pide el ID del equipo de origen y del destino
- Luego te muestra los jugadores del equipo de origen
- Eliges cuál transferir
- El jugador se borra del primer equipo y se pone en el nuevo

------

### 7. **Estadísticas y partidos**

Puedes:

- Programar un partido entre dos equipos (decidir fecha y equipos)
- Registrar el resultado del partido (goles)
- Ver las estadísticas (qué partidos se han jugado y sus resultados)

------

## 🗂️ Archivos usados

Estos archivos guardan toda la información:

- `equipos.json`: guarda los equipos
- `jugadores.json`: guarda los jugadores
- `partidos.json`: guarda los partidos
- `ligas.json`: guarda las ligas
- `transferencias.json`: guarda el historial de transferencias
- `torneos.json`: guarda torneos especiales
- `dirigentes.json`: guarda la información de los directivos del club

------

## 🧰 Archivos especiales que ayudan

- `corefiles.py`: se encarga de leer y escribir los archivos `.json`
- `screencontrollers.py`: limpia la pantalla y pausa el programa para que puedas leer los mensajes
- `validatedata.py`: revisa que escribas bien los datos (por ejemplo, que no pongas letras donde van números)

------

## ✅ En resumen

Este sistema:

- Guarda todo lo que haces en archivos `.json`
- Te muestra menús para que puedas hacer todo fácil desde la consola
- Usa validaciones y limpiezas para que sea más amigable
- Sirve para practicar programación modular y manejo de datos reales (como en una liga de fútbol)

------

¿Quieres que lo pase también a formato PDF con este estilo más simple?