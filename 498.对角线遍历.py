#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#
# https://leetcode-cn.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (38.28%)
# Likes:    49
# Dislikes: 0
# Total Accepted:    6.9K
# Total Submissions: 17.8K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。
# 
# 
# 
# 示例:
# 
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# 输出:  [1,2,4,7,5,3,6,8,9]
# 
# 解释:
# 
# 
# 
# 
# 
# 说明:
# 
# 
# 给定矩阵中的元素总数不会超过 100000 。
# 
# 
#

# @lc code=start
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        res = []
        r = c = 0
        for _ in range(row*col):
            res.append(matrix[r][c])
            if not (r+c)%2:
                if c == col-1:
                    r += 1
                elif not r:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == row-1:
                    c += 1
                elif not c:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return res
            

# @lc code=end

