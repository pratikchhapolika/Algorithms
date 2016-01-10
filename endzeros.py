l=[1,2,0,4,0,0,8]
j=0
for i in range(len(l)):
	if l[i]!=0:
		l[j],l[i]=l[i],l[j]
		j+=1

print l