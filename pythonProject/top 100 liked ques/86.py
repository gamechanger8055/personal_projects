# The Levenshtein distance (or Edit distance) is a way of quantifying how different two strings are from one another by counting the minimum number of operations required to transform one string into the other.

X = 'kitten'
Y = 'sitting'
m=len(X)
n=len(Y)

dp=[[0 for i in range(n+1)] for j in range(m+1)]

for i in range(1,m+1):
    dp[i][0]=i
for j in range(1,n+1):
    dp[0][j]=j

for i in range(1,m+1):
    for j in range(1,n+1):
        if X[i-1]==Y[j-1]:
           cost=0
        else:
            cost=1
        dp[i][j]=min(1+dp[i-1][j],1+dp[i][j-1],dp[i-1][j-1]+cost)
print(dp[m][n])