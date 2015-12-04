'''
def arrange(A):
	n=len(A)
	p=[]
	for i in xrange(n):
		A[i]+=(A[A[i]]%n)*n    # Has space complexity of O(1)
		s=A[i]/n
		p.append(s)
	print p

arrange([ 4, 0, 2, 1, 3 ])
'''

def arrange(A):
	n=len(A)
	B=[0]*n
	for i in range(n):
		B[i]=A[i]
	for i in range(n):
		A[i]=B[B[i]]

	return A

print arrange([ 4, 0, 2, 1, 3 ])

	

