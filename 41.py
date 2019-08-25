'''
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。
'''

# -*- coding:utf-8 -*-
from heapq import *
class Solution:
 def __init__(self):
     self.heaps = [], []
 def Insert(self, num):
     # write code here
     left,right = self.heaps
     heappush(left, -heappushpop(right, num)) #将num放入小根堆，并弹出最小值，取反，放入大根堆left
     if len(right) < len(left):
         heappush(right, -heappop(left)) #弹出left中最小的值，取反，即最大的值，放入right
 def GetMedian(self,ss):
     # write code here
     left,right = self.heaps
     if len(right) > len(left):
         return float(right[0])
     return (right[0] - left[0]) /2.0


# 自己建堆
class Solution2:
               
    def __init__(self):
        self.heaps = [], []

    def big_endian(self,array,root,end):
        while True:
            child = 2*root + 1
            if child > end:
                break
            if child+1 <= end and array[child+1] > array[child]:
                child += 1
            if array[child] > array[root]:
                array[root],array[child] = array[child],array[root]
                root = child
            else:
                break
    
    def adjust(self,arr):
        #调整部分
        for i in range(len(arr)//2-1,-1,-1):
            self.big_endian(arr,i,len(arr)-1)

    def Insert(self, num):
    # write code here
        left,right = self.heaps
        right.append(-num)
        self.adjust(right)
        left.append(-right.pop(0))
        self.adjust(left)
        self.adjust(right)   # 弹出元素后需要重新调整
        if len(left) > len(right):
            right.append(-left.pop(0))
            self.adjust(right)
            self.adjust(left)  # 弹出元素后需要重新调整

    def GetMedian(self,ss):
        # write code here
        left,right = self.heaps
        if len(right) > len(left):
            return float(-right[0])
        return (left[0]-right[0]) /2.0
    





    


if __name__ == "__main__":
    sol = Solution2()
    array = [5,2,3,4,1,6,7,0,8]
    for unit in array:
        sol.Insert(unit)
        print(sol.GetMedian(''))

    
