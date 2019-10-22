#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#
# https://leetcode-cn.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (55.25%)
# Likes:    146
# Dislikes: 0
# Total Accepted:    10.9K
# Total Submissions: 19.2K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# 给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地)
# 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
# 
# 找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)
# 
# 示例 1:
# 
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠[0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠[0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# 
# 对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。
# 
# 示例 2:
# 
# 
# [[0,0,0,0,0,0,0,0]]
# 
# 对于上面这个给定的矩阵, 返回 0。
# 
# 注意: 给定的矩阵grid 的长度和宽度都不超过 50。
# 
#

# @lc code=start
class Solution:
    count = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dir = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def findArea(grid,x,y):
            for unit in dir:
                nx = x+unit[0]
                ny = y+unit[1]
                if nx>=0 and nx<len(grid) and ny>=0 and ny<len(grid[0]) and grid[nx][ny] == 1:
                    self.count += 1
                    grid[nx][ny] = 0
                    findArea(grid,nx,ny)
        res = []   
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    self.count = 1
                    grid[i][j] = 0
                    findArea(grid,i,j)
                    res.append(self.count)
        if not res:
            return 0
        else:
            return max(res)               
        
# @lc code=end

