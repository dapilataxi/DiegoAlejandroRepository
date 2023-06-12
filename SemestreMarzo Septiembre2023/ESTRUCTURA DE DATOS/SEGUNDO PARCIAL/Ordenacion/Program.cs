namespace Ordenacion
{
    class Program
    {
        static void OrdenarIntercambio(int[] arr)
        {
            int n = arr.Length;

            for (int i = 0; i < n - 1; i++)
            {
                for (int j = i + 1; j < n; j++)
                    {
                        if (arr[i] > arr[j])
                        {
                            //Realizar el intercambio
                            int temp = arr[i];
                            arr[i] = arr[j];
                            arr[j] = temp;
                        }
                    }
            }
        }

        static void ImprimirLista(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
            {
                Console.Write(arr[i] + " ");
            }
            Console.WriteLine();
        }

        static void ImprimirListaString(string[] arr)
        {
            foreach (string elemento in arr)
            {
                Console.Write(elemento + " ");
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
                        arr[j] = arr[j+1];
                        arr[j+1] = temp;
                        intercambio= true;
                    }
                }
                // Si no hubo intercambio en esta pasada, la lista está ordenada
                if (!intercambio)
                {
                    break;
                }
            }
        }

        static void OrdenamientoBurbujaPalabra(string[] arr)
        {
            int n = arr.Length;
            bool intercambio;
            string temp;

            for (int i = 0; i < n - 1; i++)
            {
                intercambio = false;
                for (int j = 0; j < n - i - 1; j++)
                {
                    if (string.Compare(arr[j], arr[j + 1]) > 0)
                    {
                        // Realizar el intercambio
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
        static void InsercionOrdenar(int[] arr)
        {
            int n = arr.Length;

            for (int i = 1; i < n; i++)
            {
                int valorActual = arr[i];
                int j = i - 1;

                while (j >= 0 && arr[j] > valorActual)
                {
                    arr[j + 1] = arr[j];
                    j--;
                }
                arr[j + 1] = valorActual;
            }
        }

        static int UbicarPivote(int[] arr, int ini, int fin)
        {
            int temp = 0;

            while (ini < fin)
            {
                while (arr[fin] >= arr[ini] && ini < fin)
                {
                    fin--;
                }
                temp = arr[ini];
                arr[ini] = arr[fin];
                arr[fin] = temp;

                while (arr[ini] <= arr[fin] && ini < fin)
                {
                    ini++;
                }
                temp = arr[fin];
                arr[fin] = arr[ini];
                arr[ini] = temp;
            }
            return ini;
        }

        static void ShellSortOrdenar(int[] arr)
        {
            int n = arr.Length;
            int gap = n / 2;

            while (gap > 0)
            {
                for (int i = gap; i < n; i++)
                {
                    int temp = arr[i];
                    int j = i;

                    while (j >= gap && arr[j - gap] > temp)
                    {
                        arr[j] = arr[j - gap];
                        j -= gap;
                    }
                    arr[j] = temp;
                }
                gap /= 2;
            }
        }

        static void QuickSort(int[] arr, int ini, int fin)
        {
            if (ini < fin)
            {
                int posiCorrecta = UbicarPivote(arr, ini, fin);
                QuickSort(arr, ini, posiCorrecta - 1);
                QuickSort(arr, posiCorrecta + 1, fin);
            }
        }

        static int[] RadixSort(int[] array)
        {
            int size = array.Length;
            int maxVal = GetMaxVal(array, size);
            for (int exponent = 1; maxVal / exponent > 0; exponent *= 10)
            {
                CountingSort(array, size, exponent);
            }
            return array;
        }

        static void CountingSort(int[] array, int size, int exponent)
        {
            int[] outputArr = new int[size];
            int[] occurences = new int[10];
            for (int i = 0; i < 10; i++)
            {
                occurences[i] = 0;
            }
            for (int i = 0; i < size; i++)
            {
                occurences[(array[i] / exponent) % 10]++;
            }
            for (int i = 1; i < 10; i++)
            {
                occurences[i] += occurences[i - 1];
            }
            for (int i = size - 1; i >= 0; i--)
            {
                outputArr[occurences[(array[i] / exponent) % 10] - 1] = array[i];
                occurences[(array[i] / exponent) % 10]--;
            }
            for (int i = 0; i < size; i++)
            {
                array[i] = outputArr[i];
            }
        }

        static int GetMaxVal(int[] array, int size)
        {
            int maxVal = array[0];
            for (int i = 1; i < size; i++)
            {
                if (array[i] > maxVal)
                {
                    maxVal = array[i];
                }
            }
            return maxVal;
        }

        static void MergeSortOrdenar(int[] arr, int inicio, int fin)
        {
            if (inicio < fin)
            {
                int medio = (inicio + fin) / 2;

                MergeSortOrdenar(arr, inicio, medio);
                MergeSortOrdenar(arr, medio + 1, fin);

                Combinar(arr, inicio, medio, fin);
            }
        }

        static void Combinar(int[] arr, int inicio, int medio, int fin)
        {
            int n1 = medio - inicio + 1;
            int n2 = fin - medio;

            int[] temp1 = new int[n1];
            int[] temp2 = new int[n2];

            for (int i = 0; i < n1; i++)
            {
                temp1[i] = arr[inicio + i];
            }
            for (int j = 0; j < n2; j++)
            {
                temp2[j] = arr[medio + 1 + j];
            }

            int p1 = 0;
            int p2 = 0;
            int k = inicio;

            while (p1 < n1 && p2 < n2)
            {
                if (temp1[p1] <= temp2[p2])
                {
                    arr[k] = temp1[p1];
                    p1++;
                }
                else
                {
                    arr[k] = temp2[p2];
                    p2++;
                }
                k++;
            }
            while (p1 < n1)
            {
                arr[k] = temp1[p1];
                p1++;
                k++;
            }
            while (p2 < n2)
            {
                arr[k] = temp2[p2];
                p2++;
                k++;
            }
        }
        static void Main(string[] args)
        {
            int[] lista = { 7, 4, 0, 10, 24, 100, 199, 243, 2901, 2023, 24, 1294, 53};
            string[] lista1 = {"mi", "mama", "me", "ama" };

            Console.WriteLine("La lista original es: ");
            ImprimirLista(lista);
            Console.WriteLine("La lista ordenada es: ");
            //OrdenarIntercambio(lista);
            //ImprimirLista(lista);

            //OrdenamientoBurbuja(lista);
            //ImprimirLista(lista);
            //ImprimirListaString(lista1);
            //OrdenamientoBurbujaPalabra(lista1);
            //ImprimirListaString(lista1);

            //InsercionOrdenar(lista);
            //ImprimirLista(lista);

            int ini = 0;
            int n = lista.Length;
            int fin = n - 1;

            MergeSortOrdenar(lista, 0, lista.Length - 1);
            ImprimirLista(lista);
        }
    }
}