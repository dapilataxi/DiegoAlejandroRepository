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

def transformaCentimetros():
    """
    Función para tranformar el ingreso de centímetros por parte del usuario

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
        #Ingreso una cantidad en centimetros que debe hacer el usuario por el teclado
        cm = input('Ingrese el valor en centímetros que desea transformar (cm): ')
        #Si el usuario ingresa un valor entero, validar adquiere el valor True
        if cm.isnumeric():
            validar = True     
        #Si el usuario ingresa una valor flotante, validar adquiere el valor True 
        elif isfloat(cm):
                validar = True    
        #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
        else:
            print('-----------------------------------------------------------')
            print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
            validar = False
    #Se transforma el valor en flotante
    cm = float(cm)
    #Se determina la operación para hacer la conversion de centimetros a metros
    m = cm * 0.01
    #Se determina la operación para hacer la conversion de centimetros a kilometros
    km = cm * 0.00001
    print('-----------------------------------------------------------')
    #Se imprimen ambos valores convertidos de centimetros, respectivamente
    print('Su conversion de centímetros a metros es',m,'m')
    print('-----------------------------------------------------------')
    print('Su conversion de centímetros a kilómetros es',km,'km')
    print('-----------------------------------------------------------')

#La función main establece que ahi se ejecutara el programa
if __name__ == '__main__':
    """
    Breve introducción para comenzar la ejecución del programa
    """
    print('-----------------------------------------------------------')
    print('BIENVENIDO A CONVERSOR DE UNIDADES')
    print('\nDiego Alejandro Pilataxi Miranda')
    print('\nNRC: 8001')
    #Se ejecuta la funcion para la conversion de centimetros a kilometros y metros
    transformaCentimetros()