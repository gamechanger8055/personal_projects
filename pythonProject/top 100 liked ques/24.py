# Given an M × N integer matrix, print it in spiral order.

a = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

m,n=4,4

p=0 # row index
b=0 # col index

while p<m and b<n:
    for i in range(p,n):
        print(a[p][i],end=",")
    p+=1
    for j in range(p,m):
        print(a[j][n-1],end=",")
    n-=1
    if p<m:
        for i in range(n-1,b-1,-1):
            print(a[m-1][i], end=",")
        m-=1

    if b<n:
        for i in range(m-1,p-1,-1):
            print(a[i][b], end=",")
        b+=1


