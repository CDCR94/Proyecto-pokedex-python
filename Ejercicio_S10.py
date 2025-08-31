def agregar_datos(lista, valor='No especificado'):
    '''Funcion que agrega un dato a una lista especificada'''
    lista.append(valor)
    return lista



nombres = []
edades = []
sexos = []

personas=int(input('¿Cuantas personas se quiere registrar? '))

for i in range(personas):
    nombre=input(f'Ingrese el nombre de la persona {i+1}: ').title()
    nombres=agregar_datos(nombres, nombre)
for i in range(personas):
    edad=input(f'Ingrese la edad de {nombres[i]} ')
    edades=agregar_datos(edades, edad)
for i in range(personas):
    sexo=input(f'¿Cual es el sexo de {nombres[i]}? ')
    sexos=agregar_datos(sexos, sexo)