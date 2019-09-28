#
# @lc app=leetcode.cn id=63 lang=python3
#
# [63] 不同路径 II
#
# https://leetcode-cn.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (31.63%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    23.5K
# Total Submissions: 74K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
# 
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
# 
# 现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
# 
# 
# 
# 网格中的障碍物和空位置分别用 1 和 0 来表示。
# 
# 说明：m 和 n 的值均不超过 100。
# 
# 示例 1:
# 
# 输入:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# 输出: 2
# 解释:
# 3x3 网格的正中间有一个障碍物。
# 从左上角到右下角一共有 2 条不同的路径：
# 1. 向右 -> 向右 -> 向下 -> 向下
# 2. 向下 -> 向下 -> 向右 -> 向右
# 
# 
#
class Solution:
    res = 0
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dir = [[1,0],[0,1]]
        def dfs(x,y):
            if x == m-1 and y == n-1:
                self.res += 1
            if x<0 or y<0 or x>m-1 or y>n-1:
                return 
            for i in range(2):
                nx = x+dir[i][0]
                ny = y+dir[i][1]
                if nx>=0 and nx<m and ny>=0 and ny<n and obstacleGrid[nx][ny]!=1:
                    obstacleGrid[nx][ny] = 1
                    dfs(nx,ny)
                    obstacleGrid[nx][ny] = 0
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        dfs(0,0)
        return self.res
        




