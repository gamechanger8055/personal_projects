# sort 0s and 1s in O(n)

# approaches- 1.  2ptr
#2. sort
# 3. using extra array
a=[1, 0, 1, 0, 1, 0, 0, 1]
n=len(a)
i,j=0,n-1
while i<j:
    if a[i]==1 and a[j]==0:
        a[i],a[j]=a[j],a[i]
    elif a[i]==0:
        i+=1
    elif a[j]==1:
        j-=1

print(a)


