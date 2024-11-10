#include <stdio.h>
#include <stdlib.h>
int main()
{
    int l,c,i,e;
    printf("Entrer le nombre de ligne\n");
    scanf("%d",&l);
    for(i=0;i<l;i++)
    {
        for(e=(l-i)-1;e>0;e--)
        {
            printf(" ");
        }
        for(c=(2*i)+1;c>0;c--)
        {
            printf("*");
        }
        printf("\n");
    }
    printf("Nous Vous Souhaitons Un Joyeux Noel\a\n");
    system("pause");
    return 0;
}
