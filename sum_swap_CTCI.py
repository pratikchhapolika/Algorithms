def sum_swap(l,p):
	d={}

	for i in l:
		d[i]=None


	k=(sum(l)-sum(p))//2

	for i in range(len(p)):
		inter=p[i]+k
		if inter in d:
			return inter,p[i]

print sum_swap([1,1,1,2,2,4],[3,3,3,6])
print sum_swap([-9, -1, -4, 8, 9, 6, -5, -7, 3, 9], [6, 6, 4, -1, 7, -6, -9, 4, -8, 8])