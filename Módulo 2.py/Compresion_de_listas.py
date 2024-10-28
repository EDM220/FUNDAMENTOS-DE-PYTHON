# Las listas son una colección ordenada que se puede modificar y permitir datos duplicados
# además de que puede tener elementos de diferentes tipos.

# cuadrados = []
# for numero in range(10):
#     numero = numero **2
#     cuadrados.append(numero)
# print(cuadrados) 
# print(numero)

# Esta manera no es siempre más eficiente, debido a que se consume espacio en la memoria temporal de
# la computadora con variables que ya no vamos a utilizar como ejemplo; si imprimimos la variable 
# "numero" se puede ver que se guarda con el último valor que tuvo esa variable "81".
# Para mejorar esto se emplea una técnica llamada compresión de listas. ejemplo:

# cubos = [cubo **3 for cubo in range(10) ]
# print(cubos)
#print(cubo) si le pedimos a python que imprima cubo marcará error porque no se ha declarado la variable
# por lo que no se esta utilizando espacio dentro de la memoria temporal (asignado espacio en memoria) esto
# es una manera de hacer un proceso más eficiente.

####################################################
# Este método se puede usar para hacer diccionarios

# cubos = {numero: numero **3 for numero in range(10)}
# print(cubos)
# esto nos permite tener más versatilidad pues se escribe menos líneas de código para tener los mismos
# resultados. También se pueden hacer uso de condicionales dentro de la misma línea de código, para
# hacer programas más especificos. ejemplo:

# pares = [numero for numero in range(1,11) if numero % 2 == 0]
# inpares = [numero for numero in range(1,11) if numero % 2 !=0]
# print(pares)
# print(inpares)
# este método de arriba es recomendable cuando las líneas de código no sean muy complejos
#Otra utilidad que tiene este método es cuando se tiene una lista definida pero se quiere hacer algunso
# cambios. Ejemplo:

nombres = ['ana','fernando', 'carlos', 'priscila']# se puede utilizar la ténica vista para imprimir la
                                                  # la primera letra de c/nombre en mayúscula
print('Lista antes de la compresión: ',nombres)
nombres = [nombre.capitalize() for nombre in nombres]
print('Lista después de la compresión: ',nombres)
