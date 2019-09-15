"""
输入两个链表，找出它们的第一个公共结点。
"""
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if not pHead1 or not pHead2:
            return None
        stack1 = []
        stack2 = []
        while pHead1 or pHead2:
            if pHead1:
                stack1.append(pHead1)
                pHead1 = pHead1.next
            if pHead2:
                stack2.append(pHead2)
                pHead2 = pHead2.next
        for i in range(1,min(len(stack1),len(stack2))+1):
            if stack1[-i] != stack2[-i]:
                break
        if i == 1:
            return None
        elif i == min(len(stack1),len(stack2)):
            if len(stack1) > len(stack2):
                return stack2[0]
            else:
                return stack1[0]
        else:
            return stack1[-(i-1)]
"""
方法二：
首先遍历两个链表得到它们的长度，如果m>n，
则m链表先走m-n步，然后两个链表再同时走，直到找到第一个相同的节点（即为它们的第一个公共节点）。
（推荐，时间复杂度O(m+n),且不需要额外辅助空间）
"""
class Solution2:
    def FindFirstCommonNode(self, pHead1, pHead2):
        length1=self.GetLength(pHead1)
        length2=self.GetLength(pHead2)
        
        if length1>length2:
            headLong=pHead1
            headShort=pHead2
        else:
            headLong=pHead2
            headShort=pHead1
        diff=abs(length1-length2)
        
        for i in range(diff):
            headLong=headLong.next
        
        while headLong!=None and headShort!=None and headLong!=headShort:
            headLong=headLong.next
            headShort=headShort.next
        return headLong
            
    def GetLength(self,pHead):
        length=0
        while pHead:
            pHead=pHead.next
            length += 1
        return length