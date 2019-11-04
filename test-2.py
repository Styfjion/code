#-*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        if not pHead:
            return
        pFast = pHead
        pSlow = pHead
        if not pFast.next:
            return
        if not pFast.next.next:
            if pFast == pFast.next:
                return pFast
            else:
                return 
        while pFast.next.next:
            pFast = pFast.next.next
            pSlow = pSlow.next
            if pFast == pSlow:
                return pFast
        return