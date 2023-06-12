namespace PilataxiDiego_ListasSimples
{
    class Nodo
    {
        public string contenido;
        public Nodo sig;

        //Constructor de un nodo con información o de un nodo vacío
        public Nodo(String dato = null)
        {
            this.contenido = dato;
            this.sig = null;
        }

        //Método  vacio que me sirve para verificar si la lista tiene datos o está vacía
        public bool Vacio()
        {
            if (this.sig == null && this.contenido == null)
            {
                return true;
            }
            return false;
        }

        public void InsertarInicio(string dato)
        {
            Nodo nuevo;
            if (Vacio())
            {
                contenido = dato;
            }
            else
            {
                nuevo = new Nodo(this.contenido);
                this.contenido = dato;
                nuevo.sig = this.sig;
                this.sig = nuevo;
            }
        }

        public void InsertarFinal(string datoNuevo)
        {
            Nodo nuevo;
            Nodo puntero = this;

            if (Vacio())
            {
                this.contenido = datoNuevo;

            }
            else
            {
                while (puntero.sig != null)
                {
                    puntero = puntero.sig;
                }
                nuevo = new Nodo(datoNuevo);
                puntero.sig = nuevo;
            }
        }

        public int ContarElementos()
        {
            int contador = 0;
            Nodo puntero = this;

            if (!Vacio())
            {
                while (puntero != null)
                {
                    contador++;
                    puntero = puntero.sig;
                }
            }
            return contador;
        }

        public void Ver()
        {
            if (!Vacio())
            {
                Nodo puntero = this;
                int numElementos = 0;
                numElementos = puntero.ContarElementos();

                Console.WriteLine("\nLos elementos de la lista son los siguientes: ");

                for (int i = 0; i < numElementos; i++)
                {
                    Console.Write(" " + puntero.contenido);
                    if (i != (numElementos - 1))
                        Console.Write(" ->");
                    puntero = puntero.sig;
                }
            }
            else
            {
                Console.WriteLine("La lista esta vacia");
            }
        }
        public bool InsertarAntesDespuesPosicion(int posicion, string dato)
        {
            Nodo puntero = this;
            int contador = 0;

            while (puntero != null)
            {
                if (contador == posicion - 1)
                {
                    Nodo nodoExistente = puntero.sig;
                    Nodo nuevoAntes = new Nodo(dato);
                    Nodo nuevoDespues = new Nodo(dato);

                    nuevoAntes.sig = nodoExistente;
                    puntero.sig = nuevoAntes;
                    nuevoDespues.sig = nodoExistente.sig;
                    nodoExistente.sig = nuevoDespues;

                    return true;
                }

                puntero = puntero.sig;
                contador++;
            }

            return false;
        }


    }



    internal class Program
    {
        static void Main(string[] args)
        {
            Nodo lista = new Nodo();

            lista.InsertarInicio("a");
            lista.InsertarFinal("b");
            lista.InsertarFinal("c");
            lista.InsertarFinal("d");
            lista.InsertarFinal("e");
            lista.InsertarFinal("f");

            lista.Ver();

            lista.InsertarAntesDespuesPosicion(3, "ys");

            lista.Ver();
        }
    }
}