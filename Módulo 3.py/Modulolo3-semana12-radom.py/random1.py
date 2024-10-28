# Random es un módulo de python que genera números aleatorios

### ejemplo 1
# import random

# print('El dado dio' + str(random.randint(1,6)))

##### ejemplo 2

import random

def tiro_dado(num_tiros):
    for dado in range(num_tiros):
        print('El dado '+ str(dado + 1) + ' dió ' + str(random.randint(1,6)))

tiro_dado(5) 
