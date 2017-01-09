def threeSumClosest(l, target):
	l=sorted(l)
	i=0
	closest=l[0] + l[1] + l[2]
	while i<len(l):
		j=i+1
		k=len(l)-1
		while j<k:
			sum = l[i]+l[j]+l[k]
			if sum == target:
				return sum
			if abs(target-sum) < abs(target-closest):
				closest = sum
			elif l[i]+l[j]+l[k] < target:
				j+=1
			else:
				k-=1
		i+=1
	
	return closest

print threeSumClosest([1,2,-1,-4], 1)
