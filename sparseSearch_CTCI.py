def sparse_search(l, x):
	left = 0
	right = len(l)-1

	while left <= right:
		mid = (left + right) / 2

		if l[mid] == '':
			i = mid - 1
			j = mid + 1

			while i>=left and j<=right:
				if l[i] != '':
					mid = i
					break
				elif l[j] != '':
					mid = j
					break
				else:
					i-=1
					j+=1

		if l[mid] == x:
			return mid
		elif l[mid] > x:
			right = i
		else:
			left = j

	return -1


print sparse_search(['at','','','','ball','','','car','','','dad','',''], 'ball')
