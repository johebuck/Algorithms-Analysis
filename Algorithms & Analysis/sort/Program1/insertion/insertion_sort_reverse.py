#NAME: John Buckley
#DATE: 9/17/17
#PROGRAM: Programming assignment 1: ordered input
#PURPOSE: Uses insertion sort to take a list of integers and sort them in increasing order

def insertionSort(alist):
   for i in range(1,len(alist)):

     k = alist[i]
     j = i

     while j>0 and alist[j-1]>k:
         alist[j]=alist[j-1]
         j = j-1

     alist[j]=k

n=input()
n=int(n)
alist = list(range(n, 0, -1))
print("Original:")
print(alist)
insertionSort(alist)
print("Sorted:")
print(alist)