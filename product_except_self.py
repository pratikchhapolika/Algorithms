def productExceptSelf(nums):
	left = [1]
	right = [1]
	final = []

	for i in range(1, len(nums)):
		left.append(nums[i-1] * left[-1])

	for i in range(len(nums)-2, -1, -1):
		right.append(nums[i+1] * right[-1])
	
	for i,j in zip(left, right[::-1]):
		final.append(i * j)

	print final

productExceptSelf([1,2,3,4])