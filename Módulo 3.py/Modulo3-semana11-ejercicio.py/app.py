# La sentencia "import" permite incluir módulos en nuevos códigos
#  se utiliza escribiendo la sentencia "import" seguida del nombre del módulo por ejemplo "random" sin la 
# extención ".py" ya que el interprete ya sabe de que se trata de un archivo del lenguaje Python
# "import randon as y un alias"

#import m_area as m #c/vez que importemos un nuevo módulo podemos ponerle un alias es decir un nombre 
                   # provicional con el cual podemos llamar al módulo durante nuestra sesión en ese código.
                   # Los alias son funcionales cuando los nombres de los módulos son muy largos o confusos
                   # y se requiere ponerles unos más cortos o especificos. Para definir un alias justo
                   # de la implemetación de un módulo se utiliza la sentancia "as, seguida del alias que se
                   # quiera utilizar por ejemplo m"

# "modulo.nombre" Cuando importamos todos los nombres definidos se establece en el namespace actual, pero para
              # usar los nombres contenidos dentro de este módulo se les debe anteponer el alias o el nombre
              # del módulo de origen. Aquí se utiliza el objeto nombre contenido dentro del modulo
              
               
#"from modulo1 import objeto1" por otro lado si sólo se quiere utilizar un objeto de algún módulo se debe de 
              # utilizar la sentecia auxiliar "from". La sentecia from permite especificar los objetos de los 
              # cuales se van a hacer uso. A estos objetos importados también se les puede asignar un alias

# ejemplos con los módulos de este archivo.

import m_factorial as mf

fact5 = mf.factorial(5)
print(f'El factorial de 5 es: {fact5}')
                                
