import java.io.*;
class account
{
int accno;
String name;
char acctype;
account()
{
accno=1010;
name="Lucarius";
acctype='s';
}
account(int i,String j,char k)
{
accno=i;
name=j;
acctype=k;
}
void display()
{
System.out.println(accno+" "+name+" "+acctype);
}
public static void main(String arg[])
{
account a=new account();
a.display();
account a2=new account(2020,"Euclius",'c');
a2.display();
}
}