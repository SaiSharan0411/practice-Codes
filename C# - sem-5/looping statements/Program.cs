using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace looping_statements
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Enter start value");
            int start = int.Parse(Console.ReadLine());
            Console.WriteLine("Enter end value");
            int end = int.Parse(Console.ReadLine());
            Console.WriteLine("Numbers in range");
            Console.WriteLine("for loop");
            for(int i=start;i<=end;i++)
            {
                Console.WriteLine(i);
            }
            Console.WriteLine("while loop");
            int j = start;
            while (j < end)
            {
                Console.WriteLine(j);
                j++;
            }
        }
    }
}
