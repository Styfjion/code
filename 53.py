"""
题目：统计一个数字在排序数组中出现的次数。

思路：二分查找法，分别找到此数字在排序数组中第一次和最后一次出现的位置，然后次数等于两个位置之差加1。

时间复杂度：O(log n)
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        number = 0
        if data !=None and len(data)>0:
            length=len(data)
            first = self.GetFirstOfK(data,k,0,length-1)
            last = self.GetEndOfK(data,k,0,length-1)
            if first > -1 and last > -1:
                number=last-first+1
        return number
    
    def GetFirstOfK(self,data,k,begin,end):
        if begin>end:
            return -1
        mid = (begin+end)//2
        if data[mid] == k:
            if (mid>0 and data[mid-1] != k) or mid == 0:
                return mid
            else:
                end = mid-1
        elif data[mid] > k:
            end = mid-1
        else:
            begin = mid+1
        return self.GetFirstOfK(data,k,begin,end)
    
    def GetEndOfK(self,data,k,begin,end):
        if begin>end:
            return -1
        mid = (begin+end)//2
        if data[mid] == k:
            if(mid<len(data)-1 and data[mid+1]!=k) or mid == len(data)-1:
                return mid
            else:
                begin = mid+1
        elif data[mid] > k:
            end = mid-1
        else:
            begin = mid+1
        return self.GetEndOfK(data,k,begin,end)

if __name__ == "__main__":
    sol = Solution()
    sol.GetNumberOfK([3,3,3,3,4,5],3)
            