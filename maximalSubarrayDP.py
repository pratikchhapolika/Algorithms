def maximal_subarray(l):
	# s=0
	# ans=0
	# for i in range(len(l)):
	# 	if s+l[i]>0:
	# 		s=s+l[i]
	# 	else:
	# 		s=0
	# 	ans=max(ans,s)
	# print ans


	# For all negative numbers
	# It also works for normal arrays
	current_sum = l[0]
	max_sum_so_far = l[0]

	for i in range(1, len(l)):
		current_sum = max(l[i], current_sum+l[i])
		max_sum_so_far = max(max_sum_so_far, current_sum)

	print max_sum_so_far

maximal_subarray([-3,-2,-1,5])
maximal_subarray([1,-1,-2])
maximal_subarray([-2, -3, 4, -1, -2, 1, 5, -3])
maximal_subarray([-2,-1,-3,-5,-7])
maximal_subarray([2,-8,3,-2,4,-10])
