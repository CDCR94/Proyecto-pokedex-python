# Elimina elementos de lista1 que estén en lista2
def eliminar_elementos(lista1, lista2):
    # Usamos comprensión de listas para eliminar elementos
    return [elemento for elemento in lista1 if elemento not in lista2]