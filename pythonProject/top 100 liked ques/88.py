# Given an M × N binary matrix, find the size of the largest square submatrix of 1's present.

mat = [
        [0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1]
]

m=len(mat)
n=len(mat[0])
mx=0
dp=[[0 for i in range(n+1)] for j in range(m+1)]
for i in range(1,m+1):
    for j in range(1,n+1):
        if mat[i-1][j-1]==1:
            dp[i][j]=1+min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1]))
            mx=max(mx,dp[i][j])
print(mx**2)
