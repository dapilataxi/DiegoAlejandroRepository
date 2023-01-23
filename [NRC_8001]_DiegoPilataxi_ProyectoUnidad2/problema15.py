#Importamos las librerias que se usara
import string, random, sys
from timeit import default_timer

def generarPalabra(num,rand):
    """
    Función que será para generar palabras a ráiz de la última letra de una palabra anterior

    Parámetros:
    -------------------
    num: numero que se debrá ingresar para saber el numero de palabras que se quiere generar (int)

    Retorna:
    -------------------
    No retorna ningun valor
    """
    #Bucle para validar el ingreso de una palabra
    validar = False
    #El primer bucle se repetira hasta que se ingrese una palabra que empiece con la letra indicada
    while validar != True:
        #El segundo bucle valida el ingreso de solo caracteres
        while validar != True:
        #Se pide al usuario que ingrese una cadena de texto
            print('===================================================')
            palabra = input('Ingrese una palabra con la letra, ' + rand + ', que se generó: ')
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
        #Condición si el primer caracter es igual a la letra generada
        if rand == palabra[0]:
            print('===================================================')
            print('Correcto')
            #Se imprime el mensaje de correcto y se vanza en el programa
            validar = True
        else:
            #Caso contrario se le informa que la letra no consta en la palabra
            validar = False
            print('===================================================')
            print('La palabra no empieza con la letra dada')
    #Contador para el ingreso de palabras que selecciono el usuario
    contador = 0
    #Mientras el contador sea diferente al numero ingresado menos un valor
    while contador != num - 1:
        validar = False
        while validar != True:
        #Se pide al usuario que ingrese una cadena de texto
            print('===================================================')
            palabraNueva = input('Ingrese una palabra que empiece con el caracter final de la anterior: ')
            #Si ingresa una cadena de texto
            if palabraNueva.isalpha():
                #Sale del bucle con el cambio de valor de 'validar'
                validar = True
            #Caso contrario
            else:
                #Muestra al usuario que debe ingresar solo caracteres, y se repetirá el bucle
                print('----------------------------------------')
                print('SOLO DEBE INGRESAR CARACTERES. INTENTE DE NUEVO')
                validar = False
        #Si la primera letra de la nueva palabra es igual a la última de la anterior
        if palabraNueva[0] == palabra[len(palabra)-1]:
            #Se mostrará un mensaje de correcto
            print('===================================================')
            print('Correcto')
            palabra = palabraNueva
            #Aumentará el numero del contador
            contador = contador + 1
        #Caso contrario
        else:
            #Se informará al usuario que no coinciden ambos caracteres
            print('===================================================')
            print('La palabra ingresada no empieza con el último caracter de la anterior. Intente de nuevo')

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
    result = sys.getsizeof(generarPalabra)
    print (f"{result} bytes")
    print('------------------------------------')

#Funcion main donde se pondra a ejecutar la funcion
if __name__ == '__main__':
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
    generarPalabra(num,rand)
    #Se ejecuta la función para la complejidad de tiempo
    complTiempo()
    #Se ejecuta la funcion para la complejidad de espacio
    complEspacio()
