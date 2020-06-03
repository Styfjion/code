#include <stdlib.h>
#include <stdio.h>

int* dailyTemperatures(int* T, int TSize, int* returnSize)
{
    if (TSize == 0 || T == NULL) {
        *returnSize = 0;
        return NULL;
    }
    int *result = malloc(TSize * sizeof(int));
    memset(result, 0, TSize * sizeof(int));
    int stack[TSize];
    int stackLength = 0;
    for (int i = TSize - 1; i > -1; i--) {
        while (stackLength != 0 && T[i] >= T[stack[stackLength - 1]]) {
            stackLength--;
        }
        if (stackLength != 0) {
            result[i] = stack[stackLength - 1] - i;
        }
        stack[stackLength++] = i;
    }
    *returnSize = TSize;
    return result;
}

int main(int argc, char const * argv[])
{
    int T[] = {73, 74, 75, 71, 69, 72, 76, 73};
    int returnSize;
    int *result;
    result = dailyTemperatures(T, 8, &returnSize);
    for (int i = 0; i < returnSize; i++) {
        printf("%d", result[i]);
    }
    return 0;
}
