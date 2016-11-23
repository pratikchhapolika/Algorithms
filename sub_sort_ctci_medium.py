def close_binary_search(p, item):
	left=0
	right=len(p)-1

	while right-left>1:
		mid = left + ((right - left) / 2)
		if item == p[mid]:
			return mid
		if item<p[mid]:
			right = mid
		else:
			left = mid
	return right

def sub_sort(l):
	length = len(l)
	p=[l[0]]
	end_index = 0
	m=[]

	for i in range(1, length):
		if l[i]>p[-1]:
			p.append(l[i])
		else:
			m.append(l[i])
			end_index = i

	if len(m) == 0:
		return 0,0
	
	min_no = min(m)

	if min_no < p[0]:
		start_index = 0
	else:
		# You can always use linear search instead
		# of binary search. Anyways the time complexity
		# will still be O(n)
		start_index = close_binary_search(p, min_no)

	return start_index, end_index 

print sub_sort([1,2,4,7,10,11,7,12,6,7,16,18,19])
print sub_sort([5,4,3,2,1])
print sub_sort([1,2,4,7,10,11,7,12,6,7,16,18,19,5])
print sub_sort([1,2,3,4,5])
print sub_sort([7,10,11,7,12,6,7,16,18,19])