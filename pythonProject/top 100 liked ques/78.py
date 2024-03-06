# Count number of islands
row = [-1, -1, -1, 0, 1, 0, 1, 1]
col = [-1, 1, 0, -1, -1, 1, 0, 1]

def isValid(x,y,m,n,matrix,visited):
    return 0<=x<m and 0<=y<n and visited[x][y]==0 and matrix[x][y]==1

def countIslandHelper(mat,i,j, visited,m,n):
    visited[i][j]=1
    q=[(i,j)]
    while q:
        x,y=q.pop(0)
        for k in range(8):
            a=x+row[k]
            b=y+col[k]
            if isValid(a,b,m,n,mat,visited):
                visited[a][b]=1
                q.append((a,b))


def countIslands(mat):
    m=len(mat)
    n=len(mat[0])
    q=[]
    island=0
    vis=[[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            if mat[i][j] and not vis[i][j]:
                countIslandHelper(mat,i,j,vis,m,n)
                island+=1
    return island



mat = [
    [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]
]

print('The total number of islands is', countIslands(mat))