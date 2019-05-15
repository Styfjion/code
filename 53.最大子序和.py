#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = nums[0]
        maxnum = nums[0]
        for i in range(1,len(nums)):
            sums = max(0,sums)
            sums += nums[i]
            maxnum = max(maxnum,sums)
        return maxnum

