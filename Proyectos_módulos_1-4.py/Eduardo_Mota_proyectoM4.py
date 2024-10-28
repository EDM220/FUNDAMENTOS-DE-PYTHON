# El siguiente programa realiza lo siguiente: Cuando el usuario introduzca el nombre de un Pokémon, si no existe manda
# un mensaje de error; si existe, muestra una imagen y las estadísticas (peso, tamaño, movimientos, habilidades y tipos). 
# Posteriormente, guarda toda la información del pokémon (junto con el link de la imagen frontal del pokémon) en un archivo .json 
# dentro de una carpeta llamada “pokedex”.


import requests # Libreria que permite hacer peticiones HTTP a la API de PokeAPI para obtener información del pokémon
import os # permite interactuar con el sistema de archivos, como crear carpetas y manejar rutas de archivos.
import json # Trabaja con archivos JSON (lectura y escritura).

# Función para obtener la información del Pokémon
def obtener_pokemon(nombre_pokemon): # Esta función permite introducir al usuario el nombre del pokémon que busca
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}' # se foma la URL que consulta la API.escritura en minúsculas
    response = requests.get(url)                                        # Se realiza solicitid HTTP GET para tener información del
                                                                        # pokémon desde la API
    
    if response.status_code == 200:  # Verifica si el pokémon existe. Si es 200 es correcta.
        datos_pokemon = response.json() # Se convierte respuesta API en un formato Json
        return datos_pokemon  # Si el resultado es diferente de 200 se devuelve none para mostrar mensaje de error.
    else:     
        return None

# Función para mostrar la imagen y estadísticas
def mostrar_pokemon(datos_pokemon): # Función que recibe los datos del pokémon
    nombre = datos_pokemon['name'].capitalize() # Nombre del pokémon en mayúsculas
    peso = datos_pokemon['weight'] / 10  # Convertir a kg
    altura = datos_pokemon['height'] / 10  # Convertir a metros
    imagen = datos_pokemon['sprites']['front_default'] # URL de imagen del pokémon
    movimientos = [mov['move']['name'] for mov in datos_pokemon['moves']]# Listas que permiten extraer los movimientos,habilidades y tipos
    habilidades = [hab['ability']['name'] for hab in datos_pokemon['abilities']]
    tipos = [tipo['type']['name'] for tipo in datos_pokemon['types']]
    
    print(f"Nombre: {nombre}") # Imprime los resultados de información del pokémon
    print(f"Peso: {peso} kg")
    print(f"Altura: {altura} m")
    print(f"Imagen: {imagen}")
    print(f"Movimientos: {', '.join(movimientos[:5])}...")  # muestra nada más 5 movimientos
    print(f"Habilidades: {', '.join(habilidades)}")
    print(f"Tipos: {', '.join(tipos)}")

    return { # regesa los datos que serán guardados.
        "nombre": nombre,
        "peso": peso,
        "altura": altura,
        "imagen": imagen,
        "movimientos": movimientos[:5],  # Se guardan 5
        "habilidades": habilidades,
        "tipos": tipos
    }

# Función para guardar la información en un archivo JSON
def guardar_pokemon(datos, nombre_pokemon):
    carpeta = 'pokedex'   # Nombre de la carpeta para los archivos Json
    
    if not os.path.exists(carpeta): # Verifica si la carpeta ya existe
        os.makedirs(carpeta) # Si no existe crea una
    
    archivo_json = os.path.join(carpeta, f"{nombre_pokemon.lower()}.json") # Se guardan los archivos Json en carpeta pokedex.Nombre
                                                             # del archivo será el del pokémon en minúsculas.extensión json.
    
    with open(archivo_json, 'w') as archivo: # Se crea o abre archivo json en modo escritura
        json.dump(datos, archivo, indent=4) # Se guardan los datos del pokémon. identación de 4 espacios
    
    print(f"La información del Pokémon {datos['nombre']} ha sido guardada en {archivo_json}") # imprime mensaje que los datos estan 
                                                                                              # guardados

# Función principal
def main():
    nombre_pokemon = input("Introduce el nombre del Pokémon: ") # Aqui se piede el nombre del pokémon
    datos_pokemon = obtener_pokemon(nombre_pokemon) # Se llama a la función que busca la API para tener datos del pokémon
    
    if datos_pokemon: # Verificación de si el pokémon existe
        datos_para_guardar = mostrar_pokemon(datos_pokemon) # Si existe se muestra la información
        guardar_pokemon(datos_para_guardar, nombre_pokemon) # guarda la información mostrada
    else:
        print("¡El Pokémon no existe!") # En caso de que no exista el pokémos se muestra mensaje de error

if __name__ == "__main__": # Función principal permite iniciar todo el proceso
    main()