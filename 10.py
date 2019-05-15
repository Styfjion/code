# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if not n:
            return 0
        elif n == 1:
            return 1
        fMinusTwo = 0
        fMinusOne = 1
        for i in range(int(n/2)):
            fMinusTwo = fMinusOne + fMinusTwo
            fMinusOne = fMinusTwo + fMinusOne
        if n%2:
            return fMinusOne
        else:
            return fMinusTwo


# -*- coding:utf-8 -*-
class Solution2:    
    def Fibonacci(self, n):        
        # write code here        
        res=[0,1,1,2]        
        while len(res)<=n:            
            res.append(res[-1]+res[-2])        
            return res[n]
        