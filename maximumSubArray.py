l=[-1, 3, -5, 4, 6, -1, 2, -7, 13, -3]
p=[]
for i in range(1,len(l)+1):
	for j in range(i):
		p.append(sum(l[j:i]))

print max(p)
