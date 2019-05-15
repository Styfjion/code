def longestCommonSubstring(A,B):
    if not A or not B:
        return 0
    lenA = len(A)
    lenB = len(B)
    dp = [[0 for i in range(lenB)] for i in range(lenA)]
    maxLen = 0
    for i in range(lenA):
        for j in range(lenB):
            if A[i] == B[j]:
                if not i or not j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
                maxLen = max(maxLen,dp[i][j])
    return maxLen

if __name__ == "__main__":
    A = 'abcvswuduwh'
    B = 'wdwdabcvswevepvp'
    result = longestCommonSubstring(A,B)
    print(result)
        
