#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <process.h>

struct rest
{
    int year;
    char name[30], cuisine[30], vnv[30];
}obj;
void main() {
    printf("\t\t\tRestaurant Details using Structure");
    printf("\n\nEnter the year of establishment : ");
    scanf("%d", &obj.year);
    printf("\nEnter the name of the restaurant : ");
    scanf("%s", &obj.name);
    printf("\nEnter the cuisine : ");
    scanf("%s", &obj.cuisine);
    printf("\nEnter veg or non-veg : ");
    scanf("%s", &obj.vnv);
    printf("\nThe restaurant details are :-\n\n\t Year Of Establishment : %d \n\t Name of the Restaurant : %s \n\t Cuisine Served : %s \n\t Veg or Non-Veg : %s \n\t", obj.year, obj.name, obj.cuisine, obj.vnv);
    getch();
}

