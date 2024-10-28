pila = [3,6,7]

while len(pila) >= 3 : # Este bucle while se ejecuta siempre que la longitud de la lista pila 
                       # sea mayor o igual a 3.
    if  pila[-1] % 3 : # Esta línea verifica si el último elemento de la lista pila (accedido con pila[-1]) 
                       # no es un múltiplo de 3. El cero es considerado como falso, en el caso de que
                       # en la división el residuo sea 1, se comsidera positivo
                       # 7 % 3 devuelve 1 porque al dividir 7 entre 3, el cociente es 2 y el resto es 1.
                       # 9 % 3 devuelve 0 porque 9 es divisible exactamente por 3, por lo que no hay resto.
                       # si se tiene un 1 significa que el último número no es un múltiplo de 3.
                       # Si el resto es 0 (pila[-1] % 3 == 0), significa que el último número es 
                       # un múltiplo de 3. " con valor de 1 continuara con la siguiente línea "extraido""
                       # con valor de 0 se brinca a else
                       
        extraido = pila.pop() # pila.pop() elimina el último elemento de la lista 
                              # y lo almacena en la variable extraido.
        pila.append(extraido + 1) # pila.append(extraido + 1) suma 1 al valor extraido y lo agrega de 
                                  # nuevo al final de la lista pila.
        print(pila) # muestra la lista pila actualizada.
    else : # Si la condición if no se cumple (es decir, si el último elemento es un múltiplo de 3), 
           # se ejecuta este bloque else. 
        print('Todos los elementos de la pila son múltiplos de 3')
        break
    