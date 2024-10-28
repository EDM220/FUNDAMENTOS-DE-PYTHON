numero = '147' # En este ejemplo el número se escribe entre comillas para que sea cadena de texto
print(numero)
print(type(numero))

numero = int(numero)
print(numero)
print(type(numero))

numero = float(numero)
print(numero)
print(type(numero))

numero = complex(numero)
print(numero)
print(type(numero))

#numero = 'b'
#numero = int(numero) # No se puede cambiar el valor de la letra b porque no tiene un valor numerico

numero = 0
print(f"Primero imprimir el número que es: {numero}")
numero = bool(numero)
print(f'Después del casting el número se cambia a tipo bool que es:{numero}')
print(f"finalmente se imprime {type(numero)}")

#1numero = 0 #las variables no deben comenzar con un número
#numero1 = 0 # D esta forma esta correctamente escrita la variable (no hay error de sitaxis)

#_numero = 0 # El guion bajo es el único carácter que puede escribirse al inicio de una variable,-
# pero por buenas prácticas se sugiere usar el guion bajo para hacer distinción de palabras dentro de una variable
#ejemplo

numero_uno = 0 #nomenclatura tipo serpiente
numero_dos = 1 #nomenclatura tipo serpiente

# No usar palabras reservadas

x = 9
X = 10
print(x) #variables sensitivas a mayúsculas y minúsculas
print(X)

# Como convención entre programadores no se usan mayúsculas al definir variables
numeroUno = 0
numeroDos = 1 # Uso de camel case para mantener legibilidad

# Para saber cuales son las palabras reservadas
help("keywords")