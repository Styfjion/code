#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] 快乐数
#
# https://leetcode-cn.com/problems/happy-number/description/
#
# algorithms
# Easy (53.95%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 40.1K
# Testcase Example:  '19'
#
# 编写一个算法来判断一个数是不是“快乐数”。
# 
# 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到
# 1。如果可以变为 1，那么这个数就是快乐数。
# 
# 示例: 
# 
# 输入: 19
# 输出: true
# 解释: 
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
#
class Solution:
    def isHappy(self, n: int) -> bool:
        cache = []
        while 1:
            if n == 1:
                return True
            strnList = str(n)
            n = sum([int(unit)**2 for unit in strnList])
            if n in cache:
                return False
            cache.append(n)

