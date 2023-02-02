using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace exception_handling
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] num = new int[4];
            try
            {
                Console.WriteLine("Before Exception is generated");
                for (int i=0;i<10;i++)
                {
                    num[i] = i;
                    Console.WriteLine("Nums[{0}]:{1}", i, num[i]);
                }
                Console.WriteLine("This won't be displayed");
            }
            catch(IndexOutOfRangeException)
            {
                Console.WriteLine("Index out of bounds");
            }
            Console.WriteLine("After catch block");
        }
    }
}
