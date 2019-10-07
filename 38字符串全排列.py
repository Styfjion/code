#递归法
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        if len(ss) == 1:
            return ss
        charList = list(ss)
        charList.sort()
        pStr = []
        for i in range(len(charList)):
            if i and charList[i-1] == charList[i]:
                continue
            nextCharList = self.Permutation(''.join(charList[:i])+''.join(charList[i+1:]))
            for item in nextCharList:
                pStr.append(charList[i]+item)
        return pStr


if __name__ == "__main__":
    res = Solution().Permutation('abcd')
    print(res)
    print(len(res))
