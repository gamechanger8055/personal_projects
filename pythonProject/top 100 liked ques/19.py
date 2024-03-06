# Given an integer array, find subarrays with a given sum in it.

nums = [3, 4, -7, 1, 3, 3, 1, -4]
target = 7
n=len(nums)
sm=0
d={}
d.setdefault(0,[]).append(-1)
for i in range(n):
    sm+=nums[i]
    if d.get(sm-target):
        for val in d[sm-target]:
            print(nums[val+1:i+1],end=",")
    d.setdefault(sm,[]).append(i)
    #print("sdcs",d)