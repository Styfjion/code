class Solution {
    public int minSwap(int[] A, int[] B) {
        // 动态规划，cost[0]代表当前位不换时最小交换次数
        //          cost[1]代表当前位交换时最小交换次数
        int[] cost = new int[]{0, 1};
        for(int i = 1; i < A.length; i++) {
            // 如果两个数组的当前位都大于上一位，理论上不换就可以保持两个数组单调递增
            if(A[i] > A[i - 1] && B[i] > B[i - 1]) {
                // 如果满足这个条件，当前位交不交换都满足单调递增
                if(A[i] > B[i - 1] && B[i] > A[i - 1]) {
                    // 既然当前位不换，那么当前位的最小交换次数继承上一位的交换或不交换的最小值
                    cost[0] = Math.min(cost[0], cost[1]);
                    // 既然要交换，则是上一位交换或不交换的最小值加1
                    cost[1] = Math.min(cost[0], cost[1]) + 1;
                } 
                // 如果交换当前位，就会导致不递增
                else {
                    // 如果要交换当前位，需要先交换上一位
                    cost[1] += 1;
                }
            } 
            // 必须换
            else {
                int t = cost[0];
                // 如果不交换自己，那么需要交换上一位，所以继承上一位交换的次数
                cost[0] = cost[1];
                // 如果交换自己，那么上一位不交换，所以继承上一位不交换的次数并加1
                cost[1] = t + 1;
            }
        }
        return Math.min(cost[0], cost[1]);
    }
}