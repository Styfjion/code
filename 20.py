
# -*- coding:utf-8 -*-
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        isDecimal = False
        isExponent = False
        length = len(s)
        for i in range(length):
            if '0'<=s[i]<='9':
                continue
            elif length > 1:
                if s[i] == '.':
                    if not isDecimal and not isExponent:
                        if i == length - 1 or '0'<=s[i+1]<='9':
                            isDecimal = True
                        elif i > 0 and (s[i+1] == 'e' or s[i+1] == 'E'):
                            isDecimal = True
                        else:
                            return False
                    else:
                        return False
                elif (s[i] == 'e' or s[i] == 'E'):
                    if not isExponent and 0<i<length-1:
                        if '0'<=s[i+1]<='9' or s[i+1] == '+' or s[i+1] == '-':
                            isExponent = True
                        else:
                            return False
                    else:
                        return False
                elif (s[i] == '+' or s[i] == '-'):
                    if isExponent and 0<i<length-1 and '0'<=s[i+1]<='9':
                        continue
                    elif i == 0 and (s[i+1] == '.' or '0'<=s[i+1]<='9'):
                        continue
                    else:
                        return False
                else:
                    return False
            else:
                return False
        return True

class Solution2:
#笔试做法
    def isNumeric(self, s):
        # write code here
        try:
            ss=float(s)
            return True
        except:
            return False

if __name__ == "__main__":
    Solution().isNumeric('-1E-16')
            
