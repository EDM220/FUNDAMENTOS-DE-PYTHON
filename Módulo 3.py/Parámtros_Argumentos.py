# Para trabaja con funciones se debe de comprender que hay distos valores en juego los parámetros y argumentos
# los parámetros son las variables que se declaran en la definición de la función, mientras que los argumentos
# son los valores con los cuales se invoca una función. Por lo tanto, son los valores que se tomaran como -
# parámetros dentro de la función.Un dato importante es que son posicionales, es decir se debe respetar
# la posición en la que fueron definidos los parámetros

# def sumar(parametro1,parametro2):
#     '''Función que imprime dos parámetros y los imprime en pantalla''' # "docstring" o cadenas
                                                                       # de documentación.
    # print('suma:', parametro1 + parametro2)
# argumeto1 = 5
# argumento2 = 7

# Invocando la función por medio de parámetro variables
# sumar(argumeto1,argumento2)

# Invocando la función por medio de parámetro de valor
# sumar('mundo!','Hola ')
# sumar('Hola ','mundo!')

# sumar('Hola') # aquí mandará un error porque se definio la función por medio de 2 parámetros

# Existe casos en los que se necesite jecutar funciones pero no dispongamos de la información necesaria para
# establecerla como parámetros, en esos casos existen las funciones con parámetros opcionales de esta manera
# se podría ejecutar una función que tuviera 3 parámetros estableciendo solo uno o dos o quizás ninguno.
# A cualquier parámetro se le puede asignar un valor por defecto y por lo tanto hacerlo opcional, los parámetros
# opcionales deben  de ser declarados al final de la lista de los parámetros

# Ejemplo de parámetros opcionales

def muestra_alumno(nombre,edad = 18,sexo = 'F'):
    """Es una función que muestra en pantalla, el nombre, la edad y el sexo de un alumno
    recibe tres parámetros
    1.-nombre
    2.-edad = 18
    3.-sexo = 'F'
    """
    print(f'Nombre: {nombre}, edad: {edad},sexo: {sexo}')
# Ejecución de parámetro obligatorio    
muestra_alumno('María')

# Ejecución utilizando el parámetro obligatorio y uno opcional
muestra_alumno('María',22)

# Ejecucion de función con el primer y último parámetro
muestra_alumno('Juan',sexo = 'M')
