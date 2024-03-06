# Find maximum sum submatrix present in a matrix


def findMaxSumSubmatrix(matrix):
    n=len(matrix)
    mx=0
    max_submatrix=None
    prefix_sum=[[0]*(n+1) for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefix_sum[i][j]=matrix[i-1][j-1]+prefix_sum[i-1][j]+prefix_sum[i][j-1]-prefix_sum[i-1][j-1]

    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(i,n+1):
                for l in range(j,n+1):
                    submatrix_sum = prefix_sum[k][l] - prefix_sum[i - 1][l] - prefix_sum[k][j - 1] + prefix_sum[i - 1][j - 1]

    if submatrix_sum > mx:
        mx = submatrix_sum
        max_submatrix = ((i - 1, j - 1), (k - 1, l - 1))

    return max_submatrix,mx


matrix = [
    [-5, -6, 3, 1, 0],
    [9, 7, 8, 3, 7],
    [-6, -2, -1, 2, -4],
    [-7, 5, 5, 2, -6],
    [3, 2, 9, -5, 1]
]

# find the maximum sum submatrix
print("The maximum sum is", findMaxSumSubmatrix(matrix))