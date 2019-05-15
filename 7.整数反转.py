#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#
# https://leetcode-cn.com/problems/reverse-integer/description/
#
# algorithms
# Easy (32.20%)
# Total Accepted:    112.7K
# Total Submissions: 349.8K
# Testcase Example:  '123'
#
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 
# 示例 1:
# 
# 输入: 123
# 输出: 321
# 
# 
# 示例 2:
# 
# 输入: -123
# 输出: -321
# 
# 
# 示例 3:
# 
# 输入: 120
# 输出: 21
# 
# 
# 注意:
# 
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
# 
#
class Solution:
    def reverse(self, x: int) -> int:
        strInt = str(x)
        flag = False
        if strInt[0] == '-':
            flag = True
            strInt = strInt[1:]
        strList = list(strInt)
        strList.reverse()
        strInt = ''.join(strList)
        result = int(strInt)
        if flag:
            result = -result
        if result<-(2**31) or result >= 2**31:
            result = 0
        return result
