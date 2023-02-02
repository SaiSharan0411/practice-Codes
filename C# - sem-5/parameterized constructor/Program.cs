using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace parameterized_constructor
{
    class Program
    {
        int roll;
        string name;
        Program(int a,string n)
        {
            roll = a;
            name = n;
        }
        public void display()
        {
            Console.WriteLine("name :" + name);
            Console.WriteLine("roll no :" + roll);
        }
        static void Main(string[] args)
        {
            Program obj1 = new Program(16, "SAI");
            obj1.display();
        }
    }
}
