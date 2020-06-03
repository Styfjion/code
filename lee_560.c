#include "uthash.h"

typedef struct {
    int sum;
    int count;
    UT_hash_handle hh;
} Myhash;

int subarraySum(int* nums, int numsSize, int k){
    Myhash *map = NULL;
    Myhash *node = malloc(sizeof(Myhash));
    node->sum = 0;
    node->count = 1;
    HASH_ADD_INT(map, sum, node);
    int count, pre;
    count = pre = 0;
    for (int i = 0; i < numsSize; i++) {
        pre += nums[i];
        node = NULL;
        int val = pre - k;
        HASH_FIND_INT(map, &val, node);
        if (node != NULL) {
            count += node->count;
            node = NULL;
        }
        HASH_FIND_INT(map, &pre, node);
        if (node == NULL) {
            node = malloc(sizeof(Myhash));
            node->sum = pre;
            node->count = 1;
            HASH_ADD_INT(map, sum, node);
        } else {
            node->count++;
        }
    }
    return count;
}