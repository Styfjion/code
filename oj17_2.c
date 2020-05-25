#include <stdio.h>
#include <string.h>
#define MAX_LEN 2000


char strSum[MAX_LEN+1];
char * multiStrings(char * num1, char * num2) {
    memset(strSum, '0', sizeof(strSum)-1);
    int index1,index2;
    index1 = strlen(num1)-1;
    index2 = strlen(num2)-1;
    strSum[index1 + index2 + 2] = '\0';
    int sumIndex,token1,token2;
    for (int i = index1; i >= 0; i--) {
        for (int j = index2; j >= 0; j--) {
            int temp;
            temp = (num1[i] - '0') * (num2[j] - '0') + (strSum[i+j+1] - '0');
            strSum[i+j+1] = temp%10 + '0';
            strSum[i+j] += temp/10;
        }
    }
    for (int k = 0; k <= index1 + index2 + 1; k++) {
        if (strSum[k] != '0') {
            return &strSum[k];
        }
    }
    strSum[1] = '\0';
    return &strSum;
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