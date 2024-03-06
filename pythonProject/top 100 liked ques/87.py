# Matrix chain multiplication problem: Determine the optimal parenthesization of a product of n matrices.

def mcm(a,i,j):
    if i+1>=j:
        return 0
    mn=99999
    for k in range(i+1,j):
        cost=mcm(a,i,k)+mcm(a,k+1,j)+(a[i]*a[k]*a[j])
        mn=min(mn,cost)
    return mn


a=[10, 30, 5, 60]
print(mcm(a,0,len(a)-1))
