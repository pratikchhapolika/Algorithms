def same(text,sample):
	l=[]
	f=0
	j=sample[f]
	for i in text:
		if j==i:
			f+=1
			l.append(i)
			if f>(len(sample)-1):
				break
			j=sample[f]
	
	l=''.join(l)
	if l==sample:
		print "String in same order"
	else:
		print "String not in same order"


# same("abcNjhgAhGjhfhAljhRkhgRbhjbevfhO","NAGARRO")
same("bangalore","blr")