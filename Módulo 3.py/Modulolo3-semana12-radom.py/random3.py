# Aquí se debe de instalar primeramente "numpy" escribiendo en la terminal "pip install numpy"
# Numpy, la cual esta especializada en cálculo numérico y análisis de datos.
# ejemplo 1 se importa numpy y cada vez que se ejecute el programa se tendran números aleatorios

import numpy as np

numeros = np.random.rand()
print(numeros)

# Ejemplo 2 aqui se genera un número con una salida constante no cambia, debido a que,se planta una semilla
# se genera los números a partir de otro número y con la función "seed" permite realizar esto.

import numpy as np
np.random.seed(0)# se genera un número seudoaleatorio porque se genera a partir de otro número

numeros = np.random.rand()
print(numeros)

# ejemplo 3.- si se quiere generar una lista de números aleatorios o seudoaleatorios con numpy

np.random.seed(0)# se genera un número seudoaleatorio porque se genera a partir de otro número

numeros = np.random.rand(10)
print(numeros)