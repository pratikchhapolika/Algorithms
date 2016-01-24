def interval(l,inter):
	n=0
	i=0
	p=[]
	while n<len(l):
		i=n
		n+=inter
		p.append(sum(l[i:n]))


	print p

l=[1,1,1,1,1,1,1,1,1,1]

interval(l,3)