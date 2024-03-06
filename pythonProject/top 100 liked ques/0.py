# Given an unsorted integer array, find a pair with the given sum in it.

nums = [8, 7, 2, 5, 3, 1]
target = 10
n=len(nums)
num=nums

#approach 1: 2 ptr
nums.sort()
i=0
j=n-1
while i<j:
    if nums[i]+nums[j]==target:
        print("1st",[nums[i],nums[j]])
        break
    elif (nums[i]+nums[j])>target:
        j-=1
    else:
        i+=1

#approach2: using map

mp={}
for i in range(n):
    #print(mp)
    p=target-num[i]
    if p in mp:
        print("2nd",(p, nums[i]))
        break
    mp[num[i]]=i

