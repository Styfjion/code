#
# @lc app=leetcode.cn id=137 lang=python3
#
# [137] 只出现一次的数字 II
#
# https://leetcode-cn.com/problems/single-number-ii/description/
#
# algorithms
# Medium (64.42%)
# Likes:    195
# Dislikes: 0
# Total Accepted:    14K
# Total Submissions: 21.7K
# Testcase Example:  '[2,2,3,2]'
#
# 给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
# 
# 说明：
# 
# 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？
# 
# 示例 1:
# 
# 输入: [2,2,3,2]
# 输出: 3
# 
# 
# 示例 2:
# 
# 输入: [0,1,0,1,0,1,99]
# 输出: 99
# 
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = [0]
        minus_count = 0
        for num in nums:
            if num<0:
                num = -num
                minus_count += 1
            str_num = bin(num)[2:][::-1]
            for i in range(len(str_num)):
                if i>=len(res):
                    res.append(int(str_num[i]))
                elif str_num[i] == '1':
                    res[i] += 1
        bin_target = ''
        for unit in res:
            if unit%3:
                bin_target += '1'
            else:
                bin_target += '0'
        bin_target = bin_target[::-1]
        int_target = int(bin_target,2)
        if minus_count%3:
            return -int_target
        else:
            return int_target

# @lc code=end

