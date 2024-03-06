# Find the peak element in an array

def peakElement(a):
    n=len(a)
    l=0
    r=n-1
    while l<=r:
        mid=l+(r-l)//2
        if(a[mid] > a[(mid + 1) % n] and a[mid] > a[(mid - 1 + n) % n]):
            return mid
        elif mid>0 and a[mid]<=a[mid-1]:
            r=mid-1
        elif mid<n-1 and a[mid]>=a[mid+1]:
            l=mid+1
        elif mid==0:
            return a[0] if a[0]>a[1] else a[1]
        else:
            return a[-1] if a[-1]>a[-2] else a[-2]


a=[8, 9, 10, 2, 5, 6]
print(peakElement(a))