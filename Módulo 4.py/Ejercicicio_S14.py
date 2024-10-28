personas = []
while True:
    print('''
    1.Agregar persona a la agenda
    2.Guardar datos en un archivo 
    ''')
    opcion = input('Ingrese una opción: ')

    if opcion == '1':

        contacto = []   
        while True:
            nombre = input('Introduce tu nombre: ').strip() # puedes modificar la condición para que elimine los espacios al inicio y al final 
                                                            # de la entrada con el método .strip(). Esto permitirá que el programa trate los 
                                                            # espacios en blanco como una entrada vacía.    
            # Asegúrate de que no se introduzcan espacios o se deje vacío el campo de nombre
            if len(nombre) == 0:
                print('No has introducido tu Nombre')
                continue  # Pide nuevamente el nombre si está vacío
            elif not nombre.isalpha():   # Verifica que solo contenga letras
                print('El nombre solamente debe contener letras')
                continue
            elif nombre.isspace():  # Detecta si solo son espacios
                print('El nombre no puede ser solo espacios')
                continue
            
            apellido = input('Introduce tu apellido: ').strip()
            
            if len(apellido) == 0:
                print('No has introducido tu Apellido')
                continue  # Pide nuevamente el apellido si está vacío
            elif not apellido.isalpha():  # Verifica que solo contenga letras
                print('El apellido solo debe contener letras')
                continue

            elif apellido.isspace():  # Detecta si solo son espacios
                print('El apellido no puede ser solo espacios')
                continue
            else:
                contacto.append(nombre)
                contacto.append(apellido)
            
            break  # Si todo está bien, se sale del bucle

        while True:
            try:
                edad = int(input('Introduce tu edad: '))
                contacto.append(edad)
                break
            except ValueError:
                print('Debes de introducir un número') 

        correo = input('Introduce tu correo: ')
        contacto.append(correo)

        while True:
            try:
                telefono = input('Introduce tu teléfono: ')
                int(telefono) # En esta parte comprueba que sea un entero, pero no lo cambia.
                contacto.append(telefono)
                break
            except ValueError:
                print('Debes de introducir un número')
        personas.append(contacto) 

    elif opcion == '2':
        with open('agenda.txt','w') as f_agenda:
            for persona in personas:
                f_agenda.write(f'{persona[0]} {persona[1]} Edad: {persona[2]} Correo: {persona[3]} Telefono{persona[4]}\n')
        print('Datos guardados en agenda.txt') 
        break
    else:
        print('Opción inválida') 
        print('Volver a intentarlo')                   

     