# Función para crear una lista pidiendo datos al usuario
def crear_lista(nombre_lista):
    lista = []
    longitud = int(input(f"Ingrese la longitud de {nombre_lista}: "))
    for i in range(longitud):
        elemento = input(f"Ingrese el elemento {i+1} de {nombre_lista}: ").title()
        lista.append(elemento)
    return lista

# Función para imprimir listas con mensaje
def imprimir_lista(lista, mensaje):
    print(f"\n{mensaje}:")
    for i, elem in enumerate(lista, start=1):
        print(f"{i}. {elem}")

# Función para eliminar elementos de lista1 que estén en lista2
def eliminar_elementos(lista1, lista2):
    # Usamos comprensión de listas para eliminar elementos
    return [elemento for elemento in lista1 if elemento not in lista2]

# --- Programa principal ---

# Crear las dos listas
lista1 = crear_lista("Lista 1")
lista2 = crear_lista("Lista 2")

# Imprimir listas originales
imprimir_lista(lista1, "Lista 1 original")
imprimir_lista(lista2, "Lista 2 original")

# Eliminar elementos de lista1 que estén en lista2
lista1 = eliminar_elementos(lista1, lista2)

# Imprimir lista1 actualizada
imprimir_lista(lista1, "Lista 1 después de eliminar elementos de Lista 2")