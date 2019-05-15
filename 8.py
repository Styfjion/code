# -*- coding:utf-8 -*-
class BinaryTreeNode:
    def __init__(self,x):
        self.var = x
        self.left = None
        self.right = None
        self.parent = None




class Solution:    
    def GetNext(pNode):
        pNext = None     
        if pNode.right:
            pRight = pNode.right
            while pRight.left:
                pRight = pNode.left
            pNext = pRight
        elif pNode.parent:
            pCurrent = pNode
            pParent = pNode.parent
            while pCurrent.parent and pParent.right==pCurrent:
                pCurrent = pParent
                pParent = pParent.parent
            pNext = pParent
        return pNext


