#Importo las librerias para calcular la complexity.
import big_o
import sys

def validarNombreYApellido(variables):
    """"
    Se crea la funcion para la validacion del nombre y apellido donde la primera letra de cada palabra sea mayuscula.
  
    Parametros:
    -------------------
    Recibe la variable:
    variables= []
    que incluira al nombre y apellido digitado por el usuario.
    Retorna:
    -------------------
    No retorna ningun valor.
    """
    #Mediante el metodo isupper() verifico la condicion de que la primera letra del nombre y apellido deben ser mayusculas.
    if(nombre[0].isupper() and apellido[0].isupper()):
        print("Datos correctos")
        pass
    #En caso de que el nombre o el apellido no empiece con mayusculas muestro el mensaje al usuario y hago la correcion mediante el metodo
    #title para que me muestre el primer caracter con mayusculas.
    else:
        print('El nombre y apellido del niño debe empezar con mayusculas')
        nombre_mayuscula = nombre.title()
        apellido_mayuscula = apellido.title()
        #Concateno el nombre y apellido ya con la primer letra en mayuscula para mostrarlo en pantalla.
        datos_mayuscula = nombre_mayuscula + " " + apellido_mayuscula
        print(datos_mayuscula)

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
    cadena_ejemplo = lambda example_variable: variables
    best, others = big_o.big_o(validarNombreYApellido, cadena_ejemplo)
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
    result = sys.getsizeof(validarNombreYApellido)
    print(result,'bytes')

#if main de nuestro programa donde solo ejecuto la funcion correspondiente.
if __name__ == '__main__':
    #Pido el nombre y apellido del niño ingresado por el papa.
    print('RECUERDE: \nSolo debe ingresar texto. \nEl nombre y apellido deben estar en mayusculas.')
    #Utilizo un ciclo while para validar que solo puede ingresar texto como lo pide el programa.
    while True:
        try:
            nombre = input('Ingrese el nombre del niño: ')
            apellido = input('Ingrese el apellido del niño: ')
            if(nombre.isalpha() and apellido.isalpha()):
                break    
            else:
                print('No son validos numeros ni caracteres especiales')
        except ValueError:
            print('Ingrese datos correctos :/')
    #Guardo las variables en una lista para poder mandar el parametro y calcular la complejidad de tiempo.
    variables = [nombre,apellido]
    validarNombreYApellido(variables)
    complejidadTiempo()
    complejidadEspacio()
