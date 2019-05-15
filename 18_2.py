class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
#设置哑变量
class Solution:
    def deletDuplicateNode(self,pHead):
        if not pHead:
            return pHead
        pDumb = ListNode(None)
        pDumb.next = pHead
        pNode = pHead
        preNode = pDumb
        while pNode and pNode.next:
            if pNode.val == pNode.next.val:
                value = pNode.val
                while pNode and pNode.val == value:
                    pNode = pNode.next
                preNode.next = pNode
            else:
                preNode = pNode
                pNode = pNode.next
        return pDumb.next

                
    

class Solution2:
    def deleteDuplication(self, pHead):
        # write code here
        first=ListNode(-1)
        first.next=pHead
        last=first
        
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val=pHead.val
                while pHead and pHead.val==val:
                    pHead=pHead.next
                last.next=pHead
            else:
                last=pHead
                pHead=pHead.next
        return first.next

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(2)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    Solution().deletDuplicateNode(a)

               
                        

                    


