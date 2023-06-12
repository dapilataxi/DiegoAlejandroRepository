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

        public void InsertarInicio(Pelicula pelicula)
        {
            Nodo nuevo;
            if (Vacio())
            {
                contenido = pelicula;
            }
            else
            {
                nuevo = new Nodo(this.contenido);
                this.contenido = pelicula;
                nuevo.sig = this.sig;
                this.sig = nuevo;
            }
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

        public bool Eliminar(string nombrePelicula)
        {
            if (Vacio())
            {
                Console.WriteLine("La lista está vacía. No se puede eliminar la película.");
                return false;
            }

            if (this.contenido.Nombre == nombrePelicula)
            {
                this.contenido = null;
                this.sig = null;
                Console.WriteLine("La película \"" + nombrePelicula + "\" ha sido eliminada.");
                return true;
            }

            Nodo puntero = this;
            while (puntero.sig != null)
            {
                if (puntero.sig.contenido.Nombre == nombrePelicula)
                {
                    puntero.sig = puntero.sig.sig;
                    Console.WriteLine("La película \"" + nombrePelicula + "\" ha sido eliminada.");
                    return true;
                }
                puntero = puntero.sig;
            }

            Console.WriteLine("La película \"" + nombrePelicula + "\" no se encontró en la lista.");
            return false;
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


    internal class Program
    {
        static void Main(string[] args)
        {
            Nodo lista = new Nodo();

            bool salir = false;
            while (!salir)
            {
                Console.WriteLine("\n-- Menú --");
                Console.WriteLine("1. Ingresar el nombre y el año de la película");
                Console.WriteLine("2. Mostrar las películas ingresadas por el usuario");
                Console.WriteLine("3. Eliminar películas");
                Console.WriteLine("4. Salir");
                Console.WriteLine("Ingrese la opción deseada:");

                string opcion = Console.ReadLine();

                switch (opcion)
                {
                    case "1":
                        Console.WriteLine("Ingrese el nombre de la película:");
                        string nombre = Console.ReadLine();
                        Console.WriteLine("Ingrese el año de la película:");
                        int año = int.Parse(Console.ReadLine());
                        Pelicula pelicula = new Pelicula(nombre, año);
                        lista.InsertarFinal(pelicula);
                        Console.WriteLine("La película fue ingresada con éxito.");
                        break;
                    case "2":
                        lista.Ver();
                        break;
                    case "3":
                        //Metodo eliminar
                        break;
                    case "4":
                        salir = true;
                        break;
                    default:
                        Console.WriteLine("Opción inválida. Intente nuevamente.");
                        break;
                }
            }
        }
    }
}