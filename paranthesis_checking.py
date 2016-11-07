def check(s):
	a = ['(', '{', '[']
	b = [')', '}', ']']
	stack = []

	if s==']' or s==')' or s=='}':
		return False

	for i in s:
		if i in a:
			stack.append(i)
		elif len(stack)==0:
			return False
		elif i in b:
			t = stack.pop()
			if not matched(t, i):
				return False
	if len(stack) == 0:
		return True
	else:
		return False

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
print check('[()')
