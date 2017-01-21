def trap(height):
	if len(height)==0:
		return 0

	max_element = (height[0], 0)
	sums = 0
	count = 0
	total_water = 0

	i = 0
	j = 1
	while i<len(height) and j<len(height):
		if height[i]>height[j]:
			sums+=height[j]
			count+=1
			j+=1
		else:
			max_element = (height[j], j)
			total_water+=(min(height[i], height[j]) * count) - sums
			i=j
			j+=1
			sums = 0
			count = 0


	sums = 0
	count = 0

	i = len(height)-1
	j = i-1

	while j>=max_element[1]:
		if height[i]>height[j]:
			sums+=height[j]
			count+=1
			j-=1
		else:
			total_water+=(min(height[i], height[j]) * count) - sums
			i=j
			j-=1
			sums = 0
			count = 0

	return total_water

print trap([])
print trap([0,0,1,0,2,1,0,1,3,2,1,2,1])
print trap([0,0,4,0,0,6,0,0,3,0,5,0,1,0,0,0])
print trap([2,0,2])