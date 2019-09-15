#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
# https://leetcode-cn.com/problems/move-zeroes/description/
#
# algorithms
# Easy (55.47%)
# Likes:    383
# Dislikes: 0
# Total Accepted:    65.5K
# Total Submissions: 116.1K
# Testcase Example:  '[0,1,0,3,12]'
#
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 
# 示例:
# 
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 
# 说明:
# 
# 
# 必须在原数组上操作，不能拷贝额外的数组。
# 尽量减少操作次数。
# 
# 
#
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        index = 0
        while index < len(nums):
            if not nums[index]:
                nums.pop(index)
                count += 1
            else:
                index += 1
        for i in range(count):
            nums.append(0)

"""
高票答案:
第一次遇到非零元素，将非零元素与数组nums[0]互换，第二次遇到非零元素，将非零元素与nums[1]互换，
第三次遇到非零元素，将非零元素与nums[2]，以此类推，直到遍历完数组

"""
def moveZeroes(self, nums):
    zero = 0  # records the position of "0"
    for i in xrange(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
