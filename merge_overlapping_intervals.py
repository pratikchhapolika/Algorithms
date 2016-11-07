def merge_intervals(l):
	l = sorted(l)

	stack = [l[0]]

	for i in range(1,len(l)):
		if l[i][1] < stack[-1][1]:
			continue
		elif l[i][0] > stack[-1][1]:
			stack.append(l[i])
		else:
			stack[-1][1] = l[i][1]

	print stack

merge_intervals([[5,7], [1,6], [2,4], [10,14], [8,9]])
merge_intervals([[6,8], [1,9], [2,4], [4,7]])