# Given a list of array, return a list of arrays, each array is a combination of one element in each given array.

# Let me give you an example to help you understand the question
# Input:- [[1, 2, 3], [4], [5, 6]], 
# Output:- [[1, 4, 5], [1, 4, 6], [2, 4, 5], [2, 4, 6], [3, 4, 5], [3, 4, 6]].


def permutation_array(l, index, final):
	if index == len(l):
		print final
		return

	sub_list = l[index]
	for sub in sub_list:
		permutation_array(l, index+1, final + [sub])

permutation_array([[1, 2, 3], [4, 7], [5, 6]], 0, [])


