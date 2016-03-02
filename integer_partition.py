d={}
def partition(n,m):
	if (n,m) in d:
		return d[(n,m)]

	if n<=1:
		d[(n,m)]=1

	if m>n:
		return partition(n,n)

	else:
		if (n,m) in d:
			s=d[(n,m)]
			if s!=0:
				return s
		
		s=0
		for i in range(1,m+1):
			s+=partition(n-i,i)
		d[(n,m)]=s

	return d[(n,m)]

n=5
m=5
print partition(n,m)