class solidsubstance
{
void display()
{
System.out.println("solid substance");
}
}
class shapes extends solidsubstance
{
void display()
{
System.out.println("shapes");
super.display();
}
}
class circle extends shapes
{
void display()
{
System.out.println("circle");
}
}
class square extends shapes
{
void display()
{
System.out.println("square");
super.display();
}
public static void main(String[]L)
{
square l1=new square();
l1.display();
circle l2=new circle();
l2.display();
}
}
