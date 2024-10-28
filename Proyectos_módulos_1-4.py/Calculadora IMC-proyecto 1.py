print('\n\n             *******CALCULADORA DE INDICE DE MASA CORPORAL*******\n')
print('Por favor introduce los siguientes datos:\n ')

while True:
    nombre = input('Escribe tu nombre: ')
    if nombre.isalpha():
       break
    else:
        print('Error: el nombre no debe contener números ni datos especiales. Por favor intentalo de nuevo:')

while True:
    apellido1 = input('Escribe tu apellido paterno: ')
    if apellido1.isalpha():
        break
    else:
        print('Error: el apellido no debe contener números ni datos especiales. Por favor intentalo de nuevo:')

while True:
    apellido2 = input('Escribe tu apellido materno: ')
    if apellido2.isalpha():
        break
    else:
        print('Error: el apellido no debe contener números ni datos especiales. Por favor intentalo de nuevo:')

while True:
    try:
        edad = int(input('¿Cuál es tu edad: '))
        break
    except:
         print('Error: Solamente ingresa valores numéricos enteros. Por favor intentalo de nuevo:')

while True:
    try:    
        peso= float(input('¿Cuál es tu peso en kg: '))
        if peso >=0.1:
            break
        else:
            print('Error: ingresa un valor de peso valido en kg. Por favor intentalo de nuevo:')     
    except:
        print('Error: ingresa un valor de peso valido en kg. Por favor intentalo de nuevo:') 
       
while True:
    try:        
        estatura= float(input('¿Cuál es tu estatura en metros: '))
        if 0.1<= estatura <= 4.0:
            break
        else:
            print('Error: ingresa valores numéricos en metros.Ejemplo 1.80. Por favor intentalo de nuevo:')
    except:
        print('Error: ingresa valores numéricos en metros.Ejemplo 1.80. Por favor intentalo de nuevo:')
   
imc = peso/estatura**2

print('\nDeacuerdo con los datos proporcionados:')
print(f'{nombre} {apellido1} {apellido2}:tiene {edad} años,su peso y estatura son de {peso:.2f} kg y {estatura} metros.')
print(f'Su IMC de {imc:.2f} calculada indica que',end = ' ')


if (imc < 18.5):
    print('esta bajo de peso\n\n')
elif (18.5 <= imc <24.9 ):
    print('tiene peso normal\n\n')
elif (25 <= imc < 29.9):
    print('tiene sobrepeso\n\n') 
elif (30 <= imc < 34.9):
    print('tiene obesidad tipo 1\n\n')   
elif (35 <= imc < 39.9):
    print('tiene Obesidad 2\n\n')
else:
    print('tiene obesidad tipo 3\n\n') 


print('Gracias por usar esta calculadora!')

  
       
    


