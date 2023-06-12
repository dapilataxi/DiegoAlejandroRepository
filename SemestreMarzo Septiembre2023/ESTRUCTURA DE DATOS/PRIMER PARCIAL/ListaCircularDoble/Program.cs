using System;
namespace ListaCircularDoble
{
    class Nodo
    {
        public int dato;
        public Nodo siguiente;
        public Nodo anterior;

        public Nodo(int dato)
        {
            this.dato = dato;
            this.siguiente = null;
            this.anterior = null;
        }
    }

    class ListaCircularDoble
    {
        private Nodo raiz;

        public ListaCircularDoble()
        {
            raiz = null;
        }

        public bool Vacia()
        {
            return raiz == null;
        }

        public void Insertar(int dato)
        {
            Nodo nuevoNodo = new Nodo(dato);

            if (Vacia())
            {
                nuevoNodo.siguiente = nuevoNodo;
                nuevoNodo.anterior = nuevoNodo;
                raiz = nuevoNodo;
            }
            else
            {
                Nodo ultimo = raiz.anterior;

                nuevoNodo.siguiente = raiz;
                nuevoNodo.anterior = ultimo;
                raiz.anterior = nuevoNodo;
                ultimo.siguiente = nuevoNodo;
            }
        }

        public void Mostrar()
        {
            if (Vacia())
            {
                Console.WriteLine("La lista está vacía");
                return;
            }

            Nodo actual = raiz;

            do
            {
                Console.Write(actual.dato + " ");
                actual = actual.siguiente;
            } while (actual != raiz);

            Console.WriteLine();
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            ListaCircularDoble lista = new ListaCircularDoble();

            lista.Insertar(1);
            lista.Insertar(2);
            lista.Insertar(3);

            lista.Mostrar();
        }
    }
}