def longestCommonPrefix(strs):
	if len(strs) == 0:
		return ""
	max_string = max(strs)
	min_string = min(strs)

	if len(min_string) == 0:
		return ''
		
	i = 0
	j = 0

	while i<len(min_string):
		if min_string[i] != min_string[j]:
			return min_string[:i]
		else:
			i+=1
			j+=1
	return min_string

print longestCommonPrefix(["aa","a"])
