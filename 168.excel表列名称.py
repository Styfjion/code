#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (32.62%)
# Likes:    113
# Dislikes: 0
# Total Accepted:    8.5K
# Total Submissions: 26.1K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#
class Solution:
    def convertToTitle(self, n: int) -> str:
        target = ''
        while n > 0:
            res = (n-1)%26               #注意减去‘1’的操作，与进制转换不同的是，此处无‘0’对应的字符，因此将‘A’看作‘0’
            target = chr(res+ord('A'))+target
            n = (n-1)//26
        return target


