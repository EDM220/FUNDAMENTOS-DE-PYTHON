vocales = ['a', 'e','i','o','u']
vocales[1:4] = ['E','I','O']
print(vocales)
# Para indicar el tamaño de la lista
print(vocales, len(vocales))

vocales[1:4] = []
print(vocales, len(vocales))

vocales[1:2] = ['e','i','o','u']
print(vocales,len(vocales))

# Ahora extender esta lista "vocales" con otra lista. Con la función "extend"

vocales.extend (['i','i']) # va a sumar estos dos elementos la final de la lista "vocales"
print(vocales, len(vocales))

# si se quiere imprimir solamente la primera i de toda la lista. Con la función "index"

print(vocales.index('i')) # dentro de los paréntesis de index colocamos el elemento que queremos buscar
                        # de toda la lista. Después que lo imprime nos da el valor del índice que
                        # le corresponde que sería el "2"

# si se quiere encontrar repetidos, con la función "count"  
print(vocales.count('i')) # nos imprimirá un 3, osea existen "3 i"          

# Se pueden hacer más cosas que la función "index", por ejemplo se puede imprimer el ímdice de la primera "i"
# a partir del índice 4, osea que se buscará a partir de la posición 4

print(vocales.index('i',4))

# Para revertir una lista(ponerla al reves) con la función "reverse"

vocales.reverse ()
print(vocales,len(vocales))

# Si se quiere ordenar números. Con la función "sort"

vocales.sort()
print(vocales,len(vocales))

#también en sort se pueden hacer otra cosas como alterar la forma o el orden en el que
# se quiere ordenar la lista

carros = ['audi', 'ford','bmw','vw']

carros.sort(key=len)
print(carros) # se imprime de menor caracteres a mayor y como "audi" y "ford" tiene el mismo
# número de caracteres sigue el orden alfabético para darles su posición. 

# Se pueden guardar una lista dentro de otra lista
listas = [(0,1),(2,3,4),(5,6)]
print(listas[0],listas[1:3])

# Para imprimir un valor de una lista dentro de una lista
print(listas[2][1]) # Aquí se imprimiría el 6 debido a que en el valor 2 dentro de la lista es(5,6)-
                    # y dentro de esta tupla el valor del índice 1 es el número 6

# Uso de la memoria con las listas

vocales1 = ['a', 'e','i','o','u']
vocales2 = vocales1
print(vocales1,vocales2)
# Ahora se usa la funciín "id" para las listas vocales 1 y 2
print(id(vocales1),id(vocales2)) # imprime el "id" de la lista el cual es el mismo para las dos
                                 # listas porque se estan igualando y se les asigna el mismo espacio
                                 # de memoria es decir en el mismo id

# para crear otro objeto dentro de la memoria de python a pertir de un mismo objeto anterior, se
# usará la función "copy"

vocales3 = vocales1.copy()
print(vocales1,vocales3)
print(id(vocales1),id(vocales3)) # imprime un número diferente porque ya no son el mismo objeto
                                 # tiene diferentes identificadores por usar la función "copy"

# La función "id" sirve para los elementos de la lista por ejemplo:

print(vocales1[2]) # lo que imprime es el valor de la "i" de la lista vocales1
print(id(vocales1[2]),id(vocales2[2])) # Se imprimi el mismo valor por ser el mismo objeto                                
print(id(vocales1[2]),id(vocales3[2]))

# Si de la lista original se elimina un valor por ejemplo:
del vocales1[2]
print(vocales2,vocales3) # En vocales3 se imprime completa porque es otro objeto

# Ahora imprimir el "id 3" de vocales3
print(id(vocales1[2]),id(vocales3[3])) # se imprime el mismo "id" de vocales1 y 3 porque se hace referencia
                                       # respectivamente
                                       





