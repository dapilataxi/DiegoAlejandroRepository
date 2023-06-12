import problema4, problema5, problema7, problema8, problema10, problema14, problema15, problema16, datetime, random, string
from pymongo import MongoClient

def opcion4():
    #Se llama a la funcion  para que se ejecute
    problema4.validarNumero()
    #Se presenta un mensaje de número válido 
    print('============================')
    print('NUMERO ACEPTADO')
    print('============================')

def opcion5():
    #Se pide ingreso al usuario de la hora de entrada
    print('Ingrese hora de entrada: ')
    horaEntrada = problema5.validarHora() 
    #Se pide los minutos de ingreso
    print('Ingrese minutos de entrada: ')
    minutoEntrada = problema5.validarMinuto()
    #Se pide al usuario de la hora de salida
    print('Ingrese hora de salida: ')
    horaSalida = problema5.validarHora()
    #Se pide los minutos en los que salió
    print('Ingrese minutos de salida: ')
    minutoSalida = problema5.validarMinuto()
    #Se establece las variables donde se guardara cada hora
    E = datetime.time(horaEntrada,minutoEntrada)
    L = datetime.time(horaSalida,minutoSalida)
    #Se imprime la información requerida
    print('-----------------------------------------------------------')
    print('La hora de ingreso es',E,', la hora de salida será a',L)

    #Se llama a la función para la complejidad de tiempo
    problema5.complTiempo()

def opcion7():
    #Conexion a la base de datos de Mongo DB
    cliente = MongoClient('mongodb+srv://diegop:diegop@cluster0.skonea2.mongodb.net/test')
    #Se establece una DataBase estipulada para trabajar en el ejercicio
    db = cliente['ProyectoMD']
    #Se establece el nombre de la colección de la cual se hará la eliminación
    coleccion = db['Nombres y Edades']
    #Se establece una variable para crear un bucle
    validar = False
    #El bucle se repetirá hasta que el bucle sea True
    while validar != True:
        #Se establece un menú en el cual se va a navegar
        print('------------------------------------')
        print('¿Que acción desea realizar?')
        print('1. Eliminar un registro')
        print('2. Salir')
        print('------------------------------------')
        #Se crea una nueva variable para un nuevo bucle
        validar = False
        #Se establece el bucle para que el usuario ingrese la accion que desea realizar
        while validar != True:
            #Se pide al usuario que ingrese una opcion
            opcion = input('Seleccion la acción a realizar: ')
            #Se crea la condicion para que el dato ingresado sea numérico
            if opcion.isnumeric():
                #Si es numérico la variable cambia a True
                validar = True
            #Si no es numerico
            else:
                #Se dice al usuario que la entrada es no valida
                print('-----------------------------------------------------------')
                print('ENTRADA NO VÁLIDA. SOLO DEBE INGRESAR NÚMEROS ENTEROS. INGRESE DE NUEVO')
                validar = False
        #Si la opcion escogida es 1
        if int(opcion) == 1:
            #Se procede a ejecutar la funcion para elimiar documentos en la coleccion
            problema7.eliminarNombres(coleccion)
            validar = False
        #Si la opcion es 2
        elif int(opcion) == 2:
            #Se termina la ejecución de este programa
            print('Ejecución terminada...')
            validar = True
        #Si se digita un número fuera del menú, no se podrá avanzar
        else:
            print('-----------------------------------------------------------')
            print('OPCIÓN NO VÁLIDA INTENTE DE NUEVO')
            validar = False
        
        problema7.complTiempo()

