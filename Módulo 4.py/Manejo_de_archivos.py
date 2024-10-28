# Python nos permite trabajar con archivos por medio de la función "open" la cual nos ayuda a cargar un objeto de tipo "file".
# Un objeto de tipo "file"es cualquier archivo que contenga una o varias cadenas de texto. Al utilizar archivos guardadso en nuestras
# computadoras podremos utilizar volumenes más grandes de información que pueden ser utilizados como variables durante la ejecución
# de los programas.
# Si queremos abrir un archivo ya exixtente o queremos generar un nuevo archivo se utiliza en ambos casos la función "open", la cual
#recive dos parámetros. El primero de estos parámetros es el nombre del archivo con la ruta del archivo, ya sea la ruta en donde se
# encuentra ese archivo o la ruta en la que queremos generar ese archivo. Si no se especifica una ruta el archivo se generará por 
# defecto en la misma ubicación en la que se encuentre nuestro programa

# f_archivo = # Esta variable se nombro con una "f" al principio por que es una convención entre desarrolladores. Cuando se coloca una
            # f al comienzo de una variable esamos indicando que se trata de un objeto de tipo file, aunque no es necesaria es 
            # recomdable por buenas practicas

# f_archivo = open('archivo1.txt','w') #se crea un archivo de texto plano txt y el segundo de los parámetros es el método de apertura
                                     # w = escribir o sobreescribir en el archivo
# print(f_archivo) # c/vez que se abra un archivo en python se debe de cerrar cuando ya no se utilice
# f_archivo.close() # Recordar que las funciones se escriben con parámetros y los métos se escriben después de un punto seguido de la
                  # variable. En este caso el archivo se va a cerrar con el método close
                  # En el momento de correr el programa se va acrear el archivo con el nombre que se le dió.

# Si se quiere escribir algo dentro de este archivo
# con el mismo programa solamente le agregamos el método write                  

# f_archivo = open('archivo1.txt','w')
# print(f_archivo)
# f_archivo.write('Hola mundo') # Antes de cerrar el archivo escribimos por medio del método write
# f_archivo.close() # Se puede abrir el archivo para ver que ya esta escrito "Hola mundo"

# Al abrir un archivo en el modo de escritura o sobreescritura nos permite generar un nuevo archivo que va a contener lo que sea que 
# nosostros le pasemos como cadena por el método write. Se debe de tener cuidado cuando se trabaje con este tipo de métodos para
# abrir archivos, porque se puede sobreescribir como lo indica el siguiente ejemplo. Se había escrito "Hola mundo", y ahora se
# se escribira "Este es mi primer archivo".

# f_archivo = open('archivo1.txt','w')
# f_archivo.write('Este es mi primer archivo')
# f_archivo.close()

# Si solamente queremos abrir un nuevo archivo y solamente queremos leerlo saber cuál es la información que contiene

# f_lectura = open('archivo1.txt','r')# r = read (lee) leer el archivo. Ya esta listo el archivo para abrirlo en modo lectura
                                    # para poder ver la información que contiene este archivo se utiliza el método "read" que mos
                                    # mostrará cuáles son las cadenas que contiene este archivo
# print(f_lectura.read()) # esto nos mostrará cuáles son las cadenas que contiene
# f_lectura.close()    

# print(f_archivo) # se muestra en la terminal el resulatado de impresión de las variables del archico escritura y lectura
# print(f_lectura) # Simpre que se trabaje con archivos se beben de cerrar cuando ya no se trabajen con ellos.

################################################################3
# Existen otras formas de cerrar un archivo utilizando las sentencias "with" y "as"

# f_lectura = open('archivo1.txt','r')
# print(f_lectura.closed) # confirmación de si el archivo esta cerrado o no
# f_lectura.close() # Después cerramos el archivo manualmente por medio del método close
# print(f_lectura.closed) # se verifica nuevamente si el archivo ya esta cerrado

# Ahora utilizando las sentencias with y as

# with open('archivo1.txt','r') as f_lectura: # se abre el archivo pero ahora con las sentencias with y as
#     print(f_lectura.closed) # se pregunta si el archivo esta cerrado el cual va a ser falso por estar trabajando dentro del bloque
#                             # de las sentencias. Se cierra el archivo en automático al salir del bloque del código
# print(f_lectura.closed) # y esta vez será cierto ya que el archivo se encuentra cerrado fuera de la sentecia with, fuera del bloque de
                        # código "with y as" el archivo es cerrado. Usar estas sentencias es más recomendable para evitar errores
                        # si se olvida cerrar el archivo manualmente.
# Para abrir un archivo que se quiere evitar perder la información que contiene y solamente se quiere agragar más información
# esto se hace en el modo de escritura al final

# with open('archivo1.txt','a') as f_archivo: # a = append (agrega) agragar al final del archivo
#     f_archivo.write('\nEste es mi segundo archivo 2')
#     f_archivo.write('Este es mi segundo archivo 3')
#     f_archivo.write('\n')
#     f_archivo.write('\tEste es mi segundo archivo 4')
# with open('archivo1.txt','r') as f_lectura:  
#     print(f_lectura.read())
      
# Otra cosa que se debe tener en cuenta al momento de leer archivos es que se puede guardar la información de un archivo en una variable
# pero una vez que ya se haya utilizado esta información queda libre    

# with open('archivo1.txt','r') as f_lectura:  
#     contenido = f_lectura.read() # Aquí se guarda la información en la variable
#     print(f'****{contenido}****') # El curso esta al inicio de la información y imprime lo que esta en el archivo
#     contenido = f_lectura.read() # Cuando se pide otra lectura el cursor se encuentra al final de los datos por esta razón ya no se 
#                                  # imprime la información del archivo, solamente los asteriscos
#     print(f'****{contenido}****')

####################################################################################
# Para poder leer un archivo línea por línea  

# with open('archivo1.txt','r') as f_lectura:
#     numero_de_lineas = 0
#     for i in f_lectura:
#         numero_de_lineas += 1
#         print(f'Línea{numero_de_lineas}: {i}') 
#     print(f'El archivo tiene {numero_de_lineas} líneas')    

# Creando una lista a partir de un archivo

with open('archivo1.txt','r') as f_archivo:
    lista_archivo = f_archivo.readlines()
    print(lista_archivo) # La ventaja de asignar cada línea como elemento de una lista a una variable es que podremos utilizar esta
                         # esta variable después de que se cierre el archivo
# print(lista_archivo) 

lista_archivo[1] ='Este es mi primer archivo 2\n'
lista_archivo.insert(3,'\tEste es mi primer archivo 4\n')
del lista_archivo[4] 


print(lista_archivo)

with open('archivo1.txt', 'w') as f_archivo:
    f_archivo.writelines(lista_archivo)


 

  
    

