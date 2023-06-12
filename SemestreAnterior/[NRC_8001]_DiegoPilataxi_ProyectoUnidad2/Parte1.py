import ejercicio1, ejercicio2, ejercicio3, ejercicio4, ejercicio5, ejercicio6, ejercicio7

def opcion1():
    #if main de nuestro programa donde solo ejecuto la funcion correspondiente.
    email_usuario = input('Ingrese su correo electronico: ')
    ejercicio1.validarCorreo(email_usuario)

def opcion2():
    #Pido el nombre y apellido del niño ingresado por el papa.
    print('RECUERDE: \nSolo debe ingresar texto. \nEl nombre y apellido deben estar en mayusculas.')
    #Utilizo un ciclo while para validar que solo puede ingresar texto como lo pide el programa.
    while True:
        try:
            nombre = input('Ingrese el nombre del niño: ')
            apellido = input('Ingrese el apellido del niño: ')
            if(nombre.isalpha() and apellido.isalpha()):
                break    
            else:
                print('No son validos numeros ni caracteres especiales')
        except ValueError:
            print('Ingrese datos correctos :/')
    #Guardo las variables en una lista para poder mandar el parametro y calcular la complejidad de tiempo.
    variables = [nombre,apellido]
    ejercicio2.validarNombreYApellido(variables)

def opcion3():
    print('RECUERDE: \nEl niño puede estar en Guarderia o Preescolar \nNo olvide que solo debe ingresar texto!')
    #Utilizo un ciclo while para validar que solo puede ingresar texto como lo pide el programa.
    while True:
        try:    
            año_electivo = input('Ingrese el año electivo del niño: ')
            año_electivo_mayuscula = año_electivo.title()
            if(año_electivo_mayuscula.isalpha()):
                break    
            else:
                print('No son validos numeros ni caracteres especiales')
        except ValueError:
            print('Ingrese datos correctos :/')            
    ejercicio3.validacionAñoElectivo(año_electivo_mayuscula)

def opcion4():
    #Inicialo la variable prueba para poder calcular la complejidad de tiempo.
    prueba = ''
    print('Su cupon de descuento es',ejercicio4.generarCuponDescuento(prueba),', no olvide guardarlo')

def opcion5():
    #Inicialo la variable prueba para poder calcular la complejidad de tiempo.
    prueba = ''
    ejercicio5.nombrarAnimales(prueba)

def opcion6():
    lista_palabras = ['Murcielagos','Chocolates','Universidad','Perro','Guatemala','Estacionamiento','Carro']
    print('No olvide que solo debe ingresar texto!')
    #Llamo a la funcion para que imprima la palabra desordenada.
    ejercicio6.ordenarPalabras('')
    #Utilizo un ciclo while para validar que solo puede ingresar texto como lo pide el programa y que sea la respuesta correcta.
    while True:
        try:
            #Pido la respuesta del niño respecto a la palabra ordenada.
            respuesta_niño = input('Ingrese su respuesta: ')
            #Con el metodo .title() convierto la respuesta del niño en el formato correcto para que no importe si escribe en
            #mayuscula o minuscula.
            respuesta_mayuscula = respuesta_niño.title()
            #Comparo si la respuesta es la correcta para terminar el bucle.
            if(respuesta_mayuscula in lista_palabras):
                print('Correcto! ha acertado en ordenar la palabra',respuesta_mayuscula,'su respuesta es la correcta :D')
                break
            #Si no es correcta imprimo un mensaje de error y seguira ejecutandose el juego.
            else:
                print('Intente nuevamente :/, recuerde ademas de no escribir numeros ni caracteres especiales!')
        except ValueError:
            print('Ingrese datos correctos :/')
    ejercicio6.ordenarPalabras(respuesta_niño)

def opcion7():
    #Inicialo la variable prueba para poder calcular la complejidad de tiempo.
    prueba = ''
    ejercicio7.reconocerVocalesyConsonantes(prueba)

