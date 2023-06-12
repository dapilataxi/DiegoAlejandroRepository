#Importamos todas las librerias necesarias para ejecutar el presente problema
#Date time para las horas, timeit para calcular la complejidad de tiempo
import datetime, sys
from timeit import default_timer

def validarHora():
    """
    Función creada para la entrada de horas en el presente programa

    Parámetros:
    ------------------
    hora: int, valor en horas que deberá ingresar el usuario

    Retorna:
    ------------------
    Retorna el valor de horas como tipo entero
    """
    #Se crea una variable para poder ejecutar el bucle while
    validar = False
    #Se establece que el bucle se repetirá hasta que la variable anterior sea 'True'
    while validar != True:
        #El usuario deberá ingresar la hora
        hora = input()
        #Condicion si el usuario ingresa un valor numérico
        if hora.isnumeric():
            #La variable adiquirirá un valor True y se terminará el bucle
            validar = True
            #Si el número ingresado es mayor a 23, no se podra avanzar
            if int(hora) > 23:
                print('-----------------------------------------------------------')
                print('EL RANGO DE UNA HORA COMPRENDE DESDE 0 A 23 EN FORMATO HH:MM. INTENTE DE NUEVO')
                #Adquiere el valor False porque una hora no puede ser ingresada con un número mayor a 23
                validar = False
            else:
                #Caso contrario la variable adquiere el valor True y se termina el bucle
                validar = True
                #Retornará la hora ingresada en entero
                return int(hora)
                
        else:
            #Si no es un número entero se pedirá que ingrese de nuevo el número solicitado
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. INTENTE DE NUEVO')
            validar = False
  

def validarMinuto():
    """
    Función creada para la entrada de minutos en el presente programa

    Parámetros:
    ------------------
    minuto: int, valor en horas que deberá ingresar el usuario

    Retorna:
    ------------------
    Retorna el valor de minutos como tipo entero
    """
    #Se crea una variable para poder ejecutar el bucle while
    validar = False
    #Se establece que el bucle se repetirá hasta que la variable anterior sea 'True'
    while validar != True:
        #El usuario deberá ingresar la información que se solicita en el input
        minuto = input()
        #Condición si el munto ingresado es un valor numérico
        if minuto.isnumeric():
            #La varible adquiere el valor True y se terminaría el bucle
            validar = True
            #Se plantea una nueva condición, si los minutos ingresados son mayores a 59
            if int(minuto) > 59:
                #Se le informa al usuario que el rango de un minuto es de 0 a 59, que intente de nuevo
                print('-----------------------------------------------------------')
                print('EL RANGO DE UN MINUTO COMPRENDE DESDE 0 A 59 EN FORMATO HH:MM. INTENTE DE NUEVO')
                #Adquiere el rango False y no se podrá continuar con el bucle
                validar = False
            #Si el valor numéro está dentro del rango establecido, se termina el bucle
            else:
                validar = True
                #Se retorna el valor de minuto como tipo entero
                return int(minuto)
        else:
            #Si no se ingresa un valor de tipo entero se le mostrará el mensaje al usuario de que el dato ingresado no es válido
            print('-----------------------------------------------------------')
            print('ENTRADA NO VÁLIDA. INTENTE DE NUEVO')
            validar = False

def complTiempo():
    """
    Función para calcular la complejidad de tiempo

    Parámetros:
    ----------------
    No tiene parámetros

    Retorna:
    ---------------
    No retorna ningun valor
    """
    #Mediante la funcion default_timer se ingresa la función a ser analizada junto a su respectivo parámetro
    inicio = default_timer()
    #Se ejecuta la funcion
    fin = default_timer()
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
    result = sys.getsizeof(validarMinuto)
    print (result,'bytes')
    print('------------------------------------')

#Función main donde se ejecutará el programa   
if __name__ == '__main__':
    #Se pide ingreso al usuario de la hora de entrada
    print('Ingrese hora de entrada: ')
    horaEntrada = validarHora() 
    #Se pide los minutos de ingreso
    print('Ingrese minutos de entrada: ')
    minutoEntrada = validarMinuto()
    #Se pide al usuario de la hora de salida
    print('Ingrese hora de salida: ')
    horaSalida = validarHora()
    #Se pide los minutos en los que salió
    print('Ingrese minutos de salida: ')
    minutoSalida = validarMinuto()
    #Se establece las variables donde se guardara cada hora
    E = datetime.time(horaEntrada,minutoEntrada)
    L = datetime.time(horaSalida,minutoSalida)
    #Se imprime la información requerida
    print('-----------------------------------------------------------')
    print('La hora de ingreso es',E,', la hora de salida será a',L)

    #Se llama a la función para la complejidad de tiempo
    complTiempo()
    #Se llama la función para la complejidad de espacio
    complEspacio()