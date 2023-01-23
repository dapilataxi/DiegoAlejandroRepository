#Importo las librerias para calcular la complexity y para comprobar elegir palabras aleatorias de la lista.
import big_o
import sys
from random import choice

def reconocerVocalesyConsonantes(prueba):
    """"
    Se crea la funcion donde partiendo de una lista de palabras, el niño debe reconocer cuáles caracteres son consonantes y vocales respectivamente.

    Parametros:
    -------------------
    Recibe la variable:
    str: prueba
    Correspondiente a una variable de prueba para poder calcular la complejidad de tiempo.

    Retorna:
    -------------------
    No retorna ningun valor.
    """
    #En mi lista genero las palabras que se le darán al niño.
    lista_palabras = ['Truenos','Sol','Lluvia','Lunes','Domingo','Cocodrilos','Helado','Estudiante','Escuela','Maestros']
    #Escojo una palabra aleatoria de la lista mediante el metodo choice().
    palabra_escogida = choice(lista_palabras)
    #Convierto en string la palabra para mostrarla en pantalla.
    palabra_escogida_str = ''.join(palabra_escogida)
    print('La palabra con la que debe trabajar es la siguiente:',palabra_escogida_str)
    #Saco el tamaño de la palabra_escogida_str para luego poder hallar el numero de consonantes.
    tamaño_palabra_escogida = len(palabra_escogida_str)
    #Inicializo el contador_vocales en 0 para ir aumentando en caso de que la palabra tenga vocales.
    contador_vocales = 0
    #Con el ciclo while me aseguro que las respuestas del niño sean datos numericos y se va a terminar hasta que llegue a la respuesta correcta.
    while True:
        try:
            #Pido la respuesta del niño respecto al numero de vocales y consonantes que contenga la palabra.
            print('Cuantas vocales tiene la palabra?:')
            numero_vocales = int(input())
            print('Cuantas consonantes tiene la palabra?:')
            numero_consonantes = int(input())
            #Mediante el ciclo for recorro la palabra_escogida_str para ir hayando las vocales que esten presentes.
            for i in palabra_escogida_str:
            #Utilizo el metodo .lower() para que exista inconveniente de que no cuente la  primer letra mayuscula con la que empieza la palabra 
            # aleatoria como vocal.
                if i.lower() in 'aeiou':
                #Aumento el contador_vocales las veces que vaya encontrando una vocal en la palabra.
                    contador_vocales+= 1
            #Aqui calculo el numero de consonantes presentes en la palabra, mediante la resta del tamaño de la palabra y el numero de vocales encontradas.
            consonantes = tamaño_palabra_escogida - contador_vocales
            #Con la condicion ya me aseguro de verificar que las respuestas del niño sean correctas o no.
            if(numero_vocales == contador_vocales and numero_consonantes == consonantes):
                print('Correcto! la palabra tiene',contador_vocales,'vocales','y',consonantes,'consonantes :D')
                break
            else:
                print('Parece que se ha equivocado en algo, intente nuevamente :)')
        except ValueError:
            print('Ingrese datos numericos!')
  
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
    best, others = big_o.big_o(reconocerVocalesyConsonantes, cadena_ejemplo)
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
    result = sys.getsizeof(reconocerVocalesyConsonantes)
    print(result,'bytes')

#if main de nuestro programa donde solo ejecuto la funcion correspondiente.
if __name__ == '__main__':
    #Inicialo la variable prueba para poder calcular la complejidad de tiempo.
    prueba = ''
    reconocerVocalesyConsonantes(prueba)
    complejidadTiempo()
    complejidadEspacio()

