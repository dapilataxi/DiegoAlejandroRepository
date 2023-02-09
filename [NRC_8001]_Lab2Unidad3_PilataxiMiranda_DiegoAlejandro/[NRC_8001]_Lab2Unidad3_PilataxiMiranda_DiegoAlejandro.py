def encontrarCamino(inicio, fin, camino):
    """
    Función destinada para encontrar el camino más barato entre dos nodos

    Parámetros:
    ----------------
    inicio (string): Estado inicial del grafo
    fin (string): Estado objetido del grafo
    camino(string): Ruta a seguir en el grafo

    Retorna:
    ---------------
    Retorna el camino actual con su respectivo costo
    """
    #Se plantea la variable con la cual se accederá a la ruta
    caminoActual = [inicio]
    #Costo inicial que irá incrementando acorde el avance
    costoActual = 0

    #Se hace el recorrido hasta el nodo final con el bucle while
    while caminoActual[-1] != fin:
        #Se establece un valor al nodo siguiente en caso de que ya se haya llegado al final
        siguienteNodo = None
        #Mismo criterio para el costo, que adquiere un valor nulo cuando se llegue al final
        costoSiguiente = None
        #Con el bucle for se buscará el siguiente nodo con el costo mínimo
        for nodo, costo in camino:
            #Si el nodo se encuentra en el camino que sigue el recorrido
            if nodo in caminoActual:
                #Se da la orden de avanzar
                continue
            #Si el nodo siguiente tiene un valor nulo o su costo es menor al costo siguiente
            elif (siguienteNodo is None) or (costo < costoSiguiente):
                #El siguiente nodo adquiere el valor del nodo que le prosigue al anterior
                siguienteNodo = nodo
                #El costo se actualiza por realizar el avance al siguiente nodo
                costoSiguiente = costo

        #Se actualiza el camino actual en una lista
        caminoActual.append(siguienteNodo)
        #Se actualiza el costo actual por el avance entre nodos
        costoActual += costoSiguiente
    #Retorno del camino a considerar del grafo y tambien de su costo por los avances hechos
    return caminoActual, costoActual

#Funcion main donde se ejecutará el programa en su totalidad
if __name__ == '__main__':
    
    #Nodos utilizados para determinar la ruta con menos esfuerzo
    nodoPlayon = "Playon Marin"
    nodoMarin = "Marin"
    nodoEloyAlfaro = "Eloy Alfaro"
    nodoEugenioEspejo = "Eugenio Espejo"
    nodoCasa = "Casa de la Cultura"
    nodoGalo = "Galo Plaza"
    nodoMC = "Manuela Cañizares"
    nodoPUCE = "Universídad Católica del Ecuador"
    nodoParque = "Parque de la Esfera"
    #Primeta ruta a ser considerada
    camino1 = [(nodoPlayon, 1), (nodoMarin, 1), (nodoEloyAlfaro, 1), (nodoEugenioEspejo, 1), (nodoCasa, 1), (nodoGalo, 1), (nodoMC, 1), (nodoPUCE, 1)]
    #Segunda ruta a ser considerada, mostrando su respectivo costo por avance
    camino2 = [(nodoPlayon, 1), (nodoMarin, 1), (nodoEloyAlfaro, 1), (nodoEugenioEspejo, 1), (nodoParque, 1), (nodoPUCE, 1)]
    #Se ejecuta la funcion creada anteriormente con el camino1
    camino1, costo1 = encontrarCamino(nodoPlayon, nodoPUCE, camino1)
    #Se ejecuta la funcion creada anteriormente con el camino2
    camino2, costo2 = encontrarCamino(nodoPlayon, nodoPUCE, camino2)

    #Se muestra los resultados del recorrido al usuario con su respectivo costo
    print("Camino 1: ", camino1, " Costo: ", costo1)
    print("El costo de esfuerzo : ",costo1)
    print("Camino 2: ", camino2, " Costo: ", costo2)
    print("El costo de esfuerzo : ", costo2)
