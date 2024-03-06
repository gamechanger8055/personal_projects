# Given an M × N matrix of integers where each cell has a cost associated with it,
# find the minimum cost to reach the last cell (M-1, N-1) of the matrix from its first cell (0, 0).
# We can only move one unit right or one unit down from any cell, i.e., from cell (i, j), we can move to (i, j+1) or (i+1, j).
import sys


def findMinCostRecursive(cost,m,n):
    if m==0 or n==0:
        return sys.maxsize
    if m==1 and n==1:
        return cost[m-1][n-1]
    return cost[m-1][n-1]+min(findMinCostRecursive(cost,m-1,n), findMinCostRecursive(cost,m,n-1))



def findMinCostIterative(cost,m,n):
    dp=cost
    for i in range(m):
        for j in range(n):
            if i==0 and j>0:
                dp[0][j]+=dp[0][j-1]
            elif j==0 and i>0:
                dp[i][0]+=dp[i-1][0]
            elif i>0 and j>0:
                dp[i][j]+=min(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]



cost = [
    [4, 7, 8, 6, 4],
    [6, 7, 3, 9, 2],
    [3, 8, 1, 2, 4],
    [7, 1, 7, 3, 7],
    [2, 9, 8, 9, 3]
]
m=len(cost)
n=len(cost[0])

print('The minimum cost is', findMinCostRecursive(cost,m,n))
print('The minimum cost is', findMinCostIterative(cost,m,n))