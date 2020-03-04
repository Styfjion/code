#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (39.81%)
# Likes:    131
# Dislikes: 0
# Total Accepted:    18.3K
# Total Submissions: 43.5K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 
# 示例1:
# 
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 
# 示例 4:
# 
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
# 
#

# @lc code=start
#自己答案
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern = list(pattern)
        str = str.split(' ')
        if len(pattern) != len(str):
            return False
        dict1 = {}
        dict2 = {}
        for i in range(len(pattern)):
            dict1[pattern[i]] = dict1.get(pattern[i],len(dict1)+1)
            dict2[str[i]] = dict2.get(str[i],len(dict2)+1)
            if dict1[pattern[i]] != dict2[str[i]]:
                return False
        return True

#高票答案
#利用map进行映射
class Solution2:
    def wordPattern(self, pattern: str, str: str) -> bool:
        s = pattern
        t = str.split()
        return list(map(s.find, s)) == list(map(t.index, t))

# @lc code=end

