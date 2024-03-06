# rod cutting prob

weight= [1, 2, 3, 4, 5, 6, 7, 8]
value = [1, 5, 8, 9, 10, 17, 17, 20]
W=4
n=len(weight)

dp=[[0 for i in range(W+1)] for j in range(n+1)]

for i in range(1,n+1):
    for j in range(1,W+1):
        if weight[i-1]<=j:
            dp[i][j]=max(value[i-1]+dp[i][j-weight[i-1]], dp[i-1][j])
        else:
            dp[i][j]=dp[i-1][j]
print(dp[n][W])