
def agregarCiudad(ciudad):
    """
    Función que agregará las ciudades al ejercicio

    Parámetros:
    ---------------------
    ciudad (string): Ciudades de Ecuador para el ejemplo del grafo

    Retorna:
    ---------------------
    No retorna ningun valor
    """
    #Condicional para que la ciudad se agregue en el grafo
    if ciudad not in grafo:
        #Si eso sucede se agraga la ciudad
        grafo[ciudad] = []

def agregarConexion(ciudad1, ciudad2):
    """
    Función que creará las conexiones únicas entre las ciudades

    Parámetros:
    ---------------------------
    ciudad1 (string): Primera ciudad a ser conectada
    ciudad2 (string): Ciudad a ser conectada con ciudad1

    Retorna:
    -------------------------
    No retorna ningun valor
    """
    #Condicion para estableces si ambas ciudades están en el grafo
    if ciudad1 in grafo and ciudad2 in grafo:
        #De ser así se agrega la conexión entre las ciudades
        grafo[ciudad1].append(ciudad2)

def imprimirGrafo():
    """
    Función que imprimirá las conexiones de los nodos del grafo

    Parámetros:
    ----------------------
    No tiene parámetros

    Retorna:
    ---------------------
    No retorna ningun valor
    """
    print("Grafo dirigido:")
    #Para cada ciudad que se encuentre en el grafo
    for ciudad in grafo:
        #Se establece una variable para tranformar la lista en una cadena
        adyacentes = ", ".join(grafo[ciudad])
        #Se imprime la ciudad con su conexion
        print(ciudad + " -> " + adyacentes)

#Función main donde se ejecutara todo el programa
if __name__ == '__main__':
    #Se establece un diccionario vacio con el nombre de grafo
    grafo = {}
    #Se agregan todas las ciudades para el ejercicio práctico
    agregarCiudad('Quito')
    agregarCiudad('Guayaquil')
    agregarCiudad('Cuenca')
    agregarCiudad('Ambato')
    agregarCiudad('Loja')
    agregarCiudad('Manta')
    agregarConexion('Quito', 'Cuenca')
    agregarConexion('Quito', 'Ambato')
    agregarConexion('Guayaquil', 'Manta')
    agregarConexion('Guayaquil', 'Loja')
    agregarConexion('Cuenca', 'Loja')
    imprimirGrafo()



