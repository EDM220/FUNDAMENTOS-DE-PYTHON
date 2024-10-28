# Creación de un gráfico de dispersión el cual puede emplearse para averiguar la correlación entre dos variables.

import random
import matplotlib.pyplot as plt

eje_x = [random.randint(1,100) for n in range(100)]
eje_y = [random.randint(1,100) for n in range(100)]

plt.scatter(eje_x,eje_y) # La función plt.scatter() de Matplotlib se utiliza para crear gráficos de dispersión 
                         # (scatter plots), donde cada punto en el gráfico representa una relación entre dos 
                         # variables: una en el eje X y otra en el eje Y.

plt.title('Gráfica de dispersión')

plt.show()
