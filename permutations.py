def permute(s):
	res = []
	if len(s) == 1:
		res = [s]
	else:
		for i, c in enumerate(s):
			for perm in permute(s[:i] + s[i+1:]):
				res += [c + perm]

	return res

print permute("abc")