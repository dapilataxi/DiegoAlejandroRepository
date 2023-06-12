#Importo las librerias para calcular la complexity.
import big_o
import sys

def validacionAñoElectivo(año_electivo):
    """"
    Se crea la funcion para la validación del año electivo mediante la escritura del mismo (validación de caracteres).
  
    Parametros:
    -------------------
    Recibe la variable:
    str = año_electivo

    Retorna:
    -------------------
    No retorna ningun valor.
    """
    #En mi lista genero los años electivos que puede estar el niño tanto en mayusculas como minusculas para evitar errores.
    años_electivos = ['Guarderia','Preescolar']
    #Comparo si el año electivo ingresado se encuentra dentro de los permitidos.
    if(año_electivo in años_electivos):
        print('El niño se encuentra en',año_electivo.title())
    else:
        print('Escriba un año electivo correcto, sea Guarderia o Preescolar')

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
    cadena_ejemplo = lambda example_variable: año_electivo_mayuscula
    best, others = big_o.big_o(validacionAñoElectivo, cadena_ejemplo)
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
    result = sys.getsizeof(validacionAñoElectivo)
    print(result,'bytes')

#if main de nuestro programa donde solo ejecuto la funcion correspondiente.
if __name__ == '__main__':
    print('RECUERDE: \nEl niño puede estar en Guarderia o Preescolar \nNo olvide que solo debe ingresar texto!')
    #Utilizo un ciclo while para validar que solo puede ingresar texto como lo pide el programa.
    while True:
        try:    
            año_electivo = input('Ingrese el año electivo del niño: ')
            año_electivo_mayuscula = año_electivo.title()
            if(año_electivo_mayuscula.isalpha()):
                break    
            else:
                print('No son validos numeros ni caracteres especiales')
        except ValueError:
            print('Ingrese datos correctos :/')            
    validacionAñoElectivo(año_electivo_mayuscula)
    complejidadTiempo()
    complejidadEspacio()
