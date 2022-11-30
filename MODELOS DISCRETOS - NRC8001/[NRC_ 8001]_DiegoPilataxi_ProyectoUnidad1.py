"""
En primera instancia se importa la librería random, puesto que para este juego se  necesita usar la ayuda de valores generados
totalmente al azar, es un juego en cual el usuario puede repetirlo las veces que el quiera, pero si el desafío no es el mismo
pierde in poco la gracia
"""
import random

"""
Este bloque va de la mano puesto que solo es una presentación a la dinámica del juego, donde el usuario solo debe ingresar
su nombre y posteriormente se dará una instrucción sencilla para poder empezar este juego.
"""
print('HOLA BIENVENIDO A SUMA CON ANIMALES')
nombre = input('Por favor ingresa tu nombre: ')
print('\nGracias por participar, '+nombre)
print('\nSuma con animales es un juego de razonamiento, donde deberás averiguar cuál es el valor de cada animal, en base a una pistas proporcionadas')
print('\nTu puedes elegir el número de variables con el cual quieres participar. Sea con 3 o 4 variables.')

"""
La definicion de esta variables tienen la misma función pueto que son solo contadores, para poder ejecutar las opciones
con los diferentes bucles que se emplearan más adelante.
La variable "variables" será usada para preguntar al usuario con cuantas variables quiere jugar en este minijuego de 
razonamiento.
"""
variables = 0
"""
ope1 es una variable inicializada para poder ejecutar el bucle con el procedimiento si el usuario elige jugar
con 3 variables.
"""
ope1 = 0
"""
ope7 es una variable inicializada para poder ejecutar el bucle con el procedimiento si el usuario elige jugar
con 4 variables.
"""
ope7 = 0

