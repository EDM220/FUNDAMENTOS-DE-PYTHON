### Módulo m_area(m_area.py)
'''Módulo que contiene la función área'''


def area(**dato):
    '''
    Recibe como parámetro un diccionario con los datos de una figura
    calcula el área de la figura
    '''
# Si el diccionario tiene una clave llamada 'figura' evalúa el valor de la clave  
    if dato['figura']=='Rectángulo':
     return dato['base']*dato['altura']# Si el valor de la clave es 'Rectángulo' imprime el valor de la
                                      # clave 'base' multiplicado por 'altura' 
    elif dato['figura']== 'Triángulo':
     return dato['base']* dato['altura']/2# Si el valor de la clave es 'Triángulo' imprime el valor de la
                                      # clave 'base' multiplicado por la 'altura' divido por 2
    elif dato['figura']== 'Círculo':
     return 3.141593*dato['radio']**2# Si el valor de la clave es 'TCírculo' imprime el valor de la
                                      # clave 'radio' al cuadrado multiplicado por 3.141593
    else:
     print('Figura desconocida')# Si el valor de la clave no es ninguna de las anteriores, imprime 'Figura
                                # desconocidad'
