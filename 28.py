class TreeNode:
    def __init__(self,x):
        self.val = None
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self,pRoot):
        return self.isSymmetricalCore(pRoot,pRoot)
    def isSymmetricalCore(self,pRoot1,pRoot2):
        if not pRoot1 and not pRoot2:
            return True
        if not pRoot1 or pRoot2:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetricalCore(pRoot1.left,pRoot2.right) and self.isSymmetricalCore(pRoot1.right,pRoot2.left)
        

            