# Un diccionario es una colección sin orden ni índice, en lugar del índice se utilizan llaves conocidos
# como identificadores
# 1.-Los diccionarios no permiten las llaves duplicadas
# 2.-Si son modificables
# 3.-permiten llevar un mapeo entre dos colecciones distintas mediante su funcionalidad de llaves y valores
# es decir existe una colección de llaves y coleccion de valores asociados a c/llave.

tiempos =  {
    'Hamilton':'1:49.8',
    'Bottas':'1:56.4',
    'Perez':'1:53.8',
    'Verstappen':'1:52.6'
}
# método "items" permiten devolver una lista de tuplas obteniendo la llave y su respectivo valor
print(tiempos.items()) #devuelve una lista de tuplas de c/llave con su valor asociado

# función utilizada dentro de los diccionarios es "keys"
print(tiempos.keys()) # devuelve una lista con sólo las claves, es decir solamente los nombres
                      # de los corredores

# otra funcion es "values" devuelve una lista con todos los valores del diccionario  
print(tiempos.values())       

# Para regresar el valor de una llave se utiliza la función "get"
print(tiempos.get('Hamilton')) # imprime su valor

# Existe un parámetro opcional donde se puede regresar un valor indicado en caso de no encontra una llave
print(tiempos.get('hamilton','No encontrado'))
