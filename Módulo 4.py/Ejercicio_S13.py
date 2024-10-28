# En este ejercicio se le pedirá al usuario ingresar nombre,apellido,edad,correo,teléfono, y se hará una impresión de los datos
# ingresados 

# while True:
#     nombre = input('Introduce tu nombre: ')
#     apellido = input('Introduce tu apellido')
#     if nombre == '':
#         print('No has introducido tu Nombre')
#     elif apellido == '':
#         print('No has introducido tu Apellido')
#     else:
#         break  

# Esta primera parte no funciona muy bien porque cuando se deja un espacio en el nombre se brinca hasta el apellido. Esta parte
# la original del ejercicio del video del curso.      
  
# Esta es una modificación con la ayuda de chatgpt
# Se ha añadido .strip() en las entradas de nombre, apellido. Esto eliminará los espacios en blanco al principio y al final de la 
# entrada del usuario, asegurando que no se salte el campo si solo se ha introducido un espacio.

while True:
    nombre = input('Introduce tu nombre: ').strip() # puedes modificar la condición para que elimine los espacios al inicio y al final 
                                                    # de la entrada con el método .strip(). Esto permitirá que el programa trate los 
                                                    # espacios en blanco como una entrada vacía.    
    # Asegúrate de que no se introduzcan espacios o se deje vacío el campo de nombre
    if len(nombre) == 0:
        print('No has introducido tu Nombre')
        continue  # Pide nuevamente el nombre si está vacío
    elif nombre.isspace():  # Detecta si solo son espacios
        print('El nombre no puede ser solo espacios')
        continue
    
    apellido = input('Introduce tu apellido: ').strip()
    
    if len(apellido) == 0:
        print('No has introducido tu Apellido')
        continue  # Pide nuevamente el apellido si está vacío
    elif apellido.isspace():  # Detecta si solo son espacios
        print('El apellido no puede ser solo espacios')
        continue
    
    break  # Si todo está bien, se sale del bucle

while True:
    try:
        edad = int(input('Introduce tu edad: '))
        break
    except ValueError:
        print('Debes de introducir un número') 

correo = input('Introduce tu correo: ')

while True:
    try:
        telefono = input('Introduce tu teléfono: ')
        int(telefono) # En esta parte comprueba que sea un entero, pero no lo cambia.
        break
    except ValueError:
        print('Debes de introducir un número')    

print('Nombre: '+ nombre)
print('Apellido: '+ apellido)
print('Tengo: '+ str(edad) + 'años')
print('Correo: '+ correo)
print('Teléfono: '+ telefono)
