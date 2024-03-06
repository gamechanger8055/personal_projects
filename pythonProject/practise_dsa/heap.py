import heapq
from heapq import heappush, heapify, heappop

# kth smallest and largest
a = [7, 10, 4, 3, 20, 15]
b = [(-1) * i for i in a]
k = 3
heapify(a)
heapify(b)
for i in range(k - 1):
    heappop(a)
    heappop(b)
    print(a, b)
print(a[0], -b[0])

# k sorted array
c = [10, 9, 8, 7, 4, 70, 60, 50]
k = 4
a = []
heapify(c)
for i in range(k):
    p = heappop(c)
    print(c)
    a.append(p)
while len(c):
    a.append(c.pop(0))
print(a, c)

# minimum cost to connect rope

a = [1, 2, 3, 4, 5]
hp = []
n = len(a)
sm = 0
for i in range(n):
    heappush(hp, a[i])
print(hp)
while len(hp) > 1:
    s = (heappop(hp) + heappop(hp))
    sm += s
    heappush(hp, s)
    print(hp, s)
print(sm)


