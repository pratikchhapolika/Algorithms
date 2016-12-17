def search(l, x):
	left = 0
	right = len(l) - 1

	while left<=right:
		mid = (left + right) / 2
		if l[mid] == x:
			return mid

		# Right part is sorted
		if l[mid] < l[left]:
			if x>l[mid] and x<=l[right]:
				left = mid + 1
			else:
				right = mid - 1 

		# Left part is sorted
		else:
			if x<l[mid] and x>=l[left]:
				right = mid - 1
			else:
				left = mid + 1

	return -1

print search([15,16,19,20,25,1,3,4,5,7,10,14], 5)
