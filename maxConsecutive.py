l=[-5,0,-4,1,4,3]
p=[]
for i in range(1,len(l)+1):
	for j in range(i):
		p.append(sum(l[j:i]))

print max(p)
