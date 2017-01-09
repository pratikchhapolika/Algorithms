def findRepeatedDnaSequences(s):
	d = {}
	i = 0
	j = 9
	
	while j<len(s):
		string = s[i:j+1]
		
		if string in d:
			d[string]+=1
		else:
			d[string] = 1
	
		i+=1
		j+=1

	final = []
	for i in d:
		if d[i]>1:
			final.append(i)
	
	return final


print findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
