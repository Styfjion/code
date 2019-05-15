#-*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
# 返回二维列表，内部每个列表表示找到的路
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        path = []
        result = []
        self.FindPathCore(root,expectNumber,path,result)
        result = sorted(result,key=len,reverse=True)
        return result
    def FindPathCore(self,root,expectNumber,path,result):
        path.append(root.val)
        if not root.left and not root.right and sum(path) == expectNumber:
            result.append(path.copy()) #易错，不能直接赋值，path变化后，result也变化，若为python2改为path[:]
        if root.left:
            self.FindPathCore(root.left,expectNumber,path,result)
        if root.right:
            self.FindPathCore(root.right,expectNumber,path,result)
        path.pop()
if __name__ == "__main__":
    a = TreeNode(10)
    b = TreeNode(5)
    c = TreeNode(12)
    d = TreeNode(4)
    e = TreeNode(7)
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    print(Solution().FindPath(a,22))




