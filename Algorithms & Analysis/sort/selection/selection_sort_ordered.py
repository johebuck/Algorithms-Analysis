def selectionSort(alist):
   for i in range(len(alist)-1,0,-1):
      Max=0
      for j in range(1,i+1):
         if alist[j]>alist[Max]:
            Max = j

      temp = alist[i]
      alist[i] = alist[Max]
      alist[Max] = temp

n=input()
n=int(n)
alist = list(range(0, n))
print("Original:")
print(alist)
selectionSort(alist)
print("Sorted:")
print(alist)
