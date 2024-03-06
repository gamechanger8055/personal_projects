# Longest Increasing Subsequence using Dynamic Programming


def LIS(arr):
    if not arr:
        return 0
    n=len(arr)
    lis=[0]*n
    lis[0]=1
    for i in range(n):
        for j in range(i):
            if arr[i]>arr[j] and lis[i]<(lis[j]+1):
                lis[i]=(lis[j] + 1)
    return max(lis)
arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print('The length of the LIS is', LIS(arr))