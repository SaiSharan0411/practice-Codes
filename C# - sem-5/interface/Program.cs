using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Interface
{
    interface IGrand_father
    {
        void Radio();
    }

    class Father : IGrand_father
    {
        public void Radio()
        {
            Console.WriteLine("Old is Gold");
        }

        public void btn_phone()
        {
            Console.WriteLine("Emerging");
        }
    }

    internal class Program
    {
        static void Main(string[] args)
        {
            Father f = new Father();
            f.Radio();
            f.btn_phone();
        }
    }
}
