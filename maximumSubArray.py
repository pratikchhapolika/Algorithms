# l=[-2, -3, 4, -1, -2, 1, 5, -3]
l=[2,-1,2,3,4,-5]
p=[]
for i in range(1,len(l)+1):
	for j in range(i):
		p.append(sum(l[j:i]))

print max(p)
