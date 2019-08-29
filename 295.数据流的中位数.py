#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#
# https://leetcode-cn.com/problems/find-median-from-data-stream/description/
#
# algorithms
# Hard (36.48%)
# Likes:    63
# Dislikes: 0
# Total Accepted:    5K
# Total Submissions: 13.3K
# Testcase Example:  '["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"]\n[[],[1],[2],[],[3],[]]'
#
# 中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。
# 
# 例如，
# 
# [2,3,4] 的中位数是 3
# 
# [2,3] 的中位数是 (2 + 3) / 2 = 2.5
# 
# 设计一个支持以下两种操作的数据结构：
# 
# 
# void addNum(int num) - 从数据流中添加一个整数到数据结构中。
# double findMedian() - 返回目前所有元素的中位数。
# 
# 
# 示例：
# 
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
# 
# 进阶:
# 
# 
# 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
# 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
# 
# 
#


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = [],[]
        

    def addNum(self, num: int) -> None:
        import heapq
        left,right = self.array
        min_right = heapq.heappushpop(right,num)
        heapq.heappush(left,-min_right)
        if len(left) > len(right):
            max_left = heapq.heappop(left)
            heapq.heappush(right,-max_left)

    def findMedian(self) -> float:
        left,right = self.array
        if len(left) < len(right):
            return right[0]
        else:
            return (right[0]-left[0])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



# 超时
'''
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.array = [],[]
        

    def small_heap(self,array):
        for start in range(len(array)//2-1,-1,-1):
            end = len(array)-1
            root = start
            while True:
                child = root*2+1
                if child > end:
                    break
                if child+1 <= end and array[child+1] < array[child]:
                    array[child+1],array[child] = array[child],array[child+1]
                if array[root] > array[child]:
                    array[root],array[child] = array[child],array[root]
                    root = child
                else:
                    break

    def addNum(self, num: int) -> None:
        left,right = self.array
        if len(left) == len(right):
            left.append(-num)
            self.small_heap(left)
            right.append(-left.pop(0))
            self.small_heap(right)
        else:
            right.append(num)
            self.small_heap(right)
            left.append(-right.pop(0))
            self.small_heap(left)



    def findMedian(self) -> float:
        left,right = self.array
        if len(left) == len(right):
            return (right[0]-left[0])/2
        else:
            return right[0]
'''