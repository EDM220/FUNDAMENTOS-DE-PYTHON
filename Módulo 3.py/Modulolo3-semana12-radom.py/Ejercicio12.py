# Ejercicio para realizr una gráfica.
# Seguir los siguientes pasos
# 1.- Define una función para contruir la gráfica
# 2.- Define un diccionario con las calificaciones del alumno.
# 3.- Pedir al usuario el nombre del alumno
# 4.- Manda llamar a la gráfica y muéstrala

import matplotlib.pyplot as plt

def diagramas_barras_calificaciones(notas,color,alumno): # se define la función
    '''
    Dibujar la gráfica de barras con las calificaciones
    '''
    plt.bar(notas.keys(),notas.values(),color=color)  
    plt.title('Calificaciones de: ' + alumno)  

calificaciones = {
    'Programación':9,
    'Español':6.5,
    'Cálculo':4,
    'Historia':8,
    'Bilogía':10
}

alumno = input('Nombre del alumno: ')
diagramas_barras_calificaciones(calificaciones,'blue',alumno)
plt.show()