# Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

# Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# Example 1:
# Given the list [[1,1],2,[1,1]], return 10. (four 1s at depth 2, one 2 at depth 1)

# Example 2:
# Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2, 
# and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)

def level(s):
	stack=[]
	d={}
	for i in s:
		if i=='[':
			stack.append('[')
		elif i==']':
			stack.pop()
		elif i==',':
			continue
		else:
			if len(stack) in d:
				d[len(stack)].extend([int(i)])
			else:
				d[len(stack)] = [int(i)]
			print d
	
	sums=0
	for key,value in d.items():
		sums+=(key*sum(value))
	print sums

# level('[1,2,3]')
# level('[[1,1],2,[1,1]]')
# level('[1,[4,[6]]]')
level('[1,[1,[1]]]')
# level('[1,[2,3],5]')
