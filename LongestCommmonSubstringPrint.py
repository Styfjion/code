class Node:
    value = None
    dis = 0

def longestCommonSubstring(A,B):
    if not A or not B:
        return 0
    lenA = len(A)
    lenB = len(B)
    dp = [[Node() for i in range(lenB)] for i in range(lenA)]
    endi = 0
    endj = 0
    for i in range(lenA):
        for j in range(lenB):
            if A[i] == B[j]:
                dp[i][j].value = A[i]
                if not i or not j:
                    dp[i][j].dis = 1
                else:
                    dp[i][j].dis = dp[i-1][j-1].dis + 1
                if dp[endi][endj].dis < dp[i][j].dis:
                   endi = i
                   endj = j
    sub = ''
    while endi >=0 and endj >= 0 and dp[endi][endj].value:
        sub += dp[endi][endj].value
        endi,endj = endi-1,endj-1
    sub = sub[::-1]
    return sub

if __name__ == "__main__":
    A = 'abcvswuduwh'
    B = 'abcvswevepvp'
    result = longestCommonSubstring(A,B)
    print(result)

    
