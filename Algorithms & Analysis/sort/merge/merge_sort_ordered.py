#NAME: John Buckley
#DATE: 9/17/17
#PROGRAM: merge_sort_ordered
#PURPOSE: Recursively uses merge-sort to break apart a list into smaller lists until they are single lists then merges them back together in sorted order

def merge(A):

    def merge_sort(A,p,r):
        if p<r:
            q=(p+r)//2
            merge_sort(A,p,q)
            merge_sort(A,q+1,r)
            temp=[]
            i=p
            j=q+1
            k=0

            while i<=q and j<=r:

                if A[i]<=A[j]:
                    temp.append(A[i])
                    k=k+1
                    i=i+1

                else:
                    temp.append(A[j])
                    k=k+1
                    j=j+1

            while i<=q:
                temp.append(A[i])
                k=k+1
                i=i+1

            while j<=r:
                temp.append(A[j])
                k=k+1
                j=j+1

            a=0
            b=p

            while a<k:
                A[b]=temp[a]
                b=b+1
                a=a+1

    merge_sort(A,0,len(A)-1)

    return A

n=input()
n=int(n)
alist = list(range(0, n))
print("Original:")
print(alist)
print("Sorted:")
print(merge(alist))

