# Time Complexity = O(nlogn)
def increasing_subsequence(X):
	l=len(X)
	parent=[0]*l   # tracking the parents of elements of each subsequence
	increasing_sub=[0]*(l+1)   # tracking ends of each increasing subsequence
	length=0   # length of the longest sequence

	for i in range(len(X)):
		# Binary Search
		low=1
		high=length
		while low<=high:
			mid=(low+high)//2
			if X[increasing_sub[mid]]<X[i]:
				low=mid+1
			else:
				high=mid-1

		pos=low
		# update the parent element for LIS 
		parent[i]=increasing_sub[pos-1]
		# replace or append
		increasing_sub[pos]=i

		# update the length of longest subsequence
		if pos>length:
			length=pos

	# generate LIS by traversing the parent array
	lis=[]
	k=increasing_sub[length]
	for j in range(length-1,-1,-1):
		lis.append(X[k])
		k=parent[k]

	return lis[::-1]

print increasing_subsequence([13,14,10,11,12])
print increasing_subsequence([1,3,2,3,4,8,7,9])





