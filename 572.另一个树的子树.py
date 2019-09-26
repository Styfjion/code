#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一个树的子树
#
# https://leetcode-cn.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (40.57%)
# Likes:    118
# Dislikes: 0
# Total Accepted:    7.9K
# Total Submissions: 18.9K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s
# 也可以看做它自身的一棵子树。
# 
# 示例 1:
# 给定的树 s:
# 
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# 
# 给定的树 t：
# 
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# 
# 返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。
# 
# 示例 2:
# 给定的树 s：
# 
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# 
# 给定的树 t：
# 
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
# 
# 
# 返回 false。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    node = None
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        
        def isSub(s):
            if not s:
                return False
            if s.val == t.val:
                self.node = s
                return True
            return isSub(s.left) or isSub(s.right)
        
        def isTrue(s,t):
            if not t:
                return True
            if not s and t:
                return False
            mid = (s.val==t.val)
            left = isTrue(s.left,t.left)
            right = isTrue(s.right,s.right)
            return left and mid and right

        if not s and not t:
            return True
        if not s or not t:
            return False
        flag = isSub(s)
        if not flag:
            return False
        return isTrue(self.node,t)
        
        
        

