#
# @lc app=leetcode.cn id=38 lang=python3
#
# [38] 报数
#
class Solution:
    def countAndSay(self, n: int) -> str:
        pre = '1'
        for i in range(n-1):
            newstr = ''
            k = 0
            for i in range(len(pre)):
                k += 1
                if i < len(pre) - 1 and pre[i] != pre[i+1]:
                    newstr += str(k)
                    newstr += str(pre[i])
                    k = 0
            newstr += str(k)
            newstr += str(pre[i])
            pre = newstr
        return pre
                




