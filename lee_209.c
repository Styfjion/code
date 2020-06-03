#include <stdlib.h>
#define min(a,b) (a) < (b) ? (a) : (b)
int minSubArrayLen(int s, int* nums, int numsSize){
    if (nums == NULL || numsSize == 0) {
        return 0;
    }
    int sum = 0, left = 0;
    int ans = numsSize + 1;
    for (int i = 0; i < numsSize; i++) {
        sum += nums[i];
        while (sum >= s) {
            ans = min(ans, i - left + 1);
            if(ans == 1) {
                return ans;
            }
            sum -= nums[left++];
        }
    }
    return ans;
}