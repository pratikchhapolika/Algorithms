def Add1(l):
	p=l[::-1]
	p[0]=p[0]+1
	prod=0
	for i in range(len(p)):
		prod=prod+(p[i]*(10**i))
	print prod
l=[9,9,9,9]
Add1(l)