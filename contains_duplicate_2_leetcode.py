def containsNearbyDuplicate(nums, k):
	d = {}
		
	for i in range(len(nums)):
		if nums[i] in d and i-d[nums[i]]<=k:
			return True
		d[nums[i]] = i
	
	return False

print containsNearbyDuplicate([1,2,1,1,3,5], 1)
