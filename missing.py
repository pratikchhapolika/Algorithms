l=[1,2,3,7,10]

for i in range(len(l)-1):
	j=l[i+1]-l[i]
	while j>1:
		print l[i]+j-1
		j-=1
		