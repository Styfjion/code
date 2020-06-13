#include <stdlib.h>
#include <stdio.h>
#define max(a, b) (a) > (b) ? (a) : (b)
#define MAX 100

int temp[5][2] = {{1,2},{1,2},{3,3},{1,5},{1,5}};

int ArrayCmp(const void *p1, const void *p2)
{
    int *a1 = *(int **)p1;
    int *a2 = *(int **)p2;
    return a1[1] - a2[1];
}

int maxEvents(int** events, int eventsSize){
    int hash[MAX];
    memset(hash, 0, sizeof(hash));
    int result, temp, prev;
    result = temp = prev = 0;
    qsort(events, eventsSize, 2 * sizeof(int), ArrayCmp);
    for (int i = 0; i < eventsSize; i++) {
        int j;
        j = events[i][0] >= prev ? max(events[i][0], temp) : events[i][0];
        for (; j <= events[i][1]; j++) {
            if (hash[j] == 0) {
                hash[j] = 1;
                temp = j + 1;
                prev = events[i][0];
                result++;
                break;
            }
        }
    }
    return result;
}


int main(int argc, char const *argv[])
{
    
    int **events = malloc(5*sizeof(int*));
    for (int i = 0; i < 5; i++) {
        events[i] = malloc(2*sizeof(int));
        memcpy(events[i], temp[i], 2 * sizeof(int));
    }
    printf("%d", maxEvents(events, 5));
    return 0;
}
