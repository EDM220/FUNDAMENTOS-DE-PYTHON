# Convertir una tupla o hacers casting a una tupla a un diccionario con la función "dict"
tiempos = dict(
    Hamilton = '1:49.8',
    Bottas = '1:56.4',
    Perez = '1:53.8', # si se escribiera aquí el mismo nombre de Hamilton mandaria error
                      #porque el diccionario no puede tener claves duplicadas
    Vesrtappen = '1:52.6' # pero si permite tener los valores duplicados
)
print(tiempos) # Imprime un diccionario. Las llaves son los nombres y sus valores como el valor del
               # diccionario

#####################33
# si desde el comienzo se define un diccionario con dos llaves iguales no marcará error
tiempos = {
    'Hamilton': '1:49.8',
    'Bottas':'1:56.4',
    'Hamilton':'1:53.8',
    'Hamilton ':'1:52.6'
}
print(tiempos) #solamente imprimirá la última insidencia de "Hamilton"

#############################
# Hablando de los diversos tipos de colecciones se puede hacer uso de las listas para construir
# filas y pilas

