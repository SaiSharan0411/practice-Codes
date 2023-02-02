abstract class furn
{
abstract void disp();
abstract void sayhello();
}
class table extends furn
{
void disp()
{
System.out.println("table is useful");
}
void sayhello()
{
System.out.println("L");
}
public static void main(String[]a)
{
furn t1=new table();
furn t2=new L();
t1.disp();
t2.sayhello();
}
}