using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace structure
{
    class Program
    {
        struct books
        {
            private string title;
            private string author;
            private string subject;
            private int book_id;

            public void getValues(string t,string a,string s,int id)
            {
                title = t;
                author = a;
                subject = s;
                book_id = id;
            }
            public void display()
            {
                Console.WriteLine("Title: {0}", title);
                Console.WriteLine("Author: {0}", author);
                Console.WriteLine("Subject: {0}", subject);
                Console.WriteLine("Book id: {0}", book_id);
            }
        };
        static void Main(string[] args)
        {
            books book1 = new books();
            books book2 = new books();
            book1.getValues("C Programming", "Nuha Ali", "Computer Science", 931235);
            book2.getValues("Telecom Billing", "Zara Ali", "Telecom", 846284);
            book1.display();
            book2.display();
            Console.ReadKey();
        }
    }
}
