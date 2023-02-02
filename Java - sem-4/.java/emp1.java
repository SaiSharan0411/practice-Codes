import java.util.*;
class emp1
{
int empno;
String name;
char acctype;
emp1()
{
Scanner s=new Scanner(System.in);
System.out.println("ENTER THE EMPNO:");
empno=s.nextInt();
System.out.println("ENTER THE NAME:");
name=s.next();
System.out.println("ENTER THE ACCTYPE:");
acctype=s.next().charAt(0);
}
void display()
{
System.out.println(empno+" "+name+" "+acctype);
}
public static void main(String arg[])
{
emp1 emp=new emp1(); 
emp.display();
}
}