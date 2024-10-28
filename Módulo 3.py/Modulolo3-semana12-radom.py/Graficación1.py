# Las gráficas de datos nos ofrecen una representación visual del comportamiento de la información.
# Para poder realizar gráficas en Python se necesita instalar la biblioteca "matplotlib" escribiendo en la 
# terminal pip install matplotlib

# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(0) # Se  fija semilla para reproducibilidad

# numeros = np.random.rand(10) # se genera 10 números aleatorios en el rango[0.0,1.0]
# # se definen las variables
# media_distribucion = 0
# desviación_estandar = 1
# tamaño_muestras = 1000

# np.random.normal(media_distribucion,desviación_estandar,tamaño_muestras)
# print(numeros)

# # Se grafican los números generados
# plt.plot(numeros)
# plt.show()

#########################################################
# De otra forma sugerida

import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0) # Se  fija semilla para reproducibilidad

numeros = np.random.rand(10) # se genera 10 números aleatorios en el rango[0.0,1.0]
print(numeros)

# Se grafican los números generados
plt.plot(numeros)
plt.show()

# se definen las variables
media_distribucion = 0
desviación_estandar = 1
tamaño_muestras = 1000

datos_normal = np.random.normal(media_distribucion,desviación_estandar,tamaño_muestras)