# Parámetros tipo tupla. Por convención son llamados también *args el asterisco es muy importante porque le 
# indica al interprete de python que se pueden recibir multiples parámetros de este mismo tipo


def promedio(*numeros):
    '''
    Recibe un solo parámetro de tipo tupla, de valores numéricos .-
    e imprime su promedio
    '''
    promedio = sum(numeros)/len(numeros) # Utilizando la función se hace la sumatoria de los números, además, ya no es necesario
                     # utilizar el asterisco en numeros, solamente cuando se definió la función para indicar
                     # que pueden ser multiple números
    print('El promedio es :',promedio) 

promedio(4) 
promedio(4,5,6) 
promedio(1,2,3,4,5,6,7,8,9) 

# Se realizará una función que reciba una serie de caracteres y nos indique si se trata de un número o no
# y va a imprimir un título para la serie de caracteres

def es_numero(titulo,*serie):
    '''
    Imprime un título
    Verifica si el caracter en el parámetro de tipo tupla es un número o no
    '''
    print(titulo)
    for i in serie:
        if type(i) == int or i.isdigit():
            print(f'{i} es número')
        else:
            print(f'{i} no es número')    
es_numero('numeros','1','2','3') 
es_numero('letras','a','b','c')        

# La funciones se pueden invocar también por medio de variables

nombre = 'mezcla'
lista_varios = ['a','2',3,'f',5]
es_numero(nombre,*lista_varios)

#*******************************
# Parámetros de tipo diccionario. Por convención son llamadas también **kwargs que viene del inglés 
# keyword arguments y significa argumentos de palabra clave

def area(**dato): # ' **dato ' es ua variable que recibe un diccionario
    '''Calcula el área de una figura geométrica y la imprime en pantalla''' #Docstring ????

# Si el diccionario tiene una clave llamada 'figura' evalúa el valor de la clave  
    if dato['figura']=='Rectángulo':
     print(dato['base']*dato['altura'])# Si el valor de la clave es 'Rectángulo' imprime el valor de la
                                      # clave 'base' multiplicado por 'altura' 
    elif dato['figura']== 'Triángulo':
     print(dato['base']* dato['altura']/2)# Si el valor de la clave es 'Triángulo' imprime el valor de la
                                      # clave 'base' multiplicado por la 'altura' divido por 2
    elif dato['figura']== 'Círculo':
     print(3.141593*dato['radio']**2)# Si el valor de la clave es 'TCírculo' imprime el valor de la
                                      # clave 'radio' al cuadrado multiplicado por 3.141593
    else:
     print('Figura desconocida')# Si el valor de la clave no es ninguna de las anteriores, imprime 'Figura
                                # desconocidad'
area(figura = 'Triángulo',base = 10,altura = 5)  
area(figura = 'Círculo',radio = 10,color = 'rojo')   
area(figura = 'Dodecágono',lado = 10)       

