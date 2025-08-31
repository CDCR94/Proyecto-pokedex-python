# texto_variado="Palabra 123 + -#$%"
# print(type(texto_variado))
#Podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito


# print("""Funcionamiento de\
#       programa:(opcioones)
#       -1 Para acceder a opciones
#       -2 para salir""")

# #Subscriptin e indexado
# texto= 'Python'


# ## no podemos acceder a una posicion que no existe
# print(texto[0])
# letra="d"

# #Concatenacion de texto
# texto_compuesto= texto[0]+letra

# print(texto_compuesto)

# #slicing o substringing

# print(texto[0:3]) # imprime desde la posicion 0 al 3
# print(texto[0::1])  #imprima desde la posicion 0 con saltos de 1

# texto2="Hola mundo! buenas noches"
# print(texto2.lower())  #Se imprime todo en minuscula
# print(texto2.upper())  #Se imprime todo en mayuscula
# print(texto2.capitalize())  #convertir la primera letra de una cadena en mayusculas
# print(texto2.title())     #inicial de cada palabra a mayuscula
# print(texto2.swapcase())   #intercambio de minusculas a mayusculas

# texto2=texto2.upper()
# print(texto2)

print("{} + {} = {}".format(2, 3, 2+3))
print("{} + {} = {}".format("hola", "mundo", "hola mundo"))
print("{:.3f} + {:.4f}= {}".format(2, 3, 2+3))
print("{1} + {0} = {2}".format(2, 3, 2+3))
print("{2} + {0} = {1}".format("hola", "mundo", "hola mundo"))
print("{:d}={:b}={:o}={:x}".format(15, 15, 15, 15))