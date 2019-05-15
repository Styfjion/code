# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    
    def match(self,s,pattern):
        if not s and not pattern:
            return True
        if s and not pattern:
            return False
        #注意判断条件，字符串是否为空，下标是否越界
        if len(pattern)>1 and pattern[1] == '*':
            if s and(s[0] == pattern[0] or pattern[0] == '.'):
                result = self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:]) or self.match(s[1:],pattern)
            else:
                result = self.match(s,pattern[2:])
            return result
        if s and(s[0] == pattern[0] or pattern[0] == '.'):
            return (self.match(s[1:],pattern[1:]))
        return False

if __name__ == "__main__":
    Solution().match('','.')


