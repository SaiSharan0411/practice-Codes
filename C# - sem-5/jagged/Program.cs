using System;

namespace jagged
{
    class Array
    {
        static void Main(string[] args)
        {
            string[][] arr;
            arr = new string[2][];
            arr[0] = new string[]
            {
                "sai","sharan"
            };
            arr[1] = new string[]
            {
                "lucarius","euclius"
            };
            for (int i = 0; i < 2; i++)
            {
                Console.WriteLine(arr[0][i]);
            }
            for(int j=0; j<2; j++)
            {
                Console.WriteLine(arr[1][j]);
            }
        }
    }
}
