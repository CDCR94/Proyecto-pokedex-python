# Función para crear una lista pidiendo datos al usuario
def crear_lista(nombre_lista):
    lista = []
    longitud = int(input(f"Ingrese la longitud de {nombre_lista}: "))
    for i in range(longitud):
        elemento = input(f"Ingrese el elemento {i+1} de {nombre_lista}: ").title()
        lista.append(elemento)
    return lista