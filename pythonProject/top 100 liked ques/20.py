# In this post, we will see how to right-rotate an array by specified positions.
# For example, right rotating array { 1, 2, 3, 4, 5, 6, 7 }
# three times will result in array { 5, 6, 7, 1, 2, 3, 4 }.

a=[1,2,3,4,5,6,7]
i=0
k=4
n=len(a)
b=[0]*n
for i in range(n):
    b[i]=a[(i+(k))%n]
print(b)
