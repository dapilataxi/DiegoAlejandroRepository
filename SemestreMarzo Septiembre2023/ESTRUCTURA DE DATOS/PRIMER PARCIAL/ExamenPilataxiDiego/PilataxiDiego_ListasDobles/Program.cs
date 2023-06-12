namespace PilataxiDiego_ListasDobles
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
                Nodo puntero = ini.Sig;     
                Nodo nuevo = new Nodo(dato);

                Conectar(ini, nuevo, puntero);

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
                Nodo puntero = fin.Ant;    
                Nodo nuevo = new Nodo(dato);

                Conectar(puntero, nuevo, fin);

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

            public void InsertarExtremos(string dato)
            {
                Nodo puntero = ini.Sig;
                Nodo nuevo = new Nodo(dato);

                Conectar(ini, nuevo, puntero);

                Nodo puntero1 = fin.Ant;
                Nodo nuevo1 = new Nodo(dato);

                Conectar(puntero1, nuevo1, fin); ;   
            }

        }
        internal class Program
        {
            static void Main(string[] args)
            {
                ListaDoble listaD = new ListaDoble();
                listaD.InsertarInicio("a");
                listaD.InsertarFinal("b");
                listaD.InsertarFinal("c");
                listaD.InsertarFinal("d");

                listaD.VerIniFin();

                listaD.InsertarExtremos("y");

                listaD.VerIniFin();

            }
        }
    }
}