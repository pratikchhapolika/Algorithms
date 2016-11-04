def binary(A,x):   # binary search only works for sorted lists
	low=0
	high=len(A)-1
	  
	while(low<=high):
		mid=low + (high-low)/2  # (low+high)/2 may cause overflow
		if x==A[mid]:
			return mid
		elif x<A[mid]:
			high=mid-1
		else:
			low=mid+1
	return "Number not found"


print binary([1,2,3,5,7,8,9,10],10)