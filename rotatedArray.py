def rotate(l,n):
	# USES O(N) SPACE
	# p=[]
	# size=len(l)-1
	# for i in range(size,(size-(n-1))-1,-1):
	# 	p.insert(0,l[i])

	# for i in range(size-(n-1)):
	# 	p.append(l[i])

	# return p


	# USES O(1) SPACE
	# AWESOME SOLUTION
	# REVERSE THE FIRST LEN-N ELEMENTS
	# THEN REVERSE THE REMAINING ELEMENTS
	# THEN REVERSE THE ENTIRE ARRAY TO GET THE ANSWER
	size = len(l)
	l[:size-n] = l[:size-n][::-1]
	l[size-n:] = l[size-n:][::-1]
	return l[::-1]

print rotate([1,2,3,4,5,6],2)
print rotate([1,2], 0)