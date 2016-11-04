def check(s):
	a = ['(', '{', '[']
	b = [')', '}', ']']
	stack = []
	for i in s:
		if i in a:
			stack.append(i)
		elif i in b:
			t = stack.pop()
			if not matched(t, i):
				return False
	return True

def matched(left, right):
	if left == '(':
		return right==')'
	elif left == '{':
		return right=='}'
	elif left == '[':
		return right==']'

print check('([{}])')
print check('[(])')
print check('[()]{}{[()()]()}')
