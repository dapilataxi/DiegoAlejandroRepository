"""
En primera instancia se importa la librería random, puesto que para este juego se  necesita usar la ayuda de valores generados
totalmente al azar, es un juego en cual el usuario puede repetirlo las veces que el quiera, pero si el desafío no es el mismo
pierde in poco la gracia
"""
import random

"""
Este bloque va de la mano puesto que solo es una presentación a la dinámica del juego, donde el usuario solo debe poner atención
a las instrucciones sencillas para comenzar este juego de agilidad mental
"""
print('----------------------------------------')
print('HOLA BIENVENIDO A OPERA CON ANIMALES')
print('----------------------------------------')
print('\nOpera con animales es un juego de agilidad mental, donde deberás averiguar cuál es el valor de cada animal, en base a una pistas proporcionadas')
print('\nTu puedes elegir el nivel de difucultad con el cual quieres participar. Donde "1" es el nivel más fácil y "2" el más complicado.')

"""
La definicion de esta variables tienen la misma función puesto que son solo contadores, para poder ejecutar las opciones
con los diferentes bucles que se emplearan más adelante.
La variable "variables" será usada para preguntar al usuario con cuantas variables quiere jugar en este minijuego de 
razonamiento.
"""
variables = 0
"""
ope1 es una variable inicializada para poder ejecutar el bucle con el procedimiento si el usuario elige jugar
con la menor dificultad.
"""
ope1 = 0
"""
ope6 es una variable inicializada para poder ejecutar el bucle con el procedimiento si el usuario elige jugar
con la máxima dificultad.
"""
ope6 = 0
"""
Es importante para este programa el ingreso de datos correctos, esta función esta destinada para que el usuario
obligatoriamnete deba ingrear un número entero, de no hacerlo, esta función no dejará que continúe la ejecución
del programa
"""
def lee_entero(entero):
    """
    Se sentencia con el bucle "while", mientras no sea verdadero la sentencia, en este caso, hasta que la variable
    ingresada por teclado no sea un dato de tipo entero (int) el programa no dejará continuar e imprimirá el mensaje
    de la linea 52.
    """
    while True:
        entero = input()
        try:
            entero = int(entero)
            return entero
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero. PRUEBA DE NUEVO")

"""
Para hacer un poco más sencillo la comprensión en la secuencia lógica del código se elabora una funcion, para
la ejecución del juego con la menor dificultad, que consta del bucle "while" y el condicional "if"
"""
def nivel_facil(variable1,variable2,variable3,ope1):
  """
  Se establece un bucle haciendo referencia a una equivalencia entre 2 operaciones, hasta que esa equivalencia se cumpla
  no acabará el bucle, porque esto sirve para garantizar que los resultados de las variables que ingrese el usuario
  serán correctas
  """
  while ope1 != operacion1:
    """
    Este bloque de 3 líneas simplemente muestra al usuario las operaciones que deberá resolver y averiguar el valor de cada
    animal que se muestra en las operaciones, siempre van a tener un valor diferente
    """
    print('-------------------------------------------')
    print('DADA LAS SIGUIENTES OPERACIONES:\n\npajaro + pajaro + pez =',operacion1,'\nleon - pez - pez =',operacion2,'\npajaro + leon - pez =',operacion3)
    print('-------------------------------------------')
    """
    En este bloque de 6 líneas se pregunta el valor de cada animal que ha calculado el usuario, simplemente es la entrada
    por teclado que debe registrar el usuario de estos datos, además se usa la misma función que se usó en primera instancia
    para que el sistema lea solo números enteros
    """
    print('¿Cuál es el valor de "pajaro"?: ')
    variable1 = lee_entero(variable1)
    print('\n¿Cuál es el valor de "leon"?: ')
    variable2 = lee_entero(variable2)
    print('\n¿Cuál es el valor de "pez"?: ')
    variable3 = lee_entero(variable3)
    """
    ope1 se define en una operacion para que pueda cumplir las condiciones y se cumpla el requisito que forma parte
    del bucle
    """
    ope1 = variable1 + variable1 + variable3
    """
    Este bloque de 8 líneas simplemente es un mensaje para el usuario de que los valores ingresados a los animales
    no son correctos y debe intentarlo de nuevo, si ingresó correctamente todos los valores, se informa al usuario
    que acertó
    """
    if ope1 != operacion1:
      print('**************************************')
      print('TE HAS EQUIVOCADO. INTENTA DE NUEVO')
      print('**************************************')
    else:
      print('***************************')
      print('CORRECTO. Has acertado') 
      print('***************************')

