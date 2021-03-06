import random

def partition(A,p,r):
    i = ( p-1 )
    q = A[r]
    for j in range(p , r):
        if   A[j] <= q:
            i = i+1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return ( i+1 )

def quick_sort(A,p,r):
    if p < r:
        x = partition(A,p,r)
        quick_sort(A, p, x-1)
        quick_sort(A, x+1, r),

n=input()
n=int(n)

A=[(random.randint(1,1000) ) for i in range(n)]
print("Original:")
print(A)
quick_sort(A,0,len(A)-1)
print("Sorted:")
print(A)
