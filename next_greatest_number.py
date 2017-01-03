def nextGreatestNumber(n):
	length=len(n)
	# finds the element which is smaller than its previous element(in reverse order)
	# Lets call this element 'decider'
	for i in range(length-1,0,-1):
		if n[i-1]<n[i]:
			index_small_element=i-1
			break
	else:
		return 'Not possible'

	n_list=list(n)
	
	# get the minimum element in the list greater than the element at index_small_element

	x = n_list[index_small_element]
	smallest = index_small_element + 1
	for i in range(index_small_element+1, len(n)):
		if n_list[i] > x and n_list[i] < n_list[smallest]:
			smallest = i
	
	# swapping the minimum element and the decider element
	n_list[smallest],n_list[index_small_element]=n_list[index_small_element],n_list[smallest]
	
	# sorting all the elements that come after the 'index_small_element' to give 
	# the next greatest number
	return ''.join(n_list[:index_small_element+1]+sorted(n_list[index_small_element+1:]))

print nextGreatestNumber('218765')
print nextGreatestNumber('1234')
print nextGreatestNumber('4321')
print nextGreatestNumber('534976')
print nextGreatestNumber('231')

