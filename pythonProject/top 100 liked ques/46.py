# Find the number of rotations in a circularly sorted array

def binarySearch(a):
    n=len(a)
    l=0
    r=n-1
    while l<=r:
        mid=l+(r-l)//2
        if a[mid]<a[(mid+1)%n] and a[mid]<=a[(mid-1+n)%n]:
            return mid
        elif a[l]<=a[mid]:
            l=mid+1
        else:
            r=mid-1
    return -1

nums = [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
print(binarySearch(nums))