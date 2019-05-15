# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRootOfTree):
        # write code here
        if not pRootOfTree:
            return
        self.arr = []
        self.inCore(pRootOfTree)
        for i,v in enumerate(self.arr[:-1]):
            self.arr[i].right = self.arr[i+1]
            self.arr[i+1].left = v
        return self.arr[0] 
    def inCore(self,pRoot):
        if not pRoot:
            return
        self.inCore(pRoot.left)
        self.arr.append(pRoot)
        self.inCore(pRoot.right)