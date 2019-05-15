# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]
        for i in range(len(sequence)-1):
            if sequence[i] > root:
                break
        for j in range(i,len(sequence)-1):
            if sequence[j] < root:
                return False
        left = True
        if not i:
            self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence) - 1:
            self.VerifySquenceOfBST(sequence[i:-1])
        return left and right
