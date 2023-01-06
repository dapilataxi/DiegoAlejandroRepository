def leerNumero():
    """
    Función que leera el ingreso en el menú principal.

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
        #Ingreso por teclado del dato en cuestion
        num = input()
        #Si el número ingresado en entero
        if num.isnumeric():
            #La variable validar adquiere el valor True y se rompe el bucle
            validar = True       
        #Si no es un número entero
        else:
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. INGRESE DE NUEVO')
            validar = False
    #Para terminar se retorna el valor ingresado como tipo entero
    return int(num)

def rectangulo(base,altura):
    """
    Función ejecutará el perímetro y área del rectangulo.

    Parámetros:
    ----------------
    base: int
    altura: int

    Retorna:
    ----------------
    No retorna ningun valor
    """
    print('-----------------------------------------------------------')
    print('Para el perímetro:')
    #Se hace recuento de la base y altura ingresada por el usuario
    print('El lado mayor es',base,'y el lado menor es',altura)
    #Se calcula el permietro en base a los datos ingresados
    perimetro = (2 * base) + (2 * altura)
    #Se imprime el perimetro
    print('El perímetro de su rectángulo es',perimetro)
    print('-----------------------------------------------------------')
    print('Para el área:')
    #Se hace recuento de la base y altura ingresada por el usuario
    print('La base es',base,'y la altura es',altura)
    #Se calcula el area en base a los datos ingresados
    area = altura * base
    #Se imprime el area
    print('El área de su rectángulo es',area)
    print('-----------------------------------------------------------')

def cuadrado(lado):
    """
    Función ejecutará el perímetro y área del cuadrado.

    Parámetros:
    ----------------
    lado: int

    Retorna:
    ----------------
    No retorna ningun valor
    """
    print('-----------------------------------------------------------')
    print('Para el perímetro:')
    #Se hace recuento del lado ingresado por el usuario
    print('El lado es',lado)
    #Se calcula el perimetro en base al dato ingresado
    perimetro = 4 * lado
    #Se imprime el perimetro
    print('El perímetro de su cuadrado es',perimetro)
    print('-----------------------------------------------------------')
    print('Para el área:')
    #Se hace recuento del lado ingresado por el usuario
    print('La lado es',lado)
    #Se calcula el area en base al dato ingresado
    area = lado * lado
    #Se imprime el area
    print('El área de su cuadrado es',area)
    print('-----------------------------------------------------------')

#Funcion principal main
if __name__ == '__main__':
    opcion = 0
    #Se crea un bucle para el menú que se creara para la eleccion del cálculo que se desee hacer
    while opcion != 2:
        #El menú tendrá 2 opciones, si se desea trabajar con rectangulo o cuadrado
        print('-----------------------------------------------------------')
        print('Seleccion la figura con la que desea trabajar: ')
        print('1. Rectángulo')
        print('2. Cuadrado')
        #No se detendrá hasta que se seleccione una opcion correcta dentro del menu
        print('-----------------------------------------------------------')
        print('Ingrese el número de la figura:')
        #Se lee el número que ingresara el usuario por el teclado
        opcion = leerNumero()
        #Condición si la opcion es 1
        if opcion == 1:
            print('Ingrese la base del rectángulo:')
            #Se ingresa la base para el rectangulo
            base = leerNumero()
            print('Ingrese la altura del rectángulo:')
            #Se debe ingresar la altura del rectangulo
            altura = leerNumero()
            #Se ejecuta la funcion rectangulo, y se procede a calcular tanto el perimetro como el area del rectangulo
            rectangulo(base,altura)
            opcion = 2
        #Condición si la opcion es 2
        elif opcion == 2:
            print('Ingrese la longitud del lado de su cuadrado:')
            #Se debe ingresar el lado para proceder a las operaciones del cuadrado
            lado = leerNumero()
            #Se ejecuta la funcion cuadrado y se procede a calcular tanto el perimetro como el area del cuadrado
            cuadrado(lado)
        #Si la selección está fuera de las 2 opciones
        else:
            print('-----------------------------------------------------------')
            #Se mostrará el mensaje de "opcion no disponible" hasta que se ingrese una opcion que este dentro del menú
            print('OPCION NO DISPONIBLE')
        