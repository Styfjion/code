#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (46.50%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    26K
# Total Submissions: 55.9K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#
#自己答案
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        factor = 2
        while factor < n:
            if n%factor:
                return False
            factor *= 2
        return True

#高票答案
def isPowerOfTwo(self, n):
    return (n>0) and (n & (n-1))==0


