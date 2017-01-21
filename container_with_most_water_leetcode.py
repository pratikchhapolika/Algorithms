def maxArea(height):
	low = 0
	high = len(height) - 1
	
	max_water = 0
	
	while low<high:
		water = min(height[low], height[high]) * (high - low)
		max_water = max(max_water, water)
		
		if height[low] < height[high]:
			low+=1
		else:
			high-=1
	
	return max_water

print maxArea([1,2,3,4,2])
