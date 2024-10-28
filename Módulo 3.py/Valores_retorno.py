# Valores de retorno sentencia return

def promedio(*numeros):
    # promedio = sum(numeros)/len(numeros) # se modifica y se pone return 
    return sum(numeros)/len(numeros)
x = promedio(4,5,6)
print(x) # cómo no se especificó cuál queremos que sea el valor de retorno de esta función el valor que
         # regresa es none (valor vacío). Si se quiere especificamente que el valor que regrese sea el 
         # promedio, lo que se tiene que hacer utilizar la sentencia "return". Se cambia el nombre de promedio
         # y se coloca return

#--------------------------------------------------------------------------------------------------
# Ahora utilizamos un parámetro de tipo diccionario del ejemplo "parametro_tupla_diccionario.py"

def area(**dato): # ' **dato ' es ua variable que recibe un diccionario
    '''Calcula el área de una figura geométrica y la imprime en pantalla''' #Docstring ????

# Si el diccionario tiene una clave llamada 'figura' evalúa el valor de la clave  
    if dato['figura']=='Rectángulo':
     return(dato['base']*dato['altura'])# si queremos guardar el resultado de esta operación en el ámbito
                                      # superior en alguna variable es, en lugar de pedirle una impresión
                                      # (cambiar print por return) es pedirle que regrese el dato 
    elif dato['figura']== 'Triángulo':
     return(dato['base']* dato['altura']/2)# Si el valor de la clave es 'Triángulo' imprime el valor de la
                                      # clave 'base' multiplicado por la 'altura' divido por 2
    elif dato['figura']== 'Círculo':
     return(3.141593*dato['radio']**2)# Si el valor de la clave es 'TCírculo' imprime el valor de la
                                      # clave 'radio' al cuadrado multiplicado por 3.141593
    else:
     print('Figura desconocida')# En este caso no se quiere que se guarde el valor por lo que
                                # se queda igual "print"

triangulo = area(figura = 'Triángulo',base = 10,altura = 8)# Aquí se asigna el valor a alguna variable  
print(f'El área del triángulo es: {triangulo}')
circulo = area(figura = 'Círculo',radio = 10,color = 'rojo') 
print(f'El área del Círculo es: {circulo}')  
dodecagono = area(figura = 'Dodecágono',lado = 10)
print(f'El área del Dodecágono es: {dodecagono}') # aquí mostrará "none" porque no se ha especificado a la 
                                                  # función que valor quiere que se regrese 

#-----------------------------------------------------------------------------------

#Recursividad de funciones en python

def factorial(numero):
  if numero == 0:
    return 1
  else:
    return numero * factorial(numero - 1)

print('El factorial de 0 es (0!):',factorial(0)) 
print('El factorial de 1 es (1!):',factorial(1))
print('El factorial de 3 es (3!):',factorial(3))
#print('El factorial de -1 es (-1!):',factorial(-1))# matemáticamente hablando esto no se puede hacer ses una
                                                   # operación indefinida, pero solamente para mostrar el 
                                                   # tener cuidado para que no ciclar la computadora, ya que
                                                   # si busacramos un número negativo en la oparación nunca
# llegaría a cero y asi continuaría hasta que se interrumpa de forma manual.Pero python tiene tiene un límite 
# de recursibidad de manera nativa como seguridad que es de 1000 

# El ejemplo anterior quedaría de la siguiente forma

# def factorial(numero, intentos = 0):
#   if numero == 0:
#     return 1
#   else:
#     intentos += 1
#     print(intentos)
#     return numero * factorial(numero - 1, intentos)

# print('El factorial de -1 es (-1!):',factorial(-1))


#----------------------------------------------------------------------------------------------

# Funciones lambda o funciones anónimas

suma = lambda x,y: x + y # Se escribe la función lambda, la cual recibe 2 parámetros seguido de dos puntos
                   # y las acciones que se van a realizar con esta función que es sumar "x + y"
print(suma('Hola','mundo!')) # Se hace una concatenación
print(suma(2,5))                   

lista_numeros = [1,0,-2] # si se quisiera ordenar según su valor numérico o valor absoluto se puede utilizar 
                         # la funció "sorted"
lista_numeros = sorted(lista_numeros)
print(lista_numeros) 
lista_numeros = sorted(lista_numeros, key = lambda n: abs(n))    
print(lista_numeros)  

####-------------------------------------------------------------------------
# Función Zip

paises = ['Kenia','Francia','México','Japón']
capitales = ['Nairobi','Paris','Ciudad de México','Tokio']
Poblacion = [54,66,130]

for i in zip(paises,capitales,Poblacion): # En esta ocación no se va a utilizar un solo elemento iterable, 
       # en vez de eso se utilizaran los 3 elementos iterables al mismo tiempo por medio de la función "zip"
       print(i)


                                            

   
    