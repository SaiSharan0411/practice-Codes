using System;

namespace string_handling
{
    class Program
    {
        static void Main(string[] args)
        {
            string firstname;
            string lastname;
            firstname = "sai";
            lastname = "sharan";
            Console.WriteLine(firstname.CompareTo(lastname));
            Console.WriteLine(firstname.ToLower());
            Console.WriteLine(firstname.ToUpper());
            Console.WriteLine(firstname.Insert(0, "hello"));
            Console.WriteLine(firstname.LastIndexOf("e"));
            Console.WriteLine(firstname.Length);
            Console.WriteLine(firstname.Remove(5));
            Console.WriteLine(firstname.Replace('e', 'i'));
            string[] split = firstname.Split(new char[] { 'e' });
            Console.WriteLine(split[0]);
                Console.WriteLine(split[1]);
            Console.WriteLine(split[2]);
            Console.WriteLine(firstname.StartsWith("S"));
            Console.WriteLine(firstname.Substring(2, 5));
            Console.WriteLine(firstname.ToCharArray());
            Console.WriteLine(firstname.Trim());
        }
    }
}
