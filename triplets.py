# Both the methods have a time complexity of O(n^2)

def find_triplets(l,n):
	# Using sorting and 2 pointer approach
	l=sorted(l)
	for i in range(len(l)):
		j=i+1
		k=len(l)-1
		while j<k:
			if l[i]+l[j]+l[k]==n:
				return l[i],l[j],l[k]
			elif l[i]+l[j]+l[k]<n:
				j+=1
			else:
				k-=1
	return 'No triplet found'


	#########################################
	# Using dictionary approach
	# d={}
	# for i in set(l):
	# 	d[i]='y'

	# for i in range(len(l)):
	# 	other=l[i+1:]
	# 	for j in other:
	# 		if n-l[i]-j in d:
	# 			return l[i],j,n-l[i]-j

	# return 'No triplet found'



l=[12,3,4,1,6,9]
n=24
print find_triplets(l,n)