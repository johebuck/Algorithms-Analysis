def countSort(A):
	B = [0 for i in range(10000)]
	C = [0 for i in range(10000)]
	arr = ["" for _ in A]
	for i in A:
		C[(i)] += 1
	for i in range(10000):
		C[i] += C[i-1]
	for i in range(len(A)):
		B[C[(A[i])]-1] = A[i]
		C[(A[i])] -= 1
	for i in range(len(A)):
		arr[i] = B[i]
	return arr

n=input()
n=int(n)
A = list(range(n, 0, -1))
print("Original array is")
print(A)
arr = countSort(A)
print ("Sorted character array is ")
print(arr)