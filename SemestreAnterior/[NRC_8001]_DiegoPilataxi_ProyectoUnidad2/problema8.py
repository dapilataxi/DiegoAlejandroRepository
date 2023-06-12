#Importamos la librería
import string, big_o, sys

def mostrarListas():
    """
    Funcion creada para mostra ambas listas con el abecedario para tomar de referencia

    Parámetros:
    ----------------------
    No tiene parámetros

    Retorna:
    ---------------------
    No retorna ningun valor
    """
    #Se establece 2 lista vacias para almacenar el abecedario normal y el inverso
    lista = []
    lista1 = []
    #Funcion para generar el abecedario en una cadena
    abecedario = string.ascii_lowercase
    #El for almacenara cada letra en la primera lista creada
    for i in abecedario:
        lista.append(i)
    #Imprime la lista con el abecedario
    print(lista)
    #Este segundo for es para la creacion del abecedario inverso
    for j in reversed(range(len(abecedario))):
        #Se añade desde la primera lista pero en orden reverso
        lista1.append(abecedario[j])
    #Se imprimer el abecedario inverso
    print(lista1)

def palabraInversa(palabra):
    """
    Funcion creada para invertir las letras de una cadena con su respectiva posicion en el abecedario

    Parámetros:
    -----------------------
    palabra: str (cadena de texto que debe ingresar el usuario)

    Retorna:
    ----------------------
    No retorna ningun valor
    """
    #Se crea una primera lista para almacenar el abecedario
    lista = []
    #Se crea una segunda lista para almancenar el abecedario en inverso
    lista1 = []
    #Se crea una cadena de texto de abecedario
    abecedario = string.ascii_lowercase
    #Mediante el siguiente for se pone el abecedario en una lista
    for i in abecedario:
        lista.append(i)
    #Mediante el siguiente for se crea el abecedario en inversa en una lista
    for j in reversed(range(len(abecedario))):
        lista1.append(abecedario[j])
    #Se formará una nueva lista que contenga cada caracter de la palabra que deba ingresar el usuario
    lista2 = list(palabra)
    #Se compara la nueva lista creada
    for i in range(len(lista2)):
        #Si algún elemento de la lista con las letras de la palabra creada está en la lista del abecedario
        if lista2[i] in lista:
            #Se buscara en que posición de la lista del alfabeto está
            nuevoidice = lista.index(lista2[i])
            #Se reemplazara por la ubicacion que contenga en el abecedario inverso
            lista2[i] = lista1[nuevoidice]

    #Se transforma la lista a cadena
    nuevaPalabra = ''.join(lista2)
    #Se retorna la nueva palabra inversa
    return nuevaPalabra

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
    #Se establece una variable para ser evaluada 
    variable = lambda a: palabra
    #Mediante la libreria Big-O se analiza la funcion principal con la variable definida
    best,others = big_o.big_o(palabraInversa,variable)
    #Se imprime la complejidad de tiempo
    print(best)

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
    result = sys.getsizeof(palabraInversa)
    print (f"{result} bytes")
    print('------------------------------------')

#Funcion main donde se ejecutará el programa principal
if __name__ == '__main__':
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
    mostrarListas()
    #Se asigna la nueva palabra a una nueva variable
    solucion = palabraInversa(palabra)
    #Se imprime la palabra inversa del ejercicio
    print('--------------------------------------------')
    print('La palabra inversa de',palabra,'es',solucion)
    print('--------------------------------------------')
    #Se imprime la complejidad de tiempo
    complTiempo()
    #Se imprime la complejidad de espacio
    complEspacio()