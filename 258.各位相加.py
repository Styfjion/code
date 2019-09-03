#
# @lc app=leetcode.cn id=258 lang=python3
#
# [258] 各位相加
#
# https://leetcode-cn.com/problems/add-digits/description/
#
# algorithms
# Easy (63.87%)
# Likes:    164
# Dislikes: 0
# Total Accepted:    19.8K
# Total Submissions: 30.7K
# Testcase Example:  '38'
#
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
# 
# 示例:
# 
# 输入: 38
# 输出: 2 
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
# 
# 
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
# 
#
# 暴力法

class Solution:
    def addDigits(self, num: int) -> int:
        if num//10 < 1:
            return num
        count = 0 
        while num:
            count += num%10
            num //=10
        return self.addDigits(count)

# 找规律
class Solution2:
    def addDigits(self, num: int) -> int:
        if not num:
            return 0
        return num%9 or 9
