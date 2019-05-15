class Solution:
    def NumberOf1(self, n):
        # write code here
        sum = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            n = (n-1) & n
            sum += 1
        return sum
