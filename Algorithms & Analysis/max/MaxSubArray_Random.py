import random

def crossingsubarray(A, low, mid, high):
    leftSum = float("-inf")
    sumx = 0
    for i in range(mid, low - 1, -1):
        sumx = sumx + A[i]
        if sumx > leftSum:
            leftSum = sumx
            maxLeft = i
    left = leftSum
    rightSum = float("-inf")
    sumx = 0
    for j in range(mid+1, high+1):
        sumx = sumx + A[j]
        if sumx > rightSum:
            rightSum = sumx
            maxRight = j
    right = rightSum
    return(maxLeft, maxRight, left + right)

def findmaxarray(alist, low, high):
    if high == low:
        return low,high,alist[low]
    else:
        mid = (low+high)//2
        leftmin, leftmax, leftsum = findmaxarray(alist, low, mid)
        rightmin, rightmax, rightsum = findmaxarray(alist, mid + 1, high)
        crossmin, crossmax, crosssum = crossingsubarray(alist, low, mid, high)
        if leftsum >= rightsum and leftsum >= crosssum:
            return leftmin, leftmax, leftsum
        elif rightsum >= leftsum and rightsum >= crosssum:
            return rightmin, rightmax, rightsum
        else:
            return crossmin, crossmax, crosssum

n=input()
n=int(n)
B = [(random.randint(-100,100) ) for i in range(n)]
Low,High,maximum = findmaxarray(B, 0, (n-1))
print(B)
print("Low: ")
print(Low+1)
print("High: ")
print(High+1)
print("Sum: ")
print(maximum)
