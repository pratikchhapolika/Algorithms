def four_sum(nums, target):
	final = set()
	nums.sort()
	for i in range(len(nums)):
		for j in range(i+1, len(nums)):
			k = j+1
			l = len(nums)-1

			while k<l:
				s = nums[i] + nums[j] + nums[k] + nums[l]
				if s==target:
					final.add((nums[i], nums[j], nums[k], nums[l]))	
					k+=1
					l-=1
				elif s>target:
					l-=1
				else:
					k+=1

	return final


print four_sum([1, 0, -1, 0, -2, 2], 0)


