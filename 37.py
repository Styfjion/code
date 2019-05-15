# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    flag = -1
    def Serialize(self, root):
        # write code here
        if not root:
            return '#'
        return '{},{},{}'.format(str(root.val),self.Serialize(root.left),self.Serialize(root.right))
    def Deserialize(self, s):
        # write code here
        self.flag += 1
        lis = s.split(',')
        if self.flag > len(s):
            return
        root  = None #注意此处，递归调用需置空
        if lis[self.flag] != '#':
            root = TreeNode(int(lis[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
