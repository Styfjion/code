#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#
# https://leetcode-cn.com/problems/largest-number/description/
#
# algorithms
# Medium (32.78%)
# Likes:    136
# Dislikes: 0
# Total Accepted:    10K
# Total Submissions: 30K
# Testcase Example:  '[10,2]'
#
# 给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。
# 
# 示例 1:
# 
# 输入: [10,2]
# 输出: 210
# 
# 示例 2:
# 
# 输入: [3,30,34,5,9]
# 输出: 9534330
# 
# 说明: 输出结果可能非常大，所以你需要返回一个字符串而不是整数。
# 
# 
class LargerNumKey(str):     # 继承str类
    def __lt__(x, y):       # 重写str类中的__lt__函数
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_nums = list(map(str,nums))
        str_nums.sort(key=LargerNumKey)
        return ''.join(str_nums).lstrip('0') or '0'

