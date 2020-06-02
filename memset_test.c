#include <stdio.h>
#include <stdlib.h>

/*memset为字节整体赋值，只能初始化为0和-1*/
int main(int argc, char const *argv[])
{
    int *a;
    a = (int *)malloc(3 * sizeof(int));
    printf("%d\n", sizeof(a));
    //动态数组初始化不能sizeof数组名称，因为数组名只是一个指针
    memset(a, -1, 3 * sizeof(int));
    for (int i = 0; i < 3; i++) {
        printf("%d ",a[i]);
    }
    printf("\n-----------------------");
    int b[3];
        printf("%d\n", sizeof(b));
    memset(b, -1, sizeof(b));
    for (int i = 0; i < 3; i++) {
        printf("%d ",b[i]);
    }
    printf("\n-----------------------");
    int n = 3;
    //C99标准中增加的变长数组也是数组，可以sizeof数组名
    int c[n];
    memset(c, -1, sizeof(c));
    for (int i = 0; i < 3; i++) {
        printf("%d ",c[i]);
    }
    return 0;
}
