def unique(string):
	l=[]
	for i in range(len(string)):
		if string[i] in (string[:i]+string[i+1:]):
			l.append(0)
		else:
			l.append(1) 
	if 0 in l:
		return "Not Unique"
	else:
		return "Unique"

print unique("katariya")