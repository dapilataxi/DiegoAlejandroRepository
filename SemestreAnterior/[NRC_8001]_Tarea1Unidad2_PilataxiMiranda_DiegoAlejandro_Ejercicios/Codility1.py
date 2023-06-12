#Importamos las bibliotecas
import random 
import numpy
import big_o

def crearMatriz():
    """
    Función que creará la matriz que será objeto de evaluación para el ejercicio
    
    Parámetros:
    -----------------------------
    No tiene parámetros

    Retorna:
    -----------------------------
    Retorna la matriz creada por el usuario
    """
    #Creamos una matriz vacía para poder llenarla acorde la entrada de datos del usuario
    matriz = []
    #Se pide ingresar el numero de filas 
    filas = int(input('Ingrese el número de filas: '))
    #Se pide ingresar el numero de columnas
    columnas = int(input('Ingrese el número de columnas: '))
    #Bucle "for" para el rango de filas
    for i in range(filas):
        #Se añadira las columnas ingresadas por el usuario
        matriz.append([0] * columnas)
    #Bucle "for" para la creacion de columnas
    for j in range(filas):
        #Bucle para generar valores al azar dentro de la matriz
        for k in range(columnas):
            #Se reemplaza cada valor dentro de la matriz por un valor randominco dentro del rango establecido
            matriz[j][k] = random.randint(0,10)
    #Este Bucle es para que se imprima la matriz en formato de matriz
    for l in range(len(matriz)):
        #Por cada elemento se imprime las listas dentro de las listas creadas
        print(matriz[l])
    #Retorna la matriz
    return matriz

def solucion(matriz):
    """
    Función que dará la solución al ejercicio
    
    Parámetros:
    -----------------------------
    matriz: Lista transformada en matriz

    Retorna:
    -----------------------------
    Retorna el primer digito que no se repite
    """
    #Se crea una matriz usando la biblioteca
    matr = numpy.array(matriz)
    #Para el rango de la matriz en filas se crea un bucle
    for i in range(len(matriz)):
        #Para el rando de la matriz en columnas se crea un bucle
        for j in range(len(matriz)):
            #Condicion para el primer numero que no se repita
            if numpy.count_nonzero(matr == matriz[i][j]) == 1:
                #Retrona dicho digito no repetido
                return matriz[i][j]

#Funcion main donde se ejecuta todo el programa
if __name__ == '__main__':
    #Se asigna la creacion de la matriz a una variable
    matriz = crearMatriz()
    #Se asigna la solucion al problema a otra variable
    soluc = solucion(matriz)
    #Condiciones para la solucion
    if soluc == None:
        #Si ningun numero se repite, para que no imprima "None" imprimirá el siguiente mensaje
        print('-1. TODOS LOS NUMEROS SE REPITEN')
    #Caso contrario
    else:
        #Imprimirá el primer digito como lo especifica el programa
        print('El primer digito que no se repite es: ')
        print(soluc)
    #Declaracion para analizar la complejidad de timepo del programa
    for i in range(0,len(matriz)):
        #Se asigna la variable a la cual se va a analizar la complejidad
        variable = lambda a : matriz
        #Mediante la funcion Big-o se ingresa la función a ser analizada junto a su respectivo parámetro
        best,others = big_o.big_o(solucion,variable)
    #Se imprime el tiempo de ejecución
    print(best)