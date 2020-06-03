/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextGreaterElements(int* nums, int numsSize, int* returnSize){
    if (numsSize == 0 || nums == NULL) {
        *returnSize = 0;
        return NULL;
    }
    int *result = malloc(numsSize *sizeof(int));
    memset(result, -1, numsSize *sizeof(int));
    int stack[numsSize*2];
    int stackLength = 0;
    for (int i = 2*numsSize - 1; i > -1; i--) {
        while (stackLength != 0 && nums[i % numsSize] >= nums[stack[stackLength - 1]]) {
            stackLength--;
        }
        if (stackLength != 0) {
            result[i % numsSize] = nums[stack[stackLength - 1]];
        }
        stack[stackLength++] = i % (numsSize);
    }
    *returnSize = numsSize;
    return result;
}