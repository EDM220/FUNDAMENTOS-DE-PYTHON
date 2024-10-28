# Un namespace es un espacio abstracto en el que viven los identificadores. IMPORTANTE, no se pueden tener dos
# identificadores iguales en un mismo namespace.
# Para distinguir los naspace se pueden separa en dos grandes tipos o ámbito
# Ámbito global es aquel en el que trabajamos desde que abrimos el intérprete de python, es decir todo lo que
# se declara fuera de una función.
# Ámbito local corresponde al espacio que se crea durante la ejecución de una función, se debe tener en cuenta
# de que es un espacio temporal ya que dejará de existir cuando termime la ejecución del programa. Entonces
# el ámbito local se crea dentro del ámbito global y se pueden ejecutar funciones dentro de otras funciones
# de esta manera se pueden anidar o crear ámbitos que existirán dentro de otros ámbitos, los cuales serán
# ámbitos de nivles inferiores
# Algo que se debe saber es que los objetos de un ámbito superior solo son accesibles como lectura en un
# ambito inferior.

# Probando ámbitos

titulo = 'Probando ámbitos'
suma = 10.5

def sumar():
    suma = 2 + 2
    # titulo = titulo + 'mundo' # Mandara un error explicado en el comemtario de abajo.
    print(titulo) # aquí se puede imprimir la variable titulo porque solo se esta leyendo pero en la línea
                 # arriba que esta cometada si se ejecuta mandará error porque se quiere manipular una variable
                 # de un ámbito superior que no esta declarada en esta función.
    print('suma en ambito local',suma,id(suma))
print('Antes de llamar a la función')
print('Suma en ámbito global',suma,id(suma))
sumar()
print('Después de llamar a la función sumar')
print('Suma en ámbito global',suma,id(suma))

# Entendiendo esto, se puede trabajar con parámetros y argumentos
# Para trabaja con funciones se debe de comprender que hay distos valores en juego los parámetros y argumentos
# loa parámetros son las variables que se declaran en la definición de la función, mientras que los argumentos
# son los valores con los cuales se invoca una función por lo tanto, son los valores que se tomaran como -
# parámetros dentro de la función.Un dato importante es que son posicionales, es decir se debe respetar
# la posición en la que fueron definidos los parámetros
