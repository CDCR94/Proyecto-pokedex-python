while True:
    print("\n=== Calculadora de IMC ===")

    # Pedir nombre (solo letras y espacios)
    while True:
        nombre = input("Escribe tu nombre: ")
        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("Nombre inválido. Solo puedes usar letras y espacios.")

    # Pedir edad (solo números enteros)
    while True:
        edad = input("Escribe tu edad (en años): ")
        if edad.isdigit():
            edad = int(edad)
            if edad > 0:
                break
        print("Edad inválida. Debe ser un número entero positivo.")

    # Pedir estatura (decimal en metros)
    while True:
        estatura = input("Escribe tu estatura en metros (ej. 1.75): ")
        try:
            estatura = float(estatura)
            if estatura > 0:
                break
            else:
                print("La estatura debe ser mayor que cero.")
        except ValueError:
            print("Entrada inválida. Usa punto para los decimales.")

    # Pedir masa (decimal en kg)
    while True:
        masa = input("Escribe tu masa en kilogramos (ej. 68.5): ")
        try:
            masa = float(masa)
            if masa > 0:
                break
            else:
                print("La masa debe ser mayor que cero.")
        except ValueError:
            print("Entrada inválida. Usa punto para los decimales.")

    # Calcular IMC
    imc =masa / (estatura ** 2)

    # Mostrar resultados
    print("\n--- Resultado ---")
    print("Nombre:", nombre)
    print("Edad:", edad, "años")
    print("Estatura:", estatura, "m")
    print("Masa:", masa, "kg")
    print("Tu IMC es:", round(imc, 2))

    # Clasificación
    if imc < 18.50:
        print("Clasificación: Bajo peso")
    elif imc >= 18.50 and imc <=24.99:
        print("Clasificación: Peso normal")
    elif imc >= 25.00 and imc <=29.99:
        print("Clasificación: Sobrepeso")
    elif imc >=30.00 and imc <=34.99:
        print("Clasificación: Obesidad leve")
    elif imc >=35.00 and imc <= 39.99:
        print("Clasificación: Obesidad media")
    else :
        print("Clasificación: Obesidad morbida")


    # Preguntar si quiere calcular otro IMC
    repetir = input("\n¿Quieres calcular otro IMC? (sí/no): ").strip().lower()
    if repetir != "sí" and repetir != "si":
        print("¡Gracias por usar la calculadora!")
        break
