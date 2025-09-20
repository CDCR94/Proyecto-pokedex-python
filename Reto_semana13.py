def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar un nuevo alumno")
    print("2. Ver alumnos y calificaciones")
    print("S. Salir")
    return input("Selecciona una opción: ").strip()


def agregar_alumno(alumnos):
    while True:
        nombre = input("Nombre del alumno: ").strip()
        if nombre == "":
            print("El nombre no puede estar en blanco. Intenta de nuevo.")
        elif nombre in alumnos:
            print("El alumno ya existe. Intenta con otro nombre.")
        else:
            break

    while True:
        try:
            cantidad = int(input(f"¿Cuántas calificaciones deseas ingresar para {nombre}? "))
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que 0.")
            break
        except ValueError as e:
            print(f"Error: {e}. Intenta de nuevo.")

    calificaciones = []
    for i in range(cantidad):
        while True:
            try:
                calificacion = float(input(f"Calificación {i+1}: "))
                if calificacion < 0 or calificacion > 10:
                    raise ValueError("La calificación debe estar entre 0 y 10.")
                calificaciones.append(calificacion)
                break
            except ValueError as e:
                print(f"Error: {e}. Intenta de nuevo.")

    alumnos[nombre] = calificaciones
    print(f"Alumno {nombre} agregado correctamente.")


def ver_alumnos(alumnos):
    if not alumnos:
        print("No hay alumnos registrados.")
        return
    print("\n===== LISTA DE ALUMNOS =====")
    for nombre, calificaciones in alumnos.items():
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"{nombre}: Promedio {promedio:.2f}")


def salir():
    while True:
        opcion = input("¿Seguro que deseas salir? (S/N): ").strip().upper()
        if opcion == "S":
            print("Cerrando el programa...")
            return True
        elif opcion == "N":
            print("Regresando al menú principal...")
            return False
        else:
            print("Opción inválida, escribe 'S' o 'N'.")


def main():
    alumnos = {}
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            agregar_alumno(alumnos)
        elif opcion == "2":
            ver_alumnos(alumnos)
        elif opcion.upper() == "S":
            if salir():
                break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    main()