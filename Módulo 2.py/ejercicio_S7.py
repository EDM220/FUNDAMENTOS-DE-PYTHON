# Este programa creará una lista que capturará el nombre y dos calificaciones de hasta 5 alumnos en
# un ciclo que termine cuando se cumpla cierta condición específica. Esta condición específica nosotros
# la podemos definir como por ejemplo: ingresar un nombre vacío, o por medio de un sistema de opciones,etc.
# Al finalizar el programa se debe de mostrar en pantalla una lista con el nombre de los alumnos, con la
# inicial de c/uno de sus nombres en mayuscula y sus respectivas calificaciones.

lista = []

alumnos = 0
while alumnos <= 5: 
    opcion = input('agregar alumno (1) o terminar (2): ')
    if opcion == '1':
        nombre = input('Ingrese el nombre del alumno: ').capitalize()
        
        calificacion1 = int(input(f'Ingrese la primera calificación de {nombre}: '))
        calificacion2 = int(input(f'Ingrese la segunda calificación de {nombre}: '))
        alumno = [nombre, calificacion1, calificacion2]
        lista.append(alumno)
        alumnos += 1
    elif opcion == '2':
        print(f'El programa ha terminado con{alumnos} alumnos.')
        break
    else:
        print('Se ha ingresado una opción inválida.')
        continue

print('La lista de alumnos es: ')    
print(lista)    
