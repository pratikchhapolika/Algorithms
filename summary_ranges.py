def summaryRanges(nums):
	final = []
	i = 0
	j = 1
		
	while i<len(nums) and j<len(nums):
		if abs(nums[j] - nums[j-1]) <= 1:
			j+=1
		else:
			if j-1 == i:
				final.append(str(nums[i]))
			else:
				final.append(str(nums[i]) + '->' + str(nums[j-1]))
			i=j
			j+=1
	
	if j-1 == i:
		final.append(str(nums[i]))
	else:
		final.append(str(nums[i]) + '->' + str(nums[j-1]))
	return final

print summaryRanges([0,1,2,4,5,7])
print summaryRanges([-1])
print summaryRanges([0,1,2,4,5,7,8])
print summaryRanges([1,3])


