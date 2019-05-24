#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (37.75%)
# Likes:    120
# Dislikes: 0
# Total Accepted:    18.2K
# Total Submissions: 47.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
# 
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 给定二叉树 [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最小深度  2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#----------------------------------------------------------------
#自己的解法
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        count = 1
        lastLayer = [root]
        while True:
            layer = []
            for unit in lastLayer:
                if not unit.left and not unit.right:
                    return count
                if unit.left:
                    layer.append(unit.left)
                if unit.right:
                    layer.append(unit.right)
            count += 1
            lastLayer = layer
#----------------------------------------------------------------
#高票答案
class Solution2:
    # @param root, a tree node
    # @return an integer    
    def minDepth(self, root):
        if root == None:
            return 0
        if root.left==None or root.right==None:
            return self.minDepth(root.left)+self.minDepth(root.right)+1
        return min(self.minDepth(root.right),self.minDepth(root.left))+1