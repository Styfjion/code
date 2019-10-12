"""
如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。

给你一个字符串 text，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。

 

示例 1：

输入：text = "ababa"
输出：3
示例 2：

输入：text = "aaabaaa"
输出：6
示例 3：

输入：text = "aaabbaaa"
输出：4
示例 4：

输入：text = "aaaaa"
输出：5
示例 5：

输入：text = "abcdef"
输出：1
 

提示：

1 <= text.length <= 20000
text 仅由小写英文字母组成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-for-longest-repeated-character-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def maxRepOpt1(self, text: str) -> int:
        res = []
        count = 1
        for i in range(1,len(text)):
            if text[i] == text[i-1]:
                count += 1
            else:
                res.append([text[i-1],count])
                count = 1
        res.append([text[i],count])
        if len(res) == 1:
            return len(text)
        if len(res) == 2:
            return max(res[0][1],res[1][1])
        chdict = {}
        countdict = {}
        for item in res:
            if item[0] not in countdict:
                countdict[item[0]] = 1
            else:
                countdict[item[0]] += 1
        maxLen = res[0][1]
        for i,unit in enumerate(res):
            if unit[0] not in chdict:
                chdict[unit[0]] = unit[1]
                temp = unit[1]
            else:
                if i>=2 and res[i-2][0] == unit[0] and res[i-1][1] == 1:
                    temp = chdict[unit[0]]+unit[1]
                    if countdict[item[0]] > 2:
                        temp += 1
                else:
                    temp = max(chdict[unit[0]],unit[1])+1
                chdict[unit[0]] = unit[1]
            maxLen = max(maxLen,temp)
        return maxLen

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxRepOpt1("abbabaabababaaabbaaa"))
