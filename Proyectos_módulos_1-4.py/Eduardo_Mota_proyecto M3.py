# Programa para generar una simulación física de una máquina de Galton, mediante la obtención de números
# aleatorios y la graficación usando matplotlib. 
# Cararacterísticas del programa
# 1.Será la simulación de una máquina de Galton de 3000 canicas. 
# 2.En total tendrá 12 niveles de obstáculos. Decidir si va a caer a un lado o al otro 12 veces.
# 3.El resultado final será un histograma que represente la cantidad de canicas en cada contenedor, y 
# colocar nombre a los ejes y un título al gráfico. 
# 4. Se deberá emplear dos funciones, una para calcular los resultados de las canicas y la segunda para 
# la graficación del histograma.

import random # Biblioteca que se usa para generación de números aleatorios.
import matplotlib.pyplot as plt # Esta biblioteca se usa para crear gráficos

def maquina_galton(num_canicas,num_niveles): # Se crea la función para simular el recorrido de las canicas
    contenedores = [0] * (num_niveles + 1) # creación de una lista a partir de cero donde cada índice va a
                                           # representar los contenodores.
    
    for i in range(num_canicas): # sencencia for para la caida de las canicas
        posicion = 0 # La variable "posición "indica el inicio del movimiento
        for j in range(num_niveles): # Para cada nivel la canica podrá ir a la derecha o a la izquierda.
            if random.random() < 0.5:  # randon.randon genera un número aleatorio que va de 0-1, si el 
                                       # número obtenido es menor a 0.5 la canica va a la derecha o si
                                       # es mayor toma la izquierda y se incrementa la posición.
                posicion += 1
        contenedores[posicion] += 1  # después de pasar por lo niveles la canica cae en un contenedor y se
                                     # incrementa en uno.    
    return contenedores # Aqui se regresa la cantidad de canicas que cayeron en c/contenedor

def grafica_histograma(contenedores): # Función va a graficar los resultados de la simulación.
    plt.bar(range(len(contenedores)), contenedores) # Aquí se grafican el número de contenedores con 
                                                    # "len(contenedores))" y la altura de las barras ya que
                                                    # en "contenedores" tendremos la cantidad de canicas que
                                                    # cayeron en c/contenedor
    plt.xlabel('Contenedores') # En el eje x se desplegara la etiqueta "Contenedores"
    plt.ylabel('Canicas') # En el eje se tendra la cantidad de canicas en cada contenedor por lo que etique
                          # será llamada canicas
    plt.title('Máquina de Galton') # como título del histograma es " Máquina de Galton"
    plt.show() # Esta función nos permite mostrar el gráfico en pantalla

num_canicas = 3000 # Se declaran las variables con los parámetros del ejercicio.
num_niveles = 12

contenedores = maquina_galton(num_canicas, num_niveles) # Aquí es donde se llama a la función
grafica_histograma(contenedores) # Con esta función se graficará el resultado de la simulación
                                 # con un Histograma.

                                                               

