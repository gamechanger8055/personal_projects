# equal partition of subsets

#s=[3, 1, 1, 2, 2, 1]
#s=[2,3,5,6,8,10]
s=[7, 3, 2, 1, 5, 4, 8]
sm=sum(s)
if sm%3:
    print("given array cant be partitioned")
else:
    p=sm//3
    #p=10
    n = len(s)
    dp = [[0 for i in range(p + 1)] for j in range(n + 1)]
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1, n + 1):
        for j in range(1, p + 1):
            if s[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - s[i - 1]] or dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    print(dp[n][p])