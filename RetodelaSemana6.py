# Programa de verificación de contraseña con intentos limitados

# Solicitar contraseña que comience con un número
while True:
    contrasena = input("Crea una contraseña que comience con un número: ")
    if contrasena and contrasena[0].isdigit():
        break
    else:
        print("Error: La contraseña debe comenzar con un número.\n")

# Verificación de la contraseña con máximo 3 intentos
intentos = 0
while intentos < 3:
    verificacion = input("Vuelve a ingresar la contraseña para verificar: ")
    if verificacion == contrasena:
        print("Contraseña verificada con éxito.")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta. Intento {intentos} de 3.\n")

if intentos == 3:
    print("Has superado el número máximo de intentos. El programa se cerrará.")