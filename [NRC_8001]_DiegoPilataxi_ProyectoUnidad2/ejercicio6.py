#Importo las librerias para calcular la complexity y para comprobar elegir palabras aleatorias de la lista.
import big_o
import sys
from random import choice
import random

def ordenarPalabras(respuesta_niño):
    """"
    Se crea la funcion donde partiendo de una lista de palabras, cada una se desordenará aleatoriamente mostrándose así en pantalla, el niño debe 
    ordenar mentalmente los caracteres para ir formando palabras correctas correspondiente a la lista de palabras.
  
    Parametros:
    -------------------
    Recibe la variable:
    str: prueba
    Correspondiente a una variable de prueba para poder calcular la complejidad de tiempo.

    Retorna:
    -------------------
    No retorna ningun valor.
    """
    #En mi lista genero las palabras que se desordenaran aleatoriamente.
    lista_palabras = ['Murcielagos','Chocolates','Universidad','Perro','Guatemala','Estacionamiento','Carro']
    #Escojo una palabra aleatoria de la lista mediante el metodo choice().
    palabra_escogida = choice(lista_palabras)
    #Saco el tamaño de la palabra escogida para usarlo de parametro en la siguiente funcion.
    tamaño_palabra_escogida = len(palabra_escogida)
    #Desordeno aleatoriamente la palabra escogida mediante el metodo random.sample().
    desordenar_palabra = random.sample(palabra_escogida,tamaño_palabra_escogida)
    #Convierto en string la palabra ya desordenada para mostrarla en pantalla.
    palabra_desordenada = ''.join(desordenar_palabra)
    print('La palabra desordenada es la siguiente:',palabra_desordenada,'\nOrdene las letras y forme la palabra correcta.')

def complejidadTiempo():
    """"
    Se crea la funcion para el calculo de la complejidad de tiempo del algoritimo.
  
    Parametros:
    -------------------
    No recibe ninguna variable.

    Retorna:
    -------------------
    No retorna ninguna variable.
    """
    #Calculo de la complejidad de tiempo.
    cadena_ejemplo = lambda example_variable: respuesta_niño
    best, others = big_o.big_o(ordenarPalabras, cadena_ejemplo)
    print(best)

def complejidadEspacio():
    """"
    Se crea la funcion para el calculo de la complejidad de espacio del algoritimo.
  
    Parametros:
    -------------------
    No recibe ninguna variable.

    Retorna:
    -------------------
    No retorna ninguna variable.
    """
    #Calculo de la complejidad de espacio.
    result = sys.getsizeof(ordenarPalabras)
    print(result,'bytes')

#if main de nuestro programa donde solo ejecuto la funcion correspondiente.
if __name__ == '__main__':
    lista_palabras = ['Murcielagos','Chocolates','Universidad','Perro','Guatemala','Estacionamiento','Carro']
    print('No olvide que solo debe ingresar texto!')
    #Llamo a la funcion para que imprima la palabra desordenada.
    ordenarPalabras('')
    #Utilizo un ciclo while para validar que solo puede ingresar texto como lo pide el programa y que sea la respuesta correcta.
    while True:
        try:
            #Pido la respuesta del niño respecto a la palabra ordenada.
            respuesta_niño = input('Ingrese su respuesta: ')
            #Con el metodo .title() convierto la respuesta del niño en el formato correcto para que no importe si escribe en
            #mayuscula o minuscula.
            respuesta_mayuscula = respuesta_niño.title()
            #Comparo si la respuesta es la correcta para terminar el bucle.
            if(respuesta_mayuscula in lista_palabras):
                print('Correcto! ha acertado en ordenar la palabra',respuesta_mayuscula,'su respuesta es la correcta :D')
                break
            #Si no es correcta imprimo un mensaje de error y seguira ejecutandose el juego.
            else:
                print('Intente nuevamente :/, recuerde ademas de no escribir numeros ni caracteres especiales!')
        except ValueError:
            print('Ingrese datos correctos :/')
    ordenarPalabras(respuesta_niño)
    complejidadTiempo()
    complejidadEspacio()
