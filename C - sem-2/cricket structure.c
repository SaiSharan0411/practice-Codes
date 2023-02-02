#include<stdio.h>
#include<string.h>
struct cricket
{
    char     P_Name[20];
    char     T_Name[20];
    float B_Ave;
};
void main()
{
    struct cricket s[5],t;
    int    i,j,n=5;
    float    p;
    printf("Enter Data Of %d Player\n",n);
    for(i=0;i<n;i++)
    {
        printf("\nEnter Player Name,Team Name And Bating Average For Player %d :- \n",i+1);
        scanf("%s %s %f",s[i].P_Name,s[i].T_Name,&p);
        s[i].B_Ave=p;
    }
    for(i=1;i<=n-1;i++)
    {
        for(j=0;j<=n-i;j++)
        {
            if(strcmp(s[j-1].T_Name,s[j].T_Name)>0)
            {
                t=s[j-1];
                s[j-1]=s[j];
                s[j]=t;
            }
        }
    }
    printf("\nAfter Teamwise Sorting...Player List Is");
    for(i=0;i<n;i++)
    {
            printf("\n%-20s %-20s %.2f",s[i].P_Name,s[i].T_Name,s[i].B_Ave);
    }
}
