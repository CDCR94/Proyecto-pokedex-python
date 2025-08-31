# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")

# Calcular la longitud de la palabra
longitud = len(palabra)

# Verificar la longitud y mostrar el mensaje correspondiente
if 4 <= longitud <= 8:
    print("La palabra es correcta.")
elif longitud < 4:
    print(f"Hacen falta letras. Solo tiene {longitud} letras.")
else:
    print(f"Sobran letras. Tiene {longitud} letras.")