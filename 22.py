class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
    def FindKthToTail(self,head,k):
        if not head or k<=0:
            return None
        pAhead = head
        pBihind = None
        for i in range(k-1):
            if pAhead.next:#注意此处为next不为空
                pAhead = pAhead.next
            else:
                return None
        pBihind = head
        while pAhead.next:
            pAhead = pAhead.next
            pBihind = pBihind.next
        return pBihind
        
