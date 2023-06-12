#Importo las librerias para calcular la complexity y para comprobar la igualdad de listas en la respuesta.
import big_o
import sys
import random
from collections import Counter

def nombrarAnimales(prueba):
    """"
    Se crea la funcion donde a partir de una lista de palabras dadas el niño debe escribir solo los que correspondan animales.
  
    Parametros:
    -------------------
    Recibe la variable:
    str: prueba
    Correspondiente a una variable de prueba para poder calcular la complejidad de tiempo.

    Retorna:
    -------------------
    No retorna ningun valor.
    """
    #En mi lista genero las palabras que se daran al niño.
    lista_palabras = ['Casa','Mesa','Silla','Computadora','Celular','Reloj','Collar','Planta','Arbol','Arbusto','Oso','Leon','Delfin','Tigre',
    'Elefante','Loro','Gato','Conejo']
    #Con el metodo random.shuffle() desordeno aleatoriamente la lista de palabras dadas al niño. 
    random.shuffle(lista_palabras,random.random)
    #Convierto la lista en strings mediante el metodo .join() con un - y espacio para que sea mas estetico.
    str_palabras = " - ".join(lista_palabras)
    print('Las palabras son las siguientes:\n',str_palabras)
    print('De las siguientes palabras escriba las que solo correspondan a animales:')
    #Genero la lista de animales que corresponde a las respuestas que debe escribir el niño.
    lista_animales = ['Oso','Leon','Delfin','Tigre','Elefante','Loro','Gato','Conejo']
    #Inicializo la variables respuestas_niño para ir agregando lo que va escribiendo.
    respuestas_niño = []
    print('-----PISTA: Son 8 animales en total-----')
    tamaño_lista_animales = len(lista_animales)
    #A partir del tamaño de lista_animales dentro de mi ciclo for voy guardando las respuestas del niño agregandolas a la lista respuestas_niño 
    #mediante el metodo append().
    for i in range(0,tamaño_lista_animales):
        #Con el ciclo while me aseguro que las respuestas ingresadas sean caracteres.
        while True:
            try:
                print('Animal',i+1,":")
                animales = input()
                if(animales.isalpha()):
                    #Transformo las respuestas del niño en formato de titulo mediante el metodo .title() para que asi no existan errores si escribe las 
                    #respuestas en mayusculas o minusculas.
                    datos_mayusculas = animales.title()
                    #Voy agregando las respuestas del niño mediante el metodo .append().
                    respuestas_niño.append(datos_mayusculas)
                    break
                    
                else:
                    print('Recuerde ingresar solo texto')
            except ValueError:
                print('Ingrese datos correctos :/')
    if(Counter(respuestas_niño) == Counter(lista_animales)):
        print('Correcto! ha acertado en encontrar los animales :D')
    else:
        print('Parece que su respuesta no es del todo correcta, vuelva a intentar :(')

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
    cadena_ejemplo = lambda example_variable: prueba
    best, others = big_o.big_o(nombrarAnimales, cadena_ejemplo)
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
    result = sys.getsizeof(nombrarAnimales)
    print(result,'bytes')

#if main de nuestro programa donde solo ejecuto la funcion correspondiente.
if __name__ == '__main__':
    #Inicialo la variable prueba para poder calcular la complejidad de tiempo.
    prueba = ''
    nombrarAnimales(prueba)
    #complejidadTiempo()
    complejidadEspacio()



