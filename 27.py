class TreeNode:
    def __init__(self,x):
        self.val = None
        self.left = None
        self.right = None
    def Mirror(self,root):
        if not root:
            return
        if not root.right or root.left:
            return
        root.left,root.right = root.right,root.left
        if root.left:
            self.Mirror(root.left)
        if root.right:
            self.Mirror(root.right)
            