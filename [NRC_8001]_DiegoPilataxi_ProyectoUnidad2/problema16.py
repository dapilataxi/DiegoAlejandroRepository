#Importamos la librería pylabeador
import pylabeador, sys
from timeit import default_timer

def numPalabras():
    """
    Funcion creada para el numero de palabras que debe ingresar el usuario acorde a la dinamica del ejercicio

    Parámetros:
    --------------------
    No tiene parámetros de entrada

    Retorna:
    --------------------
    No retorna ningún valor
    """
    #Se crea una variable false para la creacion del bucle
    validar = False
    #Se crea un bucle para validar el ingreso de solo numeros enteros
    while validar != True:
        #Se pide el ingreso del numero de palabras al usuario
        num = input('Ingrese un número de palabras a generar: ')
        #Si el numero ingresado es numerico
        if num.isnumeric():
            #Se asigna el valor de True a la variable y terminaria este bucle
            validar = True
            return num
        #Caso contraio
        else:
            #Se le informa al usuario que el caracter ingresado no es numérico y debe ingresar de nuevo
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. SOLO DEBE INGRESAR NÚMEROS ENTEROS. INGRESE DE NUEVO')
            validar = False

def primeraPalabra():
    """
    Funcion creada para el ingreso de una primer palabra por parte del usuario

    Parámetros:
    ---------------------
    No tiene parametros de entrada

    Retorna:
    --------------------
    Retorna las sílabas de la palabra
    """
    #Define una variable para la validacion de la palabra que debe ingresar el usuario
    validar = False
    #Se crea el bucle para dicha validación
    while validar != True:
        #Se le pide al usuario que ingrese una palabra
        cadena = input('Ingrese una palabra: ')
        #Si la cadena es alfabetica
        if cadena.isalpha():
            #Validar adquiere el valor True y terminaría el bucle
            validar = True
        #Caso contrario
        else:
            #Se le dice al usuario que solo debe ingresar caracteres numéricos 
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. SOLO DEBE INGRESAR CARACTERES. INGRESE DE NUEVO')
            validar = False
    #Se define la variable sílabas en la cual se separara la palabra ingresada
    silabas = pylabeador.syllabify(cadena)
    #Se muestra la separación de las sílabas del usuairo
    print('Las sílabas generadas de su palabra son',silabas)
    #Se muestra el numero de silabas de la palabra
    print('Su palabra tiene',len(silabas),'sílabas')
    #Retorna las sílabas formadas de la palabra
    return silabas

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
    result = sys.getsizeof(juegoSilabas)
    print (f"{result} bytes")
    print('------------------------------------')

def juegoSilabas(num):
    """
    Funcion creada para la dinámica que hará el programa con sílabas

    Parámetros:
    -------------------
    num: int, numero de palabras que deberá ingresar el usuario

    Retorna:
    -------------------
    No retorna ninguna valor
    """
    #Se asigna a la variable sílabas lo que retorna la funcion creada anteriormente
    silabas = primeraPalabra()
    #Se inicia un contador para el bucle while que se pondrá a continuación
    contador = 0
    #Mientras el contador sea diferente del número ingresado por el usuario
    while contador != int(num):
        #Se asigna una nueva variable validar para un nuevo bucle
        validar = False
        #Se inicia el nuevo bucle para validar la palabra que debe ingresar el usuario
        while validar != True:
            #Se pide el ingreso de la nueva cadena al usuario
            nuevaCadena = input('Ingrese una palabra que contenga el mismo numero de silabas: ')
            #Si la nueva cadena ingresada es alfabética
            if nuevaCadena.isalpha():
                #Se asigna la variable True y se termina este bucle
                validar = True
            #Caso contrario
            else:
                #Se le informa al usuario que solo debe ingresar caracteres alfabéticos
                print('-----------------------------------------------------------')
                print('ENTRADA NO VÁLIDA. SOLO DEBE INGRESAR CARACTERES. INGRESE DE NUEVO')
                validar = False
        #Se separa en sílabas la nueva cadena
        silabas1 = pylabeador.syllabify(nuevaCadena)
        #Se hace la comparacion de las sílabas ingresadas con las anteriores
        if len(silabas) == len(silabas1):
            #Si el número de sílabas concuerda, se le dice al usuario que es correcto y las sílabas coinciden
            print('Número de sílabas coincide')
            #Se aumenta el contador en 1
            contador = contador + 1
        #Caso contrario
        else:
            #Se le dice al usuario que no coincide el número de sílabas
            print('La palabra ingresada no contiene el mismo número de sílabas. Intente de nuevo')

#Funcion main para la ejecucion del programa
if __name__ == '__main__':
    #Se llama la primera funcion para determinar el número de palabras
    num = numPalabras()
    #Se ejecuta la función para el juego con las sílabas
    juegoSilabas(num)
    #Se llama la función para determinar la complejidad de tiempo
    complTiempo()
    #Se llama la funcion para determinar la complejidad de espacio
    complEspacio()