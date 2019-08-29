'''
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置。
'''
# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if not s:
            return -1
        for i in s:
            if s.count(i) == 1:
                return s.index(i)

class Solution2:
    def FirstNotRepeatingChar(self, s):
    # write code here
        if not s:
            return -1
        dict_ch = {}
        for i in s:
            if i not in dict_ch:
                dict_ch[i] = 1
            else:
                dict_ch[i] += 1
        for i,ch in enumerate(s):
            if dict_ch[ch] == 1:
                return i
