#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (70.44%)
# Likes:    421
# Dislikes: 0
# Total Accepted:    52.4K
# Total Submissions: 72.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一个没有重复数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
#

# @lc code=start

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            subList = self.permute(nums[:i]+nums[i+1:])
            for item in subList: 
                res.append(item+[nums[i]])
        return res



# @lc code=end

