#
# @lc app=leetcode.cn id=204 lang=python3
#
# [204] 计数质数
#
# https://leetcode-cn.com/problems/count-primes/description/
#
# algorithms
# Easy (28.81%)
# Likes:    169
# Dislikes: 0
# Total Accepted:    21.1K
# Total Submissions: 73.2K
# Testcase Example:  '10'
#
# 统计所有小于非负整数 n 的质数的数量。
# 
# 示例:
# 
# 输入: 10
# 输出: 4
# 解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
# 
# 
#
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        nums = [1]*(n)
        nums[0] = 0
        nums[1] = 0
        factor = int(n**0.5)
        for i in range(2,factor+1):
            if nums[i]:
                for j in range(i**2,n,i):
                    nums[j] = 0
        return sum(nums)
        

