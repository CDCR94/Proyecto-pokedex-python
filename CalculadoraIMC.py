def pedir_nombre():
    while True:
        nombre = input("Ingresa tu nombre: ")
        if all(c.isalpha() or c.isspace() for c in nombre) and nombre.strip() != "":
            return nombre.strip()
        else:
            print("Entrada inválida. Solo se permiten letras y espacios.")

def pedir_edad():
    while True:
        entrada = input("Ingresa tu edad (solo números): ")
        if entrada.isdigit():
            edad = int(entrada)
            if edad > 0:
                return edad
        print("Edad inválida. Ingresa un número entero positivo.")

def pedir_numero_decimal(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            numero = float(entrada)
            if numero > 0:
                return numero
            else:
                print("Debe ser un número positivo.")
        except ValueError:
            print("Entrada inválida. Ingresa solo números (usa punto para decimales).")

# --- Programa principal ---
print("=== Calculadora de IMC ===")

nombre = pedir_nombre()
edad = pedir_edad()
estatura = pedir_numero_decimal("Ingresa tu estatura en metros (ej. 1.75): ")
masa = pedir_numero_decimal("Ingresa tu masa en kilogramos (ej. 68.5): ")

# Calcular IMC
imc = masa / (estatura ** 2)

# Mostrar resultados
print("\n--- Resultado ---")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Estatura: {estatura} m")
print(f"Masa: {masa} kg")
print(f"Tu IMC es: {imc:.2f}")

# Clasificación opcional
if imc < 18.5:
    print("Clasificación: Bajo peso")
elif imc < 24.9:
    print("Clasificación: Normal")
elif imc < 29.9:
    print("Clasificación: Sobrepeso")
else:
    print("Clasificación: Obesidad")
