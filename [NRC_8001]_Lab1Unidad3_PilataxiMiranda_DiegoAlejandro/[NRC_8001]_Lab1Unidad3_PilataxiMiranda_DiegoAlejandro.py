def mensajeInformativo():
    """
    Funcion que muestra mensaje de las selecciones de carreteras asociadas al agente inteligente

    Parámetros:
    -------------------------
    No tiene Parámetros

    Retorna:
    -------------------------
    No retorna ningún valor
    """
    print('**************************************IMPORTANTE*************************************************')
    print('Recuerde que la carretera debe ser OBLIGATORIAMENTE escrita tal y como se le muestra en pantalla.')
    print('CASO CONTRARIO NO PODRA PROSEGUIR')
    print('Las carreteras asociadas son "Quito", "Aloag", "Sangolqui", "Machachi"')

def elegirCarretera():
    """
    Funcion que hace la selección de las carreteras asociadas, con su respectiva validación.

    Parámetros:
    ------------------
    No contiene parámetros

    Retorna:
    -----------------
    Retorna la variable locación que es la carretera que ha decidido seleccionar el usuario
    """
    #Se establece una variable para poder iniciializar un bucle de validacion
    validar = False
    #El bucle while nos permitirá pedir la entrada del dato hasta que se ingrese el necessario
    while validar != True:
        #Se pide el ingreso de la carretera que desea ubicarse el usuario
        print('---------------------------------------------')
        locacion = input("Ingrese la carretera deseada: ")
        #Si el dato ingresado por el usuario difiere de cualquiera de las opciones disponibles
        if locacion != 'Quito' and locacion != 'Aloag' and locacion != 'Sangolqui' and locacion != 'Machachi':
            #Se le informa al usuario que el dato ingresado es erróneo y lo intente de nuevo
            print('---------------------------------------------')
            print('Carretera no disponible o mal escrita. Intente de nuevo')
            validar = False
        else:
            #Caso constrario se le agradece la elección
            print('---------------------------------------------')
            print('Gracias por elegir')
            break
    #Se retorna la carretera asignada en la variable 'locación'
    return locacion

def abrirCarretera(locacion,costo):
    """
    Función creada para la apertura de las carreteras elegidas

    Parámetros:
    -----------------
    locacion (str): Indica la carretera que ha seleccionado el usuario
    costo (int): Registra el costo por cada accion que realiza el agente inteligente

    Retorna:
    -----------------
    Retorna el valor del costo de las acciones
    """
    #En primer lugar se asigna la locacion a una nueva variable
    carretera = locacion
    #Se muestra el mensaje al usuario de la carretera en la cuál se encontraría
    print('Usted se encuentra en la carretera de ' + carretera)
    #Se crea una variable booleana para iniciar un bucle
    validar = False
    #Se inicia un bucle de validación para el estado de la carretera
    while validar != True:
        #Se pide el ingreso del estado de la carretera
        estado = input('Ingrese el estado de la carretera: ')
        #Condicion del estado de la carretera, validacion si el ingreso es incorrecto
        if estado != '0' and estado != '1':
            #Si ingresa un valor que no sea los estipulados anteriormente, se mostrará el sisguiente mensaje
            print('El estado se define unicamente con 0 (carretera abierta) y 1 (carretera cerrada). INTENTE DE NUEVO')
            #Se mantiene el valor de false para que se repita el bucle
            validar = False
        #Caso contrario
        else:
            #Condicion si el estado ingresado es 1
            if estado == '1':
                #Se muestra el usuario en la cual se encuentra
                print('Carretera',carretera,'está cerrada')
                #Se cambia el estado ingresado de la carretera por 0 
                estadoDeseado[carretera] = '0'
                #Se incrementa el costo por la accion
                costo += 1
                #Se muestra los mensajes respectivos de la apertura
                print("Abriendo carretera")
                print("Costo por apertura: " + str(costo))
                #Se retorna el valor del costo por la apertura
                return costo
            else:
                #Caso contrario la carretera ya se encuentra abierta y no necesita ninguna accion
                print('La carretera se encuentra abierta. No se realiza ninguna acción.')
                #El costo será 0
                costo = 0
                #Se retorna el valor del costo
                return costo
