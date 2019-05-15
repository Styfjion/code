# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    
    def push(self, node):
        # write code here
        self.stackA.append(node)
    def pop(self):
        # return xx
        if self.stackB:
            return self.stackB.pop()
        elif self.stackA:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()
        else:
            return None