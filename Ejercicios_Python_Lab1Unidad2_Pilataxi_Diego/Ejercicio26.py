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

def calcularAngulo():
    """
    Función para el ingreso de los grados de los 2 lados de un triángulo

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
        #Ingreso del primer ángulo del triangulo
        angulo1 = input('Ingrese el primer ángulo de su triángulo: ')
        #Si el usuario ingresa un valor entero, validar adquiere el valor True
        if angulo1.isnumeric():
            validar = True     
        #Si el usuario ingresa una valor flotante, validar adquiere el valor True 
        elif isfloat(angulo1):
                validar = True    
        #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
        else:
            print('-----------------------------------------------------------')
            print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
            validar = False
    #Se declara nuevamente esta variable para establecer un segundo bulce para el ingreso de otro dato
    validar = False
    #Se usa el bucle while, y se va a repetir hasta que la sentencia tenga un valor de "True"
    while validar != True:
        print('-----------------------------------------------------------')
        #Ingreso del segundo ángulo del triangulo
        angulo2 = input('Ingrese el segundo ángulo de su triángulo: ')
        #Si el usuario ingresa un valor entero, validar adquiere el valor True
        if angulo2.isnumeric():
            validar = True     
        #Si el usuario ingresa una valor flotante, validar adquiere el valor True 
        elif isfloat(angulo2):
                validar = True    
        #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
        else:
            print('-----------------------------------------------------------')
            print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
            validar = False
    #Se transforman ambos ángulos en valores de tipo flotante
    angulo1 = float(angulo1)
    angulo2 = float(angulo2)
    #Se establece una operación para hallar el tercer ángulo del triángulo
    angulo3 = 180 - angulo1 - angulo2
    """
    Se crearon condicionales para establecer el tipo de tirnagulo que se genera cuando el usuario ingresa los
    dos ángulos requeridos para el ejercicio
    """
    #Si al ingresar datos, se genera que los 3 ángulos son iguales.
    if (angulo1 == angulo2) and (angulo2 == angulo3):
        print('-----------------------------------------------------------')
        #Se imprime el valor del tercer ángulo y se munestra el tipo de triángulo que tiene 3 lados iguales
        print('El tercer ángulo mide',angulo3)
        print('\nSU TRIÁNGULO ES UN TRIÁNGULO EQUILÁTERO')
        print('-----------------------------------------------------------')
    #Si al ingresar datos, se genera que los 2 ángulos son iguales.
    elif (angulo1 == angulo2) or (angulo1 == angulo3) or (angulo2 == angulo3):
        print('-----------------------------------------------------------')
        #Se imprime el valor del tercer ángulo y se munestra el tipo de triángulo que tiene 2 lados iguales
        print('El tercer ángulo mide',angulo3)
        print('\nSU TRIÁNGULO ES UN TRIÁNGULO ISÓSCELES')
        print('-----------------------------------------------------------')
    #Esta condición es si el usuario ingres angulos mayores o iguales a 180
    elif (angulo1 >= 180) or (angulo2 >= 180):
        print('-----------------------------------------------------------')
        #Se imprime un mensaje que no puede ingresar un angulo mayor a 180°
        print('NO PUEDE INGRESAR UN ANGULO SUPERIOR O IGUAL A 180°')
        print('-----------------------------------------------------------')
    #Si no es ninguno de esos casos
    else:
        print('-----------------------------------------------------------')
        #El usuario ingreso angulos diferentes y se muestra la medida del tercer angulo y el tipo de triangulo
        print('El tercer ángulo mide',angulo3)
        print('\nSU TRIÁNGULO ES UN TRIÁNGULO ESCALENO')
        print('-----------------------------------------------------------')

#La función main establece que ahi se ejecutara el programa
if __name__ == '__main__':
    """
    Breve introducción para comenzar la ejecución del programa
    """
    print('-----------------------------------------------------------')
    print('BIENVENIDO A CALCULAR EL ÚLTIMO ÁNGULO DE TU TRIÁNGULO')
    print('\nDiego Alejandro Pilataxi Miranda')
    print('\nNRC: 8001')
    #Se ejecuta la funcion para calculat el tercer ángulo de un triángulo
    calcularAngulo()