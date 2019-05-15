class TreeNode:
    def __init__(self,x):
        self.val = None
        self.left = None
        self.right = None
class Solution:
    def HasSubTree(self,pRoot1,pRoot2):
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.SubTreeCore(pRoot1,pRoot2)
            if not res:
                res = self.HasSubTree(pRoot1.left,pRoot2)
            if not res:
                res = self.HasSubTree(pRoot1.right,pRoot2)
        return res
    def SubTreeCore(self,pRoot1,pRoot2):
        if not pRoot2:
            return True
        if not pRoot1:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.SubTreeCore(pRoot1.left,pRoot2.left) and self.SubTreeCore(pRoot1.right,pRoot2.right)
        
