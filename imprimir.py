# Función para imprimir listas con mensaje
def imprimir_lista(lista, mensaje):
    print(f"\n{mensaje}:")
    for i, elem in enumerate(lista, start=1):
        print(f"{i}. {elem}")
