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

X=[13,14,10,11,12]
print increasing_subsequence(X)

###############################################################################

# Time Complexity = O(2^n)

# from itertools import combinations

# # l=[3,2,6,4,5,1]
# # l=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
# l=[13,14,10,11,12]

# def longest(l):
# 	for i in range(len(l),0,-1):
# 		for sub in combinations(l,i):
# 			if list(sub)==sorted(sub):
# 				return sub

# print longest(l)




