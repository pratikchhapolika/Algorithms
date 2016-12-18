def peaks_valleys(l):
	# There are 2 methods to solve this problem.

	# First method runs in O(nlogn)
	# Sort the list and then swap every
	# adjacent elements
	# l = sorted(l)
	# for i in range(0, len(l)-1, 2):
	# 	l[i], l[i+1] = l[i+1], l[i]
	# return l


	# Second method runs in O(n)
	for i in range(0, len(l), 2):
		if i>0 and l[i]<l[i-1]:
			l[i], l[i-1] = l[i-1], l[i]

		if i<(len(l)-1) and l[i]<l[i+1]:
			l[i], l[i+1] = l[i+1], l[i]
	return l

print peaks_valleys([5,3,1,2,3])
print peaks_valleys([2,3,4,5])
print peaks_valleys([9,1,0,4,8,7])
