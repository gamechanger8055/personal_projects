# Given an integer array, move all zeros present in it to the end. The solution should maintain the relative order of items in the array and should not use constant space.

a=[6, 0, 8, 2, 3, 0, 4, 0, 1]
n=len(a)
i=j=0
while i<n:
    if a[i]:
        a[i],a[j]=a[j],a[i]
        j+=1
    i+=1
print(a)
