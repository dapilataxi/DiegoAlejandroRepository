#Importamos py mongo para poder conectar a la base de datos el programa
from pymongo import MongoClient
from timeit import default_timer
import sys
def registroMongoDB(coleccion):
    """
    Funcion crada para registrar información en la base de datos

    Parámetros:
    ----------------------
    coleccion: Parámetro asociado a la base de datos de Mongo DB

    Retorna:
    ----------------------
    No retorna ningun valor
    """
    #Se pide al usuario el ingreso de los 3 dato siguientes
    print('------------------------------------')
    nombre = input('Ingrese un nombre: ')
    apellido = input('Ingrese el apellido: ')
    edad = int(input('Ingrese la edad: '))
    #Se asigna a una coleccion, para la cración de un nuevo documento 
    coleccion.insert_one({'Nombre y apellido':nombre + ' ' + apellido,'Edad':edad})
    print('------------------------------------')
    #Mensaje de registro con exito
    print('Registro exitoso')

def sacarNombres(coleccion):
    """"
    Funcion designada para sacar los nombres de cierta edad que ingrese el usuario

    Parámetros:
    ----------------------
    coleccion: Parámetro asociado a la base de datos de Mongo DB

    Retorna:
    ----------------------
    No retorna ningun valor
    """
    #Se pide al usuario que ingrese un número que corresponde a la edad que quiere mostrar
    validar = False
    while validar != True:
        print('------------------------------------')
        n = input('Ingrese la edad de los niños que quiere mostrar: ')
        #Se crea la condicion para que el dato ingresado sea numérico
        if n.isnumeric():
            #Si es numérico la variable cambia a True
            validar = True
        #Si no es numerico
        else:
            #Se dice al usuario que la entrada es no valida
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. SOLO DEBE INGRESAR NÚMEROS ENTEROS. INGRESE DE NUEVO')
            validar = False
    n = int(n)
    #Para cada i que se presente en la colección designada
    print('===============================================')
    print("{:30} {:20}".format("Nombre y apellido","Edad"))
    print('===============================================')
    for i in coleccion.find({'Edad':n}).limit(10):
        print("{:<30} {:,.0f}".format(i['Nombre y apellido'],i['Edad']))

def complTiempo():
    """
    Función para calcular la complejidad de tiempo

    Parámetros:
    ----------------
    No tiene parámetros

    Retorna:
    ---------------
    No retorna ningun valor
    """
    #Mediante la funcion default_timer se ingresa la función a ser analizada junto a su respectivo parámetro
    inicio = default_timer()
    #Se ejecuta la funcion
    fin = default_timer()
    print('------------------------------------')
    #Se imprime el tiempo de ejecución
    print(fin - inicio,'sec')
    print('------------------------------------')

def complEspacio():
    """
    Función para determinar la complejidad de espacio del programa

    Parámetros:
    -------------------
    No tiene parámetros

    Retorna:
    -------------------
    No retorna ningún valor
    """
    result = sys.getsizeof(registroMongoDB)
    print (result,'bytes')
    print('------------------------------------')

#Funcion main donde se pondra a ejecutar el programa
if __name__ == '__main__':
    #Conexion a la base de datos de Mongo DB
    cliente = MongoClient('mongodb+srv://diegop:diegop@cluster0.skonea2.mongodb.net/test')
    #Se define la DataBase donde se va a trabajar en este programa
    db = cliente['ProyectoMD']
    #Se define la colección en la cual se hara esta accion
    coleccion = db['Nombres y Edades']
    #Se ejcuta la funcion de registrar en Mongo DB
    registroMongoDB(coleccion)
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
        opcion = input('Seleccione una opción: ')
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
            registroMongoDB(coleccion)
            validar = False
        #Si la opción es 2, se sacara los nombres y las edades respectivas
        elif int(opcion) == 2:
            #Con la funcion creada anteriormente
            sacarNombres(coleccion)
            validar = False
        #Si la opción es 3 se terminará la ejecucion
        elif int(opcion) == 3:
            print('Ejecución terminada...')
            validar = True
        #Si se ingresa cualquier otro número, se pedira nuevamente
        else:
            print('OPCIÓN NO VALIDA')
            validar = False
    #Función para calcular la complejidad de tiempo
    complTiempo()
    #Funcion para calcular la complejidad de espacio
    complEspacio()