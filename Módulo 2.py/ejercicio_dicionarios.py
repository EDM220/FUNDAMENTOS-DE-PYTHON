# Programa que pide al usuario ingresar una frase, después el programa hará una impresión de esta frase,
# pero cambiará algunas palabras por emojis.

emoji_diccionario = {'amo':"😀","Sonrisa grande":"😃","feliz":"😄",\
                     "Sonrisa mostrando dientes":"😁","Risa con ojos cerrados":"😆",\
                     "Risa con lágrimas":"😂","Risa rodando por el suelo": "🤣","Sonrisa tímida": "😊",\
                     "Carita con halo (inocente)":"😇","Guiño":"😉","python":"🐍" }

frase = input('Escribe una frase: ')
frase = frase.lower()
palabras = frase.split()

respuesta = ''

for palabra in palabras:
    if palabra in emoji_diccionario:
        respuesta = respuesta + emoji_diccionario[palabra] + ' '
    else:
        respuesta = respuesta + palabra + ' '

print(respuesta)


