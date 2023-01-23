#Importamos la librería para calcular la complejidad de tiempo
import timeit, sys

def  validarNumero():
    """
    Función creada para la validación de un número telefónico
    
    Parámetros:
    ----------------------
    No tiene parámetros

    Retorna
    ---------------------
    No retorna ningún valor
    """
    #Creamos una variable para poder ejecutar un bucle en la funcion
    validar = False
    #Se establece el bucle while que se repetirá hasta que validar sea verdadero
    while validar != True:
        #Se pide ingresar el número telefónico
        print('-----------------------------------------------------------')
        numero = input('Ingrese un número telefónico: ')
        #Validación para que el usuario solo ingrese números
        if numero.isnumeric():
            #Si lo ingresa, la sentencia dejara de repetirse
            validar = True
            #Se establece una nueva condición, el usuario debe ingresar obligatoriamente 10 dígitos, caso contrario no avanzará el programa
            if len(numero) == 10:
                #De ser así la sentencia se hará True
                validar = True
                #Última condición para que el número de teléfono empiece por 0, ya que es un registro de ecuador
                if numero[0] == '0':
                    #Se asigna el valor de True, y termina la ejecución
                    validar = True
                #Caso contrario
                else:
                    #Se le dice al usuario que el primer digito no empieza por 0 y no es un numero válido en Ecuador
                    print('-----------------------------------------------------------')
                    print('EL PRIMER DÍGITO DEBE EMPEZAR POR 0 PARA SER VÁLIDO EN ECUADOR')
                    #La variable validar adquiere un valor de False
                    validar = False
            #Si el número no tiene 10 dígitos
            else:
                #Se le dice al usuario que el número ingresado debe tener 10 dígitos
                print('-----------------------------------------------------------')
                print('EL NÚMERO INGRESADO DEBE SER DE 10 DÍGITOS')
                #Se asigna el variable False a la variable designada
                validar = False
        #Si el usuario no ingresa números
        else:
            #Se le pide ingresar de nuevo porque no debe ingresar caracteres
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. SOLO DEBE INGRESAR NÚMEROS ENTEROS. INGRESE DE NUEVO')
            #Se asigna el valor False
            validar = False

def complTiempo():
    """
    Función para determinar la complejidad de tiempo del programa

    Parámetros:
    -------------------
    No tiene parámetros

    Retorna:
    -------------------
    No retorna ningún valor
    """
    #Mediante la funcion default_timer se ingresa la función a ser analizada junto a su respectivo parámetro
    inicio = timeit.default_timer()
    #Se ejecuta la funcion
    fin = timeit.default_timer()
    print('------------------------------------')
    #Se imprime el tiempo de ejecución
    print(fin - inicio,'sec')
    print('------------------------------------')

def complEspacio():
    """
    Función para determinar la complejidad de espacio del programa

    Parámetros:
    -------------------
    No tiene parámetros

    Retorna:
    -------------------
    No retorna ningún valor
    """
    result = sys.getsizeof(validarNumero)
    print (result,'bytes')

#Función para ejecutar el programa
if __name__ == '__main__':
    #Se llama a la funcion  para que se ejecute
    validarNumero()
    #Se presenta un mensaje de número válido 
    print('============================')
    print('NUMERO ACEPTADO')
    print('============================')
    #Ejecutamos la función para la complejidad de tiempo
    complTiempo()
    complEspacio()
