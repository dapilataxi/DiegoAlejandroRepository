#Libreria que me permite graficar en python 
from turtle import *

def opera_animales():
  """
  Se crea una función para el segundo juego del proyecto realizado, se la llama como opera_animales para un mejor manejo en el programa
  
  Parámetros:
  -------------------
  No tiene parámetros

  Retorna:
  -------------------
  No retorna ningun valor
  """
  import random #importe de la librería para el uso de valores randómicos

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
      Función creada para la validación de un número entero al ingreso de datos por teclado, esta función permitirá
      ingresar únicamente el dato del tipo solicitado, caso contrario no avanzará su ejecución.
  
      Parámetros:
      -------------------
      entero: int
        variable que guarda el dato ingresado por el usuario como número entero

      Retorna:
      -------------------
      Retorna "entero" como número entero
      """
      while True: #Bucle para que no avance el programa hasta que se cumpla la condición dada
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
    Función creada para el nivel de dificultad "fácil" del juego elaborado.
  
    Parámetros:
    -------------------
    variable1: int
        Valor que se debe ingresar por teclado para hallar una primera incógnita
    variable2: int
        Valor que se debe ingresar por teclado para hallar una segunda incógnita
    variable3: int
        Valor que se debe ingresar por teclado para hallar una tercera incógnita
    ope1: int
        Valor que se guarda al ejecutarse una operación establecida y debe ser comparada        

    Retorna:
    -------------------
    No retorna ningun valor
    """
    while ope1 != operacion1: #Bucle establecido para que se repita un proceso hasta que no se cumpla la condición dada
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
    Función creada para el nivel de dificultad "complicado" del juego elaborado.
  
    Parámetros:
    -------------------
    variable1: int
        Valor que se debe ingresar por teclado para hallar una primera incógnita
    variable2: int
        Valor que se debe ingresar por teclado para hallar una segunda incógnita
    variable3: int
        Valor que se debe ingresar por teclado para hallar una tercera incógnita
    ope6: int
        Valor que se guarda al ejecutarse una operación establecida y debe ser comparada        

    Retorna:
    -------------------
    No retorna ningun valor
    """
    while ope6 != operacion6: #Bucle establecido para que se repita un proceso hasta que no se cumpla la condición dada
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

def lee_entero(entero):
    """
    Función creada para la validación de un número entero al ingreso de datos por teclado, esta función permitirá
    ingresar únicamente el dato del tipo solicitado, caso contrario no avanzará su ejecución.
  
    Parámetros:
    -------------------
    entero: int
    variable que guarda el dato ingresado por el usuario como número entero

    Retorna:
    -------------------
    Retorna "entero" como número entero
    """
    while True:
        entero = input()
        try:
            entero = int(entero)
            return entero
        except ValueError:
            print("ATENCIÓN: Debe ingresar un número entero. PRUEBA DE NUEVO") 

def adivina_cuadros():

    def bienvenida():
        """
        Realizamos una función sencilla para adornar una bienvenida al programa. 
        Parametros:
        ------------
        No tiene parametros de entrada

        Retorna:
        ------------
        No retorna Ningun valor
        """
        print('\n')
        print('*' * 65)
        print('*Te doy la bienvenida al juego Advina el numero de cuadradros :D*')
        print('*' * 65)
        print('\n')

    def despedida():
        """
        Realizamos una función sencilla para adornar una despedida al programa. 
        Parametros:
        ------------
        No tiene parametros de entrada
        
        Retorna:
        ------------
        No retorna Ningun valor
        """
        print('\n')
        print('*' * 71)
        print('* Gracias por jugar al Adivina el numero de cuadrados. ¡Hasta pronto! *')
        print('*' * 71)
        print('\n')

    
    def jugar_otra_vez():
        """
        Realizamos una función sencilla para volver a ejecutar el programa o no, dependiendo de la decisión del usuario. 
        Parametros:
        ------------
        No tiene parametros de entrada
        
        Retorna:
        ------------
        No retorna Ningun valor
        """
        return input('\nDeseas jugar otra vez (introduce s para sí o cualquier otra cosa para no): ')

    """
    Encerramos el comportamiento de los cuadrados para elaborarlos respectivamente en dos funciones. 
    """
    def cuadrado_catorce(longitud):
        """
        Es un procedimiento que me permite graficar los cuadrados que se mostrarán en pantalla para que el usuario pueda adivinar el número total. En este caso
        me dibuja un cuadrado de 3x3 para que la respuesta sea 14, por eso el nombre de la función.
        Parametros:
        ------------
            Recibe el parámetro "longitud" el cuál es el tamaño con el que se va a graficar los cuadrados, entre más alto el valor obviamente el cuadrado
            será más grande.
        Retorna:
        ------------
        No retorna ningún valor.
        """
        # Cuatro veces...
        for i in range(4):
            speed(0) #Velocidad a la que grafica la figura, podemos cambiarla para que sea mas rápida o mas lenta.
            # Ir hacia adelante
            forward(longitud)
            # Y girar 90 grados
            right(90)
            for i in range(4):
                # Ir hacia adelante
                forward(longitud*2)
                # Y girar 90 grados
                right(90)
    def cuadrado_cinco(longitud):
        """
        Es un procedimiento que me permite graficar los cuadrados que se mostrarán en pantalla para que el usuario pueda adivinar el número total. En este caso
        me dibuja un cuadrado de 2x2 para que la respuesta sea 5, por eso el nombre de la función.
        Parametros:
        ------------
            Recibe el parámetro "longitud" el cuál es el tamaño con el que se va a graficar los cuadrados, entre más alto el valor obviamente el cuadrado
            será más grande.
        Retorna:
        ------------
        No retorna ningún valor.
        """
        # Cuatro veces...
        for i in range(4):
            speed(1) 
            # Ir hacia adelante
            forward(longitud*2)
            # Y girar 90 grados
            right(90)
            # Cuatro veces...
            for i in range(4):
                # Ir hacia adelante
                forward(longitud)
                # Y girar 90 grados
                right(90)

    #Main para la ejecucion principal del programa.
    if __name__ == '__main__':
    #Ciclo do-while para ejecutar el programa y utilizar la función jugar_otra_vez dependiendo de la decisión del usuario. 
        while True: 
            reset() #Limpia las graficas de la pantalla.
            bienvenida()
            cuadrado_catorce(70)
            print('¿Cuantos cuadrados hay?')
            respuesta = 0
            respuesta = lee_entero(respuesta)
            if int(respuesta) == 14:
                print('\nCorrecto!, siga al siguiente nivel')
                print('\n-----Revise el nuevo cuadrado-----')
                reset()
                cuadrado_cinco(50)
                print('\nCuantos cuadrados hay?')
                respuesta2 = 0
                respuesta2 = lee_entero(respuesta2)
                if int(respuesta2) == 5:
                    print('\nCorrecto!, ha ganado el juego :D')
                    despedida()
                    exit()
                else:
                    print('\nIncorrecto!')
                    print('\nVuelva a intentarlo, suerte!')
                    if jugar_otra_vez() != 's' : break
            else:
                print('\nIncorrecto!')
                print('\nVuelva a intentarlo, suerte!')
                if jugar_otra_vez() != 's': break
        despedida()

opcion = 0

opcion2 = 0

while  opcion != 3:
    print('--------------------------------')
    print('BIENVENIDO A JUEGOS DE LÓGICA')
    print('--------------------------------')
    print('1. Adivina el número de cuadrados')
    print('2. Opera con animales')
    print('3. Salir')
    print('------------------------------')
    print('Ingrese el juego que desea ejecutar: ')
    opcion = lee_entero(opcion)
    if opcion == 1:
        adivina_cuadros()
        print('¿Desea volver al menú principal?')
        print('1. Si')
        print('2. No')
        opcion2 = lee_entero(opcion2)
        if opcion2 == 1:
            opcion = 0
        elif opcion2 == 2:
            opcion = 3
            print('\nGRACIAS POR JUGAR :D') 
    elif opcion == 2:
        opera_animales()
        print('¿Desea volver al menú principal?')
        print('1. Si')
        print('2. No')
        opcion2 = lee_entero(opcion2)
        if opcion2 == 1:
            opcion = 0
        elif opcion2 == 2:
            opcion = 3
            print('\nGRACIAS POR JUGAR :D')
    elif opcion == 3:
        print('--------------')
        print('VUELVE PRONTO!')
        print('--------------')
    else:
        print('**********************************')
        print('OPCIÓN NO VALIDA. INTENTA DE NUEVO :/')
        print('**********************************')
    
