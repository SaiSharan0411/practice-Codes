public class je
{
public static void main(String[]L)
{
int a[]={1,2,3};
try
{
System.out.println(a[3]);
}
catch(ArrayIndexOutOfBoundsException b)
{
System.out.println(b);
}
System.out.println("rest of the code....");
}
}
