# Given an array containing only 0’s, 1’s, and 2’s, sort it in linear time and using constant space.

a=[0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
n=len(a)
i=0
j=n-1
mid=0
pivot=1
while mid<=j:
    if a[mid]<pivot: #0par
        a[i],a[mid]=a[mid],a[i]
        mid+=1
        i+=1
    elif a[mid]>pivot: #2par
        a[j],a[mid]=a[mid],a[j]
        j-=1
    else: #1 par
        mid+=1
print(a)