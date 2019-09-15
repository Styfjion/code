#
# @lc app=leetcode.cn id=1013 lang=python3
#
# [1013] 将数组分成和相等的三个部分
#
# https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (47.87%)
# Likes:    11
# Dislikes: 0
# Total Accepted:    3.4K
# Total Submissions: 6.7K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# 给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
# 
# 形式上，如果我们可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ...
# + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
# 
# 
# 
# 示例 1：
# 
# 输出：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 
# 
# 示例 2：
# 
# 输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
# 
# 
# 示例 3：
# 
# 输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000
# 
# 
#

#超时答案

"""
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sumA = sum(A)
        if sumA%3:
            return False
        p1 = -1
        for i in range(1,len(A)-1):
            if sum(A[i:]) == 2*sum(A[:i]):
                p1 = i
                break
        if p1<0:
            return False
        p2 = -1
        for j in range(p1+1,len(A)):
            if sum(A[j:]) == sum(A[p1:j]):
                p2 = j
                break
        if p2<0:
            return False
        else:
            return True
"""
class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sumA = sum(A)
        if sumA%3 or not len(A):
            return False
        cumsum = 0
        sub_sum = sumA // 3
        number = 0
        for unit in A:
            cumsum += unit
            if cumsum == sub_sum:
                cumsum = 0
                number += 1
        return number == 3


            
