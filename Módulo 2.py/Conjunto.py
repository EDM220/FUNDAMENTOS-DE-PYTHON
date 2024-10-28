# Un conjunto no posee un orden ni un índice, además de que no existen datos duplicados no se pueden colocar 
# dos mismos datos en un conjunto y se definen por llaves {}
# se utilizan para agilizar el desarrollo del nuestro código y verificación de datos

# Se pueden cambiar listas a conjuntos mediante la función "set"

canasta = {'manzana','naranja','manzana','pera','naranja','platano'}
print(canasta) # imprime sin repetir los datos repetidos

print('manzana' in canasta) # se pregunta si manzana esta dentro de canasta, e imprime true
print('melón' in canasta)

#################################

vocales = ['a','e','i','o','u','a']
print(vocales)

vocales = list(set(vocales))#Aquí se está convirtiendo la lista vocales en un conjunto usando set(vocales).
                         # set(vocales): Convierte la lista en un conjunto, eliminando cualquier duplicado.
                         # list(set(vocales)): Convierte el conjunto de vuelta en una lista. 
print(vocales) # Impresión de la lista sin duplicados.

####################################
# Función "issubset" que sirve para identificar si un conjunto es un subconjunto dentro de otro
# es decir si ese conjunto esta dentro de otro conjunto más grande

vocales1 = {'a','e','i','o','u','a'} # los conjuntos en Python solo almacenan elementos únicos,
                                     #  el segundo 'a' es eliminado automáticamente.
vocales2 = {'e','i','o'}
print(vocales2.issubset(vocales1)) # issubset() se utiliza para verificar si todos los elementos 
                                 # de vocales2 están presentes en vocales1. Si vocales2 es un subconjunto 
                                 # de vocales1, la función devolverá True; de lo contrario, devolverá False.

##########################################################
# Para imprimir la diferencia se puede utilizar el operador de resta

vocales1 = {'a','e','i','o','U',}
vocales2 = {'A','E','I','O','U',}
print(vocales1 - vocales2) # no imprime ninguna por que todos son diferentes

# También se pueden unir los conjuntos

print(vocales1 | vocales2)

# Para imprimir la intersección (los elementos que estan en ambos conjuntos)

print(vocales1 & vocales2) # imprime un conjunto vacío porque todos son diferentes
                           # pero si cambias una minuscula en vocales 1 imprime la que es igual

# Ahora para imprimir la diferencia simétrica (elementos que estan en un conjunto u otro) 
# pero no en ambos
print(vocales1 ^ vocales2)# no va a imprimir la U porque esta en ambos  
                   

