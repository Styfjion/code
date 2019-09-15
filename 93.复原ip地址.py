#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#
# https://leetcode-cn.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (45.25%)
# Likes:    128
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 29.9K
# Testcase Example:  '"25525511135"'
#
# 给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。
# 
# 示例:
# 
# 输入: "25525511135"
# 输出: ["255.255.11.135", "255.255.111.35"]
# 
#
class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.dfs(s,0,"",res)
        return res
    
    def dfs(self,s,index,path,res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return
        for i in range(1,4):
            if i<=len(s):
                if i == 1:
                    self.dfs(s[i:],index+1,path+s[:i]+'.',res)
                elif i == 2 and s[0] != '0':
                    self.dfs(s[i:],index+1,path+s[:i]+'.',res)
                elif i == 3 and s[0] != '0' and int(s[:3])<256:
                    self.dfs(s[i:],index+1,path+s[:i]+'.',res)



