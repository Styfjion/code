#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        s = s[::-1]
        if not ' ' in s:
            return len(s)
        else:
            return s.index(' ')

