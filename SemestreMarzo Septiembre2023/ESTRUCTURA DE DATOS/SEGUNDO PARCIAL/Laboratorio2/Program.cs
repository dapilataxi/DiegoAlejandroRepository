namespace Laboratorio2
{
    class Nodo
    {
        public Pelicula contenido;
        public Nodo sig;

        public Nodo(Pelicula pelicula = null)
        {
            this.contenido = pelicula;
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

        public void InsertarFinal(Pelicula pelicula)
        {
            Nodo nuevo;
            Nodo puntero = this;

            if (Vacio())
            {
                this.contenido = pelicula;

            }
            else
            {
                while (puntero.sig != null)
                {
                    puntero = puntero.sig;
                }
                nuevo = new Nodo(pelicula);
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
                Console.WriteLine("\nLos elementos de la lista son los siguientes: ");

                while (puntero != null)
                {
                    Console.WriteLine("Nombre: " + puntero.contenido.Nombre + ", Año: " + puntero.contenido.Año);
                    puntero = puntero.sig;
                }
            }
            else
            {
                Console.WriteLine("La lista está vacía");
            }
        }

        public void VerTabla()
        {
            if (!Vacio())
            {
                Nodo puntero = this;

                while (puntero != null)
                {
                    Console.ForegroundColor = ConsoleColor.Yellow;
                    Console.WriteLine($"| {puntero.contenido.Nombre,-25} | {puntero.contenido.Año,20} |");
                    puntero = puntero.sig;
                }
            }
            else
            {
                Console.WriteLine("No hay ningún registro de alguna pelicula");
            }
        }

        public bool Eliminar(string nombrePelicula)
        {
            if (Vacio())
            {
                Console.WriteLine("La lista está vacía. No se puede eliminar la película.");
                return false;
            }

            if (this.contenido.Nombre == nombrePelicula)
            {
                if (this.sig == null)
                {
                    this.contenido = null;
                    Console.WriteLine("La película \"" + nombrePelicula + "\" ha sido eliminada.");
                    return true;
                }
                else
                {
                    this.contenido = this.sig.contenido;
                    this.sig = this.sig.sig;
                    Console.WriteLine("La película \"" + nombrePelicula + "\" ha sido eliminada.");
                    return true;
                }
            }

            Nodo puntero = this;
            while (puntero.sig != null)
            {
                if (puntero.sig.contenido.Nombre == nombrePelicula)
                {
                    Nodo nodoEliminado = puntero.sig;
                    puntero.sig = nodoEliminado.sig;
                    nodoEliminado.sig = null;
                    nodoEliminado.contenido = null;
                    Console.WriteLine("La película \"" + nombrePelicula + "\" ha sido eliminada.");
                    return true;
                }
                puntero = puntero.sig;
            }

            Console.WriteLine("La película \"" + nombrePelicula + "\" no se encontró en la lista.");
            return false;
        }

        public void ordenarBurbujaNombre()
        {
            Nodo puntero = this;
            int n = this.ContarElementos();
            bool intercambio;
            Pelicula aux;
            for (int i = 0; i < n - 1; i++)
            {
                puntero = this;
                intercambio = false;
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (puntero.contenido.Nombre.CompareTo(puntero.sig.contenido.Nombre) == 1)
                    {
                        aux = puntero.contenido;
                        puntero.contenido = puntero.sig.contenido;
                        puntero.sig.contenido = aux;
                        intercambio = true;
                    }
                    puntero = puntero.sig;
                }
                if (!intercambio)
                {
                    break;
                }
            }
        }

        public void ordenarBurbujaAño()
        {
            Nodo puntero = this;
            int n = this.ContarElementos();
            bool intercambio;
            Pelicula aux;
            for (int i = 0; i < n - 1; i++)
            {
                puntero = this;
                intercambio = false;
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (puntero.contenido.Año.CompareTo(puntero.sig.contenido.Año) == 1)
                    {
                        aux = puntero.contenido;
                        puntero.contenido = puntero.sig.contenido;
                        puntero.sig.contenido = aux;
                        intercambio = true;
                    }
                    puntero = puntero.sig;
                }
                if (!intercambio)
                {
                    break;
                }
            }
        }

        public void shellSortNombre()
        {
            Nodo puntero1 = this;
            Nodo puntero2 = this;
            Nodo puntero3 = this;
            int n = this.ContarElementos();
            int gap = n / 2;
            while (gap > 0)
            {
                puntero1 = this;
                for (int k = 0; k < gap; k++)
                {
                    puntero1 = puntero1.sig;
                }
                for (int i = gap; i < n; i++)
                {
                    Pelicula temp = puntero1.contenido;
                    int j = i;
                    puntero2 = puntero1;
                    puntero3 = this;
                    for (int k = 0; k < j - gap; k++)
                    {
                        puntero3 = puntero3.sig;
                    }
                    while (j >= gap && puntero3.contenido.Nombre.CompareTo(temp.Nombre) == 1)
                    {
                        puntero2.contenido = puntero3.contenido;
                        j -= gap;
                        puntero2 = this;
                        for (int k = 0; k < j; k++)
                        {
                            puntero2 = puntero2.sig;
                        }
                        puntero3 = this;
                        for (int k = 0; k < j - gap; k++)
                        {
                            puntero3 = puntero3.sig;
                        }
                    }
                    puntero2.contenido = temp;
                    puntero1 = puntero1.sig;
                }
                gap /= 2;
            }
        }

        public void shellSortAño()
        {
            Nodo puntero1 = this;
            Nodo puntero2 = this;
            Nodo puntero3 = this;
            int n = this.ContarElementos();
            int gap = n / 2;
            while (gap > 0)
            {
                puntero1 = this;
                for (int k = 0; k < gap; k++)
                {
                    puntero1 = puntero1.sig;
                }
                for (int i = gap; i < n; i++)
                {
                    Pelicula temp = puntero1.contenido;
                    int j = i;
                    puntero2 = puntero1;
                    puntero3 = this;
                    for (int k = 0; k < j - gap; k++)
                    {
                        puntero3 = puntero3.sig;
                    }
                    while (j >= gap && puntero3.contenido.Año.CompareTo(temp.Año) == 1)
                    {
                        puntero2.contenido = puntero3.contenido;
                        j -= gap;
                        puntero2 = this;
                        for (int k = 0; k < j; k++)
                        {
                            puntero2 = puntero2.sig;
                        }
                        puntero3 = this;
                        for (int k = 0; k < j - gap; k++)
                        {
                            puntero3 = puntero3.sig;
                        }
                    }
                    puntero2.contenido = temp;
                    puntero1 = puntero1.sig;
                }
                gap /= 2;
            }
        }

        public void OrdenarPorAño()
        {
            int cantidadElementos = ContarElementos();
            QuickSort(this, 0, cantidadElementos - 1);
        }

        private void QuickSort(Nodo inicio, int ini, int fin)
        {
            if (ini < fin)
            {
                int posicionCorrecta = UbicarPivote(inicio, ini, fin);
                QuickSort(inicio, ini, posicionCorrecta - 1);
                QuickSort(inicio, posicionCorrecta + 1, fin);
            }
        }

        private int UbicarPivote(Nodo inicio, int ini, int fin)
        {
            Pelicula pivote = EncontrarPelicula(inicio, fin);
            int i = ini - 1;

            for (int j = ini; j < fin; j++)
            {
                Pelicula aux = EncontrarPelicula(inicio, j);
                if (aux.Año < pivote.Año)
                {
                    i++;
                    Intercambio(EncontrarNodo(inicio, i), EncontrarNodo(inicio, j));
                }
            }
            Intercambio(EncontrarNodo(inicio, i + 1), EncontrarNodo(inicio, fin));
            return i + 1;
        }

        private Nodo EncontrarNodo(Nodo inicio, int indice)
        {
            Nodo puntero = inicio;
            for (int i = 0; i < indice; i++)
            {
                puntero = puntero.sig;
            }
            return puntero;
        }

        private Pelicula EncontrarPelicula(Nodo inicio, int index)
        {
            return EncontrarNodo(inicio, index).contenido;
        }

        private void Intercambio(Nodo nodo1, Nodo nodo2)
        {
            Pelicula temp = nodo1.contenido;
            nodo1.contenido = nodo2.contenido;
            nodo2.contenido = temp;
        }

        public void OrdenarPorNombre()
        {
            int cantidadElementos = ContarElementos();
            QuickSortN(this, 0, cantidadElementos - 1);
        }

        private void QuickSortN(Nodo inicio, int left, int right)
        {
            if (left < right)
            {
                int pivotIndex = UbicarPivote2(inicio, left, right);
                QuickSortN(inicio, left, pivotIndex - 1);
                QuickSortN(inicio, pivotIndex + 1, right);
            }
        }

        private int UbicarPivote2(Nodo inicio, int ini, int fin)
        {
            Pelicula pivot = EncontrarPelicula(inicio, fin);
            int i = ini - 1;

            for (int j = ini; j < fin; j++)
            {
                Pelicula current =EncontrarPelicula(inicio, j);
                if (string.Compare(current.Nombre, pivot.Nombre) < 0)
                {
                    i++;
                    Intercambio(EncontrarNodo(inicio, i), EncontrarNodo(inicio, j));
                }
            }

            Intercambio(EncontrarNodo(inicio, i + 1), EncontrarNodo(inicio, fin));
            return i + 1;
        }
    }
    public class Pelicula
    {
        public string Nombre { get; set; }
        public int Año { get; set; }

        public Pelicula(string nombre, int año)
        {
            Nombre = nombre;
            Año = año;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Nodo lista = new Nodo();
            bool volverMenuPrincipal = false;

            bool salir = false;
            while (!salir)
            {
                Console.Clear();
                Console.ForegroundColor = ConsoleColor.Green;
                Console.Write(@" 
                
                ░░░░░██╗░░░░█████╗░░░░██████╗░
                ░░░░░██║░░░██╔══██╗░░░██╔══██╗
                ░░░░░██║░░░██║░░╚═╝░░░██║░░██║
                ██╗░░██║░░░██║░░██╗░░░██║░░██║
                ╚█████╔╝██╗╚█████╔╝██╗██████╔╝
                ░╚════╝░╚═╝░╚════╝░╚═╝╚═════╝░                      
                ");
                Console.ForegroundColor = ConsoleColor.White;
                Console.WriteLine(@"                                 
                    █▀▄▀█ █▀█ █░█ █ █▀▀ █▀
                    █░▀░█ █▄█ ▀▄▀ █ ██▄ ▄█
                ");
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.WriteLine("\n-- Menú --");
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("1. Ingresar el nombre y el año de la película");
                Console.WriteLine("2. Mostrar las películas ingresadas por el usuario");
                Console.WriteLine("3. Eliminar películas");
                Console.WriteLine("4. Ordenar peliculas");
                Console.WriteLine("5. Salir");
                Console.ForegroundColor = ConsoleColor.Yellow;
                Console.Write("Ingrese la opción deseada: ");
                Console.ForegroundColor = ConsoleColor.White;
                string opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1":
                        Console.Clear();
                        Console.Write("Ingrese el nombre de la película: ");
                        string nombre = Console.ReadLine();
                        Console.Write("Ingrese el año de la película: ");
                        string añoString = Console.ReadLine();
                        int año;
                        bool esNumero = int.TryParse(añoString, out año);

                        if (esNumero && año > 0)
                        {
                            Pelicula pelicula = new Pelicula(nombre, año);
                            lista.InsertarFinal(pelicula);
                            Console.WriteLine("La película fue ingresada con éxito.");
                        }
                        else
                        {
                            Console.WriteLine("Año ingresado no válido.");
                        }
                        break;

                    case "2":
                        Console.Clear();
                        Console.WriteLine("\n-- Películas ingresadas --");

                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("-------------------------------------------------");
                        Console.WriteLine("|   Nombre de la película   |   Año de la película  |");
                        Console.WriteLine("-------------------------------------------------");
                        lista.VerTabla();
                        Console.ForegroundColor = ConsoleColor.Red;
                        Console.WriteLine("-------------------------------------------------");
                        break;

                    case "3":
                        Console.Clear();
                        Console.Write("Ingrese el nombre de la película que desea eliminar: ");
                        string nombreEliminar = Console.ReadLine();
                        bool eliminada = lista.Eliminar(nombreEliminar);
                        if (!eliminada)
                        {
                            Console.WriteLine("La película \"" + nombreEliminar + "\" no se encontró en la lista.");
                        }
                        break;

                    case "4":
                        Console.Clear();
                        Console.WriteLine("-- Ordenar películas --");
                        Console.ForegroundColor = ConsoleColor.Yellow;
                        Console.WriteLine("1. Por nombre");
                        Console.WriteLine("2. Por año");
                        Console.WriteLine("3. Volver al menú principal");
                        Console.ForegroundColor = ConsoleColor.White;
                        Console.Write("Ingrese una opción: ");
                        string opcionOrdenar = Console.ReadLine();

                        switch (opcionOrdenar)
                        {
                            case "1":
                                Console.Clear();
                                Console.WriteLine("-- Seleccione el método de ordenación --");
                                Console.ForegroundColor = ConsoleColor.Yellow;
                                Console.WriteLine("1. Burbuja");
                                Console.WriteLine("2. Shellsort");
                                Console.WriteLine("3. Quicksort");
                                Console.ForegroundColor = ConsoleColor.White;
                                Console.Write("Ingrese una opción: ");
                                string opcion1 = Console.ReadLine();

                                switch (opcion1)
                                {
                                    case "1":
                                        Console.Clear();
                                        lista.ordenarBurbujaNombre();
                                        Console.WriteLine("Las películas han sido ordenadas por nombre con el método Burbuja.");
                                        break;
                                    case "2":
                                        Console.Clear();
                                        lista.shellSortNombre();
                                        Console.WriteLine("Las películas han sido ordenadas por nombre con el método Shellsort.");
                                        break;
                                    case "3":
                                        Console.Clear();
                                        lista.OrdenarPorNombre();
                                        Console.WriteLine("Las películas han sido ordenadas por nombre con el método Quicksort");
                                        break;
                                }
                                break;

                            case "2":
                                Console.Clear();
                                Console.WriteLine("-- Seleccione el método de ordenación --");
                                Console.ForegroundColor = ConsoleColor.Yellow;
                                Console.WriteLine("1. Burbuja");
                                Console.WriteLine("2. Shellsort");
                                Console.WriteLine("3. Quicksort");
                                Console.ForegroundColor = ConsoleColor.White;
                                Console.Write("Ingrese una opción: ");
                                string opcion2 = Console.ReadLine();

                                switch (opcion2)
                                {
                                    case "1":
                                        Console.Clear();
                                        lista.ordenarBurbujaAño();
                                        Console.WriteLine("Las películas han sido ordenadas por año con el método Burbuja.");
                                        break;
                                    case "2":
                                        Console.Clear();
                                        lista.shellSortAño();
                                        Console.WriteLine("Las películas han sido ordenadas por año con el método Shellsort.");
                                        break;
                                    case "3":
                                        Console.Clear();
                                        lista.OrdenarPorAño();
                                        Console.WriteLine("Las películas han sido ordenadas por año con el método Quicksort");
                                        break;
                                }
                                break;

                            case "3":
                                volverMenuPrincipal = true;
                                break;

                            default:
                                Console.WriteLine("Opción inválida. Intente nuevamente.");
                                break;
                        }

                        break;

                    case "5":
                        salir = true;
                        break;

                    default:
                        Console.WriteLine("Opción inválida. Intente nuevamente.");
                        break;
                }
                Console.ForegroundColor = ConsoleColor.Cyan;
                Console.WriteLine("Presione enter para continuar...");
                Console.ReadLine();
            }
        }
    }
}