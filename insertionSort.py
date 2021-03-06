def insertion(A):   # Time Complexity is Best Case:-O(n), Worst Case:- O(n^2)
	n=len(A)
	for i in range(1,n):
		value=A[i]
		hole=i
		while hole>0 and A[hole-1]>value:
			A[hole]=A[hole-1]
			hole-=1
		A[hole]=value

	return A

print insertion([7,2,4,1,5,3])
