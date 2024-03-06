# longest common subsequence
# The Longest Common Subsequence (LCS) problem is finding the longest subsequence present in given two sequences in the same order, i.e., find the longest sequence which can be obtained from the first original sequence by deleting some items and from the second original sequence by deleting other items.

X="ABCBDAB"
Y="BDCABA"

m=len(X)
n=len(Y)

dp=[[0 for i in range(n+1)] for j in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if X[i-1]==Y[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
print(dp[m][n])