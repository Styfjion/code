if __name__ == "__main__":
    nums = list(map(int,input().split()))
    if len(nums)%2 == 0 or len(nums) == 1:
        print('No')

    n = len(nums)
    dp = [[[0,0] for row in xrange(n)] for _ in xrange(n)]
    for i in range(n):
        dp[i][i] = [nums[i], 0]
    for length in xrange(2,n+1):
        for i in range(n-length+1):
            j = i + length-1
            pi = dp[i+1][j][1] + nums[i]
            pj = dp[i][j-1][1] + nums[j]
            if pi > pj:
                dp[i][j][0] = pi
                dp[i][j][1] = dp[i+1][j][0]

            else:
                dp[i][j][0] = pj
                dp[i][j][1] = dp[i][j-1][0]
    if dp[0][-1][0] >= dp[0][-1][1]:
        print('Yes')
    else:
        print('No')
    
    

