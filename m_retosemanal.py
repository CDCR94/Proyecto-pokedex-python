import Crear
import Eliminar
import imprimir

def main():
       # Crear las dos listas
    lista1 = Crear.crear_lista("Lista 1")
    lista2 = Crear.crear_lista("Lista 2")

    # Imprimir listas originales
    imprimir.imprimir_lista(lista1, "Lista 1 original")
    imprimir.imprimir_lista(lista2, "Lista 2 original")

    # Eliminar elementos de lista1 que estén en lista2
    lista1 = ELiminar.eliminar_elementos(lista1, lista2)

    # Imprimir lista1 actualizada
    imprimir.imprimir_lista(lista1, "Lista 1 después de eliminar elementos de Lista 2")

if __name__=="__main__":
   main()
