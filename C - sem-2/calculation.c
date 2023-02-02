#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include "Calculator.h"
 
void main()
{
    int a=4, b=8;
    system("cls");
    printf("\t\t Using Custom Header Files\n\n");
    printf("\nSum is %d", add(a,b));
    printf("\nDifference is %d", sub(a,b));
    printf("\nProduct is %d", mul(a,b));
    printf("\nQuotient is %d", qout(a,b));
    getch();
}

