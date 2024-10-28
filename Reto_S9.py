# Función que obtiene la letra anterior y siguiente en el alfabeto
def letras_adyacentes(letra):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    
    if letra in alfabeto:
        index = alfabeto.index(letra)
        anterior = alfabeto[index - 1] if index > 0 else None
        siguiente = alfabeto[index + 1] if index < len(alfabeto) - 1 else None
        
        # Muestra el resultado
        print(f"Letra ingresada: {letra}")
        if anterior:
            print(f"Letra anterior: {anterior}")
        else:
            print("No hay letra anterior (al inicio del alfabeto)")
        
        if siguiente:
            print(f"Letra siguiente: {siguiente}")
        else:
            print("No hay letra siguiente (al final del alfabeto)")
    else:
        print(f"'{letra}' no es una letra válida en el alfabeto.")

# Bucle principal del programa
def main():
    print("Escribe una letra. Para salir del programa, escribe 'alto'.")
    
    while True:
        # Solicitar entrada al usuario
        entrada = input("Ingresa una letra (o 'alto' para salir): ").lower()
        
        if entrada == "alto":
            print("¡Programa terminado!")
            break
        elif len(entrada) == 1 and entrada.isalpha():
            # Si es una sola letra válida, llamamos a la función
            letras_adyacentes(entrada)
        else:
            print("Por favor, ingresa una letra válida.")

# Ejecutamos el programa principal
if __name__ == "__main__":
    main()