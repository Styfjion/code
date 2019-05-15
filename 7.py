# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:    
    def reConstructBinaryTree(self, pre, tin):         
        if not pre or not tin:            
            return None        
        root = TreeNode(pre.pop(0))
        if not root.val in tin:
            raise ValueError('Invalid input')    
        index = tin.index(root.val)        
        root.left = self.reConstructBinaryTree(pre, tin[:index])        
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])        
        return root

class Solution2:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre:
            return []
        if not tin:
            return []
        rootValue = pre[0]
        root = TreeNode(rootValue)
        if len(pre) == 1:
            if len(tin) == 1 and pre[0] == tin[0]:
                return root
            else: 
                raise ValueError('Invalid input')
        for i in range(len(tin)):
            if tin[i] == rootValue:
                break
        if tin[i]!= rootValue:
            raise ValueError('Invalid input')
        leftLength = i
        if leftLength > 0:
            root.left = self.reConstructBinaryTree(pre[1:leftLength+1],tin[:leftLength])
        if leftLength < len(pre)-1 and leftLength< len(tin)-1:
            root.right = self.reConstructBinaryTree(pre[leftLength+1:],tin[leftLength+1:])
        return root
if __name__ == "__main__":
    sol = Solution()
    sol.reConstructBinaryTree([1,2,4,7,3,5,6,8],[4,7,2,1,5,3,8,6])
