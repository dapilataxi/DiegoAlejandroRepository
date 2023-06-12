def leerNumeroInicio():
    """
    Función que leera la cantidad de números que el usuario desea sumar.

    Parámetros:
    ----------------
    No tiene parámetros
    ----------------
    Retorna:
    ----------------
    Retorna el valor ingresado como tipo int
    """
    validar = False #Se crea una variable con valor booleano
    #Bucle while que no se romperá hasta que validar sea False
    while validar != True:
        print('-----------------------------------------------------------')
        #Se pide al usuario el ingreso de un número por teclado
        num = input('Ingrese el número de elementos que desea operar: ')
        #Si el número ingresado en entero
        if num.isnumeric():
            #La variable validar adquiere el valor True y se rompe el bucle
            validar = True       
        #Si no es un numero entero
        else:
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. SOLO DEBE INGRESAR NÚMEROS ENTEROS. INGRESE DE NUEVO')
            #La variable validar adquiere el valor False y no se rompe el bucle
            validar = False
    #Para terminar se retorna el valor ingresado como tipo entero
    return int(num)

def operacion(num):
    """
    Función principal que realiza el objetivo principal del programa, el cual es sumar una operacion sucesivamente, este apartado ayuda a que se realice
    la acometida del programa.
    -------------------
    Parámetros:
    -------------------
    num: int
    Variable que denota la cantidad de numeros que el usuario quiere sumar entre sí
    -------------------
    Retorna:
    -------------------
    No retorna ningún valor
    """
    numerosSumar = num #Se asigna el numero de numeros a sumar a otra nueva variable
    #Se crea una lista vacia donde se creara la serie de números a sumar.
    lista = []
    #Se crea un bucle for para crear una lista con la longitud de los elementos que el usuario desea sumar
    for i in range(numerosSumar):
        #Con "variable" se crean lista genericas en orden progrsivo para hacer referencia solo al número de elementos a sumar
        variable = i + 1
        lista.append(variable)
        i = i+1
    """
    Este bucle for establece un ingreso de datos, que se añadirán a una lista, hasta que la longitud de la lista
    sea igual a la cantidad de números que el usario quiera sumar
    """
    for i in range(len(lista)):
        #Se declara una variable con un valor booleano, para que se pueda cumplir de mejor manera el bucle siguiente
        validar = False
        #Se usa el bucle while, y se va a repetir hasta que la sentencia tenga un valor de "True"
        while validar != True:
            print('-----------------------------------------------------------')
            #Se pide ingresar el primer numero que es la base de a expresion
            numBase = input('Ingrese la base (x): ')
            #Si el usuario ingresa un valor entero, validar adquiere el valor True, y se termina el bucle
            if numBase.isnumeric():
                validar = True     
            #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
            else:
                print('-----------------------------------------------------------')
                print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
                validar = False
        validar = False
        #Se usa este bucle para el ingreso correcto del segundo termino de la expresion
        while validar != True:
            print('-----------------------------------------------------------')
            #Se pide ingresar el segundo numero que es el exponente de la expresion
            numExponente = input('Ingrese el exponente (y): ')
            #Si el usuario ingresa un valor entero, validar adquiere el valor true y se termina el bucle
            if numExponente.isnumeric():
                validar = True     
            #Si el usuario ingresa una cadena validar mantendra el valor de False, y empezará de nuevo este bucle secundario.
            else:
                print('-----------------------------------------------------------')
                print('NO PUEDE INGRESAR CARACTERES. SOLO NUMEROS')
                validar = False
        #Se transforma ambas variables a numeros enteros
        numBase = int(numBase)
        numExponente = int(numExponente)
        #Se añade a la lista creada la operación realizada que expone el ejercicio
        lista[i] = numBase ** numExponente
    #Se defina la variable suma, para realizar la operacion
    suma = 0
    #Este bucle for se lo usara para sumar todos los elementos de la nueva lista, que contienen los número que el usario va a sumar
    for i in range(len(lista)):
        #Se establece que todos los elementos de la nueva lista se transformen a flotantes, para poder operarlos
        lista[i] = float(lista[i])
        #Se ejecuta la suma entre cada elemento durante el bucle
        suma = suma + lista[i]
    #Bloque que imprimirá la SUMA TOTAL DE LA OPERACION
    print('-----------------------------------------------------------')
    print('LA SUMA TOTAL ES:',suma)
    print('-----------------------------------------------------------')

#La funcion principal main establece el proceso a ejecutar
if __name__ == '__main__':
    """
    Breve introducción para comenzar la ejecución del programa
    """
    print('-----------------------------------------------------------')
    print('BIENVENIDO A SUMA SUCESIVA DEL MODELO y = x**y')
    print('\nDiego Alejandro Pilataxi Miranda')
    print('\nNRC: 8001')
    #Se llama a la funcion leerNumeroInicio para que el usuario ingrese el número de elementos que quiere sumar
    num = leerNumeroInicio()
    #Se llama a la función operacion con el número ingresado y se ejecuta la suma efectuada de la expresion realizada
    operacion(num)