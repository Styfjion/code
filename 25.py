class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class Solution:
    def Merge(self,pHead1,pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        pMergeHead = None
        if pHead1.val<pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next,pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1,pHead2.next)
        return pMergeHead