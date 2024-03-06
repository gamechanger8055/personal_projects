# Given a chessboard, find the shortest distance (minimum number of steps) taken by a knight to reach a given destination from a given source.

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

def isValid(x,y,m):
    return 0<=x<m and 0<=y<m

def findShortestDistance(src, dest, N):
    q = [(src[0],src[1],0)]
    visited = set()
    visited.add(src)
    while q:
        x, y,z = q.pop(0)
        if x==dest[0] and y==dest[1]:
            return z
        for k in range(8):
            a = x + row[k]
            b = y + col[k]
            if isValid(a, b, N) and (a, b) not in visited:
                visited.add((a, b))
                q.append((a, b,z+1))
    return 999999


N = 8  # N x N matrix
src = (0, 7)  # source coordinates
dest = (7, 0)  # destination coordinates

print("The minimum number of steps required is",
      findShortestDistance(src, dest, N))