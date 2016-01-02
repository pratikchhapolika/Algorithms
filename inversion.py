l=[2,4,1,3,5]
p=[]
for i in range(len(l)):
	for j in l[i+1:]:
		if l[i]>j:
			p.append((l[i],j))

print len(p)