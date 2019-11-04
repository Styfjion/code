#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#
# https://leetcode-cn.com/problems/permutations-ii/description/
#
# algorithms
# Medium (52.95%)
# Likes:    172
# Dislikes: 0
# Total Accepted:    25.7K
# Total Submissions: 46.9K
# Testcase Example:  '[1,1,2]'
#
# 给定一个可包含重复数字的序列，返回所有不重复的全排列。
# 
# 示例:
# 
# 输入: [1,1,2]
# 输出:
# [
# ⁠ [1,1,2],
# ⁠ [1,2,1],
# ⁠ [2,1,1]
# ]
# 
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return 
        if len(nums) == 1:
            return [nums]
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i and nums[i-1] == nums[i]:
                continue
            subList = self.permuteUnique(nums[:i]+nums[i+1:])
            for item in subList: 
                res.append(item+[nums[i]])
        return res 
# @lc code=end

