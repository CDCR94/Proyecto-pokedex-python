# Programa para comparar años con opción de repetir

while True:
    # Solicitar los años al usuario
    year_actual = int(input("Ingresa el año actual: "))
    year_cualquiera = int(input("Ingresa otro año: "))

    # Comparar los años
    if year_actual == year_cualquiera:
        print("Has ingresado el mismo año dos veces.")
    elif year_cualquiera < year_actual:
        diferencia = year_actual - year_cualquiera
        if diferencia == 1:
            print(f"Ha pasado 1 año desde {year_cualquiera}.")
        else:
            print(f"Han pasado {diferencia} años desde {year_cualquiera}.")
    else:
        diferencia = year_cualquiera - year_actual
        if diferencia == 1:
            print(f"Falta 1 año para llegar a {year_cualquiera}.")
        else:
            print(f"Faltan {diferencia} años para llegar a {year_cualquiera}.")

    # Preguntar si desea continuar
    respuesta = input("\n¿Deseas comparar otros años? (s/n): ").strip().lower()
    if respuesta != 's':
        print("Programa finalizado.")
        break
