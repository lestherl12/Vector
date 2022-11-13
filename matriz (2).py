using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Matriz
{
    class Matriz
    {
        private int[,] mat;

        public void Cargar()
        {
            mat = new int[3, 4];
            for (int f = 0; f < 3; f++)
            {
                for (int c = 0; c < 4; c++)
                {
                    Console.Write("Ingrese posicion ["+(f+1)+","+(c+1)+"]: ");
                    string linea;
                    linea = Console.ReadLine();
                    mat[f, c] = int.Parse(linea);
                }
            }
        }

        public void PrimerFila()
        {
            Console.WriteLine("\nPrimer fila de la matriz:");
            for (int c = 0; c < 4; c++)
            {
                Console.Write(mat[0, c]+"  ");
            }
        }

        public void UltimaFila()
        {
            Console.WriteLine("\nUltima fila de la matriz:");
            for (int c = 0; c < 4; c++)
            {
                Console.Write(mat[2, c]+"  ");
            }
        }

        public void PrimerColumna()
        {
            Console.WriteLine("\nPrimer columna:");
            for (int f = 0; f < 3; f++)
            {
                Console.Write(mat[f, 0]+"  ");
            }
        }

        static void Main(string[] args)
        {
            Matriz ma = new Matriz();
            ma.Cargar();
            ma.PrimerFila();
            ma.UltimaFila();
            ma.PrimerColumna();
            Console.ReadKey();
        }
    }
}