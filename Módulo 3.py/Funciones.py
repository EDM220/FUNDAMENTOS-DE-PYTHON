# Qué son las funciones?
# Una función nos ayuda: No duplicar código,dividir una tarea compleja en varias más específicas,-
# ocultar los detalles de la implementación, mejorar la legibilidad del código, mejorar la trazabilida
# del código.

# función simple. Utizar la sentencia "def" después el nombre que se desee darle seguida de parentesis

# def funcion_simple():
    # pass
# print('Antes de llamar a la función')
# funcion_simple()
# print('Ya se ha llamado a la función')

# Otro ejemplo con otra función que va a saludar al mundo

# def saluda():
#     print('Hola Mundo!')
# print('Antes de llamar a la función')
# funcion_simple()
# saluda()
# print('Ya se ha llamado a ala función')    

# Se puede hacer uso de la función "help" para desplegar en pantalla acerca de las funciones que se tiene duda
# nos muestra la documentación de la función, de esta misma manera nosotros podemos usar la función "help"
# para que se muestre información acerca de nuestras funciones. Esto se hace por medio de triple comillas
# simples o dobles y todo lo que se escriba dentro de este block de código se llmará  "docstring" o cadenas
# de documentación.

def funcion_simple():
    """Esta función no hace nada""" # definiendo las cadenas de documentación
    pass

def saluda():
    '''Función que saluda al mundo'''
    print('Hola Mundo!')


help(funcion_simple) # Aquí no se usan comillas porque se estan empleando parámetros a diferencia de print("")
help(saluda) # Los parámetros son variables que vamos a utilizar para dar valores de entrada en diferentes
             # funciones o métodos
