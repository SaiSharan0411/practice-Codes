import java.io.*;
interface hello
{
void print();
}
class welcome implements hello
{
public void print()
{
System.out.println("hello");
}
public static void main(String[]args)
{
hello obj=new welcome();
obj.print();
}
}