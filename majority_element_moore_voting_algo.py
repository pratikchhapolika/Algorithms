# Majority Element: A majority element in an array A of size n is an 
# element that appears more than n/2 times (and hence there is at most one such element).

def majorityElement(nums):
	candidate = nums[0]
	count = 1

	for i in range(1, len(nums)):
		if count == 0:
			candidate = nums[i]
			count+=1
		elif candidate!=nums[i]:
			count-=1
		else:
			count+=1

	length = 0
	for i in nums:
		if i==candidate:
			length+=1
	
	if length > len(nums)/2:
		return candidate
	
	return -1

print majorityElement([3,3,4,2,4,4,2,4,4])
print majorityElement([3,3,4,2,4,4,2,4])
print majorityElement([1,3,3,1,2])
print majorityElement([10,9,9,9,10])
print majorityElement([10.548, 451.05546, 10.548, 213154.84, 2.154, 2.369])


