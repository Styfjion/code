#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#
# https://leetcode-cn.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (58.85%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 22.7K
# Testcase Example:  '[1,2,3,null,5]'
#
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例:
# 
# 输入:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# 输出: ["1->2->5", "1->3"]
# 
# 解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def construct_path(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += '->'
                    if root.left:
                        construct_path(root.left,path)
                    if root.right:
                        construct_path(root.right,path)
        paths = []
        construct_path(root,'')
        return paths

