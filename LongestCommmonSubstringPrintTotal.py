class Node:
    value = None
    dis = 0

def longestCommonSubstring(A,B):
    if not A or not B:
        return 0
    lenA = len(A)
    lenB = len(B)
    dp = [[Node() for i in range(lenB)] for i in range(lenA)]
    maxList = [[0,0]]
    for i in range(lenA):
        for j in range(lenB):
            if A[i] == B[j]:
                dp[i][j].value = A[i]
                if not i or not j:
                    dp[i][j].dis = 1
                else:
                    dp[i][j].dis = dp[i-1][j-1].dis + 1
                endi,endj = maxList[0]
                if dp[endi][endj].dis < dp[i][j].dis:
                    maxList = [[i,j]]
                elif dp[endi][endj].dis == dp[i][j].dis:
                    maxList.append([i,j])
    subList = []
    for endi,endj in maxList:
        sub = ''
        while endi >=0 and endj >= 0 and dp[endi][endj].value:
            sub += dp[endi][endj].value
            endi,endj = endi-1,endj-1
        sub = sub[::-1]
        subList.append(sub)
    return subList

if __name__ == "__main__":
    A = 'abcvswuduwhibhjk'
    B = 'abcvswevduwhivphibhjkl'
    result = longestCommonSubstring(A,B)
    print(result)

    
