# Given an integer array, find the maximum product of two integers in it.
# TC- O(nlogn)

a=[-10, -3, 5, 6, -2]
# a.sort()
# if len(a)==2:
#     print(a[0]*a[1])
# mx=max(a[0]*a[1],a[-1]*a[-2])
# print(mx)

# 2nd approach min and max (1st and 2nd) in O(n)
mx1,mn1=a[0],a[0]
mx2=-9999
mn2=9999
n=len(a)
for i in range(1,n):
    if a[i]>mx1:
        mx2=mx1
        mx1=a[i]
    elif a[i]>mx2:
        mx2=a[i]
    if a[i]<mn1:
        mn2=mn1
        mn1=a[i]
    elif a[i]<mn2:
        mn2=a[i]
print(max(mx1*mx2,mn1*mn2))


