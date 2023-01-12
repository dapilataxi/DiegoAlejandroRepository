#Se importa las bibliotecas que se usará en el desarrollo del programa
import random
from timeit import default_timer

def solucion(A,B):
    """
    Función que dará la solución al ejercicio
    
    Parámetros:
    -----------------------------
    A: numero de letras 'a' que se debe imprimir

    B: numero de letras 'b' que se debe imprimir
    

    Retorna:
    -----------------------------
    Retorna la cadena de texto respuesta
    """
    #Se crea una lista para poder crear una cadena de texto aleatoria
    lista = []
    #Para el primer bucle en el rango de A
    for i in range(A):
        #Por cada A se agregara el numero 1 en la lista
        lista.append(1)
    #Bucle en el rango de B
    for i in range(B):
        #Por cada B se agrega el numero 2 en la lista
        lista.append(2)
        #Se mezcla la lista para que sea una cadena al azar
        random.shuffle(lista)
    #Bucle en el rango de la lista creada que contiene la dimension de la cadena
    for i in range(A+B):
        #Condicion para cada elemento "1" de la lista
        if lista[i] == 1:
            #Se reemplazara por el caracter 'a'
            lista[i] = 'a'
        #Condicion para cada elemento "2" de la lista
        elif lista[i] == 2:
            #Se reemplazara por el caracter 'b'
            lista[i] = 'b'
    #Se transforma la lista en cadena
    cadena = "".join(map(str, lista))
    #Se imprime la cadena de texto creada
    print(cadena)

    #Se crea una variable inicial con valor booleano
    valida = False

    #Se crea un bucle while que se repetira hasta que la variable sea diferente de True
    while valida != True:
        #Si dentro de la cadena creada se encuentra la repeticion que establece el ejercicio
        if ('aaa' in cadena) or ('bbb' in cadena):
            #Se transforma la cadena nuevamente en lista
            nuevaLista = list(cadena)
            #Se mezcla dicha lista
            random.shuffle(nuevaLista)
            #Se vuelve a transformar la lista en cadena
            cadena = "".join(map(str, nuevaLista))
            #Nueva mente se evalua si se repite ambas cadenas
            if ('aaa' in cadena) or ('bbb' in cadena):
                #Si se siguen repitiendo, se seguira repitiendo el proceso
                valida = False
            #Caso contrario se imprime la cadena solucion
            else:
                valida = True
                print(cadena) 
        #Si no se repite desde la primera cadena, esta se imprimira 
        else:
            valida = True
            print(cadena)

#En la fucnion main se ejecutara la corrida 
if __name__ == '__main__':
    #Se pide el ingreso de ambas variables que solicita el programa
    A = int(input('Ingrese un número de "A" : '))
    B = int(input('Ingrese un número de "B" : '))
    
    #Mediante la funcion default_timer se ingresa la función a ser analizada junto a su respectivo parámetro
    inicio = default_timer()
    #Se ejecuta la solución del problema con la función creada anteriormente
    solucion(A,B)
    fin = default_timer()
    print('------------------------------------')
    #Se imprime el tiempo de ejecución
    print(fin - inicio,'sec')
    print('------------------------------------')
    
