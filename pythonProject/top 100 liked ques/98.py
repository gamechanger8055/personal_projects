#knapsack 0-1 dp

value = [ 20, 5, 10, 40, 15, 25 ]
weight = [ 1, 2, 3, 8, 7, 4 ]
W = 10
n=len(weight)

dp=[[0 for i in range(W+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,W+1):
        if weight[i-1]<=j:
            dp[i][j]=max(value[i-1]+dp[i-1][j-weight[i-1]], dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][W])