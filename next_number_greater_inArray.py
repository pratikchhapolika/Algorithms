# Given an array, print the Next Greater Element (NGE) for every element. 
# The Next greater Element for an element x is the first greater element on the right side of x in array. 
# Elements for which no greater element exist, consider next greater element as -1.

def next_greatest_number(l):
	stack = [l[0]]

	for i in range(1, len(l)):
		current = l[i]

		top = stack.pop()

		while current>top:
			print (top, current)
			if len(stack) == 0:
				break
			top = stack.pop()

		if current < top:
			stack.append(top)
		stack.append(current)

	while len(stack) > 0:
		top = stack.pop()
		print (top, -1)


# next_greatest_number([13,7,6,12])
# next_greatest_number([4,5,2,25])
# next_greatest_number([5,4,3,2,1])
next_greatest_number([1,2,3,4,5])

