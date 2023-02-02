import java.util.Scanner;
public class wc
{
public static void main(String[]L)
{
int x=5,y=2,lbx=20,ubx=40,lby=20,uby=40;
int nomx,nomy;
nomx=(lbx+ubx)/2;
nomy=(lby+uby)/2;
System.out.println("Worst Case Testing \n");
System.out.println("Boundary Value of X:"+lbx+" "+ubx+" ");
System.out.println("Nominal"+nomx);
System.out.println("Boundary Value of Y:"+lby+" "+uby+" ");
System.out.println("Nominal"+nomy);
System.out.println("Test Points");
System.out.println("X Test Points "+" "+lbx+" "+(lbx+1)+" "+nomx+" "+(ubx-1)+" "+ubx+" ");
System.out.println("Y Test Points "+" "+lby+" "+(lby+1)+" "+nomy+" "+(uby-1)+" "+uby+" ");
double tot=Math.pow(5,2);
System.out.println("Test Cases "+tot);
System.out.println("\n Test Cases are:\n");
int[]xar={20,21,30,39,40};
int[]yar={20,21,30,39,40};
int k=1;
for(int i=0;i<5;i++)
{
for(int j=0;j<5;j++)
{
System.out.println(" "+k+" "+xar[i]+" "+yar[j]+"\n");
k=k+1;
}
}
}
}