"""
Para hacer un poco más sencillo la comprensión en la secuencia lógica del código se elabora una funcion, para
la ejecución del juego con 3 variables, que consta del bucle "while" y el condicional "if"
"""
def tres_variables(variable1,variable2,variable3,ope1):
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
    print('DADA LAS SIGUIENTES OPERACIONES:\n\npajaro + pajaro + pez =',operacion1,'\nleon - (pez + pez) =',operacion2,'\n(pajaro + pajaro) - (leon + leon) - pez =',operacion3)
    print('-------------------------------------------')
    """
    En este bloque de 6 líneas se pregunta el valor de cada animal que ha calculado el usuario, simplemente es la entrada
    por teclaso que debe registrar el usuario y se transforma el valor digitado a una variable de tipo entero
    """
    variable1 = input('¿Cuál es el valor de "pajaro"?: ')
    variable1 = int(variable1)
    variable2 = input('\n¿Cuál es el valor de "leon"?: ')
    variable2 = int(variable2)
    variable3 = input('\n¿Cuál es el valor de "pez"?: ')
    variable3 = int(variable3)
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
Para hacer un poco más sencillo la comprensión en la secuencia lógica del código se elabora una funcion como el caso anterior, para
la ejecución del juego con 4 variables, que consta del bucle "while" y el condicional "if"
"""
def cuatro_variables(variable1,variable2,variable3,variable4,ope7):
  """
  Se establece un bucle haciendo referencia a una equivalencia entre 2 operaciones, hasta que esa equivalencia se cumpla
  no acabará el bucle, porque esto sirve para garantizar que los resultados de las variables que ingrese el usuario
  serán correctas
  """
  while ope7 != operacion7:
      """
      Este bloque de 3 líneas simplemente muestra al usuario las operaciones que deberá resolver y averiguar el valor de cada
      animal que se muestra en las operaciones, siempre van a tener un valor diferente
      """
      print('-------------------------------------------')
      print('DADA LAS SIGUIENTES OPERACIONES:\n\npajaro + pajaro - leon - (pez + pez) + gallo =',operacion4,'\n(pajaro + pajaro) - (leon + leon) + (pez + pez) - gallo =',operacion5,'\n(gallo + gallo) - (pajaro + pajaro) - (leon + leon) + pez =',operacion6,'\npajaro + leon + pez + gallo =',operacion7)
      print('-------------------------------------------')
      """
      En este bloque de 8 líneas se pregunta el valor de cada animal que ha calculado el usuario, simplemente es la entrada
      por teclaso que debe registrar el usuario y se transforma el valor digitado a una variable de tipo entero
      """
      variable1 = input('¿Cuál es el valor de "pajaro"?: ')
      variable1 = int(variable1)
      variable2 = input('\n¿Cuál es el valor de "leon"?: ')
      variable2 = int(variable2)
      variable3 = input('\n¿Cuál es el valor de "pez"?: ')
      variable3 = int(variable3)
      variable4 = input('\n¿Cuál es el valor de "gallo"?: ')
      variable4 = int(variable4)
      """
      ope7 se define en una operacion para que pueda cumplir las condiciones y se cumpla el requisito que forma parte
      del bucle
      """
      ope7 = variable1 + variable2 + variable3 + variable4
      """
      Este bloque de 8 líneas simplemente es un mensaje para el usuario de que los valores ingresados a los animales
      no son correctos y debe intentarlo de nuevo, si ingresó correctamente todos los valores, se informa al usuario
      que acertó
      """
      if ope7 != operacion7:
        print('**************************************')
        print('TE HAS EQUIVOCADO. INTENTA DE NUEVO')
        print('**************************************')
      else:
        print('***************************')
        print('CORRECTO. Has acertado') 
        print('***************************')

"""
Inicio el ciclo while para que el usuario ingrese el valor con el numero de variables que quiere jugar, solo se puede jugar
con 3 o 4 variables, si ingresa un numéro diferente, este while le dirá que la opción no es válida
"""
while variables != 4:
    """
    Este bloque de 4 líneas simplemente devuelve un variable aleatorio a la variable de los animales, cada vez que se ejecute
    esta parte las variables tendran un valor diferente
    """
    pajaro = random.randint(1,15)
    leon = random.randint(1,15)
    pez = random.randint(1,15)
    gallo = random.randint(1,15)
    """
    Este bloque de 7 líneas son operaciones que constan en las dos funciones creadas anteriormente, simplemente se las escribe
    aquí para que se pueda ejecutar bien el bucle con variables aleatorios, y muestre los valores, porque ambas funciones
    llaman a las variables operacion#
    """
    operacion1 = pajaro + pajaro + pez 
    operacion2 = leon - (pez + pez)
    operacion3 = (pajaro + pajaro) - (leon + leon) - pez
    operacion4 = pajaro + pajaro - leon - (pez + pez) + gallo
    operacion5 = (pajaro + pajaro) - (leon + leon) + (pez + pez) - gallo
    operacion6 = (gallo + gallo) - (pajaro + pajaro) - (leon + leon) + pez
    operacion7 = pajaro + leon + pez + gallo 
    """
    Se pide al usuario que ingrese un valor para poder saber, el número de variables que quiere usar
    para el juego
    """
    variables = input('\nPor favor. Ingrese la cantidad de variables con las cuales quiere jugar: ')
    """
    Se transforma el valor ingresado en valor entero, para que de esta manera se lo pueda usar como
    valor numérico
    """
    variables = int(variables) 
    """
    Si el usuario ingresa el valor 3, significa que quiere jugar con tres variables y se ejecuta
    el condicional con las 3 variables
    """
    if variables == 3:
        """
        Este bloque de 7 líneas, debe explicarse en conjunto, primero se ejecuta la funcion creada para tres variables
        que se creó previamente, si se resuelve correctamente, se le pregunta al usuario si quiere seguir jugando, si 
        su respuesta es "si", se devuelve a la pregunta de cuantas variables quiere jugar. Si la respuesta es no
        el "else" me ayuda a terminar el juego y termina la ejecución
        """
        tres_variables(pajaro,leon,pez,ope1)   
        pregunta = input('¿Deseas seguir jugando?\n1. si\n2. no\n\nIngresa tu respuesta (si o no): ')
        if pregunta == 'si':
          variables = 3 
        else:
          variables = 4
          print('GRACIAS POR JUGAR')
          """
          Si el usuario ingresa el valor 3, significa que quiere jugar con tres variables y se ejecuta
          el condicional con las 3 variables
          """       
    elif variables == 4:
        """
        Este bloque de 7 líneas, debe explicarse en conjunto, primero se ejecuta la funcion creada para cuatro variables
        que se creó previamente, si se resuelve correctamente, se le pregunta al usuario si quiere seguir jugando, si 
        su respuesta es "si", se devuelve a la pregunta de cuantas variables quiere jugar. Si la respuesta es no
        el "else" me ayuda a terminar el juego y termina la ejecución
        """
        cuatro_variables(pajaro,leon,pez,gallo,ope7)
        pregunta = input('¿Deseas seguir jugando?\n1. si\n2. no\n\nIngresa tu respuesta (si o no): ')
        if pregunta == 'si':
          variables = 3
        else:
          variables = 4
          print('GRACIAS POR JUGAR')                
        """
        Este "else" es un mensaje que muestra al usuario si ingresó una cantidad de variables con las cuales
        no se puede jugar y solo se le pide que el dato ingresado es correcto y que lo intente de nuevo
        """
    else:
        print('\nNUMERO DE VARIABLES NO VALIDA. INTENTA DE NUEVO')
  