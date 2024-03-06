# Find the first or last occurrence of a given number in a sorted array

def findFirstOccurrence(nums, target):
    n=len(nums)
    l=0
    r=n-1
    ind=-1
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]==target:
            ind=mid
            r=mid-1
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return ind

def findLastOccurrence(nums, target):
    n=len(nums)
    l=0
    r=n-1
    ind=-1
    while l<=r:
        mid=(r+l)//2
        if nums[mid]==target:
            ind=mid
            l=mid+1
        elif nums[mid]>target:
            r=mid-1
        else:
            l=mid+1
    return ind

nums = [2, 5, 5, 5, 6, 6, 8, 9, 9, 9]
target = 5
index1 = findFirstOccurrence(nums, target)
index2 = findLastOccurrence(nums, target)
print(index2-index1+1)