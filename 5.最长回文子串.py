#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (26.07%)
# Likes:    1299
# Dislikes: 0
# Total Accepted:    112.9K
# Total Submissions: 415.3K
# Testcase Example:  '"babad"'
#
# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
# 
# 示例 1：
# 
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 
# 
# 示例 2：
# 
# 输入: "cbbd"
# 输出: "bb"
# 
# 
#
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        maxSub = [0,1]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(len(s)-2,-1,-1):
            for j in range(i+1,len(s)):
                if j == i+1:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j]:
                    if j-i+1 > maxSub[1] -maxSub[0]:
                        maxSub = [i,j+1]
        return s[maxSub[0]:maxSub[1]]
        
        

