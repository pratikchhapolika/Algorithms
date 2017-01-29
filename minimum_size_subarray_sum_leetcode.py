import sys
def minSubArrayLen(s, nums):
	min_length = sys.maxsize
	i = 0
	j = 0
	total = 0
	while j<len(nums):
		total+=nums[j]
		j+=1
		while total >= s:
			min_length = min(min_length, j-i)
			total-=nums[i]
			i+=1
	
	if min_length == sys.maxsize:
		return 0
	return min_length

	



	# THIS METHOD WILL GIVE TIME LIMIT EXCEEDED
	# BECAUSE OF CALCULATING THE SUM AGAIN AND AGAIN

	# min_length = sys.maxsize
	# i = 0
	# j = 0
	# total = 0
	# while j<len(nums):
	# 	if sum(nums[i:j+1]) >= s:
	# 		min_length = min(min_length, j-i+1)
	# 		i+=1
	# 	elif sum(nums[i:j+1]) < s:
	# 		j+=1
	
	# if min_length == sys.maxsize:
	# 	return 0
	# return min_length

print minSubArrayLen(7, [2,3,1,2,4,3])

