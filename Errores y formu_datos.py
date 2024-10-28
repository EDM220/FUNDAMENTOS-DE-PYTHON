# 1.- Error de sintaxis: Un error que impide la ejecución del programa y que necesita ser resuelto antes
# de que este se pueda probar

# 2.- Errores en tiempo de ejecución: Comunmente suele deberse a la falta de validación de un dato,
# por parte del programador, o la inexistencia de un dato(que este sea nulo),etc.

# ejemplo de error 

numHuevos = 12
# print('Tengo' + numHuevos + 'huevos') # este es el error
#Solución de 2 maneras
# Opción 1
print('Tengo' + str(numHuevos) + 'huevos') 
# Opción 1
print('Tengo',str(numHuevos),'huevos') 

# Opción 2
print('Tengo %s huevos'%(numHuevos)) 

# Error de lógica: Los dos errores anteriores impedirían la ejecución del programa,
# pero un error en la lógica de programación no. Este simplemente mostraría un resultado
# no deseado.
#ejemplo: calcular la superficie o área de un cuadrado

lado = int(input('ingrese la medida del lado del cuadrado: '))
#superficie = lado * lado * lado # se introduce mal la fórmula
# print('la superficie del cuadrado es: %s'%(superficie))
# print("la superficie del cuadrado es:",str(superficie))
# print("la superficie del cuadrado es:" + str(superficie))

superficie = lado**2
print('la superficie del cuadrado es: %s'%(superficie))
print("la superficie del cuadrado es:",str(superficie))
print("la superficie del cuadrado es:" + str(superficie))

# Ejercico: Formulario de ejercico de usuario, Nombre, apellidos, edad, correo y teléfono

nombre = input('Introduce tu nombre: ')
apellido = input('Introduce tu apellido: ')
edad = int(input('Cúal es tu edad:  '))
correo = input('Introduce tu correo electrónico: ')
telefono = input('Introduce tu teléfono: ') # se deja sin casting (int) porque se perdería el cero
# si el número del teléfono empezara con un cero. 

print('Nombre: %s'%(nombre))
print('Nombre: ' + nombre)
print('apellidos: %s'%(apellido))
print('edad: %s'%(edad))
print('Años: ' + str(edad))
print('Correo: %s'%(correo))
print('Teléfono: 4%s'%(telefono))



