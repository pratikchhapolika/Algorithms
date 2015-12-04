def simplifyPath(A):
	stack = []
	A = A.split('/')
	for a in A:
		if a == '..':
			if len(stack) > 0:
				stack.pop()
		elif a == '.':
			continue
		elif len(a) != 0:
			stack.append(a)
	return '/'+'/'.join(stack)

print simplifyPath("/a/b/../../c")
