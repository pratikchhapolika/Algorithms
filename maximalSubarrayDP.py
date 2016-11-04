def maximal_subarray(l):
	s=0
	ans=0
	for i in range(len(l)):
		if s+l[i]>0:
			s=s+l[i]
		else:
			s=0
		ans=max(ans,s)
	print ans

l=[-3,-2,-1,5]
maximal_subarray(l)


