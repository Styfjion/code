#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
class Solution:
    def mySqrt(self, x: int) -> int:
        left,right = 0,x
        while left <= right:
            mid = (left+right)//2
            if mid**2 <= x < (mid+1)**2:
                return mid
            elif x < mid**2:
                right = mid
            elif x == (mid+1)**2:
                return mid+1
            else:
                left = mid + 1
                

