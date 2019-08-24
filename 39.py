'''
题目：数组中出现次数超过一半的数字

题：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。

'''
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        target = numbers[0]
        times = 1
        for i in range(1,len(numbers)):
            if not times:
                times = 1
                target = numbers[i]
            elif target == numbers[i]:
                times += 1
            else:
                times -= 1
        count = 0
        for unit in numbers:
            if unit == target:
                count += 1
        if 2*count <= len(numbers):
            target = 0
        return target
        