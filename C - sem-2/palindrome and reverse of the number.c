#include<stdio.h>
int main()
{
    int n,r,sum=0,temp;
    printf("enter the number ");
    scanf("%d",&n);
    temp=n;
    while(n>0)
    {
        r=n%10;
        sum=(sum*10)+r;
        n=n/10;
    }
    if(temp==sum)
    printf("this number is a palindrome");
    else
    printf("this number is not a palindrome");
    printf("\nthe reverse of this number is %d",sum);
    return 0;
}
