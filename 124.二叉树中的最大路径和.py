#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#
# https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/description/
#
# algorithms
# Hard (34.22%)
# Total Accepted:    5.2K
# Total Submissions: 15.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个非空二叉树，返回其最大路径和。
# 
# 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点。
# 
# 示例 1:
# 
# 输入: [1,2,3]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   3
# 
# 输出: 6
# 
# 
# 示例 2:
# 
# 输入: [-10,9,20,null,null,15,7]
# 
# -10
# / \
# 9  20
# /  \
# 15   7
# 
# 输出: 42
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    ret = -2**31
    def maxPathSum(self, root: TreeNode) -> int:
        def getMax(root):
            if not root:
                return 0
            if root.left:
                left = max(0,getMax(root.left))
            else:
                left = 0
            if root.right:
                right = max(0,getMax(root.right))
            else:
                right = 0
            self.ret = max(self.ret,root.val+left+right)
            return max(left,right)+root.val
        getMax(root)
        return self.ret

