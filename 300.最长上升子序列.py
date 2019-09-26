#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长上升子序列
#
# https://leetcode-cn.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (42.57%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    29K
# Total Submissions: 67.1K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# 给定一个无序的整数数组，找到其中最长上升子序列的长度。
# 
# 示例:
# 
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4 
# 解释: 最长的上升子序列是 [2,3,7,101]，它的长度是 4。
# 
# 说明:
# 
# 
# 可能会有多种最长上升子序列的组合，你只需要输出对应的长度即可。
# 你算法的时间复杂度应该为 O(n^2) 。
# 
# 
# 进阶: 你能将算法的时间复杂度降低到 O(n log n) 吗?
# 
#
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)<2:
            return len(nums)
        cell = [nums[0]]
        for i in range(1,len(nums)):
            if nums[i]>cell[-1]:
                cell.append(nums[i])
                continue
            l,r = 0,len(cell)-1
            while l<r:
                mid = (l+r)>>1
                if cell[mid] < nums[i]:
                    l = mid+1
                else:
                    r = mid
            cell[l] = nums[i]
        return len(cell)

        
        

