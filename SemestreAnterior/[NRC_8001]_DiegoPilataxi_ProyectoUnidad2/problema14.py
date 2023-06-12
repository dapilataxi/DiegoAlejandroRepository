#Se importa las librerias a utilizar en este programa
import string, random, sys
from timeit import default_timer

def crearPalabras():
    """
    Funcion que está destinada para que el usuario pueda crear palabras a partir de ciertas letras
    
    Parámetros:
    ---------------------
    No tiene parámetros

    Retorna:
    ---------------------
    No retorna ningun valor
    """
    #Se crea una lista vacia
    lista = []
    #For para crear letras randómicas
    for i in range(3):
        #Función que creara las letras
        rand = random.choice(string.ascii_letters)
        #Si la letra sale Mayúscula
        if rand.upper():
            #Se la transforma a minuscula
            rand = rand.lower()
            #Se agrega a una lista
            lista.append(rand)
        else:
            #Caso contrario solo se agrega a la lista
            lista.append(rand)
    #Se mostrará un mensaje con las letras que el usuario debe incluir en su palabra
    print('------------------------------------')
    print('Genere una palabra que incluya TODAS las letras siguientes',lista)
    #Se asigna las letras aleatorias en ciertas variables
    for i in range(len(lista)):
        b = lista[i-2]
        c = lista[i-1]
        d = lista[i]
    #Variable creada para iniciar un bucle
    validar = False
    #El bucle se repetirá hasta que la sentecia sea True 
    while validar != True:
        while validar != True:
            #Se pide al usuario que ingrese una cadena de texto
            print('----------------------------------------')
            palabra = input('Ingrese dicha palabra: ')
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
        #Condicion para establecer que las 3 letras generadas estén incluidas en la palabra
        if (b in palabra) and (c in palabra) and (d in palabra):
            #De ser así se muestra el mensaje que las letras están incluida
            print('------------------------------------')
            print('Todas las letras están incluidas')
            validar = True
        #Caso contrario
        else:
            #Se le muestra al usuario que no están incluidas todas las letras
            print('------------------------------------')
            print('No todas las letras están incluidas')
            validar = False

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
    result = sys.getsizeof(crearPalabras)
    print (f"{result} bytes")
    print('------------------------------------')

#Funcion main donde se ejecutara el programa
if __name__ == '__main__':
    #Primero se ejecutará la funcion para crear palabras
    crearPalabras()
    #Posteriormente la funcion creada para la complejidad de tiempo
    complTiempo()
    #Se llama a la función para determinar la complejidad de espacio
    complEspacio()