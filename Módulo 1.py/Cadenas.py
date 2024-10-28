# texto_variado ="Palabra 123 +-* #%&"
# print(type(texto_variado))

#Podemos usar comillas triples para que el texto se muestre como la cadena que hemos escrito
# print('''
# funcionamiento de 
# programa: (opciones)    
# -1 para acceder
# -2 para salir''')

# print('''
# funcionamiento de \
# programa: (opciones)    
# -1 para acceder
# -2 para salir''') # en este caso la "\" permite ver en pantalla el texto completa la línea funcionamiento y programa 

# print('''
# funcionamiento de \
# programa: (opciones)    
#      -1 para acceder
#         -2 para salir''')

#####################################################
# suscriptin e indexado
# texto='Python'
# print(texto[0])
# print(texto[5])
# print(texto[-1])
# print(texto[-6])

# print(texto[6]) # esto produce error no se puede acceder a una posición que no existe
# print(texto[-7]) # esto produce error no se puede acceder a una posición que no existe

# letra = texto[-4]
# print(letra)

#texto[0] = 'p' # error no podemos modificar una cadena

# letra = 'p' # Se puede redefinir la variable letra
# print(letra)

# texto_compuesto = letra + texto[1] #Concatenación
# print(texto_compuesto)

############################################################

# slicing o substringing
# texto = 'Python'
# print(texto[0:3])
# print(texto[0:-3])
# print(texto[0:-2])
# print(texto[2:]) # Si queremos mostrar índices desde un determinado punto hasta el final
# print(texto[:3]) # Lo mismo se puede hacer si se quiere imprimir desde el principio hasta un determinado punto

# print(texto[-3::-1])
# print(texto[::-1])
# print(texto[::1])

# print(texto[1:50])
# print(texto[2:2]) # aquí no se imprime nada porque tiene más preponderancia el último de los índices que es donde comienza 

#######################################################################

# Cadenas y formatos

texto = 'Hola mundo! Buenastardes'
print(texto.lower())
print(texto.upper())
print(texto.capitalize())
print(texto.title())
print(texto.swapcase())

print(texto) # La variable sigue teniendo el mismo valor que se le había asignado a menos que se le
             #cambie como por ejemplo texto = texto.upper() antes de print(texto)

print('{} + {} = {}'.format(2,3,2+3))
print('{} + {} = {}'.format('Hola','mundo','Hola mundo'))
print('{:.3f} + {:.4f} = {}'.format(2,3,2+3))
print('{1} + {0} = {2}'.format(2,3,2+3))
print('{2} + {0} = {1}'.format('Hola','mundo','Hola mundo'))
print('{:d} = {:b} =  {:0} = {:x}'.format(15,15,15,15))

# Para corroborrar los demás métodos que Python tiene instalados, escribir en la terminal(ventana de abajo)
#python para acceder a la terminal y después de esto dir(str)



