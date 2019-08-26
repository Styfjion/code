#
# @lc app=leetcode.cn id=233 lang=python3
#
# [233] 数字 1 的个数
#
# https://leetcode-cn.com/problems/number-of-digit-one/description/
#
# algorithms
# Hard (29.45%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    2.6K
# Total Submissions: 8.7K
# Testcase Example:  '13'
#
# 给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。
# 
# 示例:
# 
# 输入: 13
# 输出: 6 
# 解释: 数字 1 出现在以下数字中: 1, 10, 11, 12, 13 。
# 
#
class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        i = 1
        while i<=n:
            count += n//(i*10)*i + min(max(n%(i*10)-i+1,0),i)
            i*=10
        return count

