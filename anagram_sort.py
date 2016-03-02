l=['yash','abcd','hsay','iopl','fas','dcba']
p=[]

for i in range(len(l)):
	other=l[i+1:]
	for j in other:
		if sorted(l[i])==sorted(j):
			p.append(l[i])
			p.append(j)

for i in l:
	if i not in p:
		p.append(i)

print p

