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
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys

class Solution:
    
    result = -sys.maxsize-1
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxValue(root)
        return self.result
    
    """
    最大路径和：根据当前节点的角色，路径和可分为两种情况：
    一：以当前节点为根节点
    1.只有当前节点
    2.当前节点+左子树
    3.当前节点+右子书
    4.当前节点+左右子树    
    这四种情况的最大值即为以当前节点为根的最大路径和
    此最大值要和已经保存的最大值比较，得到整个树的最大路径值
    
    二：当前节点作为父节点的一个子节点
    和父节点连接的话则需取【单端的最大值】
    1.只有当前节点
    2.当前节点+左子树
    3.当前节点+右子书
    这三种情况的最大值    
    """
    def maxValue(self,root):
        if root == None:            
            return 0
        
        leftValue = self.maxValue(root.left)
        rightValue = self.maxValue(root.right)
        
        value1 = root.val
        value2 = root.val + leftValue
        value3 = root.val + rightValue
        value4 = root.val + rightValue + leftValue
        
        #以此节点为根节点的最大值
        maxValue = max([value1,value2,value3,value4])
        
        #当前遍历树的最大值
        self.result = max(maxValue, self.result)
        
        #要和父节点关联，则需要取去除情况4的最大值
        return max([value1,value2,value3])

class Solution2:
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
        