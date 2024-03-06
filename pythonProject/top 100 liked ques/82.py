# wildcard pattern matching

def isMatch(word, pattern):
    m=len(word)
    n=len(pattern)
    dp=[[False for i in range(n+1)] for j in range(m+1)]
    dp[0][0]=True
    for i in range(1,n+1):
        if pattern[i-1]=='*':
            dp[0][i]=dp[0][i-1]

    for i in range(1,m+1):
        for j in range(1,n+1):
            if pattern[j-1]=='*':
                dp[i][j]=dp[i-1][j] or dp[i][j-1]
            elif pattern[j-1]=='?' or word[i-1]==pattern[j-1]:
                dp[i][j]=dp[i-1][j-1]

    return dp[-1][-1]


word = 'xyxzzxy'
pattern = 'x***x?'

if isMatch(word, pattern):
    print('Match')
else:
    print('No Match')