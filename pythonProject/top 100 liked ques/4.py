# Given an integer array, find the maximum length subarray having a given sum.

nums = [ 5, 6, -5, 5, 3, 5, 3, -2, 0 ]
target = 8

n=len(nums)
i,j=0,0
sm=0
mx=0
a=[]
while j<n:
    sm+=nums[j]
    if sm==target:
        if (j-i+1)>mx:
            mx=j-i+1
            a=nums[i:j+1]
    if sm>target:
        while sm>target:
            sm-=nums[i]
            i+=1
    j+=1
print(a,mx)
