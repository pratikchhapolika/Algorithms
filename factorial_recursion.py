def factorial(A):   
	if A==0:
		return 1
	if A>0:
		return A*factorial(A-1)

print factorial(4)
