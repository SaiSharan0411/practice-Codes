import java.util.Scanner;
public class robust
{
public static void main(String[]L)
{
System.out.println("Robust Testing \n");
int lbx=20,ubx=40,lby=70,uby=110,lbz=30,ubz=80;
int nomx,nomy,nomz;
nomx=(lbx+ubx)/2;
nomy=(lby+uby)/2;
nomz=(lbz+ubz)/2;
System.out.println("Lower and Upper bound of x"+lbx+" "+ubx);
System.out.println("Lower and Upper bound of y"+lby+" "+uby);
System.out.println("Lower and Upper bound of z"+lbz+" "+ubz);
System.out.println("Nominal value of x, y and z is "+nomx+" "+nomy+" "+nomz);
System.out.println("Test Points");
System.out.println("Test Points"+" "+(lbx-1)+" "+lbx+" "+(lbx+1)+" "+nomx+" "+(ubx-1)+" "+ubx+" "+(ubx+1)+" ");
System.out.println("Test Points"+" "+(lby-1)+" "+lby+" "+(lby+1)+" "+nomy+" "+(uby-1)+" "+uby+" "+(uby+1)+" ");
System.out.println("Test Points"+" "+(lbz-1)+" "+lbz+" "+(lbz+1)+" "+nomz+" "+(ubz-1)+" "+ubz+" "+(ubz+1)+" ");
int tot=6*3+1;
System.out.println("Test Cases "+tot);
System.out.println("Test Cases are \n");
int[]xar={19,20,21,30,39,40,41};
int[]yar={69,70,71,90,109,110,111};
int[]zar={29,30,31,55,79,80,81};
int k=1;
for(int j=0;j<7;j++)
{
System.out.println(" "+k+"\t"+nomx+"\t"+nomy+"\t"+zar[j]+"\n");
k=k+1;
}
for(int j=0;j<7;j++)
{
if(xar[j]!=nomx)
{
System.out.println(" "+k+"\t"+xar[j]+"\t"+nomy+"\t"+nomz+"\n");
k=k+1;
}
}
for(int j=0;j<7;j++)
{
if(yar[j]!=nomy)
{
System.out.println(" "+k+"\t"+nomx+"\t"+yar[j]+"\t"+nomz+"\n");
k=k+1;
}
}
}
}