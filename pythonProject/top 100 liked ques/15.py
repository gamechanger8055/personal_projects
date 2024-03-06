# Given an integer array, find the subarray that has the maximum product of its elements.
# The solution should return the maximum product of elements among all possible subarrays.

a=[-6, 4, -5, 8, -10, 0, 8]
mx=mn=a[0]
mx1=a[0]
for i in range(1,len(a)):
    temp=mx
    mx=max(a[i],max(a[i]*mx,a[i]*mn))
    mn=min(min(temp*a[i], a[i]*mn),a[i])
    mx1=max(mx1,mx)
print(mx1)