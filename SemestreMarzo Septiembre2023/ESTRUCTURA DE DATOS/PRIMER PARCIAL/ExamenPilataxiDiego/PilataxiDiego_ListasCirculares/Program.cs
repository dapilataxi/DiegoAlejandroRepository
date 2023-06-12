namespace PilataxiDiego_ListasCirculares
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

        public int EliminarLongitud(int longitud)
        {
            int elementosEliminados = 0;
            NodoC puntero = this;

            if (Vacia())
            {
                Console.WriteLine("La lista está vacía. No se encontraron elementos para eliminar.");
                return elementosEliminados;
            }

            if (puntero.contenido.Length == longitud)
            {
                puntero = puntero.siguiente;
                this.contenido = puntero.contenido;
                this.siguiente = puntero.siguiente;
                elementosEliminados++;
            }

            while (puntero.siguiente != this)
            {
                if (puntero.siguiente.contenido.Length == longitud)
                {
                    NodoC nodoEliminar = puntero.siguiente;
                    puntero.siguiente = nodoEliminar.siguiente;
                    elementosEliminados++;
                }
                else
                {
                    puntero = puntero.siguiente;
                }
            }
            if (elementosEliminados == 0)
            {
                Console.WriteLine("No se encontraron elementos con la longitud ingresada.");
            }

            return elementosEliminados;
        }


    }
    internal class Program
    {
        static void Main(string[] args)
        {
            NodoC listaC = new NodoC();

            listaC.InsertarInicio("a");
            listaC.InsertarFinal("bee");
            listaC.InsertarFinal("cwe");
            listaC.InsertarFinal("d");

            listaC.Ver();

            listaC.EliminarLongitud(3);


            listaC.Ver();
        }
    }
}