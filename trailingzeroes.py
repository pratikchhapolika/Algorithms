import math
def trailingZeroes(n):
	count = 0
	i = 5
	while n/i>0:
		count+=(n/i)
		i*=5		
	print count

trailingZeroes(25)
