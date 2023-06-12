namespace ListasDobles
{
    class Nodo
    {
        protected string contenido;   //Contenido del nodo
        protected Nodo sig;           //Referencia al siguiente nodo
        protected Nodo ant;           //Referencia al nodo anterior

        //Constructor
        public Nodo(string dato)
        {
            this.sig = null;
            this.ant = null;
            this.contenido = dato;
        }

        //Creacion de get y set para acceder a cambiar y obtener datos
        public Nodo Sig
        {
            get { return this.sig; }
            set { this.sig = value; }
        }

        public Nodo Ant
        {
            get { return this.ant; }
            set { this.ant = value; }
        }

        public string Contenido
        {
            get { return this.contenido; }
            set { this.contenido = value; }
        }

        class ListaDoble
        {
            public Nodo ini;      //Puntero al primer nodo
            public Nodo fin;      //Puntero al último nodo

            public ListaDoble()
            {
                ini = new Nodo(null);
                fin = new Nodo(null);
                ini.Sig = fin;
                fin.Ant = ini;
            }

            public void InsertarInicio(string dato)
            {
                Nodo puntero = ini.Sig;     //Apuntará siempre al segundo nodo
                Nodo nuevo = new Nodo(dato);

                //Conectar nodos en la lista doble
                Conectar(ini, nuevo, puntero);

                /* ini.Sig = nuevo;
                 nuevo.Sig = puntero;
                 puntero.Ant = nuevo;
                 nuevo.Ant = ini;*/
            }

            public void Conectar(Nodo A, Nodo B, Nodo C)
            {
                A.Sig = B;
                B.Sig = C;
                C.Ant = B;
                B.Ant = A;
            }

            public void InsertarFinal(string dato)
            {
                Nodo puntero = fin.Ant;    //Apuntara siempre al primer nodo
                Nodo nuevo = new Nodo(dato);

                //Conectar nodos en la lista doble
                Conectar(puntero, nuevo, fin);

                /*fin.Ant = nuevo;
                nuevo.Ant = puntero;
                puntero.sig = nuevo;
                nuevo.sig = fin;*/
            }

            public bool Vacio()
            {
                bool retorno = false;

                if (ini.Sig == fin && fin.ant == ini && ini.Contenido == null && fin.Contenido == null)
                {
                    retorno = true;
                }
                return retorno;
            }

            public void VerIniFin()
            {
                Nodo puntero = ini.Sig;
                if (Vacio())
                {
                    Console.WriteLine("La lista no tiene elementos");
                }
                else
                {
                    Console.WriteLine("Los elementos de la lista son: ");
                    while (puntero != fin)
                    {
                        Console.Write(puntero.Contenido);
                        if (puntero.Sig != fin)
                        {
                            Console.Write(" <-> ");
                        }
                        puntero = puntero.Sig;
                    }
                    Console.WriteLine();
                }
            }

            public void VerFinIni()
            {
                Nodo puntero = fin.Ant;
                if (Vacio())
                {
                    Console.WriteLine("La lista no tiene elementos");
                }
                else
                {
                    Console.WriteLine("\nLos elementos de la lista son: ");
                    while (puntero != ini)
                    {
                        Console.Write(puntero.Contenido);
                        if (puntero.Ant != ini)
                        {
                            Console.Write(" <-> ");
                        }
                        puntero = puntero.Ant;
                    }
                }
            }

            public int Contar()
            {
                int contador = 0;
                Nodo puntero = ini.Sig;

                if (!Vacio())
                {
                    while (puntero != fin)
                    {
                        contador++;
                        puntero = puntero.sig;
                    }
                }
                return contador;
            }

            public int NumVeces(string buscado)
            {
                int contador = 0;
                Nodo puntero = ini.Sig;

                if (!Vacio())
                {
                    while (puntero != fin)
                    {
                        if (puntero.Contenido == buscado)
                        {
                            contador++;
                        }
                        puntero = puntero.sig;
                    }
                }
                return contador;
            }

            public void ReemplazarElementos(string buscado, string nuevo)
            {
                Nodo puntero = ini.Sig;
                int contador = 0;

                if (!Vacio())
                {
                    while (puntero != fin)
                    {
                        if (puntero.Contenido == buscado)
                        {
                            contador++;
                            if (contador == 1)
                            {
                                puntero.Contenido = nuevo;
                            }
                        }
                        puntero = puntero.sig;
                    }
                }
            }

            public void InsertarLD(string dato, int posicion)

            {

                int contador = 0;

                Nodo nuevo;

                Nodo puntero = ini.Sig;



                while (contador < posicion - 1)

                {

                    puntero = puntero.Sig;

                    contador++;

                }



                nuevo = new Nodo(dato);

                nuevo.Sig = puntero.Sig;

                puntero.Sig.Ant = nuevo;

                nuevo.Ant = puntero;

                puntero.Sig = nuevo;

            }
        }
        internal class Program
        {

            static void Main(string[] args)
            {
                ListaDoble lista = new ListaDoble();

                lista.InsertarInicio("a");
                lista.InsertarFinal("b");
                lista.InsertarFinal("c");
                lista.InsertarFinal("d");
                lista.InsertarFinal("e");
                lista.InsertarLD("y", 3);
                lista.VerIniFin();

                /*
                //Incio a Fin
                lista.VerIniFin();
                Console.WriteLine("\nLa lista tiene " + lista.Contar() + " elementos ");
                Console.WriteLine("La letra b se repite " + lista.NumVeces("b"));
                lista.ReemplazarElementos("b", "y");
                lista.VerIniFin();
                */
            }
        }
    }
}