entrada = input('¡Hola! introduce tu edad: ')

edad = 0

if entrada.isnumeric():
    edad = int(entrada)
else :
    print('Dato incorrecto: Debes de introducir un número.')

if edad <= 0:
    print('Hay un error en tus datos, introduce sólo números positivos') 
elif edad > 115 : 
    print('Verifica tus datos. Tienes muchos años')
elif edad < 18:
    print('Eres menor de edad, no puedes comprar cigarros')
else:
    print('Eres mayor de edad. Puedes comprar cigarros')    
    
