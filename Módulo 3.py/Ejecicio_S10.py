# Indicaciones
# 1.- Solicite al usuario cierto número de personas para agregar a un formulario.
# 2.- Qué primero, solicite el nombre de todas las personas que se ingresarán.
# 3.- Después pregunte la edad de cada persona.
# 4.- En seguida pregunte el sexo de cada persona, refierendose a ella por su nombre.
# 5.- Si no se especifica el sexo, se guarda la variable como 'no especificado'.
# 6.- se unen los tres datos introducidos en una tupla por persona y se imprime en la pantalla.
# 7.- Usar al menos una función. 

def agregar_datos(lista,valor):
    '''
    Función que agraga un dato a una lista especificada
    '''
    if valor == '':
        valor = 'No especificado'
    lista.append(valor)
    return lista

nombres = []
edades = []
sexos= []

personas = int(input('Cúantas personas se quieren registrar? '))

for i in range(personas):
    nombre = input(f'Ingrese el nombre de la persona {i + 1}: ').title() # Se escribre "{i + 1}" debido 
    # a que el range comienza en 0, entonces sería 0 + 1. El mensaje diría "Ingrese el nombre de la persona 1",
    # además se desea que el nombre comience con la primera letra en mayúscula por lo que se escribe "title"
    nombres = agregar_datos(nombres,nombre) # se agrega los nombres a la lista "nombres = []"

# se hace lo mismo para "edad" y " sexo"   

for i in range(personas):
    edad = input(f'Ingrese la edad de  {nombres[i]}: ') # se pregunta la edad de la primera persona (iteración)
    edades = agregar_datos(edades,edad)
for i in range(personas):
    sexo = input(f'Cuál es el sexo de {nombres[i]}: ')
    sexos = agregar_datos(sexos,sexo)  

for i in zip(nombres,edades,sexos):
    print(i)
