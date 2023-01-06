def isfloat(num):
    """
    Función para validar el ingreso de un número de tipo flotante

    Parámetros:
    ----------------
    num: int
    Numero que se evaluará si es flotante o no
    ----------------
    Retorna:
    ----------------
    Retorna un valor flotante dependiendo el caso
    """
    try:
        #Si el valor es flotante devuelve el valor True
        float(num)
        return True
    #Caso contrario devuelve el valor False
    except ValueError:
        return False

def transformaCelsius():
    """
    Función para el ingreso de grados Celsius por parte del usuario

    Parámetros:
    ----------------
    No tiene parámetros

    ----------------
    Retorna:
    ----------------
    Retorna un valor flotante dependiendo el caso
    """
    #Se declara una variable con un valor booleano, para que se pueda cumplir de mejor manera el bucle siguiente
    validar = False
    #Se usa el bucle while, y se va a repetir hasta que la sentencia tenga un valor de "True"
    while validar != True:
        print('-----------------------------------------------------------')
        #Ingreso de los grados celsius que el usuario desea transformar
        celsius = input('Ingrese el valor en grados Celsius que desea transformar (°C): ')
        #Si el usuario ingresa un valor entero, validar adquiere el valor True
        if celsius.isnumeric():
            validar = True     
        #Si el usuario ingresa una valor flotante, validar adquiere el valor True 
        elif isfloat(celsius):
                validar = True    
        #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
        else:
            print('-----------------------------------------------------------')
            print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
            validar = False
    #Se transforma el valor en flotante
    celsius = float(celsius)
    #Se determina la operación para hacer la conversion de grados celsius a Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    print('-----------------------------------------------------------')
    #Se imprimen la conversión de grados Celsius a Fahrenheit
    print('Su conversion de Celsius a Fahrenheit es',fahrenheit,'°F')
    print('-----------------------------------------------------------')

def transformaFahrenheit():
    """
    Función para el ingreso de grados Fahrenheit por parte del usuario

    Parámetros:
    ----------------
    No tiene parámetros

    ----------------
    Retorna:
    ----------------
    Retorna un valor flotante dependiendo el caso
    """
    #Se declara una variable con un valor booleano, para que se pueda cumplir de mejor manera el bucle siguiente
    validar = False
    #Se usa el bucle while, y se va a repetir hasta que la sentencia tenga un valor de "True"
    while validar != True:
        print('-----------------------------------------------------------')
        #Ingreso de los grados fahrenheit que el usuario desea transformar
        fahrenheit = input('Ingrese el valor en grados Fahrenheit que desea transformar (°F): ')
        #Si el usuario ingresa un valor entero, validar adquiere el valor True
        if fahrenheit.isnumeric():
            validar = True     
        #Si el usuario ingresa una valor flotante, validar adquiere el valor True 
        elif isfloat(fahrenheit):
                validar = True    
        #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
        else:
            print('-----------------------------------------------------------')
            print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
            validar = False
    #Se transforma el valor en flotante
    fahrenheit = float(fahrenheit)
    #Se determina la operación para hacer la conversion de grados Fahrenheit a Celsius
    celsius = (fahrenheit - 32) * 5/9
    print('-----------------------------------------------------------')
    #Se imprimen la conversión de grados Fahrenheit a Celsius
    print('Su conversion de Fahrenheit a Celsius es',celsius,'°C')
    print('-----------------------------------------------------------')

#La función main establece que ahi se ejecutara el programa
if __name__ == '__main__':
    """
    Breve introducción para comenzar la ejecución del programa
    """
    print('-----------------------------------------------------------')
    print('BIENVENIDO A CONVERSOR DE PESO')
    print('\nDiego Alejandro Pilataxi Miranda')
    print('\nNRC: 8001')
    validar = False
    #Se establece un bucle para el menú que se creará para el progrmama
    while validar != True:
        """
        El menú consiste en que el usuario debe seleccionar si desea transformar de °C a °F o de °F a °C
        para esto se establecen las opciones que se muestran en las siguientes líneas
        """
        print('-----------------------------------------------------------')
        print('Conversiones a poder realizar:')
        print('1. Tranformar de °C a °F')
        print('2. Transformar de °F a °C')
        print('-----------------------------------------------------------')
        #El usuario debe seleccionar la conversión que desea hacer
        opcion = input('Seleccione la opción que desea transformar: ')
        #Presenta su validación para que el ingreso de opciones del menú sea solamente numeros enteros
        if opcion.isnumeric():
            #Si es un número entero, el bucle terminara
            validar = True     
        else:
            print('-----------------------------------------------------------')
            #Caso contrario el bucle se repetira hasta que el usuario ingrese un número entero que esté dentro de los límite.
            print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
            validar = False
    #Se transforma la elección del usuario en entero
    opcion = int(opcion)
    #Condición si la elección del usuario es 1
    if opcion == 1:
        #Se ejecutará la función que tranforma grados Celsius a Fahrenheit
        transformaCelsius()
    #Condición si la elección del usuario es 2
    elif opcion == 2:
        #Se ejecutará la función que tranforma grados Fahrenheit a Celsius
        transformaFahrenheit()
    #Si la opcion esta fuera de 1 o 2
    else:
        print('-----------------------------------------------------------')
        #Se muestr al usuario que la opcion no está disponible
        print('OPCIÓN NO DISPONIBLE.')
        print('-----------------------------------------------------------')