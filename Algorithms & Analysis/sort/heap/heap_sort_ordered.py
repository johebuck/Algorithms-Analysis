def MAX_HEAPIFY(A,n,i):
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and A[i]<A[l]:
        largest=l
    if r<n and A[largest]<A[r]:
        largest=r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        MAX_HEAPIFY(A, n, largest)

def heap_sort(A):
    n=len(A)
    #BUILD-MAX-HEAPIFY
    for i in range(n,-1,-1):
        MAX_HEAPIFY(A,n,i)
    for i in range(n-1,0,-1):
        A[i],A[0] = A[0],A[i]
        MAX_HEAPIFY(A,i,0)

n=input()
n=int(n)

A  = list(range(0, n))
print("Original:")
print(A)
heap_sort(A)
print("Sorted:")
print(A)