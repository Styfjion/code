'''
把只包含质因子2、3和5的数称作丑数（Ugly Number）。
例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if not index:
            return 0
        res = [1]
        t2 = t3 = t5 = 0
        token = 1
        while token < index:
            res.append(min(res[t2]*2,res[t3]*3,res[t5]*5))
            while res[t2]*2 <= res[-1]:   # 等号很关键
                t2 += 1
            while res[t3]*3 <= res[-1]:
                t3 += 1
            while res[t5]*5 <= res[-1]:
                t5 += 1
            token += 1
        return res[token-1]