#
# @lc app=leetcode.cn id=329 lang=python3
#
# [329] 矩阵中的最长递增路径
#
# https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (39.02%)
# Likes:    80
# Dislikes: 0
# Total Accepted:    5.4K
# Total Submissions: 13.7K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# 给定一个整数矩阵，找出最长递增路径的长度。
# 
# 对于每个单元格，你可以往上，下，左，右四个方向移动。 你不能在对角线方向上移动或移动到边界外（即不允许环绕）。
# 
# 示例 1:
# 
# 输入: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径为 [1, 2, 6, 9]。
# 
# 示例 2:
# 
# 输入: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# 输出: 4 
# 解释: 最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。
# 
# 
#

# @lc code=start
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(path,x,y):
            if path[x][y]:
                return path[x][y]
            for i in range(4):
                nx = x+dir[i][0]
                ny = y+dir[i][1]
                if nx>=0 and nx<len(matrix) and ny>=0 and ny<len(matrix[0]) and matrix[nx][ny] > matrix[x][y]:
                    path[x][y] = max(path[x][y],dfs(path,nx,ny))
            path[x][y] += 1
            return path[x][y]
        path = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        ans = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,dfs(path,i,j))
        return ans
        
# @lc code=end

