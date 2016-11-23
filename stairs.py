d={}
def hop(n):
	if n<0:
		d[n]=0
	if n==0:
		d[n]=1
	if n in d:
		return d[n]
	else:
		d[n]=hop(n-1)+hop(n-2)
	
	return d[n]

print hop(4)
