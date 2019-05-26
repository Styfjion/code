#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode-cn.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (60.79%)
# Likes:    152
# Dislikes: 0
# Total Accepted:    24K
# Total Submissions: 38.5K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 5
# 输出:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
# 
#
#----------------------------------------------------------------
#自己答案
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        if numRows == 1:
            return [[1]]
        result = [[1],[1,1]]
        for layer in range(numRows-2):
            lastlayer = result[-1]
            layer = []
            for i in range(len(lastlayer)-1):
                if not i:
                    layer.append(1)
                layer.append(lastlayer[i]+lastlayer[i+1])
            layer.append(1)
            result.append(layer)
        return result
#----------------------------------------------------------------
#高票答案
def generate(numRows):
    pascal = [[1]*(i+1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1,i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal

                    
            



