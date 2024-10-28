import requests

latitud = 49.8879177
longitud = -119.495902

api_key = 'xxxxxxxxxxxxxxxxxx'

url_destino =f'https://api.openweathermap.org/data/2.5/weather?lat={latitud}&
lon={latitud}&lang=es&appid={api_key}'

respuesta = requests.get(url_destino)

if respuesta.status_code != 200 :
    print('Ha ocurrido un error.Intenta nuevamente')
    exit()
