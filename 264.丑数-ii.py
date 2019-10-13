#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#
# https://leetcode-cn.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (46.18%)
# Likes:    123
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 16.8K
# Testcase Example:  '10'
#
# 编写一个程序，找出第 n 个丑数。
# 
# 丑数就是只包含质因数 2, 3, 5 的正整数。
# 
# 示例:
# 
# 输入: n = 10
# 输出: 12
# 解释: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 是前 10 个丑数。
# 
# 说明:  
# 
# 
# 1 是丑数。
# n 不超过1690。
# 
# 
#

"""
思路二：动态规划

dp[i] 表示第i个丑数

那么dp[i] = min(2 * dp[l_2], 3 * dp[l_3], 5 * dp[l_5])

这里 l_2, l_3, l_5是表示，指到的位置。

"""

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if not n:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        token = 1
        while token < n:
            res.append(min(res[t2]*2,res[t3]*3,res[t5]*5))
            while res[t2]*2 <= res[-1]:
                t2 += 1
            while res[t3]*3 <= res[-1]:
                t3 += 1
            while res[t5]*5 <= res[-1]:
                t5 += 1
            token += 1
        return res[token-1]

