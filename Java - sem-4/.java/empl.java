import java.util.*;
class empl
{
static int empno;
static String name;
static char acctype;
empl(int i,String t,char c)
{
empno=i;
name=t;
acctype=c;
Scanner s=new Scanner(System.in);
System.out.println("ENTER THE empno:");
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
empl emp1=new empl(empno,name,acctype);
emp1.display();
}
}