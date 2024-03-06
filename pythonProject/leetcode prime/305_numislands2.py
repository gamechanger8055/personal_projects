class UnionFind:
    def __init__(self, n):
        self.parent = [-1 for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def numIsland2(m, n, positions):
    uf = UnionFind(m * n)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    island = 0
    result = []
    for pos in positions:
        r, c = pos[0], pos[1]
        index = r * n + c
        uf.parent[index] = index
        island += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            new_index = nr * n + nc
            if 0 <= nr < m and 0 <= nc < n and uf.parent[new_index] != -1:
                # unnecessary as maybe union will take casre of these things
                root_index = uf.find(index)
                root_new_index = uf.find(new_index)
                if root_index != root_new_index:
                    uf.union(index, new_index)
                    island -= 1
        result.append(island)
    return result


m = 3
n = 3
positions = [[0, 0], [0, 1], [1, 2], [2, 1]]
print(numIsland2(m, n, positions))



