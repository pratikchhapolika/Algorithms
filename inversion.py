l=[1,3,5,2,4,6]
p=[]
for i in range(len(l)):
	for j in l[i+1:]:
		if l[i]>j:
			p.append((l[i],j))

print p
print len(p)