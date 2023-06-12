namespace PilataxiDiego_PilasDinamicas
{
    class Pila
    {
        protected string contenido;
        protected Pila siguiente;

        public Pila(string dato = null)
        {
            this.contenido = dato;
            siguiente = null;
        }

        //True si esta vacia
        public bool Vacia()
        {
            if (siguiente == null && contenido == null)
            {
                return true;
            }
            return false;
        }

        //Agregar un elemento a la Pila
        public void Push(string dato)
        {
            Pila puntero = this;
            Pila nuevo;
            while (puntero.siguiente != null)
            {
                puntero = puntero.siguiente;
            }
            nuevo = new Pila(dato); //Aqui creo el Nodo
            puntero.siguiente = nuevo; //Crea la flecha del anterior al NuevoNodo
        }

        //Elimina un elemento de la pila, devuelve el elemento eliminado
        public string Pop()
        {
            string retorno = null;
            Pila puntero = this;
            Pila nodoFinal = this;

            if (!Vacia())
            {
                while (puntero.siguiente != null)
                {
                    puntero = puntero.siguiente; //Aqui llegamos hasta el ulimo nodo antes de null
                }
                while (nodoFinal.siguiente != puntero) //Pero aqui vamos hacia el nodo uno antes del
                {
                    nodoFinal = nodoFinal.siguiente;
                }
                retorno = puntero.contenido;
                nodoFinal.siguiente = null; //Desconectamos el nodo y deja de existir
            }
            return retorno;
        }

        public int Contar()
        {
            int contador = 0;
            Pila puntero = this;

            if (!Vacia())
            {
                while (puntero.siguiente != null)
                {
                    puntero = puntero.siguiente;
                    contador++;
                }
            }
            return contador;
        }

        public void Ver()
        {
            if (Vacia())
            {
                Console.WriteLine("PILA VACIA");
            }
            else
            {
                Pila puntero = this;
                int contar = Contar();

                Console.WriteLine("\nELEMENTOS DE LA PILA: ");

                while (contar != 0)
                {
                    for (int i = 0; i < contar; i++)
                    {
                        puntero = puntero.siguiente;
                    }
                    Console.Write(puntero.contenido);
                    contar--;
                    puntero = this;

                    if (contar != 0)
                    {
                        Console.Write(" -> ");
                    }
                }
            }
        }

        public Pila InvertirDobleElemento()
        {
            Pila nuevaPila = new Pila();
            Pila puntero = this;

            while (!puntero.Vacia())
            {
                string dato = puntero.Pop();
                nuevaPila.Push(dato);
                nuevaPila.Push(dato);
            }

            return nuevaPila;
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Pila pila = new Pila();

            pila.Push("a");
            pila.Push("b");
            pila.Push("c");
            pila.Push("d");

            pila.Ver();

            Pila pilaE = pila.InvertirDobleElemento();

            pilaE.Ver();

        }
    }
}