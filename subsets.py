def subsets(l,length):
	ans=[]
	for i in range(1<<length):
		p=[]
		for j in range(length):
			if i&(1<<j):
				p.append(l[j])

		ans.append(p)
	
	print ans


subsets([2,3,2],3)