def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range(i):
            if alist[j]>alist[j+1]:
                temp = alist[j]
                alist[j] = alist[j+1]
                alist[j+1] = temp

n=input()
n=int(n)
alist = list(range(n, 0, -1))
print("Original:")
print(alist)
bubbleSort(alist)
print("Sorted:")
print(alist)
