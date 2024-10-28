# Programa para ejemplicar un par de errores más comunes cuando se incicia en la programación.

numerador = 10 
denominador = 0
cadena = '3'
numerico = 5

# print(numerador / denominador) # Aquí se tendría un error porque el denominador es un cero
# print(cadena + numerico) # Se tendría otro error, ya que cadena se definio como string

# Cuando el promaga se ejecuta nos marcará un error, es necesario copiar el tipo de error que describe, ya no continuara
# para describir el segundo error que se tiene por lo que es mejor comentar la línea de impresión para copiar el segundo
# tipo de error que describe.

# La descripción de los dos errores mostrados son los siguientes:

# error 1- ZeroDivisionError
# Error 2- TypeError
# Utilizando las sentencias "try" y "except" podemos evitara que se interrumpa el programa si es que se tuviera un error.

try: # En este bloque de la sentencia se describen las acciones que se quieren proteger en caso de un error
    print(numerador / denominador) # se empieza con el caso de la división y en caso de que ocurra el error va a saltar una excepción
except ZeroDivisionError:          # Aquí colocamos el nombre del error que nos dió al correr el programa
    print('ha ocurrido un error') # escribimos el tipo de mensaje que deseamos ver 

print('Fin del programa')


# try: 
    # print(cadena + numerico) # En este caso como se esta colacando la concatenación entre una cadena y numérico
# except ZeroDivisionError:    # se tendría el aviso de error y se interrumpiría el programa porque la descripción del error no         
    # print('ha ocurrido un error') # corresponde

# print('Fin del programa')


# Lo que se puede hacer es una tupla de errores en la la línea de "except"
# try: 
#     print(cadena + numerico) 
# except (ZeroDivisionError, TypeError):# se especifica cuales son los posibles errores que pueden encontrarse en el programa          
#     print('ha ocurrido un error')

# print('Fin del programa')


# Se pueden tener varias sentencias de error dentro del bloque de sentencia "try", pero debemos de tener cuidado de como utilizarlas
# ya que aquí al llegar a la primera impresión del programa se saltará a except y se tendría el mismo resultado para los dos errores
# por lo que se podría estar omitiendo parte del programa que fuera importante.
# try: 
#     print(numerador / denominador)
#     print(cadena + numerico) 
# except (ZeroDivisionError, TypeError):         
#     print('ha ocurrido un error') 

# print('Fin del programa')

# Algo que se puede hacer es tener varios bloques con la sentencia "try" y la sentencia " except" de esta manera podemos tener mensajes
# más especificos para cada error que encontremos

try: 
    print(numerador / denominador)
except ZeroDivisionError:         
    print('ha ocurrido una división entre cero') 

try: 
    print(cadena + numerico)
except TypeError:         
    print('ha ocurrido un error de tipo')    

print('Fin del programa')

# Otras de las funcionalidades este par de sentencias es que podemos tener varios bloques de la sentencia "except" por c/bloque
# de la sentencia "try"

try:
    print(10/0) # el programa va a tratar de dividir 10 / 0 pero eso mandará un error
except TypeError: # pero como no es un error de tipo se salta hasta el segundo except
    print('ha ocurrido un error de tipo')
except:
    print('Ha ocurrido un error desconocido') 

# esto nos ayuda a optimizar la depuración de nuestros programas hacer c/vez más eficientes en el manejo de nuestros errores al 
# moento de programarlos y evitar que vayan a surgir errores en ejecuciones posteriores que no estaban contemplados al momento
# de diseñar nuestros programas.

############################################################################################33

# Se pueden usar este tipo de estructuras para el menejo de errores con otro tipo de estructuras para crear programas que sean cada
# vez más amigables con el usuario

# Manejo de errores con excepciones y ciclos

while True:
    try:
       dividendo = int(input('Ingrese el dividendo: '))
       divisor = int(input('Ingrese el divisor: '))
       print('El resultado es: ',dividendo/divisor)
       break
    except ValueError:
        print('Debe de ingresar un número')
    except ZeroDivisionError:
        print('No se puede dividir entre cero')    

print('Fin del programa')        
    