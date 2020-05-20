#include <stdio.h>
#include <string.h>
#define MAX_LEN 1000000


char strSum[MAX_LEN+1];
char * multiStrings(char * num1, char * num2) {
    memset(strSum, '0', sizeof(strSum)-1);
    int index1,index2;
    index1 = strlen(num1)-1;
    index2 = strlen(num2)-1;
    if(strlen(num2) == 1 && num2[0] == '0' || strlen(num1) == 1 && num1[0] == '0')
    {
        strSum[MAX_LEN-1] = '0';
        return &strSum[MAX_LEN-1];
    }
    int sumIndex,token1,token2,cnt=0;
    for(int i=index2;i>-1;i--)
    {
        token1 = token2 = 0;
        sumIndex = MAX_LEN-1-cnt;
        for(int j=index1;j>=-1;j--)
        {
            if(j == -1)
            {
                if(token1+token2 > 0) {
                    strSum[sumIndex--] = (token2 + token1)%10 + '0';
                }
                if(token1+token2 >= 10) {
                    strSum[sumIndex--] = (token2 + token1)/10 + '0';
                }   
                break;
            }
            int sumStr;
            sumStr = (num1[j] - '0')*(num2[i] - '0') + token2;
            token2 = sumStr/10;
            sumStr %= 10;
            int temp;
            temp = strSum[sumIndex] - '0' + sumStr + token1;
            strSum[sumIndex] = temp%10 + '0';
            token1 = temp/10;
            sumIndex--;
        }
        cnt++;
    }
    return &strSum[++sumIndex];
}

int main()
{
    int n;
    char bigA[MAX_LEN+1], bigB[MAX_LEN+1];
    while(scanf("%s %s",bigA,bigB)!=EOF) {
        printf("%s\n", multiStrings(bigA, bigB));
    }

    return 0;
}
