# Características del programa.
# 1.- Utilizar al menos 2 funciones.
# 2.- Preguntar cuantos alumnos se registraran. En caso de no ingresar un catidad, se sumira que se registraran
# 3 alumnos
# 3.- Preguntar nombre y 2 calificaciones.
# 4.- Mostrar en pantalla con inicial mayúscula y promedio
# 5.- Al finalizar el programa, se mostrará una lista con el npmbre de c/alumno y sus calificaciones.

def captura_alumnos(numero = 3):
    '''
    Función que registra alumnos y dos de sus calificaciones
    recibe como parámetros la cantidad de alunos a registrar
    si no se especifica el número de alumnos, se registraran 3
    '''
    lista_alumnos = []
    for i in range(numero):
        nombre = input(f'{i + 1},Ingrese el nombre del alumno: ').capitalize()
        calificacion1 = int(input(f'Ingrese la primera calificación de {nombre} '))
        calificacion2 = int(input(f'Ingrese la segunda calificación de {nombre} '))
        lista_alumnos.append([nombre,calificacion1,calificacion2])
        promedio(nombre,calificacion1,calificacion2)
    print(lista_alumnos)
    

def promedio(nombre,calificacion1,calificacion2):
    '''
    Calcula el promedio de un aluno y lo despliega en pantalla por medio de un mensaje
    recibe como parámetros el nombre y dos calificaciones del alumno.
    '''
    promedio = (calificacion1 + calificacion2)/2
    print(f'El promedio de {nombre} es: {promedio}')


numero_alumnos = input('Cuantos alumnos deseas ingresar? ')
if numero_alumnos.isdigit():
    numero_alumnos = int(numero_alumnos)
    captura_alumnos(numero_alumnos)
else:
    captura_alumnos()    
