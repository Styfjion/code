#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (39.11%)
# Likes:    144
# Dislikes: 0
# Total Accepted:    8.4K
# Total Submissions: 20.4K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 
# 示例 1 :
# 
# 
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 
# 
# 说明 :
# 
# 
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 
# 
#

# @lc code=start
"""
java,cpp过，python超时
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        P = [0]
        for num in nums:
            P.append(P[-1]+num)
        count = 0
        for i in range(len(P)):
            for j in range(i+1,len(P)):
                if P[j]-P[i] == k:
                    count += 1
        return count
"""
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sumn = 0
        count_dict = {0:1}
        for num in nums:
            sumn += num
            if sumn-k in count_dict:
                count += count_dict[sumn-k]
            count_dict[sumn] = count_dict.get(sumn,0)+1
        return count

        
# @lc code=end

