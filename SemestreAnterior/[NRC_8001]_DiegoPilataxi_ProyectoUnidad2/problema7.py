#Importamos la librería pymongo para poder utilizar la base de datos
from pymongo import MongoClient
from timeit import default_timer
import sys

def eliminarNombres(coleccion):
    """
    Función para eliminar nombre de la base de datos

    Parámetros:
    ---------------
    coleccion: variable a hacer usada en referencia con la base de datos que será Mongo DB

    Retorna:
    ---------------
    No retorna ningún parámetro
    """
    #Se pide al usuario que ingrese el nombre y apellido del usuario para buscarlo en la base de datos
    print('------------------------------------')
    nombre1 = input('Ingrese el nombre del niños que quiere borrar: ')
    apellido1 = input('Ingrese el apellido del niño: ')
    #Se busca por el nombre y apellido estipulados para eliminarlos
    coleccion.delete_one({'Nombre y apellido':nombre1 + ' ' + apellido1})

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
    result = sys.getsizeof(eliminarNombres)
    print (f"{result} bytes")
    print('------------------------------------')

#Funcion main donde se ejecutara el programa principal
if __name__ == '__main__':
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
            eliminarNombres(coleccion)
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
    #Función para la complejidad de tiempo  
    complTiempo()
    #Funcion para la complejidad de espacio
    complEspacio()