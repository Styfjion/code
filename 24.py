class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self,pHead):
        pReverseHead = None
        pNode = pHead
        pPrev = None
        while pNode:
            pNext = pNode.pNext
            if not pNext:
                pReverseHead = pNode
            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReverseHead
        
            

