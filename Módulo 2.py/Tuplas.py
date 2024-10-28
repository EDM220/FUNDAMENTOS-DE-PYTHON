# Tuplas: Las tuplas son una colección similar a las listas ya que son una colección ordenada 
# que permiten datos duplicados, pero su mayor diferencia con las listas es que es una colección
# inmutable, es decir un conjunto de elementos que ya no se pueden modificar una vez definidos.
# Esto es útil cuando se quieren guardar valores relacionados entre si y que y que no se quieren
# confundir con otros. las tuplas se definen con ().

vocales = ('a', 'e', 'i','o', 'u')  
print(vocales[2]) # Aquí se imprime el valor que es "i"

# vocales[2] = "I" manda error porque no se puede modificar los valores dentro de una tupla
# solamente se pueden consultar

print(vocales[:3],vocales[2:]) 
print(vocales[:3] + vocales[2:]) # se manda llamar la tupla de la misma manera que las listas

# Algo que se puede hacer dentro de las tuplas es buscar el ídice de un valor
print(vocales.index('o'))

# Si se quisiera modificar el valor de la tupla. Se puede usar la función "list ()" que devuelve una
# lista a partir de una tupla

lista_vocales = list(vocales)
lista_vocales[2] = 'I' # se crea la lista a partir de la tupla
print(lista_vocales) # muestra la modificación en la lista

# Ahora para convertir de una lista a una tupla

tupla_vocales = tuple(lista_vocales)
tupla_vocales[2] = 'I' # aquí mostrará un error porque en una tupla no se puede modificar sus valores
