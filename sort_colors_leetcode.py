def sortColors(nums):
	j = 0
	k = len(nums) - 1
	i = 0
	
	while i<=k and j<k:
		if nums[i] == 0:
			nums[i], nums[j] = nums[j], nums[i]
			j+=1
		elif nums[i] == 2:
			nums[i], nums[k] = nums[k], nums[i]
			k-=1
			i-=1
		i+=1
		
	print nums

sortColors([1,1,2,0,1,0,2,1])		
sortColors([1,1,2,0])
sortColors([1,2,2,2,2,0,0,0,1,1])
sortColors([2,1,2])
sortColors([1,0])

