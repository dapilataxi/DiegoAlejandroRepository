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

def transformaLibras():
    """
    Función para validar tranformar el ingreso de libras por parte del usuario

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
        #Ingreso de las libras que debe hacer el usuario por el teclado
        libras = input('Ingrese el valor en libras que desea transformar (lb): ')
        #Si el usuario ingresa un valor entero, validar adquiere el valor True
        if libras.isnumeric():
            validar = True     
        #Si el usuario ingresa una valor flotante, validar adquiere el valor True 
        elif isfloat(libras):
                validar = True    
        #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
        else:
            print('-----------------------------------------------------------')
            print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
            validar = False
    #Se transforma el valor en flotante
    libras = float(libras)
    #Se hace la operacion para tranformar a kilos
    kilos = libras * 0.453592
    #Se hace la operacion para tranformar a gramos
    gramos = libras * 453.592
    print('-----------------------------------------------------------')
    #Se imprimen ambos valores convertidos de libras, respectivamente
    print('Su conversion de libras a kilos es',kilos,'kg')
    print('-----------------------------------------------------------')
    print('Su conversion de libras a gramos es',gramos,'g')
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
    #Se ejecuta la funcion para la conversion de libras a kilos y gramos
    transformaLibras()