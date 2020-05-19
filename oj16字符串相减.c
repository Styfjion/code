#include <string.h>
#include <stdlib.h>
#define MAX_LEN 1000


char strSum[MAX_LEN+2] = {'\0'};

char* substrStrings(char * num1, char * num2) 
{
    int index1,index2;
    int sumIndex = MAX_LEN;
    int positive = 0;
    if(strlen(num1) < strlen(num2) || (strlen(num1) == strlen(num2) && strcmp(num1, num2) < 0))
    {
        char *temp = num1;
        num1 = num2;
        num2 = temp;
        positive = -1;
    }
    if(strcmp(num1,num2) == 0)
    {
        strSum[1000] = '0';
        return &strSum[1000];
    }
    index1 = strlen(num1)-1;
    index2 = strlen(num2)-1;
    int token = 0;
    while (index1 >= 0 || index2 >= 0) {
        int sumStr;
        sumStr = (index1 >= 0 ? num1[index1]-'0':0) - (index2 >= 0 ? num2[index2]-'0':0) + token;
        strSum[sumIndex--] = (sumStr < 0 ? sumStr+10 : sumStr) + '0';
        token = sumStr < 0 ? -1 : 0;
        index1--;
        index2--;
    }
    sumIndex++;
    while(strSum[sumIndex] == '0') {
        sumIndex++;
    } 
    if(positive == -1)
    {
        strSum[--sumIndex] = '-';
    }
    return &strSum[sumIndex];
}

int main()
{
    int n;
    char bigA[MAX_LEN+1], bigB[MAX_LEN+1];
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%s %s", bigA, bigB);
        printf("Case %d:\n",i+1);
        printf("%s - %s = %s", bigA, bigB, substrStrings(bigA, bigB));
        if(i != n-1)
            printf("\n\n");
    }
    return 0;
}
