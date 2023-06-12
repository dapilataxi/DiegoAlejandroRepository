namespace Laboratorio1
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

        //Insertar un nodo al final de la lista
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
            Console.WriteLine("El nuevo dato " + dato + " fue ingresado con exito");
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

        //Eliminar el primer nodo y retorna su contenido
        //Si la lista está vacía, retorna null
        //No se puede eliminar el nodo this, así que lo que se hará
        //es reemplazar el contenido del segundo nodo por el del primero
        //y eliminar el segundo nodo
        public string EliminarPrimero()
        {
            Nodo puntero; //Apuntador que se ubicará en el 2do nodo
            string retorno = null;
            if (!Vacio()) //Solo se puede eliminar si la lista contiene datos
            {
                if (this.sig == null) //Se quiere eliminar el último nodo
                {
                    retorno = this.contenido;
                    this.contenido = null;
                }
                else //Hay al menos 2 nodos en la lista
                {
                    retorno = this.contenido; //Se almacena el contenido
                    puntero = this.sig;
                    //Se copia el contenido del 2do nodo en el 1ro
                    this.contenido = puntero.contenido;
                    //Se hace apunta el primer nodo al 3er nodo
                    this.sig = puntero.sig;
                    puntero.sig = null;
                }
            }
            return retorno;
        }

        public string EliminarAntesDe(string buscado)
        {
            Nodo puntero = this;
            Nodo nodoEliminado;

            if (this.sig == null || this.sig.sig == null)
            {
                // No hay suficientes nodos en la lista
                return null;
            }
            while (puntero.sig.sig != null)
            {
                if (puntero.sig.sig.contenido == buscado)
                {
                    nodoEliminado = puntero.sig;
                    puntero.sig = puntero.sig.sig;
                    nodoEliminado.sig = null;
                    return nodoEliminado.contenido;
                }
                puntero = puntero.sig;
            }

            return null; // Si no se encuentra el elemento buscado, se retorna null
        }

        public string EliminarDespuesDe(string buscado)
        {
            Nodo puntero = this;
            Nodo nodoEliminado;

            while (puntero != null && puntero.contenido != buscado)
            {
                puntero = puntero.sig;
            }

            if (puntero != null && puntero.sig != null)
            {
                nodoEliminado = puntero.sig;
                puntero.sig = nodoEliminado.sig;
                nodoEliminado.sig = null;
                return nodoEliminado.contenido;
            }

            return null; // Si no se encuentra el elemento buscado o no hay un nodo siguiente, se retorna null
        }

        public bool eliminarDesdeHasta(int desde, int hasta)
        {
            Nodo punteroDesde = this;
            Nodo punteroHasta = this;
            if (!Vacio() && desde < hasta && hasta <= this.ContarElementos())
            {
                for (int i = 1; i < desde; i++)
                {
                    punteroDesde = punteroDesde.sig;
                }
                for (int i = 1; i < hasta; i++)
                {
                    punteroHasta = punteroHasta.sig;
                }
                punteroDesde.sig = punteroHasta;
                Console.WriteLine("\n\nSe elimino lo comprendido desde " + punteroDesde.contenido + " hasta " + punteroHasta.contenido + " de manera exitosa");
                return true;

            }
            else
            {
                return false;
            }
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine("Hello, World!");
            string palabra;
            string palabra1;
            Nodo nodo = new Nodo();
            //nodo.InsertarDatosAleatorios();
            nodo.InsertarFinal("b");
            nodo.InsertarFinal("c");
            nodo.InsertarFinal("d");
            nodo.InsertarFinal("e");
            nodo.InsertarInicio("a");
            Console.WriteLine("El numero de nodos es igual a: " + nodo.ContarElementos());
            nodo.Ver();

            //Método implementados para el laboratorio quitar el codigo comentario para comprobar cada una

            /*
            nodo.EliminarPrimero();
            nodo.Ver();
            */

            
            //palabra = nodo.EliminarDespuesDe("b");
            //nodo.Ver();
            //Console.WriteLine("\nEl elemento eliminado fue: " + palabra);
            

            
            //palabra1 = nodo.EliminarAntesDe("b");
            //nodo.Ver();
            //Console.WriteLine("\nEl elemento eliminado fue: " + palabra1);
            

            
            nodo.eliminarDesdeHasta(-1, -2);
            nodo.Ver();
            
        }
    }
}