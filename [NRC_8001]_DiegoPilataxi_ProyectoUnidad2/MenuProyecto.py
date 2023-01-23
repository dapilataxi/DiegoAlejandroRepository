import Parte1, Parte2
def menuGeneral():
    print('===============================================')
    print('                 MENÚ GENERAL                  ')
    print('===============================================')
    print('1. Validación de correo electrónico')
    print('2. Validación de nombre y apellido')
    print('3. Ingreso de un número de teléfono')
    print('4. Registro de hora de entrada y hora de salida')
    print('5. Ingreso del año lectivo al que pertenece')
    print('6. Registro de información en la base de datos')
    print('7. Eliminar información de la base de datos')
    print('8. Obtener un cupón por registro')
    print('================================================')
    print('                    JUEGOS                      ')
    print('================================================')
    print('9. Caracter inverso de una palabra')
    print('10. Ordenar letras para formar palabras')
    print('11. Identificar consonantes y vocales')
    print('12. Escribir nombres solo de animales')
    print('13. Formar palabras a partir de letras')
    print('14. Formar palabras con la última letra')
    print('15. Escribir palabras con el mismo N° sílabas')
    print('16. Salir')
    validar = False
    while validar != True:
        print('================================================')
        opcion = input('Seleccione una opción para continuar: ')
        if opcion.isnumeric():
            #Sale del bucle con el cambio de valor de 'validar'
            validar = True
            if int(opcion) > 17:
                print('================================================')
                print('OPCION NO DISPONIBLE. INTENTE DE NUEVO')
                validar = False
            elif int(opcion) < 1:
                print('================================================')
                print('OPCION NO DISPONIBLE. INTENTE DE NUEVO')
                validar = False
            else:
                validar = True
        #Caso contrario
        else:
            #Muestra al usuario que debe ingresar solo caracteres, y se repetirá el bucle
            print('================================================')
            print('NO SE PERMITE EL INGRESO DE CARACTERES. INTENTE DE NUEVO')
            validar = False
    return int(opcion)

def accionMenu(opcion):
    if opcion == 1:
        Parte1.opcion1()
        opcion = menuGeneral()
        accionMenu(opcion)

    elif opcion == 2:
        Parte1.opcion2()
        menuGeneral()

    elif opcion == 3:
        Parte2.opcion4()
        menuGeneral()

    elif opcion == 4:
        Parte2.opcion5()
        menuGeneral()

    elif opcion == 5:
        Parte1.opcion3()
        menuGeneral()

    elif opcion == 6:
        Parte2.opcion10()
        menuGeneral()
    
    elif opcion == 7:
        Parte2.opcion7()
        menuGeneral()
    
    elif opcion == 8:
        Parte1.opcion4()
        menuGeneral()

    elif opcion == 9:
        Parte2.opcion8()
        menuGeneral()
    
    elif opcion == 10:
        Parte1.opcion6()
        menuGeneral()
    
    elif opcion == 11:
        Parte1.opcion7()
        menuGeneral()
    
    elif opcion == 12:
        Parte1.opcion5()
        menuGeneral()

    elif opcion == 13:
        Parte2.opcion14()
        menuGeneral()

    elif opcion == 14:
        Parte2.opcion15()
        opcion = menuGeneral()
        accionMenu(opcion)

    elif opcion == 15:
        Parte2.opcion16()
        opcion = menuGeneral()
        accionMenu(opcion)
        
    elif opcion == 16:
        print('Ejecucion terminada...')

if __name__ == '__main__':
    opcion = menuGeneral()
    accionMenu(opcion)
