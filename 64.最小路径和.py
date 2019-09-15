#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode-cn.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (61.91%)
# Likes:    272
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 48.3K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
# 
# 说明：每次只能向下或者向右移动一步。
# 
# 示例:
# 
# 输入:
# [
# [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# 输出: 7
# 解释: 因为路径 1→3→1→1→1 的总和最小。
# 
# 
#
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        for i in range(len(grid)-1,-1,-1):
            for j in range(len(grid[0])-1,-1,-1):
                if i == len(grid)-1 and j!=len(grid[0])-1:
                    grid[i][j] += grid[i][j+1]
                elif i != len(grid)-1 and j ==len(grid[0])-1:
                    grid[i][j] += grid[i+1][j]
                elif i<len(grid)-1 and j<len(grid[0])-1:
                    grid[i][j] += min(grid[i][j+1],grid[i+1][j])
        return grid[0][0]

