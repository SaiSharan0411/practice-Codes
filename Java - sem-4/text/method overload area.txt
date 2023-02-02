import java.io.*;
class area
{
int h,r;
double pi;
area(int a,int b,int c)
{
h=a;
r=b;
pi=c;
}
area()
{
h=5;
r=7;
pi=3.14;
}
void area()
{
System.out.println("area of circle is "+(pi*r*r)+" ");
}
void cylinder(int h,int r,double pi)
{
System.out.println("area of cylinder is "+(pi*r*r*h)+" ");
}
public static void main(String[]arg)
{
area out=new area();
out.area();
area out2=new area();
out2.cylinder(5,7,3.14);
}
}