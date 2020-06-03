#include <stdlib.h>

int* dailyTemperatures(int* T, int TSize, int* returnSize){
    if (T == NULL && TSize == 0) {
        *returnSize = 0;
        return NULL
    }
    int stack[TSize];
    int *result = malloc(TSize * sizeof(int));
    memset(result, 0, TSize * sizeof(int));
    int stackLength = 0;
    for (int i = 0; i < TSize; i++) {
        while(stackLength != 0 && T[i] > T[stack[stackLength - 1]]) {
            result[stack[stackLength - 1]] = i - stack[stackLength - 1];
            stackLength--;
        }
        stack[stackLength++] = i;
    }
    *returnSize = TSize;
    return result;
}

int main(int argc, char const *argv[])
{
    int T[] = {73, 74, 75, 71, 69, 72, 76, 73};
    int returnSize;
    int *result;
    dailyTemperatures(T, 8, &returnSize);
    for (int i = 0; i < returnSize; i++) {
        prinf("%d ", result[i]);
    }
    return 0;
}
