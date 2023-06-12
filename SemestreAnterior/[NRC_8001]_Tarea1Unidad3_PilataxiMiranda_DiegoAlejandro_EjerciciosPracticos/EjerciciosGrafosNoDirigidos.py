
def redesSociales(redSocial):
    """
    Función creada para establecer un tipo de red social para hacer amigos

    Parámetros:
    ---------------------
    redSocial (diccionario): Diccionario vacío creada que almacenará información

    Retonra:
    ---------------------
    No retorna ningún valor
    """
    #Se establece una red social con usuarios y distintos amigos
    redSocial["Juan"] = ["Pedro", "Ana"]
    redSocial["Pedro"] = ["Juan", "Ana", "María"]
    redSocial["Ana"] = ["Juan", "Pedro", "María"]
    redSocial["María"] = ["Pedro", "Ana"]

    #Se imprime la red social
    print("Red social:")
    #Mediante un bucle for, se imprime a cada usuario con su respectiva amistad
    for usuario in redSocial:
        #Acorde a lo almacenado en el diccionario vacío creado anteriormente
        print(usuario, "es amigo de:", redSocial[usuario])

    #Se le permite al usuario ingresar un nuevo integrante a la red social
    nuevoUsuario = input("Ingrese el nombre del nuevo usuario: ")
    redSocial[nuevoUsuario] = []

    #Se le pide al usuario que ingrese los amigos del nuevo nombre ingresado
    while True:
        #Se le da la opcion de terminar con la palabra "fin"
        amistad = input("Ingrese el nombre de un amigo del nuevo usuario (o 'fin' para terminar): ")
        #Si el usuario ingresa "fin se termina el bucle"
        if amistad == "fin":
            break
        #Se actualiza la red social actualizada incluido el nuevo nombre ingresado por el usuario
        redSocial[nuevoUsuario].append(amistad)
        redSocial[amistad].append(nuevoUsuario)

    #Se imprime la red social con los nombres actualizados
    print("Red social actualizada: ")
    for usuario in redSocial:
        print(usuario, "es amigo de:", redSocial[usuario])

#Funcion main para ejecutar todo el programa
if __name__ == '__main__':
    #Se establece un diccionario vacio
    redSocial = {}
    #Se llama a la función creada anteriormente
    redesSociales(redSocial)

