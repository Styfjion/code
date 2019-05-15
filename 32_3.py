# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        deque = []
        result = []
        subresult = []
        node = pRoot
        deque.append(node)
        nextLevel = 0
        toBePrinted = 1
        level = 1
        while deque:
            node = deque.pop(0)
            toBePrinted -= 1
            subresult.append(node.val)
            if node.left:
                deque.append(node.left)
                nextLevel += 1
            if node.right:
                deque.append(node.right)
                nextLevel += 1
            if not toBePrinted:
                toBePrinted = nextLevel
                nextLevel = 0
                if not level & 1:
                    subresult = subresult[::-1]
                result.append(subresult)
                subresult = []
                level += 1
        return result

class Solution2:
    def Print(self, pRoot):
        if not pRoot:
            return
        res,nodes = [],[pRoot]
        leftToRight = True
        while nodes:
            curStack,nextStack = [],[]
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            if not leftToRight:
                curStack.reverse()
            leftToRight = not leftToRight
            res.append(curStack)
            nodes = nextStack
        return res


        
