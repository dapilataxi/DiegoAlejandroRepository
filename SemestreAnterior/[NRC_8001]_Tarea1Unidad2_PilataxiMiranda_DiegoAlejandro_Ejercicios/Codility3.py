import datetime
from timeit import default_timer

def solucion(E,L):
    """
    Función que dará la solucion al problema planteado
    
    Parámetros:
    -----------------------------
    E: Tiempo de Entrada
    S: Tiempo de Salida

    Retorna:
    -----------------------------
    Retorna el conteo desde el índice
    """
    #Diferencia entre horas tanto de entrada y salida
    difHora = L.hour - E.hour
    #Diferencia de minutos en entrada y salida
    difMin = L.minute - E.minute
    #Se define el costo de entrada
    costoEntrada = 2
    #Se define el costo de la ptimera hora que siempre se cuenta
    primeraHora = 3
    #Si la diferencia de hora es igual a 1
    if difHora == 1:
        #No existirian horas extra
        horaExtra = 0
        #Si la diferencia de minutros es diferente de 0
        if difMin != 0:
            #Cada minuto extra costara 4
            minutosExtra = 4
        #Caso contrario
        else:
            #No habria costo en el tiempo extra
            minutosExtra = 0
    #Caso contrario si la dierencia de hora es mayor a 4
    elif difHora > 1:
        #El costo de hora extra se multiplica por 4
        horaExtra = 4 * (difHora - 1)
        #Adicional si la diferencia de minutos es mayor a 0
        if difMin > 0:
            #Los minutos extra tienen costo
            minutosExtra = 4
        #Caso contrario
        else:
            #No hay costo
            minutosExtra = 0
    
    #Se aplica la operacion para determinar el costo del parqueadero
    costo = costoEntrada + primeraHora + horaExtra + minutosExtra
    #Se imprime el costo 
    print('El costo del parqueadero es',costo,'dólares')
    
#Se crea la funcion main donde se ejecutara el programa
if __name__ == '__main__':
    #Se pide ingreso al usuario de la hora de entrada
    horaEntrada = int(input('Ingrese hora de entrada: '))
    minutoEntrada = int(input('Ingrese minutos de entrada: '))
    #Se pide al usuario de la hora de salida
    horaSalida = int(input('Ingrese hora de salida: '))
    minutoSalida = int(input('Ingrese minutos de salida: '))
    #Se establece las variables donde se guardara cada hora
    E = datetime.time(horaEntrada,minutoEntrada)
    L = datetime.time(horaSalida,minutoSalida)

    #Mediante la funcion default_timer se ingresa la función a ser analizada junto a su respectivo parámetro
    inicio = default_timer()
    #Se ejecuta la funcion
    solucion(E,L)
    fin = default_timer()
    print('------------------------------------')
    #Se imprime el tiempo de ejecución
    print(fin - inicio,'sec')
    print('------------------------------------')

