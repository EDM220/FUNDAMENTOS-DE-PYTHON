import numpy as np
import matplotlib.pyplot as plt

datos = np.random.normal(0,1.0,1000) # Generar datos de una distribución normal

plt.hist(datos,bins=10) # se usa la función "hist" para imprimir los datos la cual genera un histograma.
                        # la parte bins=30 es opcional, ya que ajusta el número de barras
plt.show()