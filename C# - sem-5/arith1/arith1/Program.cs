using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace arith1
{
    class Program
    {
        static void Main(string[] args)
        {
            int a, b;
            float quot;
            Console.Write("Enter a:");
            a = int.Parse(Console.ReadLine());
            Console.Write("Enter b:");
            b = int.Parse(Console.ReadLine());
            Console.WriteLine("/n Arithmetic operations");
            Console.WriteLine("sum = " + (a + b));
            Console.WriteLine("difference =" + (a - b));
            Console.WriteLine("product =" + (a * b));
            Console.WriteLine("modulus =" + (a % b));
            Console.ReadKey();
        }
    }
}
