# minm no of deletion to make a string palindrome

X='ACBCDBAA'
Y=X[::-1]
m=len(X)
n=len(Y)

dp=[[0 for i in range(n+1)] for j in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if X[i-1]==Y[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(m-dp[m][n])