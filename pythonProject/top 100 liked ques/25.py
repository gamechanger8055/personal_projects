# Given an M × N matrix consisting of only 0 or 1, change all elements of row i and column j to 0 if cell (i, j) has value 0. Do this without using any extra space for every (i, j) having value 0.

mat = [
    [5, 3, 0, 8, 1],
    [8, 1, 8, 4, 7],
    [2, 6, 5, 0, 3],
    [1, 4, 2, 7, 9],
    [0, 1, 3, 6, 5]
]
row=set()
col=set()
m=len(mat)
n=len(mat[0])
for i in range(m):
    for j in range(n):
        if mat[i][j]==0:
            row.add(i)
            col.add(j)

for j in row:
    for i in range(n):
        mat[j][i]=0

for j in col:
    for i in range(m):
        mat[i][j]=0
print(mat)
