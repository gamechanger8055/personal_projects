# Find the shortest path from source to destination in a matrix that satisfies given constraints
# up, down, right and bottom with no diagonal

def isValid(x,y,N):
    return 0<=x<N and 0<=y<N
row = [-1, 0, 0, 1]
col = [0, -1, 1, 0]
def findPath(matrix):
    x,y=0,0
    if not matrix:
        return 0
    n=len(matrix)
    q=[(x,y)]
    visited=set()
    visited.add((x,y))
    while q:
        x,y=q.pop(0)
        for k in range(4):
            a=x+row[k]
            b=y+col[k]
            if isValid(a,b,n) and (a,b) not in visited:
                visited.add((a,b))
                q.append((a,b))
                # will continue




matrix = [
    [4, 4, 6, 5, 5, 1, 1, 1, 7, 4],
    [3, 6, 2, 4, 6, 5, 7, 2, 6, 6],
    [1, 3, 6, 1, 1, 1, 7, 1, 4, 5],
    [7, 5, 6, 3, 1, 3, 3, 1, 1, 7],
    [3, 4, 6, 4, 7, 2, 6, 5, 4, 4],
    [3, 2, 5, 1, 2, 5, 1, 2, 3, 4],
    [4, 2, 2, 2, 5, 2, 3, 7, 7, 3],
    [7, 2, 4, 3, 5, 2, 2, 3, 6, 3],
    [5, 1, 4, 2, 6, 4, 6, 7, 3, 7],
    [1, 4, 1, 7, 5, 3, 6, 5, 3, 4]
]

# Find a route in the matrix from source cell (0, 0) to
# destination cell (N-1, N-1)
path = findPath(matrix)

if path:
    print('The shortest path is', path)
else:
    print('Destination is not found')