"""
Para hacer un poco más sencillo la comprensión en la secuencia lógica del código se elabora otra funcion como el caso anterior, para
la ejecución del juego con más dificultad, que consta del bucle "while" y el condicional "if"
"""
def nivel_complicado(variable1,variable2,variable3,ope6):
  """
  Se establece un bucle haciendo referencia a una equivalencia entre 2 operaciones, hasta que esa equivalencia se cumpla
  no acabará el bucle, porque esto sirve para garantizar que los resultados de las variables que ingrese el usuario
  serán correctas
  """
  while ope6 != operacion6:
      """
      Este bloque de 3 líneas simplemente muestra al usuario las operaciones que deberá resolver y averiguar el valor de cada
      animal que se muestra en las operaciones, siempre van a tener un valor diferente
      """
      print('-------------------------------------------')
      print('DADA LAS SIGUIENTES OPERACIONES:\n\npajaro + pajaro - leon - (pez + pez) =',operacion4,'\n(pajaro + pajaro) - (leon + leon) + (pez + pez) =',operacion5,'\npajaro - (leon + leon) + pez =',operacion6)
      print('-------------------------------------------')
      """
      En este bloque de 6 líneas se pregunta el valor de cada animal que ha calculado el usuario, simplemente es la entrada
      por teclado que debe registrar el usuario de estos datos, además se usa la misma función que se usó en primera instancia
      para que el sistema lea solo números enteros
      """
      print('¿Cuál es el valor de "pajaro"?: ')
      variable1 = lee_entero(variable1)
      print('\n¿Cuál es el valor de "leon"?: ')
      variable2 = lee_entero(variable2)
      print('\n¿Cuál es el valor de "pez"?: ')
      variable3 = lee_entero(variable3)
      """
      ope6 se define en una operacion para que pueda cumplir las condiciones y se cumpla el requisito que forma parte
      del bucle
      """
      ope6 = variable1 - (variable2 + variable2) + variable3
      """
      Este bloque de 8 líneas simplemente es un mensaje para el usuario de que los valores ingresados a los animales
      no son correctos y debe intentarlo de nuevo, si ingresó correctamente todos los valores, se informa al usuario
      que acertó
      """
      if ope6 != operacion6:
        print('**************************************')
        print('TE HAS EQUIVOCADO. INTENTA DE NUEVO')
        print('**************************************')
      else:
        print('***************************')
        print('CORRECTO. Has acertado') 
        print('***************************')

"""
Inicio del ciclo while para que el usuario ingrese el valor con la dificulatad que quiere jugar, solo se tiene 2 niveles
de dificultad, el "1" representa al nivel con menos dificultad, mientras que el "2" representa al nivel con mayor
dificultad, si ingresa un numéro diferente, este while le dirá que la opción no es válida
"""
while variables != 2:
    """
    Este bloque de 3 líneas simplemente devuelve un valor aleatorio a la variable de cada animal, cada vez que se ejecute
    esta parte las variables tendran un valor diferente entre el rango establecido, que en este caso es de 1 a 10
    """
    pajaro = random.randint(1,10)
    leon = random.randint(1,10)
    pez = random.randint(1,10)
    """
    Este bloque de 6 líneas son operaciones que constan en las dos funciones creadas anteriormente, simplemente se las escribe
    aquí para que se pueda ejecutar bien el bucle con variables aleatorios, y muestre los valores, porque ambas funciones
    llaman a las variables "operacion" acorde al número asignado
    """
    operacion1 = pajaro + pajaro + pez 
    operacion2 = leon - pez - pez
    operacion3 = pajaro + leon - pez
    operacion4 = pajaro + pajaro - leon - (pez + pez) 
    operacion5 = (pajaro + pajaro) - (leon + leon) + (pez + pez) 
    operacion6 = pajaro - (leon + leon) + pez 
    """
    Se pide al usuario que ingrese un valor para poder saber, el nivel de dificulad con el que quiere jugar, además se usa la función
    creada para validar el número entero, de esta manera si el usuario ingresa una cade de letras, no se podrá continuar, se debe
    ingresar únicamente un numero entero
    """
    print('\nPor favor. Ingrese el nivel de dificultad con el cual quiere jugar: ')
    variables = lee_entero(variables) 
    """
    Si el usuario ingresa el valor 1, significa que quiere jugar con la menor dificultad y se ejecuta
    el condicional con la función creada para dicha modalidad
    """
    if variables == 1:
        """
        Este bloque de 7 líneas, debe explicarse en conjunto, primero se ejecuta la funcion creada para el nivel de dificultad
        que se creó previamente, si se resuelve correctamente, se le pregunta al usuario si quiere seguir jugando, si 
        su respuesta es "si", se devuelve a la pregunta del nivel de dificulad con el que quiere jugar. Si la respuesta es no
        el "else" ayuda a terminar el juego y termina la ejecución
        """
        nivel_facil(pajaro,leon,pez,ope1)   
        pregunta = input('¿Deseas seguir jugando?\n1. si\n2. no\n\nIngresa tu respuesta (si o no): ')
        if pregunta == 'si':
          variables = 1 
        else:
          variables = 2
          print('GRACIAS POR JUGAR')
          """
          Si el usuario ingresa el valor 2, significa que quiere jugar con la mayor dificultad y se ejecuta
          el condicional con la función creada para dicha modalidad
          """       
    elif variables == 2:
        """
        Este bloque de 7 líneas, debe explicarse en conjunto, primero se ejecuta la funcion creada para el nivel de dificultad
        que se creó previamente, si se resuelve correctamente, se le pregunta al usuario si quiere seguir jugando, si 
        su respuesta es "si", se devuelve a la pregunta de cuantas variables quiere jugar. Si la respuesta es no
        el "else" ayuda a terminar el juego y termina la ejecución
        """
        nivel_complicado(pajaro,leon,pez,ope6)
        pregunta = input('¿Deseas seguir jugando?\n1. si\n2. no\n\nIngresa tu respuesta (si o no): ')
        if pregunta == 'si':
          variables = 1
        else:
          variables = 2
          print('GRACIAS POR JUGAR')                
        """
        Este "else" es un mensaje que muestra al usuario si ingresó una cantidad de variables con las cuales
        no se puede jugar y solo se le pide que el dato ingresado es correcto y que lo intente de nuevo
        """
    else:
        print('\nNUMERO DE VARIABLES NO VALIDA. INTENTA DE NUEVO')
  