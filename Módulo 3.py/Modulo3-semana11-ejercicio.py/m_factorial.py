# Un módulo es un archivo que contiene varias definiciones y sentencias de Python.
# Es importante tener en cuenta que cada módulo debe tener un nombre de archivo que lo identifique,
# sin olvivar que al nombre del móudlo se le debe de agragar la extencion "py".


#Módulo m_factorial(m_factorial.py)
''' Módulo que cotiene la función recursiva del factorial '''

def factorial(num): # se crea una función de nombre "factorial" y se pasa un parámetro que se llama "num"
    ''' Calcular el factorial de un número'''

    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
        

