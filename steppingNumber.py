n=10
m=124
l=[]
for i in range(n,m+1):
	l.append(list(str(i)))

d={}
count=1
p=[]
flag=True
for i in range(len(l)):
	if len(l[i])==1:
		p.append(int(''.join(l[i])))
	for j in range(len(l[i])-1):
		if abs(int(l[i][j])-int(l[i][j+1]))==1 or abs(int(l[i][j+1])-int(l[i][j]))==1:
			if ''.join(l[i]) in d:
				d[''.join(l[i])]+=1
			else:
				d[''.join(l[i])]=count
			

for key,val in d.items():
	if val==len(key)-1:
		p.append(int(key))


print sorted(p)

