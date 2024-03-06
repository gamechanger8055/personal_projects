#extension problem 1: print all subarray with 0 sum

a = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
mp={}
mp[0]=[-1]
sm=0
curr=-1
ans=[]
for i in range(len(a)):
    #print(mp,sm)
    sm+=a[i]
    if mp.get(sm):
        mp[sm].append(i)
        #ans.append(a[mp[sm]+1:i+1])
    else:
        mp[sm]=[i]
print(ans,mp)

sm=0
d={}
nums=a
n=len(a)
d.setdefault(0,[]).append(-1)
for i in range(n):
    sm+=nums[i]
    if d.get(sm):
        for val in d[sm]:
            print(nums[val+1:i+1],end=",")
    d.setdefault(sm,[]).append(i)
