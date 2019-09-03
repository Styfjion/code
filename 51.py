'''
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
'''

# 空间换时间
# -*- coding:utf-8 -*-
class Solution:
    
    def InversePairs(self, data):
        # write code here
        if len(data)<=0:
            return 0
        length=len(data)
        copy=[0]*length
        for i in range(length):
            copy[i]=data[i]
        #copy数组为原数组data的复制,在后面充当辅助数组
        count=self.Core(data,copy,0,length-1)
        return count % 1000000007
    
    def Core(self,data,copy,start,end):
        if start==end:
            copy[start]=data[start]
            return 0

        length=(end-start)//2 #length为划分后子数组的长度

        left=self.Core(copy,data,start,start+length)
        right=self.Core(copy,data,start+length+1,end)

        #初始化i为前半段最后一个数字的下标
        i=start+length
        #初始化j为后半段最后一个数字的下标
        j=end

        #indexCopy为辅助数组的指针，初始化其指向最后一位
        indexCopy=end
        #准备开始计数
        count=0
        #对两个数组进行对比取值的操作：
        while i>=start and j>=start+length+1:
            if data[i]>data[j]:
                copy[indexCopy]=data[i]
                indexCopy-=1
                i-=1
                count += j-start-length
            else:
                copy[indexCopy]=data[j]
                indexCopy-=1
                j-=1
        
        #剩下一个数组未取完的操作：
        while i>=start:
            copy[indexCopy]=data[i]
            indexCopy-=1
            i-=1
        while j>=start+length+1:
            copy[indexCopy]=data[j]
            indexCopy-=1
            j-=1
        
        return count+left+right