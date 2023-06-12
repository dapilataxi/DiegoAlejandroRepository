namespace PruebaPracticaDiegoPilataxi
{
    class Nodo
    {
        public string contenido;
        public Nodo sig;

        public Nodo(String dato = null)
        {
            this.contenido = dato;
            this.sig = null;
        }

        public bool Vacio()
        {
            if (this.sig == null && this.contenido == null)
            {
                return true;
            }
            return false;
        }

        public void InsertarFinal(string datoNuevo)
        {
            Nodo nuevo; //Nuevo nodo que se va a insertar
            Nodo puntero = this; //Recorrera la lista hasta el último nodo

            if (Vacio())
            {
                this.contenido = datoNuevo;

            }
            else // Si encuentra nodos creados, desde el siguientees necesario crear un nodo
            {
                while (puntero.sig != null)
                {
                    puntero = puntero.sig;
                }
                nuevo = new Nodo(datoNuevo);
                puntero.sig = nuevo;
            }
            Console.WriteLine("El nuevo dato " + datoNuevo + " fue ingresado de forma exitosa al final de la lista");
        }

        public void InsertarDatosAleatorios()
        {
            InsertarFinal("a");
            InsertarFinal("b");
            InsertarFinal("c");
            InsertarFinal("d");
            InsertarFinal("e");
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

        public void Ver() //Metodo ver que mediante un for recorrera todos los espacios
        {
            if (!Vacio())
            {
                Nodo puntero = this;
                int numElementos = 0;
                numElementos = puntero.ContarElementos();

                Console.WriteLine("\n\nLos elementos de la lista son los siguientes: ");

                for (int i = 0; i < numElementos; i++) //For que servira para volver el
                {
                    Console.Write(" " + puntero.contenido);
                    if (i != (numElementos - 1))
                        Console.Write(" ->");
                    puntero = puntero.sig;
                }
            }
            else
            {
                Console.WriteLine("La lista esta vacia"); //Imprime el mensaje si la lista se encuentra vacia
            }
        }

        public void ConvertirMayúscula()
        {
            Nodo puntero = this;
            if (!Vacio())
            {
                while (puntero != null)
                {
                    puntero.contenido = puntero.contenido.ToUpper();
                    puntero = puntero.sig;
                }

                Console.WriteLine("\n\nCONVERTIDO");
            }
            else
            {
                Console.WriteLine("La lista no contiene elementos.");
            }
        }

        public void InsertarDespues(string dato)
        {
            Nodo nuevoNodo = new Nodo(dato);

            if (this.sig == null)
            {
                this.sig = nuevoNodo;
            }
            else
            {
                Nodo siguienteNodo = this.sig;
                this.sig = nuevoNodo;
                nuevoNodo.sig = siguienteNodo;
            }
        }

        public bool RepetirElemento(string buscado, int num)
        {
            Nodo puntero = this;
            bool encontrado = false;

            if (num < 0)
            {
               Console.WriteLine("\n\nDEBE INGRESAR OBLIGATORIAMENTE UN NUMERO ENTERO POSITVO");
                return false;
            }

            if (!Vacio())
            {
                while (puntero != null)
                {
                    if (puntero.contenido == buscado)
                    {
                        encontrado = true;
                        break;
                    }
                    puntero = puntero.sig;
                }

                if (encontrado)
                {
                    for (int i = 0; i < num; i++)
                    {
                        InsertarDespues(buscado);
                    }

                    return true;
                }
                else
                {
                    Console.WriteLine("\n\nEl elemento buscado no se encuentra en la lista.");
                    return false;
                }
            }
            else
            {
                Console.WriteLine("La lista no contiene elementos.");
                return false;
            }
        }

    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Nodo nodo = new Nodo();

            nodo.InsertarDatosAleatorios();
            nodo.Ver();
            nodo.RepetirElemento("c", 2);
            nodo.Ver();
            nodo.ConvertirMayúscula();
            nodo.Ver();
        }
    }
}