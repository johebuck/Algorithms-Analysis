#NAME: John Buckley
#DATE: 9/17/17
#PROGRAM: Programming assignment 1: ordered input
#PURPOSE: Uses insertion sort to take a list of integers and sort them in increasing order

import random

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
alist = [(random.randint(1,1000) ) for i in range(n)]
print("Original:")
print(alist)
insertionSort(alist)
print("Sorted:")
print(alist)

