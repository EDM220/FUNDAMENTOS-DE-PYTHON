# Los archivos de módulo se pueden ejecutar como si fueran scripts normales de python es decir como cualquier
# otro archivo de texto en el que se ejecuta el código de python. Se puede hacer desde la terminal simple-
# mente ingresando el nombre de la ruta del archivo.
#"Un script en Python es un archivo de texto que contiene código escrito en el lenguaje de programación Python"
# todos los módulos en python tienen un atributo o una variable especial llamada "__name__" la cual define
# el nemespace en la que el módulo se esta ejecutando. Si el módulo se ejecuta como el programa principal
# el interprete le asigna a esta variable el valor de "__main__" que es el nombre del ámbito superior, sin 
#embargo cuando se importa un módulo desde otro programa el valor de la variable es __name__ y si se importa
#un módulo desde otro programa el valor de la variable __name__ pasa a ser el del nombre del archivo de nuestro
#módulo

def factorial(num): 
    ''' Calcular el factorial de un número'''

    if num == 0:
        return 1
    else:
        return num * factorial(num-1)
    
print(__name__)

if __name__ == "__main__":
    import sys
    print(factorial(int(sys.argv[1])))


  