def rotate(l,n):
	p=[]
	size=len(l)-1
	for i in range(size,(size-(n-1))-1,-1):
		p.insert(0,l[i])

	for i in range(size-(n-1)):
		p.append(l[i])

	return p


print rotate([1,2,3,4,5,6],2)
print rotate([1,0,0], 2)