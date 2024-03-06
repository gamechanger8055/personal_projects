# Given an unsorted integer array, find a triplet with a given sum in it.

nums = [ 2, 7, 4, 0, 9, 5, 1, 3 ]
target = 6
mp={}
n=len(nums)
for i,j in enumerate(nums):
    mp[j]=i
for i in range(n-1):
    for j in range(i+1,n):
        p=target-(nums[i]+nums[j])
        if mp.get(p):
                if (mp[p] != i and mp[p] != j):
                    print("quadruplet", p,nums[i], nums[j])
        #mp[nums[i]+nums[j]]=i

#approach 2 - 2 ptr
nums.sort()

for i in range(n-1):
    a,b=i+1,n-1
    while a<b:
        p=nums[i]+nums[a]+nums[b]
        if (p==target):
            print("sfse", nums[i],nums[a],nums[b])
            a+=1
            b-=1
        elif p>target:
            b-=1
        else:
            a+=1
