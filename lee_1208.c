#include "securec.h"
#define max(a,b) (a) > (b) ? (a) : (b)

int equalSubstring(char * s, char * t, int maxCost){
    int length = strlen(s);
    int maxLength, cumSum, left, right;
    maxLength = cumSum = left = 0;
    for (int i= 0; i < length; i++) {
        cumSum += abs(s[i] - t[i]);
        while (cumSum > maxCost) {
            cumSum -= abs(s[left] - t[left]);
            left++;
        }
        maxLength = max(maxLength, i - left + 1);
    }
    return maxLength;
}

int main(int argc, char const *argv[])
{
    char *s = "pxezla";
    char *t = "loewbi";
    printf("%d", equalSubstring(s, t, 25));
    return 0;
}
