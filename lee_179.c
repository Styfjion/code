#include <stdlib.h>
#include <string.h>
#define MAX 10

int cmp (const void *p1, const void *p2) {
    char a1[MAX*2 + 1], a2[MAX*2 + 1];
    sprintf(a1, "%d%d", *(int*)p1, *(int*)p2);
    sprintf(a2, "%d%d", *(int*)p2, *(int*)p1);
    return (strcmp(a2, a1));  
}

char * largestNumber(int* nums, int numsSize){
    char *result = malloc(numsSize * MAX + 1);
    memset(result, '\0', numsSize * MAX + 1);
    qsort(nums, numsSize, sizeof(int), cmp);
    char *p = result;
    for (int i = 0; i < numsSize; i++) {
        sprintf(p, "%d", nums[i]);
        p += strlen(p);
    }
    return p;
}