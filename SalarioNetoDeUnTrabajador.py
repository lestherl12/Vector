using System;

namespace SalarioNetoDeUnTrabajador
{
    class SalarioNetoDeUnTrabajador
    {
        static void Main(string[] args)
        {
            double horas_extras, horas_normales, impuestos, numero_de_horas, precio_de_la_hora;
            double salario_final, sueldo_mensual;
            Console.Write("Ingresa el valor de numero de horas: ");
            numero_de_horas = double.Parse(Console.ReadLine());
            Console.Write("Ingresa el valor de precio de la hora: ");
            precio_de_la_hora = double.Parse(Console.ReadLine());
            impuestos=0;
            if(numero_de_horas>35)
            {
                horas_normales=35;
                horas_extras=numero_de_horas-35;
            }
            else
            {
                horas_normales=numero_de_horas;
                horas_extras=0;
            }
            sueldo_mensual=horas_normales*precio_de_la_hora+horas_extras*precio_de_la_hora*1.5;
            if(sueldo_mensual>=600&&sueldo_mensual<=1000)
                impuestos=sueldo_mensual*0.2;
            if(sueldo_mensual>1000)
                impuestos=sueldo_mensual*0.3;
            salario_final=sueldo_mensual-impuestos;
            Console.WriteLine("Valor de horas extras: " + horas_extras);
            Console.WriteLine("Valor de horas normales: " + horas_normales);
            Console.WriteLine("Valor de impuestos: " + impuestos);
            Console.WriteLine("Valor de salario final: " + salario_final);
            Console.WriteLine("Valor de sueldo mensual: " + sueldo_mensual);
            Console.WriteLine();
            Console.Write("Presiona una tecla para terminar . . . ");
            Console.ReadKey();
        }
    }
}