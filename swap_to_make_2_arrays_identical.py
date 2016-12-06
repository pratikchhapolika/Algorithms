# Given two arrays which have same values but in different order,
# we need to make second array same as first array using minimum number of swaps.

def swap(l,p):
	d={}
	count = 0
	for i in range(len(p)):
		d[p[i]] = i

	for i in range(len(l)):
		if l[i]!=p[i]:
			index = d[l[i]]
			d[p[index]] = i
			d[p[i]] = index
			p[i], p[index] = p[index], p[i]
			count+=1
	
	print count

swap([2,4,8,6,9], [8,6,4,2,9])
swap([1,2,3,4,5], [4,5,1,2,3])
swap([1,2,3,4], [3,1,4,2])

