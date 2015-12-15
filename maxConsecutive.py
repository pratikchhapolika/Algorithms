l=[2,-8,3,-2,2]
p=[]
for i in range(1,len(l)+1):
	for j in range(i):
		p.append(sum(l[j:i]))

print max(p)