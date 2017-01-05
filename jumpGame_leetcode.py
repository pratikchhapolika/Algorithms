def canJump(nums):
	if len(nums) == 1:
		return True
	if nums[0] == 0:
		return False
		
	maxJump = nums[0]
	
	for i in range(1, len(nums)-1):
		maxJump = max(maxJump-1, nums[i])
		if maxJump == 0:
			return False
	
	return True

print canJump([2,3,1,1,4])
print canJump([3,2,1,0,4])
print canJump([2,0,0])
