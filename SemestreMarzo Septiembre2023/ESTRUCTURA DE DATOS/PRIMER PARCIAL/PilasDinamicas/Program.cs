using System;
using System.Collections.Specialized;
using System.ComponentModel.DataAnnotations;

namespace PilasDinamicas
{
    class Pila
    {
        protected string contenido;
        protected Pila siguiente;

        public Pila(string dato = null)
        {
            this.contenido = dato;
            siguiente = null;
        }

        //True si esta vacia
        public bool Vacia()
        {
            if(siguiente == null && contenido == null)
            {
                return true;
            }
            return false;
        }

        //Agregar un elemento a la Pila
        public void Push(string dato)
        {
            Pila puntero = this;
            Pila nuevo;
            while (puntero.siguiente != null)
            {
                puntero = puntero.siguiente;
            }
            nuevo = new Pila(dato); //Aqui creo el Nodo
            puntero.siguiente = nuevo; //Crea la flecha del anterior al NuevoNodo
        }

        //Elimina un elemento de la pila, devuelve el elemento eliminado
        public string Pop()
        {
            string retorno = null;
            Pila puntero = this;
            Pila nodoFinal = this;

            if (!Vacia())
            {
                while (puntero.siguiente != null)
                {
                    puntero = puntero.siguiente; //Aqui llegamos hasta el ulimo nodo antes de null
                }
                while (nodoFinal.siguiente != puntero) //Pero aqui vamos hacia el nodo uno antes del
                {
                    nodoFinal = nodoFinal.siguiente;
                }
                retorno = puntero.contenido;
                nodoFinal.siguiente = null; //Desconectamos el nodo y deja de existir
            }
            return retorno;
        }

        public int Contar()
        {
            int contador = 0;
            Pila puntero = this;
 
            if (!Vacia())
            {
                while (puntero.siguiente != null)
                {
                    puntero = puntero.siguiente;
                    contador++;
                }
            }
            return contador;
        }

        public void Ver()
        {
            if (Vacia())
            {
                Console.WriteLine("PILA VACIA");
            }
            else
            {
                Pila puntero = this;
                int contar = Contar();

                Console.WriteLine("ELEMENTOS DE LA PILA: ");

                while (contar != 0)
                {
                    for (int i = 0; i < contar; i++)
                    {
                        puntero = puntero.siguiente;
                    }
                    Console.Write(puntero.contenido);
                    contar--;
                    puntero = this;

                    if (contar != 0)
                    {
                        Console.Write(" -> ");
                    }
                }
            }
        }

        public Pila Copia()
        {
            Pila copia = new Pila();
            Pila puntero = this.siguiente; // Apunta al primer elemento de la pila con datos
            Pila punteroCopia = copia; //Apunta a la Copia que vamos hacer
            if (!Vacia())
            {
                while (puntero != null)
                {
                    punteroCopia.siguiente = new Pila(puntero.contenido);
                    punteroCopia = punteroCopia.siguiente;
                    puntero = puntero.siguiente;
                }
            }
            return copia;
        }

        public int validarPE(Pila E)
        {
            int resultado = 0;
            Pila temp = new Pila();
            Pila puntero = E.siguiente;
            int operando1 = 0;
            int operando2 = 0;

            if (!E.Vacia())
            {
                while (puntero != null)
                {
                    if (!puntero.contenido.Equals("+") && !puntero.contenido.Equals("-") && !puntero.contenido.Equals("*") && !puntero.contenido.Equals("/") && !puntero.contenido.Equals("^"))
                    {
                        temp.Push(puntero.contenido);
                        
                    }
                    else
                    {
                        operando1 = Convert.ToInt32(temp.Pop());
                        operando2 = Convert.ToInt32(temp.Pop());
                        switch (puntero.contenido)
                        {
                            case "^":
                                resultado = (int)Math.Pow(operando2, operando1);
                                break;
                            case "/":
                                resultado = operando2 / operando1;
                                break;
                            case "*":
                                resultado = operando2 * operando1;
                                break;
                            case "+":
                                resultado = operando2 + operando1;
                                break;
                            case "-":
                                resultado = operando2 - operando1;
                                break;
                        }
                        temp.Push(resultado.ToString());
                    }
                    puntero = puntero.siguiente;
                }
            }
            else
            {
                Console.WriteLine("La pila esta vacia");
            }
            return resultado;
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Pila pila = new Pila();
            int res = 0;

            pila.Push("1");
            pila.Push("2");
            pila.Push("3");
            pila.Push("*");
            pila.Push("+");

            pila.validarPE(pila);

            res = pila.validarPE(pila);
            Console.WriteLine(res);

            Pila Npila = pila.Copia();
            Console.WriteLine("La pila copiada es: ");
            Npila.Ver();





            Console.WriteLine(pila.Contar());
        }
    }
}