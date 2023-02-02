abstract class  furn
{
abstract void disp();
void sayhello()
{
System.out.println("Hello");
}
}
class table extends furn
{
void disp()
{
System.out.println("table is useful");
}
public static void main(String[]a)
{
furn t1=new table();
t1.disp();
t1.sayhello();
}
}