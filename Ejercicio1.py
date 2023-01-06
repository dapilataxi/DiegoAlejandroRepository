def leerValorhoras():
    """
    Función que leera la cantidad de horas trabajadas en el día.

    Parámetros:
    ----------------
    No tiene parámetros

    Retorna:
    ----------------
    Retorna el valor ingresado como tipo int
    """
    validar = False #Se crea un varibale con valor booleano
    #Bucle while que no se romperá hasta que validar sea False
    while validar != True:
        print('-----------------------------------------------------------')
        #Se pide al usuario el ingreso de un número por teclado que representa al numero de horas trabajadas
        num = input('Ingrese el número de horas trabajadas al día: ')
        #Si el número ingresado en entero
        if num.isnumeric():
            #La variable validar adquiere el valor True y se rompe el bucle
            validar = True
            # Se establece el valor int a la variable ingresada para un codicional
            num = int(num)
            #Si es mayor a 24 se ejecutara una accion
            if num > 24:
                #Primero se establece el valor False y se reinicia el bucle
                validar = False
                print('-----------------------------------------------------------')
                #Se muestra el mensaje que no puede ingresar mas de 24 
                print('UN DIA SOLO TIENE 24 HORAS')      
            else:
                validar = True
        #Si no es un número entero
        else:
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA')
            #La variable validar adquiere el valor False y no se rompe el bucle
            validar = False
    #Para terminar se retorna el valor ingresado como tipo entero
    return int(num)

def leerValorDias():
    """
    Función que leera el número de días trabajados.

    Parámetros:
    ----------------
    No tiene parámetros

    Retorna:
    ----------------
    Retorna el valor ingresado como tipo int
    """
    validar = False #Se crea un varibale con valor booleano
    #Bucle while que no se romperá hasta que validar sea False
    while validar != True:
        print('-----------------------------------------------------------')
        #Se pide al usuario el ingreso de un número por teclado que representa al numero de dias trabajados
        num = input('Ingrese el número de días trabajados: ')
        #Si el número ingresado en entero
        if num.isnumeric():
            #La variable validar adquiere el valor True y se rompe el bucle
            validar = True       
        #Si no es un número entero
        else:
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA')
            #La variable validar adquiere el valor False y no se rompe el bucle
            validar = False
    #Para terminar se retorna el valor ingresado como tipo entero
    return int(num)

def leerValorCosto():
    """
    Función que leera el valor de costo por hora que genera.

    Parámetros:
    ----------------
    No tiene parámetros

    Retorna:
    ----------------
    Retorna el valor ingresado como tipo int
    """
    validar = False #Se crea un varibale con valor booleano
    #Bucle while que no se romperá hasta que validar sea False
    while validar != True:
        print('-----------------------------------------------------------')
        #Se pide al usuario el ingreso de un número por teclado que representa al costo por hora que se genera
        num = input('Ingrese el costo por hora que genera: ')
        #Si el número ingresado en entero
        if num.isnumeric():
            #La variable validar adquiere el valor True y se rompe el bucle
            validar = True       
        #Si no es un número entero
        else:
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA')
            #La variable validar adquiere el valor False y no se rompe el bucle
            validar = False
    #Para terminar se retorna el valor ingresado como tipo entero
    return int(num)

def calcularValores(horas,dias,costo):
    """
    Función que calculará los valores que requiere el programa.

    Parámetros:
    ----------------
    horas: int (dato ingresado por el usuario)    
    
    dias: int (dato ingresado por el usuario)

    costo: int (dato ingresado por el usuario)
 
    Retorna:
    ----------------
    Retorna la variable total
    """
    total = horas * dias * costo
    return total

#Funcion principal del programa
if __name__ == '__main__':
    #Se asigna la primera funcion a una variable para poder ser trabajada
    horasTrabajadas = leerValorhoras()
    #Se asigna la segunda funcion a una variable para poder ser trabajada
    costo = leerValorCosto()
    #Se asigna la tercera funcion a una variable para poder ser trabajada
    diasTrabajados = leerValorDias()
    #Se asigna la cuarta funcion a una vairable que es el resultado de este programa
    total = calcularValores(horasTrabajadas,diasTrabajados,costo)
    """
    Las siguientes líneas simplemente imprimen el resultado del programa mostrando lo que el enunciado establece,
    se hace un recuento de los datos ingresados por el usuario, y despues se muestra la ganancia que generará 
    el usuario
    """
    print('---------------------------------------------------------------------------------------')
    print('RESUMIENDO:')
    print(horasTrabajadas,'horas trabajadas')
    print('Con un costo de',costo,'dolares por hora')
    print('Trabajando por',diasTrabajados,'días')
    print('---------------------------------------------------------------------------------------')
    print('Usted ganará',total,'dólares, trabajando',horasTrabajadas,'horas al día, durante',diasTrabajados,'días')
    print('---------------------------------------------------------------------------------------')
