# Given an integer array, find the maximum sum of subsequence where the subsequence contains no element at adjacent positions.

a=[1, 2, 9, 4, 5, 0, 4, 11, 6]
n=len(a)
dp=[0]*n
dp[1]=a[0]
#dp[2]=max(a[0],a[1])
for i in range(2,n):
    dp[i]=max(a[i-1]+dp[i-2],dp[i-1])
print(dp)