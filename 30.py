class Solution:
    def __init__(self):
        self.stack = []
        self.ministack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.ministack:
            self.ministack.append(node)
        elif node < self.ministack[-1]:
            self.ministack.append(node)
        else:
            self.ministack.append(self.ministack[-1])
    def pop(self):
        # write code here
        if not self.stack or not self.ministack:
            return
        self.stack.pop()
        self.ministack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.ministack[-1]
        
        
