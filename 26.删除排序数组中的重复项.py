#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow = 0
        if not nums:
            return 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1
