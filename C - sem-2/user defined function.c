#include <stdio.h>
float areaOfcircle(float radius_circle);
float interest_calc(float a, float b, float c);
int main() 
{
    float radius;
    printf("Enter the radius of circle : ");
    scanf("%f", &radius);
	printf("Area of circle : %.2f", areaOfcircle(radius));
	printf("\n");
	float principal, period, rate;
    float res;
    printf("\nEnter Prinicpal Amount:\t");
    scanf("%f", &principal);
    printf("\nEnter Period of Years:\t");
    scanf("%f", &period);
    printf("\nEnter Rate of Interest:\t");
    scanf("%f", &rate);
    res = interest_calc(principal, period, rate);
    printf("\nSimple Interest = %f\n", res);
    printf("\n");
	return 0;
}
float areaOfcircle(float radius_circle)
{
   float area_circle;
   area_circle = 3.14 * radius_circle * radius_circle;
   return area_circle;
}
float interest_calc(float a, float b, float c)
{
    float si;   
    si = (a * b * c)/100;
    return si;
}
