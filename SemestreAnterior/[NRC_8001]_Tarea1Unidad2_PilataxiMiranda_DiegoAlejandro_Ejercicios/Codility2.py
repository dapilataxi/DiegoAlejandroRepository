#Se importa la libreria Big-o para anlizar la complejidad de tiempo
import big_o

def solucion(S):
    """
    Función que dará la solucion al problema planteado
    
    Parámetros:
    -----------------------------
    S: Cadena de texto a ser ejecutada en el programa

    Retorna:
    -----------------------------
    Retorna el conteo desde el índice
    """
    #La longitud de la cadena se la asigna a una vriable para un mejor manejo
    conteo = len(S)
    #Se saca el residuo para determinar el índice de la mitad de la palabra
    residuo = conteo%2
    #Condicion si el residuo es 0
    if residuo != 0:
        #Se asigna una nueva variable para determinar el caracter del medio
        indice = int((conteo - 1)/2)
        #Se imprime la cantidad que hay antes del indice de la mitad
        nuevaCadena = S[:indice]
        #Retorna la cantidad de caracteres despues del indice de la mitad
        return len(nuevaCadena)
    ##Si el residuo no es 0
    else:
        #Se muestra al usuario que no existe indice intermedio
        print('No existe índice intermedio.')
        print('-1')

#Funcion main para que corra la funcion
if __name__ == '__main__':
    print('------------------------------------')
    #Se pide al usuario que ingrese una cadena de texto
    cadena = input('Ingrese una cadena de texto: ')
    print('------------------------------------')
    #Se asigna a una variable la solucion que sería el conteo desde el indice medio
    conteo = solucion(cadena)
    #Se muestra la respuesa al problema
    print('Desde el índice hay',conteo,'caracteres.')
    
    #Se asigna la variable a la cual se va a analizar la complejidad
    variable = lambda a : cadena
    #Mediante la funcion Big-o se ingresa la función a ser analizada junto a su respectivo parámetro
    best,others = big_o.big_o(solucion,variable)
    print('------------------------------------')
    #Se imprime el tiempo de ejecución
    print(best)
    print('------------------------------------')
