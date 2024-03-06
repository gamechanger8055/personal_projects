# minimum subset sum

s=[10, 20, 15, 5, 25]
n = len(s)
p=sum(s)
dp = [[0 for i in range(p + 1)] for j in range(n + 1)]
for i in range(n+1):
    dp[i][0]=1
for i in range(1, n + 1):
    for j in range(1, p + 1):
        if s[i - 1] <= j:
            dp[i][j] = dp[i - 1][j - s[i - 1]] or dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[n])
print(dp[n][p])

mn=99999
for i in range(p//2+1):
    if dp[n][i]:
        mn=min(mn,p-2*i)
print(mn)