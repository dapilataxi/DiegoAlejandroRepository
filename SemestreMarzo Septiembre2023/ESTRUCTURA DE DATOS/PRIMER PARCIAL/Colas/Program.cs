using System.Diagnostics.Metrics;

namespace Colas
{
    class Cola  //Nodo de la cola
    {
        protected string contenido;
        protected Cola siguiente;
        protected int prioridad;

        public Cola (string dato = null, int prioridad = 10)
        {
            this.contenido = dato;
            this.siguiente = null;
            this.prioridad = prioridad;
        }

        //Retorna true si la cola no tiene elemetos
        public bool Vacia()
        {
            if (this.contenido == null && this.siguiente == null)
            {
                return true;
            }
            return false;
        }

        //Funcionamiento como en una cola, primero sigue avanzando
        //Los nodos siguientes toman el lugar de su predecesor
        public void Insertar(string dato, int p = 10)
        {
            Cola nuevo;
            Cola ap = this;

            if (Vacia())
            {
                this.contenido = dato;
                this.prioridad = p;
            }
            else  //Funciona para dos o mas nodos
            {
                nuevo = new Cola(this.contenido, this.prioridad);
                nuevo.siguiente = this.siguiente;
                nuevo.prioridad = this.prioridad;
                this.siguiente = nuevo;
                this.contenido = dato;
                this.prioridad = p;
            }
        }

        public string Eliminar()
        {
            Cola ap = this;
            string retorno = null;

            if (!Vacia())  //Al menos hay un nodo
            {
                if (this.siguiente != null) //Al menos hay dos nodos
                {
                    while (ap.siguiente.siguiente != null)
                    {
                        ap = ap.siguiente;  //ap llegara al penultimo
                    }
                    retorno = ap.siguiente.contenido;
                    ap.siguiente = null;
                }
                else  //solo quedan 1 nodo
                {
                    retorno = this.contenido;
                    this.contenido = null;
                }
            }
            return retorno;
        }

        public int Contar()
        {
            Cola puntero = this;
            int contador = 0;
            if (!Vacia())
            {
                while (puntero != null)
                {
                    puntero = puntero.siguiente;
                    contador++;
                }
            }
            return contador;
        }

        public void Ver1()
        {
            Cola puntero = this;
            int contar = Contar();

            if (!Vacia())
            {
                Console.WriteLine("ELEMENTOS DE LA COLA: ");

                while (contar != 0)
                {
                    for (int i = 0; i < contar - 1; i++)  
                    {
                        puntero = puntero.siguiente;
                    }

                    if (puntero != null && puntero.contenido != null)  
                    {
                        Console.Write(puntero.contenido);
                    }

                    contar--;
                    puntero = this;

                    if (contar != 0 && puntero.contenido != null)  
                    {
                        Console.Write(", ");
                    }
                }
            }
            else
            {
                Console.WriteLine("COLA VACIA");
            }
        }

        public Cola Copiar()
        {
            Cola retorno = new Cola();
            Cola nuevo; //Nuevo nodo a insertarse
            Cola ap = this;
            Cola ap1 = retorno;
            
            while (ap != null) //Recorre la cola hasta el ultimo nodo
            {
                if (ap == this) //cuando hay solo un nodo
                {
                    retorno.contenido = ap.contenido;
                    ap1 = retorno;
                }
                else  //dos nodos o mas
                {
                    nuevo = new Cola(ap.contenido);
                    ap1.siguiente = nuevo;
                    ap1 = ap1.siguiente;
                }
                ap = ap.siguiente;
            }
            return retorno;
        }

        public void Ver2()
        {
            Cola c; //Se almacenara la cola ordenada 
            //Comprueba que la cola tenga elementos
            if (Vacia())
            {
                Console.WriteLine("Cola sin elementos");
            }
            else
            {
                Console.Write("Los elementos de la cola son: ");
                c = this.Copiar();
                while (!c.Vacia())
                {
                    if (c.Contar() == 1)
                    {
                        Console.Write(c.Eliminar());
                    }
                    else
                    {
                        Console.Write(c.Eliminar() + ", ");
                    }
                }
                Console.WriteLine();
            }
        }

        public void Organizar()
        {
            Cola ap = this; //Apunta al primer nodo
            string a, b;
            int pri, pri2;
            if (!Vacia())
            {
                while (ap.siguiente != null)  //recorre la cola
                {
                    while (ap.prioridad < ap.siguiente.prioridad)
                    {
                        pri = ap.prioridad;
                        pri2 = ap.siguiente.prioridad;
                        a = ap.contenido;
                        b = ap.siguiente.contenido;
                        ap.siguiente.contenido = a;
                        ap.siguiente.prioridad = pri;
                        ap.prioridad = pri2;
                        ap.contenido = b;
                        ap = this;
                    }
                    ap = ap.siguiente;
                }
            }
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Cola cola = new Cola();

            cola.Insertar("a",100);
            cola.Insertar("b",8);
            cola.Insertar("c",101);
            cola.Insertar("d",1);
            cola.Insertar("e",1);

            cola.Ver1();
            Console.WriteLine("\nLa cola tiene " + cola.Contar() + " elementos");

            Cola Ncola = cola.Copiar();
            Console.WriteLine("\nLa cola copiada es: ");
            Ncola.Ver1();

            Console.WriteLine();
            cola.Organizar();
            cola.Ver2();
        }
    }
}