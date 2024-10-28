# La sentencia "continue" omite una sola iteración de la repetición de un ciclo

# Uso de la sentencia "continue" en un ciclo for

# for numero in range(1,11): # se cuentan los números del 1 al 10 el número 11 queda fuera
#     if numero % 2 == 1:# si en la división el residuo es 1 continual con la iteración, pero si es cero
                       # indica que es par entonces continua el la línea de impresión
#         continue
#     print(f'{numero} es un número par')

    ##################################3
    # Uso de la sentencia continue en un ciclo while
# numero = 0
# while numero < 11:
#         numero += 1
#         if numero % 2 == 0:
#             continue
#         print(f'{numero} es un número impar')


#############################################
# La sentencia "break", interrumpe la ejecución de un ciclo
# Uso de la sentencia break en el ciclo while

# numero = int(input('Ingrese un dígito: '))
# limite_inferior = 0
# limite_superior  = 10
# buscado = 5
# intentos = 0

# while True :
#      intentos += 1
#      if numero == buscado:
#           print(f'El número {numero} fue encontrado en {intentos} intentos')
#           break
#      elif numero < buscado:
#           limite_superior = buscado
#           buscado = (buscado + limite_inferior) // 2
#      else:
#           limite_inferior = buscado
#           buscado = (buscado + limite_superior) // 2    
# print('Fin del programa')          

################################################

# Uso de la función "exit"

# numero = int(input('Ingrese un dígito: '))
# limite_inferior = 0
# limite_superior  = 10
# buscado = 5
# intentos = 0

# while True :
#      intentos += 1
#      if numero == buscado:
#           print(f'El número {numero} fue encontrado en {intentos} intentos')
#           exit() # La diferencia entre la función "exit()" y la sentencia "break" es que 'exit' ya no
                 # continua con las siguientes líneas una vez que se ejecuta.
#      elif numero < buscado:
#           limite_superior = buscado
#           buscado = (buscado + limite_inferior) // 2
#      else:
#           limite_inferior = buscado
#           buscado = (buscado + limite_superior) // 2    
# print('Fin del programa')  
# print('Impresión después de la sentencia break')
# print('Impresión después de la función exit()')   

# este se usa más para emergencia cuando se tiene ejecuciones de ciclos que consumen muchos recursos
# y que ya se han consumido durante mucho tiempo durante muchos intentos
# en el siguiente programa de se ejemplifica lo descrito arriba con un nuevo programa

intentos = 0
while True :
     intentos += 1
     print(f'Intento {intentos}')
     if intentos == 20:
          print('Fin del programa')
          exit()
print('Impresión después de la función exit()') # esta sentencia no se va a imprimir por que se esta
                                                # usando la función "exit"         
 




