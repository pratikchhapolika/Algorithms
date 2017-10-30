def partition(nums, start, end):
	pivot = nums[end]
	pIndex = start
		
	for i in range(start, end):
		if nums[i] > pivot:
			nums[pIndex], nums[i] = nums[i], nums[pIndex]
			pIndex+=1
		
	nums[end], nums[pIndex] = nums[pIndex], nums[end]   # swap pivot with element at partition index
	return pIndex

def quickselect(nums, start, end, k):
	partition_index = partition(nums, start, end)
	
	if partition_index == k-1:
		return nums[partition_index], partition_index
	elif partition_index >= k:
		return quickselect(nums, start, partition_index-1, k)
	else:
		return quickselect(nums, partition_index+1, end, k)

def findKthLargest(nums, k):
	return quickselect(nums, 0, len(nums)-1, k)

print findKthLargest([3,2,1,5,6,4], 2)
