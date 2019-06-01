#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 求众数
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (59.31%)
# Likes:    248
# Dislikes: 0
# Total Accepted:    44.7K
# Total Submissions: 75.5K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在众数。
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
#
#自己的答案
#----------------------------------------------------------------
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        countmax = 1
        numsLen = len(nums)
        for i in range(1,numsLen):
            if nums[i] == nums[i-1]:
                countmax += 1
            if countmax > numsLen//2:
                return nums[i-1]
            if nums[i] != nums[i-1]:
                countmax = 1
#----------------------------------------------------------------
#高票答案：
def majorityElement(nums):
    return sorted(nums)[len(nums)/2]
#----------------------------------------------------------------


class Solution2(object):
    def majorityElement(self, nums):
        tmp = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                tmp = nums[i]
            count = count+1 if nums[i] == tmp else count-1
        return tmp
#从第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换个数开始计数，总能找到最多的那个

#---------------------------------------------------------------
#使用字典记录出现次数
class Solution3:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = d.get(nums[i], 0) + 1
            if d[nums[i]] > len(nums) / 2:
                return nums[i]


        

