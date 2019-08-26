'''
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如输入数组{3，32，321}，则打印出这三个数字能排成的最小数字为321323。
'''


# 排列组合算法
# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ""
        import itertools
        str_numbers = list(map(str,numbers))
        str_numbers_per = itertools.permutations(str_numbers,len(numbers))
        numbers_per = []
        for unit in str_numbers_per:
            numbers_per.append(''.join(unit))
        numbers_per = list(map(int,numbers_per))
        return min(numbers_per)

'''
解题代码二：将数字转换为字符串后进行自定义排序（使得按照字符串拼接的从小到大的顺序排列）

设计比较大小的规则为 若 ab > ba 则 b应该在a前面。

 cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。

是两两对象之间的比较，排序默认是从小到大，在这个函数内部实现的两两排序。
'''
class Solution2:
    def PrintMinNumber(self, numbers):
        if not numbers:
            return ""
        str_numbers = list(map(str,numbers))
        str_numbers.sort(cmp=lambda x,y:cmp(x+y,y+x)) # python3中无此函数，可以直接比较字符串大小
        return ''.join(str_numbers)