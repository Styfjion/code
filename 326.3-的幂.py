#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3的幂
#
# https://leetcode-cn.com/problems/power-of-three/description/
#
# algorithms
# Easy (44.78%)
# Likes:    94
# Dislikes: 0
# Total Accepted:    37.6K
# Total Submissions: 80.6K
# Testcase Example:  '27'
#
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
# 
# 示例 1:
# 
# 输入: 27
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: 0
# 输出: false
# 
# 示例 3:
# 
# 输入: 9
# 输出: true
# 
# 示例 4:
# 
# 输入: 45
# 输出: false
# 
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# 
#

# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if not n:
            return False
        while n/3 >= 1:
            n /= 3
        return n==1
# @lc code=end

