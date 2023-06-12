import math
import big_o

def es_multiplo(numero, multiplo):
    """
    Función que dará los múltiplos de un número
    
    Parámetros:
    -----------------------------
    numero: número al cual se sacará sus múltiplos
    multiplo: Division exacta para el número dado

    Retorna:
    -----------------------------
    Retorna los multiplos de un numero
    """
    #Si el número dividido para el multiplo es igual a sero, es divisible para "numero"
    if numero % multiplo == 0:
        #Se retorna true
        return True
    #Caso contrario se retorna False
    else:
        return False

def solucion(numero):
    """
    Función que dará la solución al ejercicio
    
    Parámetros:
    -----------------------------
    numero: número al cual se sacará sus múltiplos
    

    Retorna:
    -----------------------------
    Retorna el resultado de K
    """
    #Se crea una lista vacia donde se van a guardar los numeros divisibles del numero ingresado
    lista = []
    #Bucle para hallar los numeros
    for i in range(1, numero+1):
        #Condición que sacará los múltiplos del número ingresado
        if es_multiplo(numero, i):
            #Cada número divisible se agregará a la lista creada
            lista.append(i)
    #Condicional para la lista creada
    if 1 in lista:
        #Se aplicara una formula en la cual la operacion para 1 es un error, además que 1 nunca será la respuesta
        lista.remove(1)
    #Se inicializa una posicion de la lista a la variable max
    max = lista[0];
    #Con el bucle "for" se buscará dentro de la lista
    for i in lista:
        #Además se hara otra operación con este segundo bucle
        for j in lista:
            #Se define la siguiente formula para la incógnita "K"
            k = math.log(j,2)
            #Una operación inversa establece la condición, que se guardará numeros con base 2
            if i**(1/k) == 2:
                #Condicional para agregar el número con el exponente mas alto
                if i > max:
                    #Se asigna el exponente a una variable
                    max = i
    #Se saca el resultado de K con la siguiente formula
    resultado = math.log(max,2)
    #Retorna el valor de "K"
    return resultado

#Función main donde correra la resolción del ejercicio
if __name__ == '__main__':
    #Se le pide al usuario que ingrese el número
    numero = int(input('Ingrese un número: '))
    print('Se buscara la potencia "K" de 2 más alta para',numero)
    #Se asigna la respuesta que brinda la funcion creada a una variable
    resultado = solucion(numero)
    #Se imprime el resultado del ejercicio
    print('La respusta de K es',resultado)

    #Se asigna la variable a ser evaluada en la funcion
    variable = lambda a: numero
    #Se asigna la funcion Big-O a la funcion a ser evaluada y la variable creada anteriormente
    best,others = big_o.big_o(solucion,variable)
    print('------------------------------------')
    #Se imprime la complejidad de tiempo del ejercicio
    print(best)
    print('------------------------------------')