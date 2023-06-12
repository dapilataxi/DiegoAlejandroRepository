#Importo las librerias para calcular la complexity y para generar la cadena aleatoria.
import big_o
import sys
import string
import random

def generarCuponDescuento(prueba):
    """"
    Se crea la funcion para ofrecer por primer registro un cupon de descuento para ser ingresado despues.
  
    Parametros:
    -------------------
    Recibe la variable:
    str: prueba
    Correspondiente a una variable de prueba para poder calcular la complejidad de tiempo.

    Retorna:
    -------------------
    str = cupon 
    Correspondiente al cupon de descuento que se le ofrece al usuario por primer registro.
    """
    #Establezco que el cupon sera de 6 caracteres.
    tamaño_cupon = 6
    #Declaro mis variables para que el cupon pueda tener mayusculas y minusculas a traves del metodo string.ascii, ademas de numeros.
    minusculas = string.ascii_lowercase
    mayusculas = string.ascii_uppercase
    numeros = "012346789"
    #Concateno todos estos caracteres para el cupon al generarse de maneara aleatoria.
    caracteres_cupon = minusculas  + mayusculas + numeros
    #Inicializo el numero_registro en 0 para ofrecer el cupon solo en caso de que sea el primer registro del usuario.
    numero_registro = 0
    #Inicializo cupon para almacenar la cadena aleatoria generada.
    cupon = ""
    if (numero_registro == 0):
        #Con el ciclo for voy agregando caracter por caracter aleatoriamente y guardando en la variable cupon.
        for i in range(tamaño_cupon):
            cupon += random.SystemRandom().choice(caracteres_cupon)
        #Retorno la variable cupon ya con la cadena aleatoria generada.
        return cupon
 
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
    best, others = big_o.big_o(generarCuponDescuento, cadena_ejemplo)
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
    result = sys.getsizeof(generarCuponDescuento)
    print(result,'bytes')

#if main de nuestro programa donde solo ejecuto la funcion correspondiente.
if __name__ == '__main__':
    #Inicialo la variable prueba para poder calcular la complejidad de tiempo.
    prueba = ''
    print('Su cupon de descuento es',generarCuponDescuento(prueba),', no olvide guardarlo')
    complejidadTiempo()
    complejidadEspacio()

