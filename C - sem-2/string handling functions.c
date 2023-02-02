#include <stdio.h>
#include <conio.h>
#include <string.h>


void main()
{
    char a[50];
    printf("Enter any string: ");
    scanf("%s", a);
    printf("\n\nString length = %d", strlen(a));
    printf("\n\nLowercase String = %s", strlwr(a));
    printf("\n\nReversed String : %s", strrev(a));
    getch();
}

