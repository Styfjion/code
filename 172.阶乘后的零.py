#
# @lc app=leetcode.cn id=172 lang=python3
#
# [172] 阶乘后的零
#
# https://leetcode-cn.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (38.33%)
# Likes:    124
# Dislikes: 0
# Total Accepted:    12.5K
# Total Submissions: 32.6K
# Testcase Example:  '3'
#
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
# 
# 示例 1:
# 
# 输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
# 
# 示例 2:
# 
# 输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
# 
# 说明: 你算法的时间复杂度应为 O(log n) 。
# 
#
#----------------------------------------------------
#自己答案
class Solution:
    def trailingZeroes(self, n: int) -> int:
        p = 5
        count = 0
        while n//p:
            count += n//p
            p *= 5
        return count
#-----------------------------------------------------
#高票答案
class Solution2(object):
    def trailingZeroes(self, n):
        zeroCnt = 0
        while n > 0:
            n = n/5; zeroCnt += n
        return zeroCnt
'''
Since 0 only company with 5*2 So only need to count the volume of 5 factor. (because 2 always enough)

So… 100! 's zero has => floor(100/5) + floor(100/25) = floor(100/5) + floor((100/5)/5)
'''


