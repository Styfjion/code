#
# @lc app=leetcode.cn id=974 lang=python3
#
# [974] 和可被 K 整除的子数组
#
# https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/description/
#
# algorithms
# Medium (32.61%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    1.4K
# Total Submissions: 4.1K
# Testcase Example:  '[4,5,0,-2,-3,1]\n5'
#
# 给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。
# 
# 
# 
# 示例：
# 
# 输入：A = [4,5,0,-2,-3,1], K = 5
# 输出：7
# 解释：
# 有 7 个子数组满足其元素之和可被 K = 5 整除：
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2,
# -3]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 30000
# -10000 <= A[i] <= 10000
# 2 <= K <= 10000
# 
# 
#

# @lc code=start
#超时方法
"""
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        dp = [0]*len(A)
        count = 0
        for i in range(len(A)):
            for j in range(i+1):
                dp[j] += A[i]
                if not dp[j]%K:
                    count += 1
        return count
"""

"""
不使用collection
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P = [0]
        for unit in A:
            P.append((P[-1]+unit)%K)
        P_dict = {}
        for item in P:
            P_dict[item] = P_dict.get(item,0)+1
        countlist = [v*(v-1)//2 for v in P_dict.values()]
        return sum(countlist)
"""
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        P = [0]
        for unit in A:
            P.append((P[-1]+unit)%K)
        from collections import Counter
        count = Counter(P)
        return (sum([v*(v-1)//2 for v in count.values()]))

# @lc code=end

