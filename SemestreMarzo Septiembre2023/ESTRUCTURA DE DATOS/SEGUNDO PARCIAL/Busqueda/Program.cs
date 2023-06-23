using System.ComponentModel;

namespace Busqueda
{
    class Program
    {
        static int BMenor(int[] arr)
        {
            int menor = arr[0];
            int n = arr.Length;
            for (int i = 1; i < n; i++)
            {
                if (arr[i] < menor)
                {
                    menor = arr[i];
                }
            }
            return menor;
        }

        static int BMayor(int[] arr)
        {
            int n = arr.Length;
            int mayor = arr[n - 1];

            for (int i = 0; i < n - 1; i++)
            {
                if (arr[i] > mayor)
                {
                    mayor = arr[i];
                }
            }
            return mayor;
        }

        static void ImprimirLista(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                Console.Write(arr[i] + " ");
            }
            Console.WriteLine();
        }

        static void OrdenamientoBurbuja(int[] arr)
        {
            int n = arr.Length;
            bool intercambio;
            int temp;

            for (int i = 0; i < n - 1; i++)
            {
                intercambio = false;
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (arr[j] > arr[j + 1])
                    {
                        //Realizar el intercambio
                        temp = arr[j];
                        arr[j] = arr[j + 1];
                        arr[j + 1] = temp;
                        intercambio = true;
                    }
                }
                // Si no hubo intercambio en esta pasada, la lista está ordenada
                if (!intercambio)
                {
                    break;
                }
            }
        }

        static int BBinario(int[] arr, int clave)
        {
            int n = arr.Length;
            int bajo = 0;
            int alto = n - 1;

            int central;

            while (bajo <= alto)
            {
                central = (bajo + alto) / 2;
                int valorCentral = arr[central];

                if (clave == valorCentral)
                {
                    return central;
                }

                if (clave < valorCentral)
                {
                    alto = central - 1;
                }

                else
                {
                    bajo = central + 1;
                }
            }
            return -1;
        }

        static void Main(string[] args)
        {
            int[] lista = { 3, 10, 11, 2, 22, 54, 1, 0, -1 };
            Console.WriteLine(BMenor(lista));
            Console.WriteLine(BMayor(lista));

            ImprimirLista(lista);
            OrdenamientoBurbuja(lista);
            ImprimirLista(lista);

            Console.WriteLine(BBinario(lista, 11));
        }
    }
}