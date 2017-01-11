def maxProduct(nums):
	result = nums[0]
	max_product = nums[0]
	min_product = nums[0]
		
	for i in range(1, len(nums)):
		temp = max_product
		max_product = max(nums[i], max(max_product*nums[i], min_product*nums[i]))
		min_product = min(nums[i], min(temp*nums[i], min_product*nums[i]))
		result = max(result, max_product)            
	return result

print maxProduct([-2, 3, -4])
print maxProduct([-4, -3, -2])
