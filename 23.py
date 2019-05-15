class ListNode:
    def __init__(self,x):
        self.val = x
        self.Next = None
    def EntryNodeOfLoop(self,pHead):
        pFast = pHead
        pSlow = pHead
        while pFast and pFast.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                break
        if not pFast or not pFast.next:
            return
        #求环中有几个节点
        meetingNode = pFast
        nodesLoop = 1
        while pFast.next != meetingNode:
            pFast = pFast.next
            nodesLoop += 1
        #求入口节点
        pFast = pHead
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast,nodesLoop
