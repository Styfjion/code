#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (43.42%)
# Likes:    234
# Dislikes: 0
# Total Accepted:    45.2K
# Total Submissions: 102.5K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
#
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        newpoint = m+n-1
        point1 = m-1
        point2 = n-1
        while point1 >= 0 and point2 >= 0:
            if nums1[point1] >= nums2[point2]:
                nums1[newpoint] = nums1[point1]
                point1 -= 1
            else:
                nums1[newpoint] = nums2[point2]
                point2 -= 1
            newpoint -= 1
        if point2 >= 0:
            nums1[:point2+1] = nums2[:point2+1]

