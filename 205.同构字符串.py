#
# @lc app=leetcode.cn id=205 lang=python3
#
# [205] 同构字符串
#
# https://leetcode-cn.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (45.19%)
# Likes:    116
# Dislikes: 0
# Total Accepted:    13.2K
# Total Submissions: 29.3K
# Testcase Example:  '"egg"\n"add"'
#
# 给定两个字符串 s 和 t，判断它们是否是同构的。
# 
# 如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。
# 
# 所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。
# 
# 示例 1:
# 
# 输入: s = "egg", t = "add"
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: s = "foo", t = "bar"
# 输出: false
# 
# 示例 3:
# 
# 输入: s = "paper", t = "title"
# 输出: true
# 
# 说明:
# 你可以假设 s 和 t 具有相同的长度。
# 
#
#自己的答案
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        schar = []
        tchar = []
        length = len(s)
        counts = 0
        countt = 0
        for i in range(length):
            if not s[i] in schar:
                counts = i
                schar.append(s[i])
            else:
                counts = schar.index(s[i])
            if not t[i] in tchar:
                countt = i
                tchar.append(t[i])
            else:
                countt = tchar.index(t[i])
            if counts!=countt:
                return False
        return True

#高票答案
def isIsomorphic4(self, s, t): 
    return [s.find(i) for i in s] == [t.find(j) for j in t]
def isIsomorphic5(self, s, t):
    return map(s.find, s) == map(t.find, t)

            
        

