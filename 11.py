# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        index1 = 0
        index2 = len(rotateArray) - 1
        indexMid = index1
        while rotateArray[index1]>=rotateArray[index2]:
            if index2 - index1 == 1:
                indexMid = index2
                break
            indexMid = (index1+index2)/2
            if rotateArray[index2] == rotateArray[index1] and rotateArray[index2] == rotateArray[indexMid]:
                return self.minNumberInOrder(index1,index2,rotateArray)
            if rotateArray[index1] <= rotateArray[indexMid]:
                index1 = indexMid
            elif rotateArray[index2] >= rotateArray[indexMid]:
                index2 = indexMid
        return rotateArray[indexMid]
    
    def minNumberInOrder(self,index1,index2,rotateArray):
        result = rotateArray[index1]
        for unit in rotateArray:
            if unit<result:
                result = unit
        return result