def LLS(A,B):
    if not A or not B:
        return 0
    dp = [[0 for i in range(len(B))] for i in range(len(A))]
    maxLen = 0
    for i in range(len(A)):
        for j in range(len(B)):
            if A[i] == B[j]:
                if not i or not j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i-1][j-1] + 1
                maxLen = max(maxLen,dp[i][j])
    return maxLen

if __name__ == "__main__":
    A = 'dcdcdcdffgjukuku'
    B = 'cdcgtnncdffgjukefe'
    print(LLS(A,B))
