# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, pRoot):
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
                result.append(subresult)
                subresult = []
        return result

class Solution2:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        if not pRoot:
            return []
        res,nodes=[],[pRoot]
        while nodes:
            curStack,nextStack=[],[]
            for node in nodes:
                curStack.append(node.val)
                if node.left:
                    nextStack.append(node.left)
                if node.right:
                    nextStack.append(node.right)
            res.append(curStack)
            nodes=nextStack
        return res

            
            