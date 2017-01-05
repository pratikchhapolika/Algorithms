# Both the methods have a time complexity of O(n^2)

def find_triplets(l,n):
	# Using sorting and 2 pointer approach
	l=sorted(l)
	i=0
	result=[]
	
	while i<len(l):
		j=i+1
		k=len(l)-1
		while j<k:
			if l[i]+l[j]+l[k]==n:
				result.append([l[i],l[j],l[k]]) 
				j+=1
				k-=1
			elif l[i]+l[j]+l[k]<n:
				j+=1
			else:
				k-=1
		i+=1
	
	final=[]
	for i in result:
		if i not in final:
			final.append(i)
	return final


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


print find_triplets([12,3,4,1,6,9], 24)
print find_triplets([-1,0,1,2,-1,-4], 0)
print

