#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#
# https://leetcode-cn.com/problems/maximal-rectangle/description/
#
# algorithms
# Hard (44.18%)
# Likes:    218
# Dislikes: 0
# Total Accepted:    10.5K
# Total Submissions: 24.6K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# 给定一个仅包含 0 和 1 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。
# 
# 示例:
# 
# 输入:
# [
# ⁠ ["1","0","1","0","0"],
# ⁠ ["1","0","1","1","1"],
# ⁠ ["1","1","1","1","1"],
# ⁠ ["1","0","0","1","0"]
# ]
# 输出: 6
# 
#

# @lc code=start

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        n = len(matrix[0])
        height = [0]*(n+1)
        ans = 0
        for row in matrix:
            for i in range(n):
                height[i] = height[i]+1 if row[i] == '1' else 0
            stack = []
            for k in range(n+1):
                while stack and height[k]<height[stack[-1]]:
                    h = height[stack.pop()]
                    w = k-stack[-1]-1 if stack else k
                    ans = max(ans,h*w)
                stack.append(k)
        return ans
            
        
# @lc code=end

