# mix = [0, 1.0,'dos', 3+4j]

# for i in mix:
#     print(f'{i:6} - Tipo: {type(i)}') # {i:6} indique que los valores están alineados a la derecha 
                                      # en una columna con un ancho mínimo de 6 caracteres.

# print(len(mix)) # "len" indica cuantos elementos existen en la lista

## crea una variable para eleimina "dos" de la lista pero uniendo el resto

# sin_dos = mix[:2] + mix[3:]
# print (mix, sin_dos)

## Para duplicar la lista
# duplicado = mix * 2
# print(duplicado)

## Hacer una lista de números elevados al cuadrado

cuadrados = [0, 1, 4, 9, 16, 25]
# for i in range(len(cuadrados)):
#     print(f'{i}**2 = {cuadrados[i]}')
# print(len(cuadrados))    

## Ahora los elevamos al cubo
for i in range(len(cuadrados)):
    cuadrados [i] = cuadrados [i] * i
    print(f'{i}**3 ahora estan al cubo = {cuadrados[i]}')
print(len(cuadrados))  
  

## A las listas se les pueden añadir y eliminar elementos con las siguientes funciones

#Ejemplo 1
cuadrados.append( 7 ** 3) #'append' Permite añadir un elemento al final de una lista
#print(cuadrados) # ve desplazando print para que veas el cambio

# Ejemplo 2
cuadrados.insert(6,6 ** 3) #'insert' inserta un elemento en la posición que le indiquemos por medio del índice
#print(cuadrados)

# Ejemplo 3
cuadrados.extend([27,1000,-1]) # "extend" Agrega multiples valores al final de la lista y puede ser también por un iterable
                               # agrega todos los valores de una lista en otra lista
#print(cuadrados)

# Ejemplo 4 tambien " extend"se puede usar con "range"
cuadrados.extend(range(-1,-4,-1)) # El constructor range(start, stop, step) genera una secuencia de
                                  # números basada en tres parámetros:
print(cuadrados)

# Otra función que se tiene es eliminar uno o varios elementos de la lista por medio de índices
# o slicing es decir dividiendo la lista como en las cadenas de texto. Esto es con la palabra 
# reservada "del" cuadrados []dentro de los corchetes va el límite inferior y superior que se 
# a eliminar por ejemplo [9:] desde el índice nueve en adelante

del cuadrados[9:]
print(cuadrados)

# También en las listas se tiene la función esta solamente eleimina la primera insidencia
# del valor por ejemplo de la lista existe dos números 27, en este caso va eliminar el primero
# valor que encuentre insidencia de ezquierda a derecha.

cuadrados.remove(27)
print(cuadrados)

# También existe la función "pop" va extrar de la lista el elemento con el índice que le indiquemos
# si no se le indica un índice extrar el último elemento.

valor_removido = cuadrados.pop(3)
print(valor_removido) # en este caso extrar el 8 porque es el índice 2 de la lista
print(cuadrados)
# La diferencia entre "pop" y "remove" es que "remove" busca un valor y "pop" los busca por medio
# de índices y devuelve el resultado que se saco de la lista y "remove" no regresa ningún resultado

# "clear" elimina todo los elementos de una lista

cuadrados.clear()
print(cuadrados)



