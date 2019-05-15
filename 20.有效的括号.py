#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in mapping:
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack