def pairs_sum(l, target):
	d={}

	for i in range(len(l)):
		if l[i] in d:
			print d[l[i]], l[i]
		else:
			d[target-l[i]] = l[i]

pairs_sum([1, 5, 7, -1, 5], 6)