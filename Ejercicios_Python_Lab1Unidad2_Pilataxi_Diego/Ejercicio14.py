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

def transformaDolares():
    """
    Función para tranformar el ingreso de dolares por parte del usuario

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
        #Ingreso de la cantidad de dólares que debe hacer el usuario por el teclado
        dolar = input('Ingrese el valor en dólares que desea transformar ($): ')
        #Si el usuario ingresa un valor entero, validar adquiere el valor True
        if dolar.isnumeric():
            validar = True     
        #Si el usuario ingresa una valor flotante, validar adquiere el valor True 
        elif isfloat(dolar):
                validar = True    
        #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
        else:
            print('-----------------------------------------------------------')
            print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
            validar = False
    #Se transforma el valor en flotante
    dolar = float(dolar)
    #Se determina la operación para hacer la conversion de dolar a euro
    euro = dolar * 0.95
    #Se determina la operación para hacer la conversion de dolar a yen
    yen = dolar * 130.67
    print('-----------------------------------------------------------')
    #Se imprimen ambos valores convertidos de dolares, respectivamente
    print('Su conversion en Euros es €',euro)
    print('-----------------------------------------------------------')
    print('Su conversion en Yen es ¥',yen)
    print('-----------------------------------------------------------')

#La función main establece que ahi se ejecutara el programa
if __name__ == '__main__':
    """
    Breve introducción para comenzar la ejecución del programa
    """
    print('-----------------------------------------------------------')
    print('BIENVENIDO A CONVERSOR DE DÓLARES')
    print('\nDiego Alejandro Pilataxi Miranda')
    print('\nNRC: 8001')
    #Se ejecuta la funcion para la conversion de dolares a yen y euros
    transformaDolares()