"""
给定一棵二叉搜索树，请找出其中的第k小的结点。例如， （5，3，7，2，4，6，8）    中，按结点数值大小顺序第三小结点的值为4
"""
#-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    index = 0
    def KthNode(self, pRoot, k):
        # write code here
        if not pRoot or not k:
            return
        return self.KthNode_core(pRoot,k)
    
    def KthNode_core(self,pRoot,k):
        if not pRoot:
            return None
        left = self.KthNode_core(pRoot.left,k)
        if left:
            return left
        self.index += 1
        if self.index == k:
            return pRoot
        right = self.KthNode_core(pRoot.right,k)
        if right:
            return right
        return None