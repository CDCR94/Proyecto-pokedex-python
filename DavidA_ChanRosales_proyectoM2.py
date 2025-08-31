# Solicitar coordenadas al usuario
x = float(input("Ingrese X: "))
y = float(input("Ingrese Y: "))

# Verificar que ninguna coordenada sea cero
if x == 0 or y == 0:
    print("Ninguna coordenada debe ser 0.")
else:
    # Determinar el cuadrante
    if x > 0 and y > 0:
        print("El punto se encuentra en el cuadrante I")
    elif x < 0 and y > 0:
        print("El punto se encuentra en el cuadrante II")
    elif x < 0 and y < 0:
        print("El punto se encuentra en el cuadrante III")
    elif x > 0 and y < 0:
        print("El punto se encuentra en el cuadrante IV")