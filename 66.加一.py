#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strdigits = ''.join(map(str,digits))
        intdigits = int(strdigits) + 1
        newstrdigits = str(intdigits)
        newstrList  = list(newstrdigits)
        resultList = list(map(int,newstrdigits))
        return resultList
