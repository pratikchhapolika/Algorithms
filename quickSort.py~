def quicksort(A,start,end):  # Time complexity is Average Case:- O(nlogn), Worst Case:- O(n^2)
	if start<end:
		pIndex=partition(A,start,end)
		quicksort(A,start,pIndex-1)
		quicksort(A,pIndex+1,end)
	return A

def partition(A,start,end):
	pivot=A[end]
	pIndex=start
	for i in range(start,end):
		if A[i]<=pivot:
			A[pIndex],A[i]=A[i],A[pIndex]  #swap if element is lesser than pivot
			pIndex+=1
	A[end],A[pIndex]=A[pIndex],A[end]   # swap pivot with element at partition index
	return pIndex
			


print quicksort([7,2,1,6,8,5,3,4],0,7)
