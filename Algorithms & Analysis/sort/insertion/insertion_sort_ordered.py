#NAME: John Buckley
#DATE: 9/17/17
#PROJECT: Programming assignment 1: ordered input
#PROGRAM: Takes an input, n, and makes a sorted list from 0 to n and outputs the original and sorted lists

def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

n=input()
n=int(n)
alist = list(range(0, n))
print("Original:")
print(alist)
insertionSort(alist)
print("Sorted:")
print(alist)
