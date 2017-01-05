def wordPattern(pattern, str):
	pattern = list(pattern)
	str = str.split()
	d = {}
	f = {}

	if len(pattern) != len(str):
		return False

	for i, j in zip(pattern, str):
		if j not in d and i not in f:
			d[j] = i
			f[i] = True
		else:
			if j not in d:
				return False
			elif d[j] != i:
				return False

	return True

print wordPattern('abba', "dog cat cat dog")
print wordPattern('abba', "dog cat cat fish")
print wordPattern('aaaa', 'dog cat cat dog')
print wordPattern('abba', 'dog dog dog dog')