def opcion8():
    #Se establece la variable para el bucle
    validar = False
    #Bucle para validar el ingreso solo de palabras
    while validar != True:
        #Se pide al usuario que ingrese una cadena de texto
        print('----------------------------------------')
        palabra = input('Ingrese una palabra: ')
        #Si ingresa una cadena de texto
        if palabra.isalpha():
            #Sale del bucle con el cambio de valor de 'validar'
            validar = True
        #Caso contrario
        else:
            #Muestra al usuario que debe ingresar solo caracteres, y se repetirá el bucle
            print('----------------------------------------')
            print('SOLO DEBE INGRESAR CARACTERES. INTENTE DE NUEVO')
            validar = False
    #Se ejecuta la función de mostrar listas para mostrar los abecedarios
    problema8.mostrarListas()
    #Se asigna la nueva palabra a una nueva variable
    solucion = problema8.palabraInversa(palabra)
    #Se imprime la palabra inversa del ejercicio
    print('--------------------------------------------')
    print('La palabra inversa de',palabra,'es',solucion)
    print('--------------------------------------------')

def opcion10():
    #Conexion a la base de datos de Mongo DB
    cliente = MongoClient('mongodb+srv://diegop:diegop@cluster0.skonea2.mongodb.net/test')
    #Se define la DataBase donde se va a trabajar en este programa
    db = cliente['ProyectoMD']
    #Se define la colección en la cual se hara esta accion
    coleccion = db['Nombres y Edades']
    #Se ejcuta la funcion de registrar en Mongo DB
    problema10.registroMongoDB(coleccion)
    #Se crea una nueva variable para establecer un bucle
    validar = False
    #Mientras la variable sea diferente de True
    while validar != True:
        #Se mostrará el siguiente menú
        print('------------------------------------')
        print('¿Que acción desea realizar?')
        print('1. Registar un nuevo niño')
        print('2. Mostrar todos los nombres de cierta edad')
        print('3. Salir')
        print('------------------------------------')
        #El usuario deberá escoger una opción
        opcion = int(input('Seleccione una opción: '))
        #Se crea la condicion para que el dato ingresado sea numérico
        if opcion.isnumeric():
            #Si es numérico la variable cambia a True
            validar = True
        #Si no es numerico
        else:
            #Se dice al usuario que la entrada es no valida
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. SOLO DEBE INGRESAR NÚMEROS ENTEROS. INGRESE DE NUEVO')
            validar = False
        #Si la opción es 1
        if int(opcion) == 1:
            #Se hara el registro en la base de datos
            problema10.registroMongoDB(coleccion)
            validar = False
        #Si la opción es 2, se sacara los nombres y las edades respectivas
        elif int(opcion) == 2:
            #Con la funcion creada anteriormente
            problema10.sacarNombres(coleccion)
            validar = False
        #Si la opción es 3 se terminará la ejecucion
        elif int(opcion) == 3:
            print('Ejecución terminada...')
            validar = True
        #Si se ingresa cualquier otro número, se pedira nuevamente
        else:
            print('OPCIÓN NO VALIDA')
            validar = False

def opcion14():
    #Primero se ejecutará la funcion para crear palabras
    problema14.crearPalabras()

def opcion15():
    validar = False
    while validar != True:
        #Se pide al usuario que ingrese una cadena de texto
        print('===================================================')
        num = input('Ingrese un número de palabras a generar: ')
        #Si ingresa un numero
        if num.isnumeric():
            #Sale del bucle con el cambio de valor de 'validar'
            validar = True
        #Caso contrario
        else:
            #Muestra al usuario que debe ingresar solo numeros, y se repetirá el bucle
            print('----------------------------------------')
            print('SOLO DEBE INGRESAR NUMEROS ENTEROS. INTENTE DE NUEVO')
            validar = False
    #Se genera una primera letra para porceder al programa
    rand = random.choice(string.ascii_letters)
    #Condicion para tranformar a minuscula
    if rand.upper():
        #Si es mayuscula se transforma a minuscula
        rand = rand.lower()
        print('===================================================')
        #Se imprime la letra
        print('La letra generada es',rand)
    else:
        #Caso contrario solo se imprime la letra
        print('===================================================')
        print('La letra generada es',rand)
    #Se transforma el número a entero
    num = int(num)
    #Se ejecuta la funcion para el programa
    problema15.generarPalabra(num,rand)

def opcion16():
    #Se llama la primera funcion para determinar el número de palabras
    num = problema16.numPalabras()
    #Se ejecuta la función para el juego con las sílabas
    problema16.juegoSilabas(num)