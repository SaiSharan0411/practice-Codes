import java.util.*;
class emp2
{
static int empno;
static String name;
static char acctype;
void display(){
Scanner s=new Scanner(System.in);
System.out.println("ENTER EMPNO:");
empno=s.nextInt();
System.out.println("ENTER NAME:");
name=s.next();
System.out.println("ENTER ACCTYPE:");
acctype=s.next().charAt(0);
}
void display(int a)
{
System.out.println(empno+" "+name+" "+acctype);
}
public static void main(String arg[])
{
emp2 emp=new emp2(); 
emp.display();
emp2 emp3=new emp2();
emp3.display(10);
}
}