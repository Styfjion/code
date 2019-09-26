#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (55.59%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 14.7K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第k小的元素。
# 请注意，它是排序后的第k小元素，而不是第k个元素。
# 
# 示例:
# 
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# 返回 13。
# 
# 
# 说明: 
# 你可以假设 k 的值永远是有效的, 1 ≤ k ≤ n^2 。
# 
#
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        def com_count(matrix,target):
            count = 0
            i,j = 0,len(matrix)-1
            while i<len(matrix) and j>=0: 
                if matrix[i][j] <= target:
                    count += j+1
                    i += 1
                else:
                    j -= 1
            return count
        left = matrix[0][0]
        right = matrix[-1][-1]
        while left < right:
            mid = (left+right)>>1
            count = com_count(matrix,mid)
            if count < k:
                left = mid+1
            else:
                right = mid
        return left



        

