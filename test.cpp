
#include<stdio.h>
#include<math.h>
#include<cstdlib>
int main()
{
    double n,m;
    while(~scanf("%lf%lf",&n,&m))
    {
        double y=n;
        m=m-1;
        while(m--)
        {
            n=sqrt(n);
            y=y+n;
        }
        printf("%.2lf\n",y);
    }
    system("pause");
    return 0;
}