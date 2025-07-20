import os  # Importamos módulo para comandos del sistema

alumnos = []  # Lista global para almacenar los alumnos

# Función para agregar un nuevo alumno
def agregar_alumno():
    global alumnos
    nombre = input("Ingrese el nombre del alumno: ").capitalize()
    alumnos.append([nombre,[0,0,0],[0,0,0,0],[0,0]])  # Inicializamos sus notas

# Función para buscar un alumno en la lista y registrar sus notas
def buscar_alumno(alumnos: list,op:int):
    nombre = input("Ingrese el nombre del alumno: ")
    for alumno in alumnos:
        if nombre.capitalize() in alumno:  # Si el nombre coincide
            ingresar_notas(alumno,op)  # Llama a la función de ingresar notas
            break

# Función para ingresar notas según el tipo (1=parciales, 2=quices, 3=trabajos)
def ingresar_notas(alumno: list,tipoNota: int):
    msg = ''
    match tipoNota:
        case 1:
            msg = 'Ingresando notas parciales'
        case 2:
            msg = 'Ingresando notas Quices'
        case 3:
            msg = 'Ingresando nota Trabajos'

    # Mostramos mensaje para el usuario
    print(f'{msg} para {alumno[0]}')
    
    # Recorremos la lista de notas correspondiente
    for idx,nota in enumerate(alumno[tipoNota]):
        if nota == 0:  # Si hay un espacio libre (nota no ingresada)
            nota_parcial =int(input('ingrese la nota : '))
            alumno[tipoNota][idx] = nota_parcial  # Guardamos la nota
            break  # Solo una nota por ejecución

    os.system('pause')  # Pausamos para que el usuario vea el resultado

# Función que muestra el menú de notas y devuelve una opción válida
def menu_notas()->int:
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia pantalla
    print('Modulo de registro de notas')
    print('1. Ingresar notas parciales')
    print('2. Ingresar notas Quices')
    print('3. Ingresar nota Trabajos')
    print('4. Regregar menu principal')
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 4:
            print("Opción no válida. Intente de nuevo.")
            return menu_notas()
        return opcion
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return menu_notas()

# Función que muestra el menú principal del sistema
def main_menu()-> int:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Menú de gestión de alumnos")
    print("1. Agregar alumno")
    print("2. Registrar notas")
    print("3. Consultar nota final")
    print("4. Mostrar planilla de alumnos")
    print("5. Salir")
    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion < 1 or opcion > 5:
            print("Opción no válida. Intente de nuevo.")
            return main_menu()
        return opcion
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")
        return main_menu()

# Punto de entrada del programa
if __name__ == "__main__":
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bienvenido al sistema de gestión de alumnos")
        opcion = main_menu()
        match opcion:
            case 1:
                agregar_alumno()
            case 2:
                while True:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    opcion_notas = menu_notas()
                    match opcion_notas:
                        case 1:
                            print("Ingresar notas parciales")
                            # ingresar_notas_parciales(estudiante, alumnos)
                            buscar_alumno(alumnos,1)
                            os.system('pause')
                        case 2:
                            print("Ingresar notas Quices")
                            buscar_alumno(alumnos,2)
                            # Aquí se agregarían las notas de quices
                            os.system('pause')
                        case 3:
                            print("Ingresar nota Trabajos")
                            buscar_alumno(alumnos,3)
                            # Aquí se agregarían las notas de trabajos
                            os.system('pause')
                        case 4:
                            break
            case 3:
                pass  # Esta opción está aún sin implementar
            case 4:
                print("Planilla de estudiantes registrados")
                print(alumnos)
                # print(tabulate(alumnos, headers=["Nombre", "Notas Parciales", "Notas Finales", "Promedio"], tablefmt="grid"))
                os.system('pause')
            case 5:
                os.system('pause')
                break
            case _:
                print("Opción no válida. Intente de nuevo.")

