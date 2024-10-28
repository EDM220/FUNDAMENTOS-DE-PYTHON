
# 1.    longitud de una frase

# Crear un programa para identificar la longitud de una frase. La palabra correcta debe tener 
# entre cuatro y ocho letras.

# 2.	Encuentra el cuadrante

# Crear un programa que, en base a 2 números de entrada, coordenadas, identifique en cuál de los 4 cuadrantes 
# se encuentra el punto. El programa debe verificar que ninguna coordenada sea 0

print('\n####################  IDENTIFICADOR DE LONGITUD DE FRASES Y PLANO CARTESIANO  ####################\n\n')

print('Hola, por favor selecciona:\n ') # se imprime la bienvenida al usuario
print('1.- Para saber la longitud de una frase. ') # Se imprime la opción entre los dos procesos
print('2.- Para saber el cuadrante de tus coordenadas en el plano cartesiano: ',end = '')

seleccion = input('') # En esta parte se carga la selección
if seleccion == '1': # Si es la opción 1, se empieza el proceso de identificar la longitud de frase

    palabra = input('\nPor favor ingresa una palabra: ') # se pide ingrese la palabra o frase
    sin_espacios = ''.join([char for char in palabra if char.isalpha()]) # aquí nada más se cuentan las palabras
                                                                         #los espacios no cuentan
    long_palabra = len(sin_espacios)# aquí se carga el tamaño de la palabra o frase

    if 4 <= long_palabra <= 8: # Se valida el tamaño de la palabra o frase
        print('La palabra es correcta.')    
    elif long_palabra < 4:
        print(f'Hace falta letras. Solo tiene {long_palabra} letras.')    
    else:
        print(f'Sobran letras.Tiene {long_palabra} letras.')

elif seleccion == '2': # En la opción 2 se le pide ingrese los valores de x,y para identificar el cuadrante
    valor_x = float(input('\nIngresa el valor de x: '))
    valor_y = float(input('Ingresa el valor de y: '))

    if valor_x == 0 and valor_y == 0: # Se empieza a validar los datos cargados por el usuario
        print('El punto esta el origen, por lo tanto no puede estar en ningún cuadrante.')
    elif valor_x == 0:
        print('Estas sobre el eje Y.') 
    elif valor_y == 0:
        print('Estas sobre el eje X.')    
    elif valor_x > 0 and valor_y > 0:
        print("El punto se encuentra en el Primer Cuadrante.")
    elif valor_x < 0 and valor_y > 0:
        print("El punto se encuentra en el Segundo Cuadrante.")
    elif valor_x < 0 and valor_y < 0:
        print("El punto se encuentra en el Tercer Cuadrante.")
    elif valor_x > 0 and valor_y < 0:
        print("El punto se encuentra en el Cuarto Cuadrante.")

print('\nEspero haya sido de tu ayuda. Saludos!\n') # Se termina el programa    
 
