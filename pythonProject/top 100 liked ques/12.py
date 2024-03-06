# Given an integer array, find the maximum difference between two elements in it such that the smaller element appears before the larger element.

a=[2, 7, 9, 5, 1, 3, 5]
n=len(a)
mx=a[-1]
mxd=0
for i in reversed(range(n)):
    if a[i]>mx:
        mx=a[i]
    else:
        mxd=max(mxd,mx-a[i])
print(mxd)
