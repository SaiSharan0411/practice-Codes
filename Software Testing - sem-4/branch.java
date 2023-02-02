import java.util.Scanner;
public class branch
{
public static void main(String[]args)
{
int a,b;
Scanner s=new Scanner(System.in);
System.out.println("Branch Coverage ");
System.out.print("\nEnter value of a: ");
a=s.nextInt();
System.out.print("\nEnter value of b: ");
b=s.nextInt();
if(a>b)
{
System.out.println("a is greater");
}
else if(b>a)
{
System.out.println("b is greater");
}
else
{
System.out.println("a and b are equal");
}
}
}