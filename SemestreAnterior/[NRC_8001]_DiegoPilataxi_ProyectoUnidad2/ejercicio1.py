#Importo las librerias para calcular la complexity.
import big_o
import sys

def validarCorreo(email_usuario):
    """"
    Se crea la funcion para la validacion del email que ingrese el papa del niño para tener su contacto.
  
    Parametros:
    -------------------
    Recibe la variable:
    str: email_usuario 
    Correspondiente al email que digite.

    Retorna:
    -------------------
    No retorna ninguna variable.
    """
    #En las siguientes lista genero los caracteres que estan permitidos al momento de ingresar el correo.
    signos = ['.','_','-']
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    dominios = ['gmail','hotmail','msn','yahoo','outlook','live']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    extensiones = ['com','net','org','es','com.ec','ec','ea','gob']
    #Inicializo la variable aviso para imprimir en caso de que ingrese algun error en el correo o para decir que el correo es correcto.
    aviso = ""
    #Genero la condicion de encontrar un arroba en el correo ingresado, caso contrario imprimir el mensaje que hace falta el @.
    if email_usuario.find('@') != -1:
        #Divido el email ingresado a partir del arroba.
        email_divido = email_usuario.split('@')
        #Guardo la parte izquierda del arroba que corresponde a los nombres del correo del usuario.
        nombre_usuario = email_divido[0]
        #Guardo la parte derecha del arroba.
        restante = email_divido[1]
        #De la parte derecha del correo divido a partir del punto.
        email_divido2 = restante.split('.')
        #Guardo la parte izquierda del punto que corresponde al dominio del correo del usuario.
        dominio = email_divido2[0]
        #Guardo la parte derecha del punto.
        restante2 = email_divido2[1]
        #Recorro la parte izquierda del arroba.
        for i in nombre_usuario:
            #Primero compruebo si el usario (parte izquierda del arroba) contiene los caracteres correctos segun la lista.
            if i in signos or i in numeros or i in minusculas or i in mayusculas:
                #Luego si el dominio es uno correcto segun la lista.
                if dominio in dominios:
                    #Por ultimo si la extension es la correcta segun la lista.
                    if restante2 in extensiones:        
                        aviso = 'El correo es correcto!'
                        break
                    else:
                        aviso += 'Error, la extension no es reconocida, pruebe con otra mas comun\n'
                        break
                else:
                    aviso += 'Error, el dominio no es reconocido, pruebe con otro mas comun\n'
                    break
            else:
                aviso += 'Error, caracter ' + i + ' no es permitido para el nombre de usuario del correo.\n'
                break
    #Mensaje de error en caso de que el correo no contenga un @.            
    else:
        aviso += 'Error, el correo que ingreso no contiene un arroba'
    #Imprimo la variable aviso dependiendo de si hubo un error con el correo o si fue correcto.
    print(aviso)

def complejidadTiempo():
    """"
    Se crea la funcion para el calculo de la complejidad de tiempo del algoritimo.
  
    Parametros:
    -------------------
    No recibe ninguna variable.

    Retorna:
    -------------------
    No retorna ninguna variable.
    """
    #Calculo de la complejidad de tiempo.
    cadena_ejemplo = lambda example_variable: email_usuario
    best, others = big_o.big_o(validarCorreo, cadena_ejemplo)
    print(best)

def complejidadEspacio():
    """"
    Se crea la funcion para el calculo de la complejidad de espacio del algoritimo.
  
    Parametros:
    -------------------
    No recibe ninguna variable.

    Retorna:
    -------------------
    No retorna ninguna variable.
    """
    #Calculo de la complejidad de espacio.
    result = sys.getsizeof(validarCorreo)
    print(result,'bytes')

#if main de nuestro programa donde solo ejecuto la funcion correspondiente.
if __name__ == '__main__':
    email_usuario = input('Ingrese su correo electronico: ')
    validarCorreo(email_usuario)
    complejidadTiempo()
    complejidadEspacio()
