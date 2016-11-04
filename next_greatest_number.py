def nextGreatestNumber(n):
	length=len(n)
	# finds the element which is smaller than its previous element(in reverse order)
	# Lets call this element 'decider'
	for i in range(length-1,0,-1):
		if n[i-1]<n[i]:
			index_small_element=n.index(n[i-1])
			break
	else:
		return 'Not possible'

	n_list=list(n)
	# getting the minimum element in the list which come after the decider element(in normal order)
	minimum_after_index=n_list.index(min(n_list[index_small_element+1:]))
	# swapping the minimum element and the decider element
	n_list[minimum_after_index],n_list[index_small_element]=n_list[index_small_element],n_list[minimum_after_index]
	# sorting all the elements that come after the 'index_small_element' to give 
	# the next greatest number
	return ''.join(n_list[:index_small_element+1]+sorted(n_list[index_small_element+1:]))

print nextGreatestNumber('218765')
print nextGreatestNumber('1234')
print nextGreatestNumber('4321')
print nextGreatestNumber('534976')