#Funcion main donde se ejecutará todo el programa del agente inteligente
if __name__ == '__main__':
    #Se ingresa el estado deseado al cual deben llegar todas las carreteras
    estadoDeseado = {'Quito':'0', 'Aloag':'0', 'Sangolqui':'0', 'Machachi':'0'}
    #Se establece un valor inicial del costo como contador
    costo = 0
    #Se da una bienvenidad al sistema
    print('Bienvenido a "Transitito S.A." tu agente de tránsito inteligente')
    #Se ejecuta la función con el mensaje informatico 
    mensajeInformativo()
    #Se asigna a una variable lo que retorna la función que se creo anteriormente
    locacion = elegirCarretera()
    #Se establece este valor a una nueva variable, para que pueda ser generica
    carretera = locacion
    #Se establece un condicional para la carretera ingresada
    if carretera == locacion:
        #Se asigna a una variable costo lo que retorne la funcion que se dedica a abrir carreteras
        costo1 = abrirCarretera(carretera,costo)
        #Se muestra el costo por las acciones realizadas en la primera carretera ingresada
        print('Costo por acciones en carretera',carretera,'es',costo1)
        print('Ahora vamos a definir las carreteras restantes')
        validar = False
        #Se inicia un bucle para empezar el trabajo con la siguiente carretera
        while validar != True:
            #Se muestra el mensaje informativo con todas las opciones disponibles
            mensajeInformativo()
            #Se asigna una nueva variable que sera de la segunda carretera ingresada
            carretera2 = elegirCarretera()
            #Condicion para que la nueva carretera ingresada no sea igual a la primera
            if carretera2 == carretera:
                #Si ya la escribió, se le informa que ya fue escogida
                print('Esta carretera ya fue usada. ESCOGA OTRA')
                #Se sigue con la asignacion de false hasta que se ingrese otra
                validar = False
            #Si ingresa una diferente se procede
            else:
                #Se establece a una nueva variable de costo la apertura de la nueva carretera
                costo2 = abrirCarretera(carretera2,costo)
                #Si el costo es igual a 1
                if costo2 == 1:
                    #Se debe ejecutar una accion que incrementa el costo por la movilización a dicha carretera
                    print('El costo de esta acción se incremente a 1 por la acción de moverse a la vía ingresada.')
                    costo2 += 1
                    #Se imprime el costo de la accion totoal
                    print('Costo por acciones en carretera',carretera2,'es',costo2)
                #Caso contrario
                else:
                    #No se ejecuta ninguna accion por la movilizacion porque no está cerrada
                    print('Costo por acciones en carretera',carretera2,'es',costo2)
                    print('Ahora vamos a definir las 2 carreteras restantes')
                #Bucle creado para la apertura de una nueva carretera
                validar = False
                while validar != True:
                    #Se muestra un nuevo mensaje informatico para la nuevo carretera
                    mensajeInformativo()
                    #Se asigna la nueva carretera ingresada a una nueva variable
                    carretera3 = elegirCarretera()
                    #Condicion para que el ingreso de la nueva carretera sea diferente
                    if carretera3 == carretera or carretera3 == carretera2:
                        #Si ya se ingresó alguna de las 2 carreteras anteriores, se le pide que seleccione otra
                        print('Esta carretera ya fue usada. ESCOGA OTRA')
                        validar = False
                    #Caso contrario
                    else:
                        #Se ejecuta una nueva asignacion a una nueva variable costo
                        costo3 = abrirCarretera(carretera3,costo)
                        #Si el costo es igual a 1
                        if costo3 == 1:
                            #Se ejecuta la mismaa accion extra por la movilizacion y adquiere un costo adicional
                            print('El costo de esta acción se incremente a 1 por la acción de moverse a la vía ingresada.')
                            costo3 += 1
                            #Se muestra el costo por las acciones realizadas
                            print('Costo por acciones en carretera',carretera3,'es',costo3)
                        #Caso contrario
                        else:
                            #No se ejecuto ninguna acción y se muestra al usuario
                            print('Costo por acciones en carretera',carretera3,'es',costo3)
                        print('Ahora vamos a definir la ultima carreteras restantes')
                        #Bucle para trabajar con la carretera restante
                        validar = False
                        #Bucle para el trabajo con la última carretera
                        while validar != True:
                            #Se muestra el mismo mensaje informativo
                            mensajeInformativo()
                            #Se asigna la nueva carretera ingresada a una nueva variable
                            carretera4 = elegirCarretera()
                            #Condicion para que se ingrese la carretera restante
                            if carretera4 == carretera or carretera4 == carretera2 or carretera4 == carretera3:
                                #Si escribe alguna de las 3 carreteras ingresadas antes
                                print('Esta carretera ya fue usada. ESCOGA OTRA')
                                #Se muestra el mensaje anterior y se mantiene el bucle
                                validar = False
                            #Caso contrario este
                            else:
                                #Se asgina una nueva variable costo con la funcion para abrir carreteras
                                costo4 = abrirCarretera(carretera4,costo)
                                #Si el costo es igual a uno
                                if costo4 == 1:
                                    #Se tuvo que mover a la carretera desginada, por lo tanto se cobra el costo por movilizar
                                    print('El costo de esta acción se incremente a 1 por la acción de moverse a la vía ingresada.')
                                    costo4 += 1
                                    #Se muestra el costo por las acciones realizadas en esa carretera
                                    print('Costo por acciones en carretera',carretera4,'es',costo4)
                                #Caso contrario
                                else:
                                    #Se informa el costo por las acciones realizados que en este caso seria 0
                                    print('Costo por acciones en carretera',carretera4,'es',costo4)
                                #Se hace una operacion para el costo total del proceso
                                costoTotal = costo1 + costo2 + costo3 + costo4
                                #Se muestra el costo total al usuario
                                print('Su precio total por las acciones realizadas es de:',costoTotal)
                                #Se informa al usuario que ya se llego al estado deseado de todas las carreteras
                                print('SE HA LLEGADO AL ESTADO DESEADO. TODAS LAS CARRETERAS ESTÁN ABIERTAS')
                                #Se imprime el estado desead
                                print(estadoDeseado)
                                #Se agradece por usar el sistema y termina la ejecución del programa
                                print('GRACIAS POR SU PREFERENCIA...')
                                validar = True