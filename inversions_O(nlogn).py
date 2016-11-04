def merge(L,R,A):    # Recursive and stable(for equal numbers it preserves their original position) algorithm
	nL=len(L)
	nR=len(R)
	i=0
	j=0
	k=0
	count=0

	while i<nL and j<nR:
		if L[i]<R[j]:
			A[k]=L[i]
			i+=1
		else:
			A[k]=R[j]
			count+=(nL-i)
			j+=1
		k+=1

	while i<nL:
		A[k]=L[i]
		i+=1
		k+=1
	while j<nR:
		A[k]=R[j]
		j+=1
		k+=1

	return count

def mergesort(A):    # Time complexity is Worst Case:- O(nlogn)
	n=len(A)	     # Space complexity is O(n)
	if n<2:
		return 0 
	mid=n/2
	left=A[:mid]
	right=A[mid:]
	return mergesort(left)+mergesort(right)+merge(left,right,A)

print mergesort([1,3,5,2,4,6])



