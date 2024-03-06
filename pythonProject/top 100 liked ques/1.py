# Given an integer array, check if it contains a subarray having zero-sum.
a = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
s=set()
s.add(0)
sm=0
curr=-1
for i in range(len(a)):
    sm+=a[i]
    if sm in s:
        curr=i
        print("hooray",i)
    s.add(sm)
    print("debug",s)

