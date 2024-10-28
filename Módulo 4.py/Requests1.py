# Primeramente importarmos "requests" y la sintaxis es la siguiente

# NOMBRE_VARIABLE = requests.VERBO_HTTP('URL_DESTINO',DATOS )

# import requests

# url = 'https://pokeapi.co/api/v2/pokemon/pikachu'

# respuesta = requests.get(url)

# if respuesta.status_code != 200:
#     print('Pokémon no encontrado')
# else:
#     print(respuesta)    


# Ahora mismo ejemplo pero usando un tiempo de espera de respuesta y "try-except"

import requests

url = 'https://pokeapi.co/api/v2/pokemon/pikachu'

try:
    respuesta = requests.get(url,timeout=10) # Tiempo en segundos
except requests.Timeout:
    print('Error: El tiempo de espera ha finalizado')    

if respuesta.status_code != 200:
    print('Pokémon no encontrado')
else:
    print(respuesta)    

datos = respuesta.json() # Como buena práctica guardamos la respuesta en una variable datos, pero convertida en formato "json"   
nombre = datos['name']
# nombre = datos['species']['name']

print('Movimientos de'+ nombre + ': ')

movimientos = datos['moves'] #Guardamos los movimientos dentro de una variable
for i in range(int(len(movimientos))) : # Longitud de cuantos movimientos tiene
    movimiento = movimientos[i]['move']['name'] # Se crea una variable movimiento
    print(movimiento) # Da una lista de los movimientos que puede aprender pikachu