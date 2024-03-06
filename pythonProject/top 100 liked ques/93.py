# The longest common substring problem
# is the problem of finding the longest string (or strings)
# that is a substring (or are substrings) of two strings.

X = 'ABC'
Y = 'BABA'

m = len(X)
n = len(Y)
mx=0
end=m
dp=[[0 for i in range(n+1)] for j in range(m+1)]

for i in range(1,m+1):
    for j in range(1,n+1):
        if X[i-1]==Y[j-1]:
            dp[i][j]=1+dp[i-1][j-1]
            if dp[i][j]>mx:
                mx=dp[i][j]
                end=i
print(X[(end-mx):end])