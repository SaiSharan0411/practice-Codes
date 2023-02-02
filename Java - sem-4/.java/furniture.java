abstract class furniture
{
abstract void disp();
}
class chair extends furniture
{
void disp()
{
System.out.println("chair has 4 legs");
}
public static void main(String[]a)
{
furniture t1=new chair();
t1.disp();
}
}