import java.util.Scanner;
public class bva
{
public static void main(String[]args)
{
System.out.println("Boundary Value Analysis");
int age,imin,imax,vmin,vmax;
Scanner s=new Scanner(System.in);
System.out.println("Enter age: ");
age=s.nextInt();
System.out.println("Enter Min value: ");
vmin=s.nextInt();
System.out.println("Enter Max value: ");
vmax=s.nextInt();
imin=vmin-1;
imax=vmax+1;
if(age<=imin || age>=imax)
{
System.out.println("Age is out of Boundary");
}
else if(age==vmin || age==vmax)
{
System.out.println("Age is on the Boundary");
}
else
{
System.out.println("Age is within the Boundary");
}
}
}