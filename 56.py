"""
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
"""
# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array or len(array)<2:
            return []
        if len(array) == 2:
            return array
        total_sum = 0
        for unit in array:
            total_sum ^= unit
        index = bin(total_sum)[::-1].index('1')
        num1 = 0
        num2 = 0
        for unit in array:
            if bin(unit)[::-1][index] == '1':
                num1 ^= unit
            else:
                num2 ^= unit
        return [num1,num2]