def kmp(string, pattern):
	lps = []
	i=0
	j=0
	lps = failure_function(pattern)

	while i < len(string):
		if pattern[j] == string[i]:
			i+=1
			j+=1
		if j == len(pattern):
			print i-j
			j = lps[j-1]
		elif i<len(string) and pattern[j] != string[i]:
			if j!=0:
				j=lps[j-1]
			else:
				i+=1

def failure_function(pattern):
	length = len(pattern)
	j=0
	i=1
	lps = [None]*length
	lps[0] = 0

	while i < length:
		if pattern[i] == pattern[j]:
			j+=1
			lps[i] = j
			i+=1
		else:
			if j!=0:
				j = lps[j-1]
			else:
				lps[i] = 0
				i+=1

	return lps


kmp('ABABDABACDABABCABAB', 'ABABCABAB')
kmp('abate', 'bat')
