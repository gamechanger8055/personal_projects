# 4-sum problem: Given an unsorted integer array,
# check if it contains four elements tuple (quadruplets) having a given sum.

nums = [ 2, 7, 4, 0, 9, 5, 1, 3 ]
target = 20
mp={}
n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        p=target-(nums[i]+nums[j])
        if mp.get(p):
            for pair in mp[p]:
                x,y=pair
                if (x != i and x != j) and (y != i and y != j):
                    print("quadruplet", nums[x], nums[y],nums[i], nums[j])
        mp.setdefault(nums[i]+nums[j],[]).append((i,j))
        #print(mp)

# 2 pointer approach
nums.sort()
for i in range(n):
    for j in range(i + 1, n):
        a,b=j+1,n-1
        while a<b:
            p=nums[i]+nums[a]+nums[b]+nums[j]
            if (p==target):
                print("sfse", nums[i],nums[a],nums[b], nums[j])
                a+=1
                b-=1
            elif p>target:
                b-=1
            else:
                a+=1
