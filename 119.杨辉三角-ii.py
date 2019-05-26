#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#
# https://leetcode-cn.com/problems/pascals-triangle-ii/description/
#
# algorithms
# Easy (54.27%)
# Likes:    69
# Dislikes: 0
# Total Accepted:    15.2K
# Total Submissions: 27.1K
# Testcase Example:  '3'
#
# 给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。
# 
# 
# 
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
# 
# 示例:
# 
# 输入: 3
# 输出: [1,3,3,1]
# 
# 
# 进阶：
# 
# 你可以优化你的算法到 O(k) 空间复杂度吗？
# 
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if not rowIndex:
            return [1]
        result = [1,1]
        for layer in range(rowIndex-1):
            lastlayer = result
            layer = []
            for i in range(len(lastlayer)-1):
                if not i:
                    layer.append(1)
                layer.append(lastlayer[i]+lastlayer[i+1])
            layer.append(1)
            result = layer
        return result   

