namespace ListasCirculares
{
    class NodoC
    {
        protected string contenido;
        protected NodoC siguiente;

        //Constructor
        public NodoC(string dato = null)
        {
            this.contenido = dato;
            this.siguiente = this;
        }

        public bool Vacia()
        {
            bool retorno = false;
            if (this.contenido == null && this.siguiente == this)
            {
                retorno = true;
            }
            return retorno;
        }

        public void InsertarInicio(string dato)
        {
            NodoC nuevo;
            if (!Vacia())
            {
                nuevo = new NodoC(this.contenido);
                this.contenido = dato;
                nuevo.siguiente = this.siguiente;
                this.siguiente = nuevo;
            }
            else
            {
                this.contenido = dato;
            }
        }

        public void InsertarFinal(string datoNuevo)
        {
            NodoC nuevo; //Nuevo nodo que se va a insertar
            NodoC puntero = this; //Recorrera la lista hasta el último nodo

            if (!Vacia())
            {
                while (puntero.siguiente != this)
                {
                    puntero = puntero.siguiente;
                }
                nuevo = new NodoC(datoNuevo);
                nuevo.siguiente = this;
                puntero.siguiente = nuevo;

            }
            else // Si encuentra nodos creados, desde el siguientees necesario crear un nodo
            {
                this.contenido = datoNuevo;
            }
        }

        public void Ver() //Metodo ver que mediante un for recorrera todos los espacios
        {
            if (!Vacia())
            {
                NodoC puntero = this;
                int contador = 1;

                //Meidante un while cuento los nodos que tiene mi lista
                while (puntero.siguiente != this)
                {
                    puntero = puntero.siguiente;
                    contador++;
                }

                //Una vez sabiendo cuantos nodos, reinicio el puntero
                puntero = this;

                for (int x = 0; x < contador; x++) //For que servira para volver el apuntador a la raiz
                {
                    Console.Write(" " + puntero.contenido);
                    if (x != (contador - 1))
                    {
                        Console.Write(" =>");
                    }
                    else
                    {
                        Console.WriteLine(" =))");
                    }
                    puntero = puntero.siguiente;
                }
            }
            else
            {
                Console.WriteLine("La lista está vacia"); //Impresion si la pila esta vacia
            }
        }

        public string EliminarPrimero()
        {
            NodoC puntero; //Apuntador que se ubicara en el 2do nodo
            string retorno = null;
            if (!Vacia())
            {
                if (this.siguiente == this) //Se quiere eliminar el ultimo nodo
                {
                    retorno = this.contenido;
                    this.contenido = null;
                }
                else  // Hay almenos 2 nodos en la lista
                {
                    retorno = this.contenido;  //Se almacena el contenido
                    //Se copia el contenido del 2do nodo en el 1ro
                    this.contenido = this.siguiente.contenido;
                    //Se hace apuntar el primer nodo al 3er nodo
                    puntero = this.siguiente;
                    this.siguiente = this.siguiente.siguiente;
                    puntero.siguiente = this;
                }
            }
            return retorno;
        }

        public string EliminarUltimo()
        {
            string retorno = null;
            NodoC puntero = this;
            if (!Vacia())
            {
                if (this.siguiente != this)
                {
                    while (puntero.siguiente.siguiente != this)
                    {
                        puntero = puntero.siguiente;
                    }
                    retorno = puntero.siguiente.contenido;
                    puntero.siguiente = this;
                }
                else
                {
                    retorno = this.contenido;
                    this.contenido = null;
                }
            }
            return retorno;
        }
        public int EliminarLong(int longitud)
        {
            NodoC puntero = this;
            NodoC puntero1 = puntero;
            int elimin = 0;

            if (!Vacia() && longitud > 0) //solo si la lista no se encuentra vacia y la longitud sea valida, es
            {
                while (puntero.siguiente != this)
                {
                    if (puntero.contenido.Length == longitud)  // si esq la longitud del apuntador es la que se
                    {
                        if (puntero == this)  //si se encuentra en el primer nodo
                        {
                            EliminarPrimero();
                            elimin++; //aumenta cuantos eliminados existen
                        }
                        else
                        {
                            while (puntero1.siguiente != puntero)  //cuando hay mas de un nodo, puntero1 llegará
                            {
                                puntero1 = puntero1.siguiente;  //puntero1 recorre
                            }
                            puntero = puntero.siguiente; //puntero1 recorre
                            puntero1.siguiente = puntero;  //puntero1 un nodo antes de ap
                            elimin++; //aumenta cuantos eliminados existen
                        }
                    }
                    else  //si no encuentra coincidencia sigue recorriendo
                    {
                        puntero = puntero.siguiente;
                    }
                }
                if (puntero.siguiente == this && puntero.contenido.Length == longitud)  //cuando esta en la ultima
                {
                    EliminarUltimo();
                    elimin++; //aumenta cuantos eliminados existen
                }
            }
            if (elimin == 0) //Si esq no encuentra coincidencias con lo que se requiere
            {
                Console.WriteLine("No existe el elemento en la lista");
            }
            return elimin;
        }

    }
    internal class Program
    {
        static void Main(string[] args)
        {
            NodoC nodo = new NodoC();

            nodo.InsertarInicio("bbb");
            nodo.InsertarFinal("ccc");
            nodo.InsertarInicio("aaa");
            nodo.InsertarFinal("d");
            nodo.Ver();

            nodo.EliminarLong(3);
            nodo.Ver();
        }
    }
}