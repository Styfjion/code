#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i<len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return i
